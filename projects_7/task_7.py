import matplotlib.pyplot as plt

import numpy as np



# ── Восстанавливаем "сырые данные" из частот ────────────────────────────────

data = (

   [10]*2 +

   [30]*5 +

   [50]*10 +

   [70]*9 +

   [90]*4

)



# ── Границы интервалов (как в исходной задаче) ──────────────────────────────

bins = [0, 20, 40, 60, 80, 100]



# ── Стиль ────────────────────────────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(9, 6), facecolor="#F8F9FA")

ax.set_facecolor("#F8F9FA")



# ── Гистограмма ──────────────────────────────────────────────────────────────

n, bin_edges, patches = ax.hist(

   data,

   bins=bins,

   edgecolor="white",

   linewidth=1.2

)



# ── Подсветка самого высокого столбца ────────────────────────────────────────

max_height = max(n)



for count, patch in zip(n, patches):

   if count == max_height:

       patch.set_facecolor("#E63946")  # пик (мода)

   else:

       patch.set_facecolor("#4C72B0")



# ── Подписи над столбцами ────────────────────────────────────────────────────

for count, patch in zip(n, patches):

   ax.text(

       patch.get_x() + patch.get_width() / 2,

       patch.get_height() + 0.2,

       int(count),

       ha="center", va="bottom",

       fontsize=12, fontweight="bold",

       color="#1A1A2E"

   )



# ── Среднее значение ─────────────────────────────────────────────────────────

mean_val = np.mean(data)



ax.axvline(mean_val,

          color="#F4A261",

          lw=2.2,

          linestyle="-.",

          label=f"Среднее ≈ {mean_val:.1f}")



# ── Оформление ───────────────────────────────────────────────────────────────

ax.set_xlabel("Интервал оценок", fontsize=13, labelpad=10)

ax.set_ylabel("Количество студентов", fontsize=13, labelpad=10)

ax.set_title("Гистограмма: оценки 30 студентов", fontsize=16, fontweight="bold")



ax.set_xticks([10, 30, 50, 70, 90])

ax.set_xticklabels(["0–20", "20–40", "40–60", "60–80", "80–100"])



ax.grid(axis="y", color="#DEE2E6", linewidth=0.9, alpha=0.8)

ax.spines[["top", "right"]].set_visible(False)



ax.legend()



plt.tight_layout()

plt.savefig("students_histogram.png", dpi=300, bbox_inches="tight", facecolor="#F8F9FA")

plt.show()



print("Готово: students_histogram.png")