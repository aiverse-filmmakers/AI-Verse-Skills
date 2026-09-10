#!/usr/bin/env python3
"""Public compatibility entrypoint for the AI-Verse Skills installer.

The lifecycle implementation remains in ``aiverse_skills_v3``. Provider Contract
v1 publication is applied here so every supported CLI operation uses the same
manifest/index validation hooks without duplicating lifecycle ownership.
"""
try:
    from . import aiverse_skills_v3 as _impl
    from .provider_contract_v1 import apply_provider_contract_v1
except ImportError:
    import aiverse_skills_v3 as _impl
    from provider_contract_v1 import apply_provider_contract_v1

apply_provider_contract_v1(_impl)

# Preserve the established import surface for callers that import this module.
for _name in dir(_impl):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_impl, _name)


if __name__ == "__main__":
    _impl.main()
