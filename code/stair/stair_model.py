# -*- coding: utf-8 -*-
"""stair_model.py —— 楼梯磨损反演主模型（按讲义二 §5 重建）

来源：D:\\Program Files\\qq\\楼梯建模_Python代码讲义_v2.html
验收：讲义 §6 的实跑输出（本文件要逐条对上）

进度（7 天表）：
  Day 1  常量区 + ellipse_volume()          → 打印 V ≈ 50 894 mm³
  Day 2  v0 = V / N（单次踩踏磨损）
  Day 3  mc_use_years() 蒙特卡洛 → 使用年数分布
  Day 4  date_from_years() + 反演 q̄
  Day 5  gmm_peaks() + dp_segments()
  Day 6  三指标 + 材料概率 + 汇总结论

今天只做 Day 1：把下面的 TODO 补完，让 `python stair_model.py` 打印出 V。
"""
import numpy as np

# ============================================================
# 0. 常量区
#    数据全部来自讲义 §5.1 的观测表，自己抄，别改单位（一律 mm）
# ============================================================
N_STEPS = 20          # 台阶数（题面：一段楼梯共 20 级）

A_MM = None           # TODO: 踏面椭圆的半轴（长轴方向），单位 mm
B_MM = None           # TODO: 踏面椭圆的半轴（短轴方向），单位 mm
WEAR_DEPTH = None     # TODO: 20 个台阶的磨损深度，单位 mm，一维数组

# 下面这几个 Day 2 之后才用到，先留着，别填
# K_WEAR = None       # 材料磨损系数
# H_HARD = None       # 硬度
# F_FREQ = None       # 单次踩踏的受力/载荷因子
# S_GEOM = None       # 接触形状因子


# ============================================================
# 1. Day 1：单级台阶磨损体积
# ============================================================
def ellipse_volume(a_mm, b_mm, depth_mm):
    """把 20 个踏面磨损深度折成一个总体积。

    参数
    ----
    a_mm, b_mm : float     椭圆踏面的两个半轴（mm）
    depth_mm   : 一维数组  每级台阶的磨损深度（mm），长度 = N_STEPS

    返回
    ----
    float   总磨损体积（mm³）

    提示：公式在讲义二 §5.2「单次磨损体积」——自己看公式写，别照抄讲义里的
    代码块；写不出来就先把 Σw 单独算出来打印看。
    """
    raise NotImplementedError("Day 1：ellipse_volume 还没写")


# ============================================================
# 2. 主程序
# ============================================================
def main():
    # 入参检查：这三行能帮你发现「常量忘了填」
    assert A_MM is not None, "A_MM 还没填（讲义 §5.1）"
    assert B_MM is not None, "B_MM 还没填（讲义 §5.1）"
    assert WEAR_DEPTH is not None, "WEAR_DEPTH 还没填（讲义 §5.1）"

    w = np.array(WEAR_DEPTH, dtype=float)
    assert w.size == N_STEPS, f"WEAR_DEPTH 应该有 {N_STEPS} 个，现在是 {w.size} 个"

    V = ellipse_volume(A_MM, B_MM, w)

    print(f"Σw = {w.sum():.2f} mm")
    print(f"V  = {V:.0f} mm³")
    print(f"V  = {V / 1000:.2f} cm³")


if __name__ == "__main__":
    main()
