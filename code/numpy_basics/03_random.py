# -*- coding: utf-8 -*-
"""第 3 课：随机数与分布

对应讲义二 §5.3：蒙特卡洛全靠这四个函数。

怎么用：把每道题里的 todo(...) 换成真正的代码，然后 `python 03_random.py`。
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
    """固定种子后，两次生成的随机数必须一模一样。"""
    rng = np.random.default_rng(42)          # 示例：现代写法的随机数生成器
    a = rng.normal(0, 1, 10)
    rng2 = todo()
    assert np.allclose(a, rng2), "两个序列不一样：种子要一模一样"


def q2():
    """lognormal(mean=0, sigma=0.5) 的中位数应该 ≈ 1（不是 0）。"""
    rng = np.random.default_rng(1)
    s = todo()
    med = todo()
    assert 0.9 < med < 1.1, f"中位数应接近 1，你得到 {med}"


def q3():
    """uniform(0,1) 抽 1000 个，均值应该 ≈ 0.5。"""
    rng = np.random.default_rng(2)
    u = todo()
    m = todo()
    assert 0.45 < m < 0.55, f"均值应接近 0.5，你得到 {m}"


def q4():
    """陷阱现场：mean 参数是**对数**的均值。

    np.random.lognormal(mean=2e-6) 的中位数 ≈ 1，不是 2e-6 —— 这是讲义二 5.3.1
    讲的那个"把 K 放大 500 倍"的坑。正确写法是先取对数。
    """
    rng = np.random.default_rng(3)
    wrong = todo()
    rng2 = np.random.default_rng(3)
    right = todo()
    assert 0.9 < wrong < 1.1, f"错写法的中位数应接近 1，你得到 {wrong}"
    assert 1e-7 < right < 1e-5, f"对写法的中位数应接近 2e-6，你得到 {right}"


def q5():
    """用 lognormal 造 5000 个使用年数，问 90% 分位落在哪个量级。"""
    rng = np.random.default_rng(5)
    years = todo()
    p90 = todo()
    assert 200 < p90 < 800, f"90% 分位应在几百年级别，你得到 {p90}"


CASES.extend([
    ("q1 可复现", q1, ""),
    ("q2 中位数", q2, ""),
    ("q3 均匀分布", q3, ""),
    ("q4 lognormal 陷阱", q4, ""),
    ("q5 分位数量级", q5, ""),
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
