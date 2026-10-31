# numpy 最小集（5 课 · 25 题）

目标：三天内把 numpy 用到"看得懂讲义二 §5 代码"的程度。**不追求全面**，
只学数模真正用到的 20%：数组、切片、向量化、随机、统计。

## 怎么跑

```
cd C:\Users\Lenovo\Desktop\Python作业\数模练习\numpy_basics
..\.venv\Scripts\python.exe run_all.py
```

一题一题做：把 `todo("...")` 换成真正的代码，再跑一次。三种反馈：

- ⏳ 还没做（提示里就是该写的思路）
- ❌ 做了但结果不对（断言会说"该是多少，你得到多少"）
- ✅ 通过

## 五课对应关系

| 文件 | 内容 | 对应讲义 |
|---|---|---|
| 01_array.py | 建数组、切片、reshape、布尔索引 | 讲义二 §5.1 |
| 02_vectorize.py | 向量化、where、布尔求和 | 讲义二 §5.4 §5.5 |
| 03_random.py | normal / uniform / lognormal、种子、分位数 | 讲义二 §5.3 |
| 04_stats.py | mean / median / percentile / histogram / 截尾 | 讲义二 §5.3 §5.5 |
| 05_two_ways.py | 同一公式 for 版 vs numpy 版（真磨损链） | 讲义二 §5.1~5.2 |

## 卡住了怎么办

1. 先看提示文字（箭头右边就是写法思路）
2. 超过 15 分钟还卡：看 `solutions.txt` 的对应一句
3. 仍然不懂：把"这一行在干什么"记进 `notes.md`，攒够三条再来问

## 哪些可以跳过（现在别学）

`np.einsum`、`np.tensordot`、stride tricks、`np.memmap`、多维高级索引的花活、
`np.polynomial`、结构化数组——这些半年内都用不上。

