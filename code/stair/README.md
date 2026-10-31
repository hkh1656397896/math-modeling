# 楼梯这一题：补充脚本

`stair_extra.py` 是讲义二 §5.10 那四块的实现，只用 numpy + math：

| 函数 | 干什么 | 实跑结果 |
|---|---|---|
| `analytic_sigma` | 一阶误差传播，算 σ_q/q | 0.847（蒙特卡洛给 1.088） |
| `decay_profile` | 人流沿台阶递减 rᵢ = wᵢ/w₁ | 前段 0.95 / 后段 0.29 ⇒ 71% 的人没走到第 9 级 |
| `t2_window` | 新增部件的年代区间（四条证据取交集） | T₂ ∈ [1930, 1960] |
| `interval_table` | 三套区间并列 + 宽度自检 | 463 → 150 → 67 年 |

跑法：

```
C:\Users\Lenovo\Desktop\Python作业\数模练习\.venv\Scripts\python.exe stair_extra.py
```

主脚本 `stair_model.py` 按讲义二 §5 自己写，不在这里。
