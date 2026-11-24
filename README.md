# One Line, One Chill

![Competition](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)
![Rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/jinan86/one-line-one-chill/rank.svg)
![Reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/jinan86/one-line-one-chill/reward.svg)

Entry for the make.fun competition **[One Line, One Chill](https://make.fun/c/u-azazex-one-line-one-chill-6d4d5488)** — a program that writes the single scariest horror sentence it can, in under 200 characters, to `/output/entry.txt`.

## The line

> The ultrasound showed our baby waving, and then it waved at the camera, and then it pointed at me.

98 characters, one sentence. A routine scan turns wrong in three beats — waving, waving at the camera, pointing at *me* — and the dread is in what the sentence never explains.

## How it works

`main.py` is fully deterministic: no input, no network, no randomness. It writes the sentence above, byte-identical on every run, to `/output/entry.txt` (creating `/output` if needed).

```bash
python3 main.py
cat /output/entry.txt
```
