#!/usr/bin/env python3
"""Compatibility entrypoint for the AI-Verse Skills installer.

The implementation lives in ``aiverse_skills_v3``. This wrapper preserves the
existing script path used by launchers, documentation, CI, and external callers.
"""
try:
    from .aiverse_skills_v3 import *  # noqa: F401,F403
except ImportError:
    from aiverse_skills_v3 import *  # noqa: F401,F403


if __name__ == "__main__":
    main()
