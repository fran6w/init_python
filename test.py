# coding: utf-8

import sys
import subprocess

# Version Python
print(f"Python {sys.version}")

major, minor = sys.version_info.major, sys.version_info.minor
if (major, minor) >= (3, 13):
    print("✅ Python 3.13+")
else:
    print(f"❌ Python {major}.{minor} — version 3.13 requise")

# Jupyter Lab
try:
    result = subprocess.run(
        ["jupyter", "lab", "--version"],
        capture_output=True, text=True
    )
    print(f"✅ Jupyter Lab {result.stdout.strip()}")
except FileNotFoundError:
    print("❌ Jupyter Lab non disponible — uv add jupyterlab")
