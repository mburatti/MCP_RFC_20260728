#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${SCRIPT_DIR}/.venv"
PYTHON_BIN="${VENV_DIR}/bin/python3.14"

if [[ ! -d "${VENV_DIR}" ]]; then
  python3.14 -m venv "${VENV_DIR}"
fi

exec "${PYTHON_BIN}" "${SCRIPT_DIR}/client.py"
