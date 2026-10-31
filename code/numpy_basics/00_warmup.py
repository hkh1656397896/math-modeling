# -*- coding: utf-8 -*-
"""第 0 课：numpy 热身（全是写好的，不用你填空）

每行代码后面 `# →` 就是它**真实跑出来的输出**，可以直接对照。
完整输出另存为 00_warmup_输出.txt（内容一样，只是没有代码）。

怎么用：
1. 先跑一遍，逐行对注释里的输出
2. 再**改一处**（每节末尾都有一句"试着改…"），再跑，看输出怎么变
3. 十二节跑完，再回去做 01~05 的填空

跑法：
    cd C:\\Users\\Lenovo\\Desktop\\数学建模\\code\\numpy_basics
    C:\\Users\\Lenovo\\Desktop\\Python作业\\数模练习\\.venv\\Scripts\\python.exe 00_warmup.py
"""
import numpy as np

line = lambda s="": print(("\n" + "─" * 56 + "\n" + s) if s else "")

# ── 1. 为什么要有 numpy：列表不能整体运算 ──────────────────
line("1. 列表 vs 数组")
lst = [1, 2, 3]
arr = np.array([1, 2, 3])
print("列表 lst * 2 =", lst * 2, "  ← 复制了三遍，不是每个数乘 2")   # → [1, 2, 3, 1, 2, 3]
print("数组 arr * 2 =", arr * 2, "  ← 每个元素都乘 2")              # → [2 4 6]
print("列表 lst + 1 会报错；数组 arr + 1 =", arr + 1)                # → [2 3 4]
# 试着改：把 [1, 2, 3] 改成 [5, 10, 15]，看两种写法的差别还在不在

# ── 2. 造数组的四种常用方式 ───────────────────────────────
line("2. 造数组")
print("np.array([4, 8, 15])      →", np.array([4, 8, 15]))          # → [ 4  8 15]
print("np.arange(1, 21)          → 1~20 的整数")                     # → 1~20 的整数（省得列出来）
print("np.linspace(0, 1, 5)      →", np.linspace(0, 1, 5), "（含两端，等间距 5 个）")
#                                                                     # → [0.   0.25 0.5  0.75 1.  ]
print("np.zeros(3) / np.ones(3)  →", np.zeros(3), np.ones(3))        # → [0. 0. 0.] [1. 1. 1.]
# 试着改：arange 的第二个参数改成 11，元素个数少了一半吗？

# ── 3. 形状、元素数、类型 ─────────────────────────────────
line("3. 形状")
a = np.arange(1, 21)
print("a =", a)                                                      # → [ 1  2  3 ... 19 20]
print("a.shape =", a.shape, " a.size =", a.size, " a.dtype =", a.dtype)
#                                                                     # → (20,)  a.size = 20  a.dtype = int64
# 试着改：a = np.linspace(0, 1, 21) 之后，size 还是 20 吗？dtype 变了吗？

# ── 4. 取元素：索引与切片 ─────────────────────────────────
line("4. 索引与切片（左闭右开）")
print("a[0]      =", a[0], "（第一个）")                            # → 1
print("a[-1]     =", a[-1], "（最后一个）")                          # → 20
print("a[2:7]    =", a[2:7], "（第 3 到第 7 个，下标 2~6）")          # → [3 4 5 6 7]
print("a[:5]     =", a[:5], "（前 5 个）")                            # → [1 2 3 4 5]
print("a[::5]    =", a[::5], "（每 5 个取一个）")                     # → [ 1  6 11 16]
# 试着改：a[2:7] 改成 a[2:8]，会变成几个数？

# ── 5. 向量化：整个数组一起算 ─────────────────────────────
line("5. 向量化")
x = np.arange(1, 6)
print("x        =", x)                              # → [1 2 3 4 5]
print("x ** 2   =", x ** 2)                         # → [ 1  4  9 16 25]
print("np.sqrt(x) =", np.sqrt(x))                   # → [1.         1.41421356 1.73205081 2.         2.23606798]
print("1 / x    =", 1 / x)                          # → [1.         0.5        0.33333333 0.25       0.2       ]
# 这就是 numpy 的全部魔法：不用写 for

# ── 6. 聚合：一次算完 ─────────────────────────────────────
line("6. 求和、均值、最大")
print("x.sum()    =", x.sum())                      # → 15
print("x.mean()   =", x.mean())                     # → 3.0
print("x.max(), x.min() =", x.max(), x.min())       # → 5 1
print("平方和 (x**2).sum() =", (x ** 2).sum())      # → 55
# 试着改：x 改成 np.arange(1, 101)，平方和应该是 338350

# ── 7. 筛选：布尔索引 ─────────────────────────────────────
line("7. 布尔索引（这是最常用的技巧）")
mask = x > 3
print("x > 3        =", mask, "（一串 True/False）")     # → [False False False  True  True]
print("x[x > 3]     =", x[x > 3])                        # → [4 5]
print("x[x % 2 == 0]=", x[x % 2 == 0], "（偶数）")        # → [2 4]
print("(x > 3).sum()=", (x > 3).sum(), "（True 的个数）")  # → 2
# 试着改：x > 3 改成 x >= 3，个数会变吗？

# ── 8. 变形：reshape ─────────────────────────────────────
line("8. reshape")
b = np.arange(1, 13)
print("b =", b)                                     # → [ 1  2  3 ... 11 12]
print("b.reshape(3, 4) =\n", b.reshape(3, 4))       # → 3 行 4 列，见下面三行
#                                                     #  [[ 1  2  3  4]
#                                                     #   [ 5  6  7  8]
#                                                     #   [ 9 10 11 12]]
print("取第二行 =", b.reshape(3, 4)[1])              # → [5 6 7 8]
# 试着改：改成 reshape(4, 3) 还能跑吗？为什么？

# ── 9. 随机数：一定要设种子 ───────────────────────────────
line("9. 随机数")
rng = np.random.default_rng(42)          # 42 是种子，换个数字结果就不一样
print("normal(0,1,5)      =", rng.normal(0, 1, 5))
#                                  # → [ 0.30471708 -1.03998411  0.7504512   0.94056472 -1.95103519]
print("uniform(0,1,5)     =", np.random.default_rng(42).uniform(0, 1, 5))
#                                  # → [0.77395605 0.43887844 0.85859792 0.69736803 0.09417735]
print("lognormal(0,0.5,5) =", np.random.default_rng(42).lognormal(0, 0.5, 5))
#                                  # → [1.16457771 0.59452527 1.45531969 1.60044603 0.37699717]
rng1 = np.random.default_rng(42).normal(0, 1, 3)
rng2 = np.random.default_rng(42).normal(0, 1, 3)
print("同种子两次生成一致吗？", np.allclose(rng1, rng2))              # → True
# 试着改：种子 42 改成 7，再用 np.allclose 比一次，还一致吗？

# ── 10. 统计函数 ─────────────────────────────────────────
line("10. 统计")
data = np.random.default_rng(7).normal(100, 15, 10000)
print("mean   =", round(data.mean(), 2))             # → 99.82
print("median =", round(np.median(data), 2))         # → 99.8
print("p90    =", round(np.percentile(data, 90), 2), "（90% 的数比它小）")   # → 118.89
counts, edges = np.histogram(data, bins=5)
print("直方图 5 箱计数 =", counts, " 合计 =", counts.sum())
#                                  # → [ 177 2678 5524 1566   55]  合计 = 10000
# 试着改：bins=5 改成 bins=10，计数会变，但合计永远是 10000

# ── 11. 三个最常见的坑 ──────────────────────────────────
line("11. 三个坑")
# 坑 1：lognormal 的 mean 是「对数的均值」，不是中位数
bad = np.random.default_rng(1).lognormal(mean=2e-6, sigma=0.3, size=2000)
good = np.random.default_rng(1).lognormal(mean=np.log(2e-6), sigma=0.3, size=2000)
print("lognormal(mean=2e-6) 的中位数 =", f"{np.median(bad):.6f}", " ← 错觉：它≈1，不是 2e-6")
#                                  # → 0.993100
print("lognormal(mean=log 2e-6) 的中位数 =", f"{np.median(good):.2e}", " ← 这才对")
#                                  # → 1.99e-06
# 坑 2：切片是「视图」，改它会改原数组
c = np.arange(10)
d = c[:3]
d[0] = 999
print("改了 d[0] 之后 c =", c, " ← 原数组也变了；要独立就 c[:3].copy()")
#                                  # → [999   1   2   3   4   5   6   7   8   9]
# 坑 3：整数除法
print("7 / 2 =", 7 / 2, "  7 // 2 =", 7 // 2, "  np.arange(5) / 2 =", np.arange(5) / 2)
#                                  # → 3.5   3   [0.  0.5 1.  1.5 2. ]

# ── 12. 预告：第 5 课那道题，其实就一行 ──────────────────
line("12. 预告")
W = np.array([0.42, 0.41, 0.40, 0.39, 0.39, 0.38, 0.37, 0.36, 0.36, 0.35,
              0.35, 0.34, 0.34, 0.33, 0.33, 0.32, 0.32, 0.31, 0.31, 0.31])
V = (np.pi * 90 * 150 * W).sum()
print("20 级台阶的磨损体积合计 V =", round(V, 1), "mm³")              # → 300697.5
print("单次磨损 v0 = V / 6.059e6 =", round(V / 6.059e6, 5), "mm³/次")   # → 0.04963
print("使用年数 T = 6.059e6 / (365 * 110.7) =", round(6.059e6 / (365 * 110.7), 1), "年")   # → 150.0
print("\n上面这三行，就是讲义二 §5.1~5.2 的核心。现在你已经看懂了。")
