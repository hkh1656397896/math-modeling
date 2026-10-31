# -*- coding: utf-8 -*-
"""第 2 课：向量化运算

对应讲义二 §5.4/§5.5：把逐级计算改成整个数组一次算。

怎么用：把每道题里的 todo(...) 换成真正的代码，然后 `python 02_vectorize.py`。
- ⏳ 还没做（会给你提示）
- ❌ 做了但结果不对（断言会告诉你差多少）
- ✅ 通过
"""
import numpy as np

CASES = []


def todo(hint):
    raise NotImplementedError(hint)


def check(name, fn, hint):
    try:
        fn()
    except NotImplementedError:
        print(f"⏳ {name}：还没做 → {hint}")
        return 0
    except AssertionError as e:
        print(f"❌ {name}：结果不对 → {e}")
        return 0
    print(f"✅ {name}")
    return 1


def q1():
    """1~100 的平方和 = 338350。"""
    x = np.arange(1, 101)
    s = todo("向量化：x**2 会把每个元素平方，再 .sum()")
    assert int(s) == 338350, f"该是 338350，你得到 {s}"


def q2():
    """1~100 里 3 的倍数有几个？答案 33。"""
    x = np.arange(1, 101)
    n = todo("布尔索引 + 求个数：x[x % 3 == 0]")
    assert int(n) == 33, f"该是 33，你得到 {n}"


def q3():
    """sqrt(x) > 5 的元素有几个？答案 75。"""
    x = np.arange(1, 101)
    n = todo("先 np.sqrt(x)，再 (… > 5).sum() —— 布尔数组求 sum 就是数 True")
    assert int(n) == 75, f"该是 75，你得到 {n}"


def q4():
    """把小于 50 的值置 0，其余不变，再求和 = 3825。"""
    x = np.arange(1, 101)
    s = todo("np.where(条件, 替换值, 原数组).sum()")
    assert int(s) == 3825, f"该是 3825，你得到 {s}"


def q5():
    """计算 sum((x+1)^2)，x 取 1~100，答案 348550。"""
    x = np.arange(1, 101)
    s = todo("(x + 1) ** 2 再 .sum()")
    assert int(s) == 348550, f"该是 348550，你得到 {s}"


CASES.extend([
    ("q1 平方和", q1, "(x**2).sum()"),
    ("q2 倍数计数", q2, "len(x[x % 3 == 0])"),
    ("q3 布尔求和", q3, "(np.sqrt(x) > 5).sum()"),
    ("q4 where", q4, "np.where(x < 50, 0, x).sum()"),
    ("q5 复合表达式", q5, "((x + 1) ** 2).sum()"),
])


def main():
    score = 0
    total = 0
    for name, fn, hint in CASES:
        total += 1
        score += check(name, fn, hint)
    print(f"\n{score}/{total} 通过")
    if score < total:
        print("提示：每题失败信息里的箭头右侧就是该填的写法思路。")


if __name__ == "__main__":
    main()
