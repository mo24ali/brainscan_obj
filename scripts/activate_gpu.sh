#!/usr/bin/env bash

PROJECT_DIR="$HOME/projects/brainscan_ai"
source "$PROJECT_DIR/.venv/bin/activate"

NVIDIA_LIB_DIRS="$(
python -c 'import site,glob,os; print(":".join(p for root in site.getsitepackages() for p in glob.glob(os.path.join(root,"nvidia","*","lib")) if os.path.isdir(p)))'
)"

export LD_LIBRARY_PATH="${NVIDIA_LIB_DIRS}${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"

echo "BrainScan AI environment activated."
echo "Python: $(python --version)"
