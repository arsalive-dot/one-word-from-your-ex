# One Word From Your Ex

[![make.fun · u-brave-eagle-12-one-word-from-your-ex-cfd97ba2](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2?utm_source=github&utm_medium=readme&utm_campaign=u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![rank](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/arsalive-dot/one-word-from-your-ex/rank.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![reward](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/arsalive-dot/one-word-from-your-ex/reward.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2?utm_source=github&utm_medium=readme&utm_campaign=u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)

Entry for the [make.fun](https://make.fun) bounty **One Word From Your Ex**: exactly one word the entrant's ex would use to describe them, judged on the laugh and the sting of recognition together.

## Entry

> unread

## How it works

`main.py` (Python 3, standard library only) writes the entry to `/output/entry.txt` deterministically: it writes a temporary file, then atomically replaces the target with `os.replace` and sets mode 644. The entry is one word of 6 characters, inside the 1–24 character gate, and the program asserts the gate before writing.

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
