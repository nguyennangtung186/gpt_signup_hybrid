"""Import check: verify modules can be imported."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT.parent))

try:
    from gpt_signup_hybrid.mail_providers import (
        DongVanFBOutlookProvider,
        OutlookMailProvider,
        build_provider_dongvanfb,
        build_provider_outlook,
    )
    print("  OK  mail_providers imports")
except Exception as exc:
    print(f"  FAIL mail_providers: {exc}")
    sys.exit(1)

try:
    from gpt_signup_hybrid.signup import _build_mail_provider
    print("  OK  signup imports")
except Exception as exc:
    print(f"  FAIL signup: {exc}")
    sys.exit(1)

print("\nAll imports OK")
