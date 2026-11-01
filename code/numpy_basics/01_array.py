# -*- coding: utf-8 -*-
"""第 1 课：数组的创建、索引、切片、形状

对应讲义二 §5.1：把 20 级台阶的深度装进数组。

怎么用：把每道题里的 todo(...) 换成真正的代码，然后 `python 01_array.py`。
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
    """造出 1~20 的数组，取出第 3~7 个（含 3 和 7），求和 = 25。"""
    a = np.arange(1, 21)                       # 示例：这一行已经写好了
    b = a[2:7]
    assert int(b.sum()) == 25, f"该是 25，你得到 {b.sum()}"


def q2():
    """1~20 里所有偶数之和 = 110。"""
    a = np.arange(1, 21)
    c = a[a%2==0]
    assert int(c.sum()) == 110, f"该是 110，你得到 {c.sum()}"


def q3():
    """把 1~20 变形成 4 行 5 列，取第一行，求和 = 15。"""
    a = np.arange(1, 21)
    d = a.reshape(4,5)[0]
    assert int(d.sum()) == 15, f"该是 15，你得到 {d.sum()}"


def q4():
    """大于 15 的元素有几个？答案 5。"""
    a = np.arange(1, 21)
    n = a[a>15].size
    assert int(n) == 5, f"该是 5，你得到 {n}"


def q5():
    """20 级台阶的磨损深度从 0.42 均匀递减到 0.31（单位 mm）。"""
    w = np.linspace(0.42,0.31,20)
    assert len(w) == 20, f"该是 20 个，你得到 {len(w)}"
    assert abs(w.max() - 0.42) < 1e-9 and abs(w.min() - 0.31) < 1e-9, \
        f"首尾应为 0.42 / 0.31，你得到 {w.max()} / {w.min()}"


CASES.extend([
    ("q1 切片", q1, ""),
    ("q2 布尔索引", q2, ""),
    ("q3 reshape", q3, ""),
    ("q4 计数", q4, ""),
    ("q5 linspace", q5, ""),
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
