import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ikasleak_Matplot.csv")

ikasgelak = df.groupby("ikasgela").agg(ikasle_kopurua=("ikasgela", "count"),batezbesteko_nota=("nota", "mean")).reset_index()

plt.figure(figsize=(12, 6))

plt.bar(ikasgelak["ikasgela"],ikasgelak["ikasle_kopurua"],label="Ikasle kopurua")

plt.plot(ikasgelak["ikasgela"],ikasgelak["batezbesteko_nota"], marker="o", label="Batez besteko nota")
    
plt.title("Ikasle kopurua eta batez besteko nota ikasgela bakoitzean")
plt.xlabel("Ikasgela")
plt.ylabel("Balioa")
plt.legend()

plt.tight_layout()
plt.show()

'''plt.figure(figsize=(18, 6))
plt.bar(df["izena"], df["nota"], color="steelblue")

plt.title("Ikasleen notak")
plt.show()'''

