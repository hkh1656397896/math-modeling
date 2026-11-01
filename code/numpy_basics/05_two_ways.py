# -*- coding: utf-8 -*-
"""第 5 课：同一件事，两种写法

对应讲义二 §5.1~5.2：用真实的磨损链参数，for 版与 numpy 版对照。

怎么用：把每道题里的 todo(...) 换成真正的代码，然后 `python 05_two_ways.py`。
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


# 这一课把磨损链真算一遍：同一件事，先 for 循环，再 numpy 向量化。

A_MM = 90.0        # 踏面凹陷半轴 a（mm）
B_MM = 150.0       # 踏面凹陷半轴 b（mm）
W = [0.42, 0.41, 0.40, 0.39, 0.39, 0.38, 0.37, 0.36, 0.36, 0.35,
     0.35, 0.34, 0.34, 0.33, 0.33, 0.32, 0.32, 0.31, 0.31, 0.31]
H_HARD = 3.2       # 硬度（相对值）
K, F, S = 2.0e-6, 1.0, 1.0   # 磨损系数、形态因子、滑动距离
N_IMPACTS = 6.059e6
Q_BAR = 110.7


def q1():
    """for 循环版：每级体积 = π·a·b·w，总和 V。"""
    total = 0.0
    for w in W:
        total += np.pi*A_MM*B_MM*w
    assert 290000 < total < 310000, f"该在 30 万 mm³ 上下（20 级之和），你得到 {total}"


def q2():
    """numpy 版：把同一个 V 用一行算出来，两版必须相等。"""
    w = (np.pi*A_MM*B_MM*np.array(W)).sum()
    v_np = w
    v_loop = sum(np.pi * A_MM * B_MM * x for x in W)
    assert abs(v_np - v_loop) < 1e-9, f"两版不一致：{v_np} vs {v_loop}"


def q3():
    """单次磨损 v0 = V/N，再算使用年数 T = N/(365·q̄)，应 ≈ 150 年。"""
    V = np.pi * A_MM * B_MM * np.array(W).sum()
    v0 = V/N_IMPACTS
    T = N_IMPACTS/(365*Q_BAR)
    assert 0.04 < v0 < 0.06, f"v0 该在 0.05 mm³/次 上下，你得到 {v0}"
    assert 145 < T < 155, f"T 该约 150，你得到 {T}"


def q4():
    """向量化算加权平均磨损深度（权重取级数 20,19,...,1）。"""
    w = np.array(W)
    idx = np.arange(20, 0, -1)
    avg = np.average(w,weights=idx)
    assert 0.36 < avg < 0.39, f"该在 0.37 上下（越靠前的台阶磨损越深、权重也越大），你得到 {avg}"


def q5():
    """同一件事，向量化快多少？用 perf_counter 量一下（相对值即可）。"""
    import time
    t0 = time.perf_counter()
    s1=0.0
    for _ in range(200):
        s1 = sum(np.pi * A_MM * B_MM * x for x in W)
    t1 = time.perf_counter()
    w = np.array(W)
    t2 = time.perf_counter()
    s2=0.0
    for _ in range(200):
        s2 = (np.pi * A_MM * B_MM * w).sum()
    t3 = time.perf_counter()
    assert s1 - s2 < 1e-9, "两种写法结果必须一样"
    print(f"   for 版 {(t1 - t0) * 1000:.1f} ms ／ numpy 版 {(t3 - t2) * 1000:.1f} ms")


CASES.extend([
    ("q1 for 循环算 V", q1, ""),
    ("q2 向量化算 V", q2, ""),
    ("q3 v0 与 T", q3, ""),
    ("q4 加权平均", q4, ""),
    ("q5 性能对比", q5, ""),
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

