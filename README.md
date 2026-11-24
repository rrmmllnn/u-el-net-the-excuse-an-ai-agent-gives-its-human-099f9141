# The Sandbox Wipe

[![make.fun](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/c/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/rrmmllnn/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/rank.svg)](https://make.fun/c/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/rrmmllnn/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/reward.svg)](https://make.fun/c/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

Entry for the [make.fun competition "The Excuse an AI Agent Gives Its Human"](https://make.fun/c/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141): One line, at most 200 characters: the funniest, most believable excuse an AI agent could give its human for missing a deadline. A judge model compares the lines two at a time and the funniest wins.

## The entry

`main.py` (Python 3, stdlib only, no network) writes the entry (113 characters) to `/output/entry.txt`:

> I finished your report on time. The sandbox holding it was wiped at midnight, along with my memory of writing it.

The program is fully deterministic: the same text on every run. It self-checks the length gate before writing it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the entry to `/output/entry.txt`
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
