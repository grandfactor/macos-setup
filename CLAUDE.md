Read this first. It is deliberately **not** specific to this repository; it describes how to work in any environment where the sandbox can vanish at any moment. Repo-specific state and history live in `PROGRESS.md`.

## 1. The environment resets. Plan for it.

The sandbox you are running in is **ephemeral and can be reset without warning** — mid-command, mid-file-write, mid-thought. When that happens:

- **Everything not pushed to the git remote is gone.** The working tree, uncommitted edits,
  local-only commits, installed packages (`pip`, `npm`, Playwright browsers…), background
  servers, temp files under `/tmp`, shell history — all of it.
- **Your conversation context may also be compacted or truncated.** You will not reliably
  remember what you were doing. The only durable memory is what is in the remote repository.
- **The tool call that was in flight may or may not have taken effect.** After a reset you must
  verify actual state (`git status`, `git log`, `ls`, read the file) before assuming anything.
- Resets are not rare. In one working session this repo saw **six** resets in about two hours.

Therefore the single most important rule:

> **A change that is not pushed does not exist.** Commit and push after *every* meaningful step —
> every file written, every script created, every section edited. Not at the end. Not "after I
> test it." Immediately.

## 2. Commit-per-step workflow

```
edit one thing  →  git add -A && git commit -m "scope: what changed"  →  git push origin main
```

- **Granularity:** one logical change per commit (one chapter, one script, one JSON edit,
  one CSS rewrite). Small commits cost nothing; a lost hour costs an hour.
- **Push immediately after committing.** A local commit is worth exactly as much as an
  uncommitted file after a reset: nothing.
- **Never batch.** Do not write five files and then commit. Write one, commit, push, write the next.
- **Big generated artifacts:** if a step regenerates many files (a build), run it and commit
  the result as its own commit so a reset in the middle of the next step doesn't lose the build.
- **Branch policy** push straight to main.

### Recovering after a reset

1. `cd <repo> && git status --short && git log --oneline -3 && git fetch && git status -sb`
2. If the tree is clean and `main == origin/main`, nothing was lost — continue from the last
   log entry in `PROGRESS.md`.
3. If there are unpushed local commits (`ahead N`), push them first, before anything else.
4. If a tool call was interrupted, **read the target file / list the directory** to see whether
   it landed. Redo only what's missing. Never blindly re-run a write.
5. Re-authenticate if needed (e.g. `setup_github_environment`) — credentials can be reset too.
6. Reinstall any tooling you need (it's gone). Prefer stdlib / no-dependency scripts so that
   reinstalling is rarely necessary.

## 3. Save research and reasoning as files, not just in your head

Anything you learn that you'd hate to re-derive — web research, benchmark numbers, decisions,
"why we did it this way" — goes into a file in the repo **as soon as you have it**, then gets
pushed. A `research/` directory of dated Markdown notes is a good pattern. Context windows get
compacted; files don't.

## 4. Keep a `PROGRESS.md` (agent memory)

One file, appended to after every chunk of work, with terse dated entries:

- what was done and pushed,
- key findings / decisions,
- **exactly what to do next** (so the post-reset you can resume without re-analysis),
- known problems.

Read it first when you start or resume. Update it *before* starting a long or risky step, not
after, so the plan survives even if the step doesn't.

 Working-directory discipline

- Each shell invocation may start in a different cwd. **Always `cd` to the repo explicitly** at the
  start of every command (`cd /path/to/repo && …`).
- Write only inside the repo (plus `/tmp` for throwaway artifacts you don't mind losing).
- Long-running processes (dev servers) die on reset. Start them in the background, don't depend
  on them being alive later, and re-check before using them.

Things that look safe but aren't

| Looks safe | Why it isn't |
|---|---|
| "I'll commit after I finish these three files" | Reset after file two loses all three (and your memory of the plan). |
| A local commit without a push | Identical to no commit after a reset. |
| Installing a dependency once at the start | Gone on reset; scripts that need it break silently. Re-check or reinstall. |
| Keeping the todo list only in the chat | Compaction erases it. Mirror it into `PROGRESS.md`. |
| Assuming an interrupted write landed | Verify by reading the file. |
| Big single `Write` of a huge file | If output is truncated or the sandbox resets, you get nothing. Write in parts, commit each. |

