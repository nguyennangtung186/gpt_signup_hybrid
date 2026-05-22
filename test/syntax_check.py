"""Syntax check: parse AST cho các file vừa sửa."""
import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
files = [
    ROOT / "browser_phase.py",
    ROOT / "mail_providers.py",
    ROOT / "signup.py",
    ROOT / "web" / "manager.py",
]

errors = []
for f in files:
    try:
        ast.parse(f.read_text(encoding="utf-8"), filename=str(f))
        print(f"  OK  {f.relative_to(ROOT)}")
    except SyntaxError as exc:
        errors.append((f, exc))
        print(f"  FAIL {f.relative_to(ROOT)}: {exc}")

if errors:
    print(f"\n{len(errors)} file(s) with syntax errors")
    sys.exit(1)
else:
    print(f"\nAll {len(files)} files OK")
