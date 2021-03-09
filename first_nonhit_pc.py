#!/usr/bin/env python3
import sys
from collections import deque

HISTORY_LEN = 16

# jvo@Jorens-Mac-mini SameBoy % ./first_nonhit_pc.sh /tmp/pc_file.txt ~/Downloads/gb_emu_pc-2.log
# First PC in Sameboy but not gb-emu is 0xffbc
with open(sys.argv[1], "r") as sameboy_pcs_file:
    with open(sys.argv[2], "r") as gb_emu_pcs_file:
        gb_emu_pcs = set(gb_emu_pcs_file.readlines())
        seen_pcs = set()
        history = deque()

        for sameboy_pc in sameboy_pcs_file.readlines():
            history.append(sameboy_pc.strip())

            if len(history) > HISTORY_LEN:
                history.popleft()

            if sameboy_pc not in seen_pcs and sameboy_pc not in gb_emu_pcs:
                print(f"First PC in Sameboy but not gb-emu is {sameboy_pc.strip()}. History:")
                print(history)
                break

            seen_pcs.add(sameboy_pc)