# Навыки (skills) для Claude

| Навык | Когда срабатывает |
|---|---|
| `organizing-genealogy-research` | начало сессии, задания агентам, приём отчётов, «сохрани всё» |
| `verifying-genealogy-findings` | проверить находку, понять, значит ли что-то «не нашёл», варианты написаний, полнотекст genealogyindexer |
| `reading-archive-scans` | читать оцифрованные дела (PDF с Commons и др.), оценить качество скана, карта тома |
| `tracing-revision-records` | идти вглубь по ревизским сказкам 1795–1858 |
| `searching-familysearch-films` | плёнки FamilySearch: каталог → DGS → кадр, границы книг, темп и капчи |
| `searching-jewishgen` | базы JewishGen: поиск, лимит 50 строк, чтение полей, переход к скану |
| `searching-nli-jewish-press` | еврейские газеты в Национальной библиотеке Израиля |
| `reading-hebrew-yiddish-sources` | надгробия, ивритская часть метрик, подписи, газеты на идише; соответствия имён |
| `tracing-emigrants-to-origin` | от документов США/Европы к местечку |

## Установка в Claude Code
Как плагин (навыки + агенты):
```
/plugin marketplace add shefelchana/genealogy-guide-ru
/plugin install genealogy-guide-ru@genealogy-guide-ru
```
Вручную: скопировать папки из `skills/` в `~/.claude/skills/`, файлы из `agents/` — в `~/.claude/agents/`.

## Claude.ai / приложение Claude
Плагины там не работают, но отдельный навык можно загрузить: заархивировать папку навыка (ZIP с `SKILL.md` внутри) и добавить в настройках навыков. Скрипты из `scripts/` в веб-версии могут не запускаться.

## Ограничения
- Навыки не проходят капчи и не входят в аккаунты — это делает человек.
- Сайты меняются: приёмы проверены в сентябре–октябре 2026 г.
