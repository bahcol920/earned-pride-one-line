#!/usr/bin/env python3
"""Write the one-line entry for 'One Line of Earned Pride' to /output/entry.txt."""

import os

ENTRY = "She failed the bar twice; tonight she signed the lease on her own one-room law office, and the pen didn't shake."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY + "\n")
