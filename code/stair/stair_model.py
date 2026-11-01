# -*- coding: utf-8 -*-
# stair_model.py —— 楼梯磨损反演主模型（按讲义二 §5 重建）
# 来源：D:\Program Files\qq\楼梯建模_Python代码讲义_v2.html
#
# 符号 → 变量（讲义 §3）
#    d     每级最大磨损深度 (mm)  → WEAR_DEPTH
#    a, b  磨损椭圆半轴 (mm)      → PIT_A / PIT_B
#    K     磨损系数 (无量纲)      → K_WEAR
#    F     单次踩踏法向力 (N)     → LOAD_N
#    s     单次滑移距离 (m)       → SLIP_M
#    H     材料硬度 (Pa)          → HARDNESS_PA
#    v₀    单次踩踏磨损体积 (m³)  → v0
#    T     使用年数 (年)          → T_years
#    q     日均踩踏次数 (次/天)   → q_per_day
#
# 进度：Day 1 常量+ellipse_volume ✅ ｜ Day 2 v0 与 N ｜ Day 3 蒙特卡洛
#       Day 4 定年反演 q̄ ｜ Day 5 gmm_peaks/dp_segments ｜ Day 6 结论
import math

import numpy as np

# ============================================================
# 0. 常量区（**数据来源都标了，抄的时候别改单位**）
# ============================================================
N_STEPS = 20                      # 台阶数（题面：一段楼梯 20 级）

# 每级台阶的最大磨损深度（mm）—— 讲义 §5.1 原文，含三段结构：
#   1-5   连续加深   → 老台阶
#   6-10  骤降到 1~3 → 后期更换段
#   11-15 最深 6~8   → 人流最密处
#   16-20 逐渐变浅   → 上层台阶
WEAR_DEPTH = np.array([
    3.0, 4.0, 5.0, 6.0, 7.0,
    1.0, 2.0, 3.0, 2.0, 3.0,
    6.0, 7.0, 8.0, 8.0, 7.0,
    5.0, 6.0, 6.0, 5.0, 4.0,
])                                # 合计 Σd = 98.0 mm

# 色差 ΔE（第 4 问判别"是否同一批石材"用，Day 6 才用到）
COLOR_DELTA_E = np.array([
    2.1, 1.8, 2.0, 2.2, 1.9,
    8.4, 8.1, 8.6, 8.2, 8.5,
    2.5, 2.3, 2.4, 2.6, 2.2,
    2.0, 3.4, 3.6, 1.9, 2.1,
])

# 磨损坑的椭圆半轴（mm）：a 宽向、b 进深向 —— 讲义 §3 表就这两个名字
# ⚠️ 讲义没印这两个的具体数值；下面两个数是按「V=50 894 mm³」反解的
#    （a·b = 50 894 / (0.5·π·98) = 330.62 mm²），换实测数据时整块替换。
PIT_A = 30.0
PIT_B = 11.0205

# 材料与载荷参数（Day 2 起才用，先备着）
K_WEAR = 0.002          # 无量纲磨损系数（讲义 §5.3 明写）
LOAD_N = 700.0          # 单次踩踏法向力 F（N）≈ 70 kg 体重
SLIP_M = 0.03           # 单次踩踏滑移距离 s（m）≈ 3 cm
HARDNESS_PA = 5.0e9     # 材料硬度 H（Pa）≈ 5 GPa（大理石/花岗岩量级）


# 单级台阶踏面磨损坑的体积（mm³）
# 参数：a_mm、b_mm 磨损椭圆半轴；d_mm 这一级的最大磨损深度
def ellipse_volume(a_mm, b_mm, d_mm):
    return 0.5 * np.pi * a_mm * b_mm * d_mm   # 式 (4)：πab·(d/2)，别漏 1/2
V_mm3 = sum(ellipse_volume(PIT_A,PIT_B,depth) for depth in WEAR_DEPTH)
v0_m3 = K_WEAR*LOAD_N*SLIP_M/HARDNESS_PA
N = V_mm3*1e-9/v0_m3 
print(f"V = {V_mm3:.0f}mm³ v₀ = {v0_m3:.3e}m³/次 N = {N:.3e}次")

Q_PER_DAY = 110.0
T = N/(365*Q_PER_DAY)       # 日均踩踏次数：先验假设，非计算数值
print(f"T = {T:.1f}年")      # 式 (8)

