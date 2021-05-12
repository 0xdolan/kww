import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

plt.style.use("ggplot")
# plt.style.use("fivethirtyeight")
# plt.style.use("seaborn-whitegrid")
# plt.xkcd()

# COUNT THE FREQUENTS
cleaned_wl = "cleaned_wl.txt"
with open(cleaned_wl, "r", encoding="utf-8") as rf:
    count = Counter(rf.read().split("\n"))
    # print(count.most_common(50))
    for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True):
        l = f"{k},{v}"
        # print(l)
mc = dict(count.most_common(30))


x = list(mc.keys())
y = list(mc.values())


# make the figure size = (wisth, height)
plt.figure(figsize=(20, 15))

# bar plot for X and Y
plt.bar(x, y)

for i in range(len(x)):
    # print(x[i], y[i])
    plt.text(
        x=x[i],
        y=y[i],
        s="  " + str(y[i]),
        # size=6,
        ha="center",
        rotation=90,
        fontname="Source Code Pro",
        color="k",
    )

plt.xticks(ticks=x, fontfamily="Vazir", weight="bold")
plt.xticks(rotation=45, ha="right")
plt.yticks(np.arange(0, 200000, 20000))

# Title of the chart
title_font = {
    "family": "Source Code Pro",
    "color": "#232323",
    "weight": "bold",
    "size": 16,
}
plt.title("Word Frequency Bar Chart\n", fontdict=title_font)

# Lable for X axis
lable_x_font = {
    "family": "Source Code Pro",
    "color": "#232323",
    "weight": "bold",
    "size": 13,
}
plt.xlabel("\nWord", fontdict=lable_x_font)

# Lable for Y axis
lable_y_font = {
    "family": "Source Code Pro",
    "color": "#232323",
    "weight": "bold",
    "size": 13,
}
plt.ylabel("Frequency\n", fontdict=lable_y_font)

# make a grid for the chart
# plt.grid(True)
# plt.grid(axis="y", linestyle="-")

# save the char bar as a PDF file
plt.savefig("bar-chart.pdf")
plt.show()
