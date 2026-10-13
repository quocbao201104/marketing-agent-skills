#!/usr/bin/env python3
"""Convenience root wrapper for sync-routing-index.py."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

SKILL_SCRIPTS = (
    Path(__file__).resolve().parents[1]
    / "skills"
    / "marketing-agent-skills"
    / "scripts"
)

script_path = SKILL_SCRIPTS / "sync-routing-index.py"
spec = importlib.util.spec_from_file_location("sync_routing_index", script_path)
if spec is None or spec.loader is None:
    sys.exit("FAIL\tcannot load sync-routing-index.py")

module = importlib.util.module_from_spec(spec)
sys.modules["sync_routing_index"] = module
spec.loader.exec_module(module)

if __name__ == "__main__":
    raise SystemExit(module.main())
