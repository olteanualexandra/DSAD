
import pandas as pd
from scipy.spatial.distance import cdist
from functii_online import nan_replace_df

#1 incarcare
data = pd.read_csv("winequality-red.csv", sep=";")

print(data)

print(data.shape)

print(data.head())

print(data.dtypes)

#2 valori lipsa

nan_replace_df(data)
print("Nr tot de NaN", data.isna().sum().sum())

#3 vinuri cu quality >=7

vinuri_peste7=data[data["quality"]>=7]
#daca as fi pus data["quality"]>=7 imi dadea tabel de true/false
vinuri_peste7.to_csv("vinuri_peste7.csv",
                     sep=";",
                     index=False)

# 4 top 50 dupa alcohol, descrescator
top_50_vinuri=data.sort_values("alcohol", ascending=False).head(49)
top_50_vinuri.to_csv("top_50_vinuri.csv",
                     sep=";",
                     index=False)

#5 media alcohol si pH pentru fiecare quality
media_alcool_ph= data.groupby("quality")[["alcohol", "pH"]].mean() #Tabel, lista de col
media_alcool_ph.to_csv("media_alcool_ph.csv")

#6 coloana noua aciditate_totala derivata
data["aciditate_totala"] = (data["fixed acidity"]+
                            data["volatile acidity"]+
                            data["citric acid"])
aciditate_deriv=data[["quality","alcohol", "pH", "aciditate_totala"]]
aciditate_deriv.to_csv("aciditate_derivation.csv")

#7 - calit cu media alcool max
medii = data.groupby("quality")["alcohol"].mean() # Series, o sg col de val
nota_calit_med_max= medii.idxmax()
# idxmax returneaza idnexul val maxime, adica quality
# pt max as primi media

rezultat = pd.DataFrame({"quality": [nota_calit_med_max]})
rezultat.to_csv("rezultat.csv")

#8 - Pentru coloanele:
#fixed acidity, volatile acidity, citric acid, alcohol, quality
#calculați matricea de corelație și salvați **data_out/R.csv

coloane = ["fixed acidity" , "volatile acidity" , "citric acid", "alcohol", "quality"]
R= data[coloane].corr()
print(R)
R.to_csv("R.csv")

#9 - alcohol_std=(alcohol-media)/std
data["alcohol_std"] = (data["alcohol"]- data["alcohol"].mean())/data["alcohol"].std()
#implicit esantion, ddof=1, n-1
cerinta_9 = data[["alcohol", "alcohol_std"]]
cerinta_9.to_csv("cerinta_9.csv")

#10 - matrice de dist pe primele 20 vinuri si pe col standardiz
# fixed acidity, volatile acidity, alcohol (standardizați fiecare coloană),
# calculați matricea distanțelor **euclidiene** 20×20 (scipy.spatial.distance.cdist sau formula voastră).

x = data[["fixed acidity", "volatile acidity", "alcohol"]]
x_std = (x-x.mean())/x.std()
x_20=x_std.head(20)
d=cdist(x_20,x_20)
print(d)

# 1.De ce corelația alcool–calitate nu implică cauzalitate?'
#Corelatia arata doar daca var cresc sau scad impr, nu ca
#una o prod pe cealalta
#calit influenteaza alcoolul
# 2.De ce standardizăm înainte de distanțe euclidiene pe coloane cu unități diferite?
#Distanta euclidiana aduna dif la patrat intre col; de ex daca o col are val
#cu unit mari, ea domina distanta; Unit de mas ar deveni factor decisiv
#Prin standardizare (val-media)/dev standard, fiecare col aj la media 0
#si std 1; Toate col au aceeasi scara si contribuie echilibrat la distanta

#dacă măsori înălțimea unor oameni în metri și greutatea în grame,
#distanța dintre ei ar fi decisă aproape numai de greutate.