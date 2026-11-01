# -*- coding: utf-8 -*-
"""第 4 课：统计函数

对应讲义二 §5.3/§5.5：中位数、分位数、直方图、截尾平均。

怎么用：把每道题里的 todo(...) 换成真正的代码，然后 `python 04_stats.py`。
- ⏳ 还没做（会给你提示）
- ❌ 做了但结果不对（断言会告诉你差多少）
- ✅ 通过
"""
import numpy as np

CASES = []


def todo():
    raise NotImplementedError("这一题还没写")


def check(name, fn, hint):
    try:
        fn()
    except NotImplementedError:
        print(f"⏳ {name}：还没做")
        return 0
    except AssertionError as e:
        print(f"❌ {name}：结果不对 → {e}")
        return 0
    except Exception as e:
        print(f"❌ {name}：出错了（{type(e).__name__}: {e}）")
        return 0
    print(f"✅ {name}")
    return 1


def q1():
    """一万个 N(100, 15) 的数，均值和中位数都应 ≈ 100。"""
    rng = np.random.default_rng(7)
    x = rng.normal(100, 15, 10000)
    m = todo()
    med = todo()
    assert abs(m - 100) < 1 and abs(med - 100) < 1, f"都该接近 100，你得到 {m} / {med}"


def q2():
    """90% 分位应该落在 117~121 之间（理论值 100 + 1.28×15 ≈ 119.2）。"""
    rng = np.random.default_rng(8)
    x = rng.normal(100, 15, 10000)
    p = todo()
    assert 117 < p < 121, f"该在 117~121，你得到 {p}"


def q3():
    """np.histogram 分 10 个箱，箱内计数加起来必须等于样本数。"""
    rng = np.random.default_rng(9)
    x = rng.normal(0, 1, 5000)
    counts, edges = todo()
    assert len(counts) == 10 and len(edges) == 11, f"箱数不对：{len(counts)} / {len(edges)}"
    assert int(counts.sum()) == 5000, f"计数和该是 5000，你得到 {counts.sum()}"


def q4():
    """截尾平均：去掉两端各 5% 再取均值，应该更稳（≈100）。"""
    rng = np.random.default_rng(10)
    x = rng.normal(100, 15, 10000)
    lo = todo()
    hi = todo()
    trimmed = todo()
    assert abs(trimmed - 100) < 1, f"该接近 100，你得到 {trimmed}"


def q5():
    """np.std 默认除 n（总体），ddof=1 才是除 n-1（样本）。两种差多少？"""
    rng = np.random.default_rng(11)
    x = rng.normal(0, 1, 20)
    s0 = todo()
    s1 = todo()
    assert s0 < s1, f"ddof=1 应该更大，你得到 {s0} / {s1}"


CASES.extend([
    ("q1 均值中位数", q1, ""),
    ("q2 90% 分位", q2, ""),
    ("q3 直方图", q3, ""),
    ("q4 截尾平均", q4, ""),
    ("q5 标准差", q5, ""),
])


def main():
    score = 0
    total = 0
    for name, fn, hint in CASES:
        total += 1
        score += check(name, fn, hint)
    print(f"\n{score}/{total} 通过")
    if score < total:
        print("卡住超过 10 分钟，再去翻 solutions.txt。")


if __name__ == "__main__":
    main()
