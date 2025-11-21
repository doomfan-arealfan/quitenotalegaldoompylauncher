import subprocess
import os

# Full path to your IWAD
wad_path = "/home/schule/doom/DOOM1.WAD"

# Check if the file exists
if not os.path.exists(wad_path):
    raise FileNotFoundError(f"WAD not found: {wad_path}")

# Launch Chocolate Doom with your WAD
subprocess.run(["chocolate-doom", "-iwad", wad_path])

