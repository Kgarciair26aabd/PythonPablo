import pandas as pd

df = pd.read_csv("ikasleak.csv")

class Ikasleak:
    def __init__(self, izena, adina, ikasgela, nota):
        self.izena = izena
        self.adina = adina
        self.ikasgela = ikasgela
        self.nota = nota


ikasleZerrenda = []

for izena, adina, ikasgela, nota in df.values:
    ikasleZerrenda.append(Ikasleak(izena, adina, ikasgela, nota))

ikasleZerrenda.sort(key=lambda x: x.nota)

for ikaslea in ikasleZerrenda:
    print(ikaslea.izena, ikaslea.adina, ikaslea.ikasgela, ikaslea.nota)