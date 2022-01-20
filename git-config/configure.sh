#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

# To activate git hooks and enable verifications after or before git commands executions
REPO_ROOT="$(git rev-parse --show-toplevel)"
pushd "${REPO_ROOT}" >/dev/null
    git config core.hooksPath git-config/hooks
popd >/dev/null
