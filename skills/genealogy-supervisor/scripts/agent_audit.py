#!/usr/bin/env python3
"""Audit subagent transcripts by REAL tool calls, not by text lines.

The list of available tools is written into every transcript, so a grep for a
tool name gives false hits. This script counts only tool_use blocks.

Usage:
  python3 -I agent_audit.py <folder-with-agent-*.jsonl> [--since YYYY-MM-DD]
                            [--flag PATTERN ...]

--flag PATTERN  flag any Bash command that contains PATTERN (case-insensitive);
                repeat for several patterns (e.g. commands your rules forbid).

Prints one line per transcript: start | tool calls | tokens (with cache) |
minutes | flagged events | start of the prompt. Read-only; no network.
"""
import glob
import json
import os
import sys
from datetime import datetime

# Phrases that mean "advice to write to an archive" (Russian and English).
ARCHIVE_ADVICE = (
    'запрос в архив', 'обратиться в архив', 'написать в архив', 'письмо в архив',
    'write to the archive', 'contact the archive', 'request to the archive',
)


def parse_args(argv):
    if len(argv) < 2 or argv[1] in ('-h', '--help'):
        print(__doc__)
        sys.exit(0 if len(argv) >= 2 else 1)
    folder, since, flags = argv[1], '', []
    i = 2
    while i < len(argv):
        if argv[i] == '--since' and i + 1 < len(argv):
            since = argv[i + 1]; i += 2
        elif argv[i] == '--flag' and i + 1 < len(argv):
            flags.append(argv[i + 1].lower()); i += 2
        else:
            sys.exit(f'unknown argument: {argv[i]}')
    return folder, since, flags


def text_of(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return ' '.join(c.get('text', '') for c in content if isinstance(c, dict))
    return ''


def audit(path, flags):
    request_ids, tools, tokens, stamps, events, prompt = set(), 0, 0, [], [], ''
    with open(path, encoding='utf-8', errors='replace') as fh:
        for line in fh:
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            if rec.get('timestamp'):
                stamps.append(rec['timestamp'])
            msg = rec.get('message') or {}
            if rec.get('type') == 'user' and not prompt:
                prompt = text_of(msg.get('content'))[:80]
            if rec.get('type') != 'assistant':
                continue
            rid, usage = rec.get('requestId'), msg.get('usage') or {}
            if rid and rid not in request_ids:
                request_ids.add(rid)
                tokens += sum(usage.get(k, 0) for k in (
                    'input_tokens', 'output_tokens',
                    'cache_read_input_tokens', 'cache_creation_input_tokens'))
            for block in msg.get('content') or []:
                if not isinstance(block, dict):
                    continue
                if block.get('type') == 'tool_use':
                    tools += 1
                    name = block.get('name', '')
                    if name in ('Agent', 'Task'):
                        events.append('launched an agent')
                    if 'Claude_Browser' in name:
                        events.append('built-in browser pane')
                    command = str((block.get('input') or {}).get('command', '')).lower()
                    for pattern in flags:
                        if pattern in command:
                            events.append(f'command matches "{pattern}"')
                elif block.get('type') == 'text':
                    if any(a in block.get('text', '').lower() for a in ARCHIVE_ADVICE):
                        events.append('advice to write to an archive (check context)')
    return stamps, tools, tokens, events, prompt


def minutes(stamps):
    try:
        first = datetime.fromisoformat(stamps[0].replace('Z', '+00:00'))
        last = datetime.fromisoformat(stamps[-1].replace('Z', '+00:00'))
        return (last - first).total_seconds() / 60
    except (ValueError, IndexError):
        return 0.0


def main():
    folder, since, flags = parse_args(sys.argv)
    files = sorted(glob.glob(os.path.join(folder, '**', 'agent-*.jsonl'), recursive=True))
    if not files:
        sys.exit(f'no agent-*.jsonl files under {folder}')
    for path in files:
        stamps, tools, tokens, events, prompt = audit(path, flags)
        if not stamps or stamps[0][:10] < since:
            continue
        flagged = ', '.join(sorted(set(events))) or '-'
        print(f"{stamps[0][:16]} | {tools:4d} tools | {tokens / 1e6:6.1f} M tok. | "
              f"{minutes(stamps):5.0f} min | {flagged} | {prompt.replace(chr(10), ' ')}")


if __name__ == '__main__':
    main()
