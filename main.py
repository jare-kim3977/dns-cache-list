"""DNS Cache List — Print the Windows DNS cache as name, type, and record, or flush after a preview count."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='dns_cache_list',
        description='Print the Windows DNS cache as name, type, and record, or flush after a preview count.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('DNS Cache List')
    print('ipconfig /displaydns as a table.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# cleanup (2026-11-03)
# wip (2026-11-03)
# revisit later (2026-11-03)
# polish (2026-11-04)
# wip (2026-11-05)
# cleanup (2026-11-06)
