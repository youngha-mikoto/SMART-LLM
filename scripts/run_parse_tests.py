import subprocess
import sys
from pathlib import Path


root = Path(__file__).resolve().parent.parent
for index in range(1, 6):
    plan = root / "logs" / f"ParseTest{index}" / "decomposed_plan.py"
    if index > 1:
        print(flush=True)
    print(f"{'=' * 20} ParseTest{index} {'=' * 20}", flush=True)
    subprocess.run([sys.executable, root / "scripts" / "parse_plan.py", plan], check=True)
