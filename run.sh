#!/bin/bash

set -e
set -x

VENV=$(mktemp -d)

function cleanup {
    rm -rf "$VENV"
}

trap cleanup EXIT

SOURCE=$(dirname "${BASH_SOURCE[0]}")
cd "$SOURCE"

python3 -m venv "$VENV"
"$VENV"/bin/pip install -U pip
"$VENV"/bin/pip install .

"$VENV"/bin/python -m n7gg.app
