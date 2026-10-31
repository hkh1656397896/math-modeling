# -*- coding: utf-8 -*-
"""依次跑五课，汇总得分。"""
import re
import subprocess
import sys
from pathlib import Path

here = Path(__file__).parent
files = sorted(p for p in here.glob("0*.py") if p.name != "00_warmup.py")
total = 0
passed = 0
for f in files:
    print(f"\n{'=' * 56}\n{f.name}\n{'=' * 56}")
    r = subprocess.run([sys.executable, str(f)], capture_output=True, text=True, encoding="utf-8")
    out = (r.stdout or "") + (r.stderr or "")
    print(out.rstrip())
    m = re.search(r"(\d+)/(\d+) 通过", out)
    if m:
        passed += int(m.group(1))
        total += int(m.group(2))

print(f"\n{'=' * 56}")
print(f"总计：{passed}/{total}")
print("全部通过之后，再回去读讲义二 §5.1~5.3——那些代码就不陌生了。")

