# -*- coding: utf-8 -*-
"""stair_extra.py —— 配合讲义一 4.4.1 / 4.9 / 5.3.1 / 5.4.1 的四块补充代码。

A. analytic_sigma()  —— 一阶误差传播 + 蒙特卡洛互证（5.3.1）
B. decay_profile()   —— 没有更换段时，磨损变浅 = 人流衰减（5.4.1）
C. t2_window()       —— 新增部件（T₂）的"不早于"定年（4.4.1）
D. interval_table()  —— 三套区间并列，防止口径混用（4.9）

只依赖 numpy + math，与 stair_model.py 同源。
"""
import math
import numpy as np

rng = np.random.default_rng(2026)

# ---------------------------------------------------------------- 与 4.3 完全一致的参数
V_MM3 = 50_894.0          # 单级踏面磨损体积，mm³
H_PA = 5.0e9              # 花岗岩硬度，Pa
F_MAIN = 750.0            # 单次法向力，N
S_MAIN = 0.25             # 单次滑移距离，m
K_MED = 2.24e-4           # 磨损系数中位值（由 v₀ = 8.4e-3 mm³/次 反推）
SIG_LN_K = 0.6            # ln K 的标准差（文献跨一个数量级）
F_LO, F_HI = 600.0, 900.0
S_LO, S_HI = 0.15, 0.35
T_LO, T_HI = 60.0, 420.0  # 使用年数先验（年）

V0_MM3 = K_MED * F_MAIN * S_MAIN / H_PA * 1e9     # 单次踩踏磨损体积，mm³
N_IMPACT = V_MM3 / V0_MM3                          # 累计踩踏次数


# ---------------------------------------------------------------- A
def analytic_sigma(n=200_000):
    cv_V = 0.086
    cv_H = 0.15
    cv_K = math.sqrt(math.exp(SIG_LN_K ** 2) - 1)
    cv_F = (F_HI - F_LO) / math.sqrt(12) / ((F_HI + F_LO) / 2)
    cv_s = (S_HI - S_LO) / math.sqrt(12) / ((S_HI + S_LO) / 2)
    cv_T = (T_HI - T_LO) / math.sqrt(12) / ((T_HI + T_LO) / 2)
    quad = np.array([cv_V, cv_H, cv_K, cv_F, cv_s, cv_T])
    sigma_analytic = float(np.sqrt((quad ** 2).sum()))

    K = rng.lognormal(math.log(K_MED), SIG_LN_K, n)
    V = V_MM3 * 1e-9 * (1 + cv_V * rng.standard_normal(n))
    H = H_PA * (1 + cv_H * rng.standard_normal(n))
    F = rng.uniform(F_LO, F_HI, n)
    s = rng.uniform(S_LO, S_HI, n)
    T = rng.uniform(T_LO, T_HI, n)
    q = V * H / (K * F * s * 365 * T)
    q = q[np.isfinite(q)]
    sigma_mc = float(q.std(ddof=1) / q.mean())

    print("=" * 64)
    print("A. 一阶误差传播 vs 蒙特卡洛")
    print("-" * 64)
    print(f"    v₀ = {V0_MM3:.4f} mm³/次   N = {N_IMPACT:.3e} 次")
    for name, cv in zip(["V", "H", "K", "F", "s", "T"], quad):
        print(f"    σ_{name}/{name} = {cv:5.3f}   贡献 {cv**2/sigma_analytic**2*100:5.1f}%")
    print(f"    σ_q/q（一阶公式）= {sigma_analytic:.3f}")
    print(f"    σ_q/q（MC {n//1000}k 次）= {sigma_mc:.3f}  ← 厚尾，一阶会低估")
    print(f"    q̄ 中位 {np.median(q):.0f}，90% [{np.percentile(q,5):.0f}, "
          f"{np.percentile(q,95):.0f}] 人次/日（T~U(60,420) 时）")
    T_post = 2025 - 1871
    print(f"    用合成后的 T = {T_post} 年代入 ⇒ q̄ = {N_IMPACT/(365*T_post):.1f} 人次/日（即 5.4 的 110）")
    return sigma_analytic, sigma_mc


# ---------------------------------------------------------------- B
def decay_profile(n_steps=20, drop_at=9, keep=0.36, decay=0.985, seed=7):
    r = np.random.default_rng(seed)
    w = []
    for i in range(1, n_steps + 1):
        level = 8.0 * decay ** (i - 1)
        if i >= drop_at:
            level *= keep
        w.append(level + r.normal(0, 0.10))
    w = np.clip(np.array(w), 0.05, None)
    ratio = w / w[0]
    print("=" * 64)
    print("B. 没有更换段时的流量衰减（演示数据）")
    print("-" * 64)
    print("    级号:", " ".join(f"{i:4d}" for i in range(1, n_steps + 1)))
    print("    w/w₁:", " ".join(f"{x:4.2f}" for x in ratio))
    print(f"    第 1~{drop_at-1} 级平均到达率 {ratio[:drop_at-1].mean():.2f}，"
          f"第 {drop_at}~{n_steps} 级 {ratio[drop_at-1:].mean():.2f}")
    print(f"    ⇒ 约 {(1-ratio[drop_at-1:].mean())*100:.0f}% 的人没走到第 {drop_at} 级")
    return ratio


# ---------------------------------------------------------------- C
def t2_window(evidence):
    lows = [lo for _, lo, _ in evidence]
    highs = [hi for _, _, hi in evidence]
    lo, hi = max(lows), min(highs)
    print("=" * 64)
    print("C. 新增部件 T₂ 的定年（只报「不早于」）")
    print("-" * 64)
    for name, a, b in evidence:
        print(f"    {name:<22} → [{a}, {b}]")
    if lo <= hi:
        print(f"    交集：T₂ ∈ [{lo}, {hi}]，即「不早于 {lo} 年」")
    else:
        print(f"    交集为空（max 下界 {lo} > min 上界 {hi}）⇒ 证据矛盾，回现场复核")
    return lo, hi


# ---------------------------------------------------------------- D
def interval_table(rows):
    """rows = [(标签, 下界, 中位, 上界)]，打印宽度并检查嵌套关系。"""
    print("=" * 64)
    print("D. 三套区间并列（同一份数据，三种口径）")
    print("-" * 64)
    for name, lo, med, hi in rows:
        print(f"    {name:<16} [{lo:6.0f}, {hi:6.0f}]  中位 {med:6.0f}  宽 {hi-lo:5.0f} 年")
    widths = [hi - lo for _, lo, _, hi in rows]
    print(f"    检查：区间宽度单调收窄 {'✔' if widths == sorted(widths, reverse=True) else '✘'}"
          f"（{widths[0]:.0f} → {widths[-1]:.0f} 年）")


if __name__ == "__main__":
    analytic_sigma()
    decay_profile()
    t2_window([
        ("防滑条：镀锌角钢", 1902, 1960),
        ("螺栓：机制六角头", 1850, 1990),
        ("勾缝：普通硅酸盐水泥", 1900, 1980),
        ("漆层：醇酸漆为最内层", 1930, 1970),
    ])
    interval_table([
        ("① 只用磨损", 1526, 1891, 1989),
        ("② 形制断代", 1750, 1825, 1900),
        ("③ 合成（主结论）", 1836, 1871, 1903),
    ])
    print("=" * 64)

