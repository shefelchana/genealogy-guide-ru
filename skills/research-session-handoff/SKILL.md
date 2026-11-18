---
name: research-session-handoff
description: Saves the full state of a genealogy research session before it ends or is compacted, and restores it at the start of the next one. On save — records unrecorded findings, updates hypotheses, the search log and lessons, and rewrites the "continue from here" file (current question, running agents with logs and resume points, what waits for the human — captchas, VPN, logins, decisions — next steps). On resume — reads that file and the project files, checks which background tasks are alive, rebuilds the picture in a few lines and confirms it with the user before searching. Use whenever a session is about to end, the context is about to be compacted, or work resumes after a break — even if the user only says "save everything", "I am about to compact the context", "let's wrap up", "continue from where we left off", "what is still pending". NOT for the first conversation when no project files exist — use genealogy-intake; NOT for the working cycle mid-session (next question, recording a find) — use organizing-genealogy-research. Also triggers on Russian requests: «сохрани всё», «я сожму контекст», «закругляемся», «продолжи с того места», «что у нас висит».
---

# Saving and resuming a research session

A new session remembers nothing of the previous one, and compacting a conversation loses exactly the details: frame numbers, exact quotations, the names of background agents, where they stopped. Everything needed tomorrow must lie **in the project files**, not in the conversation. This skill is two rituals: "save" and "resume".

## Saving ("save everything", end of session, before compaction)

Do it in order. Each step closes a specific loss.

1. **Unrecorded finds.** Go through the conversation from the end to the beginning. Every find not yet in the findings log is recorded now: the source with its archival reference, where the scan is (site, frame, link), a verbatim quotation, confidence, "verified against the scan: yes/no". Mark what is unverified as unverified, not as "found".
2. **Persons.** Everything that changed about specific people goes into their cards.
3. **Hypotheses.** Update the status in the first line: 🟢 confirmed (by what) / 🟡 open, strong version / ⚪ not tested / 🔴 withdrawn (why). If a hypothesis has been weakened, record by what.
4. **Search log.** Every search of the session, **including empty ones**: where, what, which spellings, how, coverage, result. An empty search without coverage will be repeated a month later.
5. **Background agents.** For each one launched in this session:
   - the name or task identifier;
   - the task in one line and the path to the task file;
   - the path to the coverage log and the folder of crops;
   - status: working / finished / dropped / stopped at a captcha;
   - **the resume point**: the last frame read or the last query;
   - whether the report has been accepted (finds checked against the scan?) or not yet.
   This is what is lost most in compaction. Without a resume point the agent's work will have to start over.
6. **What waits for the human.** Concretely and with the place of action: "pass the captcha on site X in agent Y's tab", "switch off the VPN for site Z", "log in to the account", "decide whether to enter N into the tree", "ask your aunt about …". The human will see this list first.
7. **Next steps.** Not "continue the search", but the first executable step: "open the film …, frame 312, finish reading the 1869 book; control record — No. 41 on frame 224".
8. **Lessons.** What worked, what slowed things down, which technique saved time. Write them in a separate methodology file in the form `assets/lessons-entry.md`, not in "Continue from here": lessons accumulate, while the state is overwritten.
9. **Rewrite "Continue from here"** (CONTINUE-FROM-HERE.md) using the template `assets/continue-from-here.md`. The top of the file must fit on one screen: the current question, what waits for the human, the next step. Move outdated material to the "History of lines of inquiry" section at the bottom or to an archive file, but do not leave it at the top.
10. **Check what was recorded.** Reread "Continue from here" through the eyes of a new session: is it enough to continue without reading the conversation? Do all the file paths exist?
11. **Tell the human** briefly: what has been saved, what awaits them, where the next session will begin.

### Rules for recording
- Add to the lessons file only a lesson that actually appeared in the session (what broke or worked); do not invent a lesson to fill space.
- Write **facts and addresses**, not a retelling of the conversation. "The agent checked 80 frames" is worse than "frames 210–290, male entries 1–163, control No. 41 found".
- Give file paths from the project root; links to scans in full.
- The word "proven" only by the criteria of proof (skill `verifying-genealogy-findings`). Otherwise "strong version".
- Do not write passwords, cookies, keys or DNA kit numbers in files. Write only "login needed on site X".
- If time is short, save in this order: finds → agents → waits for the human → next step. Lessons can be added in the next session.

## Resuming ("continue", "where did we stop", start of session)

1. **Read "Continue from here"** (CONTINUE-FROM-HERE.md) in full. Then what it refers to: the file for the current line of inquiry, the latest entries of the findings log and the search log, the hypothesis we are testing.
2. **Check the background tasks.** For each agent on the list:
   - if the environment shows a list of background tasks — look at the status;
   - look at the time of the last change of the agent's log and the last line in it;
   - if the agent has finished and the report has not been accepted — accept it by the rules for accepting results: checking finds against the frame, the control record, coverage, access errors;
   - if the agent dropped — **do not "wake" the old one**; offer to launch a new one for the remainder per the log, from the resume point.
3. **Ask the human about what was waiting for them**: was the captcha passed, is the VPN off, has a decision been made, what did the relatives say. Do not assume it was done.
4. **Rebuild the picture in 5–7 lines**: the current question; what is already known about it; what was done last time; what has changed; the proposed first step. Let the human confirm or correct. **The reply to the human is no longer than 10 lines:** the picture → a question about what was waiting for them (captcha, VPN, decision) → one proposed step → wait for the answer. Details are in the files, not in the chat. An agent standing at a captcha has not "dropped": it is continued from the same frame after the captcha; a new one is launched only if the connection dropped.
5. **Before any new search** — search your own files by surname, place and given name. Otherwise it is easy to rediscover what is already found.
6. If there is no "Continue from here" or it is outdated — assemble the picture from the findings log, the search log and the hypotheses (the latest entries by date) and first create the file from the template.

## When to save without waiting to be asked

- after each confirmed find (just the find — at once);
- before launching agents on long work;
- when the conversation has become long and compaction is near;
- before changing the line of inquiry: close the old one with the entry "closed because…", not by quietly letting it vanish.

See also the skills: `organizing-genealogy-research` (structure of the project files and the course of work within a session), `orchestrating-genealogy-agents` (accepting agents' reports), `genealogy-intake` (the first conversation, when there are no files yet).
