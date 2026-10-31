# 数学建模学习笔记

华中农业大学 · 从零开始的建模代码练习（numpy → 复现 → 真数据）

📖 **在线笔记**：`index.html`（GitHub Pages 开启后即可手机访问）

## 里面有什么

| 目录 | 内容 |
|---|---|
| `index.html` | 笔记网页：环境 / numpy 最小集 / 楼梯算例 / 易错点 / 报错速查 / 路线 |
| `code/numpy_basics/` | numpy 五课 25 题（00 热身 + 01~05 填空），带断言验收 |
| `code/stair/` | 楼梯建造年代那道题的补充脚本 `stair_extra.py`（误差传播 / 衰减剖面 / T₂ 区间 / 区间表） |

## 环境

Python 3.12 + numpy 2.5.4 · scipy 1.18.1 · matplotlib 3.11.2 · pandas 3.1.0 · pulp 3.3.2

虚拟环境在 `C:\Users\Lenovo\Desktop\Python作业\数模练习\.venv`（不进仓库），跑法：

```
cd C:\Users\Lenovo\Desktop\数学建模\code\numpy_basics
C:\Users\Lenovo\Desktop\Python作业\数模练习\.venv\Scripts\python.exe run_all.py
```

## 三句话说明这堆东西在干什么

1. **numpy_basics**：补工具。numpy 只学用得上的 20%，学完才能看懂建模代码。
2. **stair**：一个完整的小课题——用台阶磨损反推建造年代。难点不是公式，是"一个方程三个未知"该怎么诚实地回答。
3. **index.html**：把踩过的坑记下来，下次不再踩。

## 注意

- `code/numpy_basics/05_two_ways.py` 里用的是**简化算例**（V ≈ 300 697 mm³），和讲义的标准算例（V = 50 894 mm³）不是同一组数据，别混。
- 主脚本 `stair_model.py` 不在仓库里：它是学习目标，按讲义二 §5 一节一节自己打出来，而不是复制。
