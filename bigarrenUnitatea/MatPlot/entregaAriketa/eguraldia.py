import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("eguraldia.csv")

plt.figure(figsize=(18, 12))

plt.plot(df["eguna"], df["tenperatura"], marker= "o", label="Tenperatura")
plt.plot(df["eguna"], df["euria_mm"], marker= "o", label="Prezipitazioa")

plt.title("Egun bakoitzeko eguraldia eta prezipitazioa")
plt.xlabel("Eguna")
plt.ylabel("Balioa")
plt.legend()

plt.tight_layout()
plt.show()

###########################################################################

'''plt.plot(df["eguna"], df["tenperatura"])
plt.title("Tenperatura Grafikoa")
plt.xlabel("Eguna")
plt.ylabel("Tenperatura")
plt.show() 

plt.plot(df["eguna"], df["euria_mm"])
plt.title("Euri-Kopurua Grafikoa")
plt.xlabel("Eguna")
plt.ylabel("Euri-Kopurua")
plt.show()'''

###########################################################################

'''plt.figure(figsize=(18, 8))

plt.subplot(2, 1, 1)
plt.plot(df["eguna"], df["tenperatura"])
plt.title("Tenperatura Grafikoa")
plt.xlabel("Eguna")
plt.ylabel("Tenperatura")

plt.subplot(2, 1, 2)
plt.plot(df["eguna"], df["euria_mm"])
plt.title("Euri-Kopurua Grafikoa")
plt.xlabel("Eguna")
plt.ylabel("Euri-Kopurua")

plt.tight_layout()
plt.show()'''

###########################################################################