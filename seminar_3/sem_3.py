#1 - Să se salveze în fișierul Cerinta1.csv datele privind numărul de angajați pe activitățile
#din industria alimentară, pentru localitățile în care numărul de angajați este mai mare decât 0.
import pandas as pd
industrie = pd.read_csv("IndustriaAlimentara.csv")

industrii = list(industrie)[3:]
print(industrii)

# 1 - Localitatile in care numarul angajatilor este mai mare decat 0

nr_ang = industrie[industrie[industrii].sum(axis=1) > 0]
#axis = 1 op se face pe randuri, adica ia coloanele
#axis=0 se face pe coloane, adica ia randurile

nr_ang.to_csv("Cerinta1.csv", index=False)


# 2 - Procentul de angajati pe fiecare activitate la nivel de localitate

total = industrie[industrii].sum(axis=1)

procente = industrie[industrii].div(total, axis=0) * 100

procente = pd.concat(
    [industrie[["Siruta", "Localitate"]], procente],
    axis=1
)

procente.to_csv("Cerinta2.csv", index=False)


# Citim celelalte fisiere

populatie = pd.read_csv("PopulatieLocalitati.csv")
judete = pd.read_csv("Coduri_Judete.csv")
regiuni = pd.read_csv("Coduri_Regiuni.csv")


# 3 - Judetele sortate descrescator dupa ponderea angajatilor
# din industria alimentara in populatia totala

industrie["TotalAngajati"] = industrie[industrii].sum(axis=1)

data = industrie.merge(populatie, on="Siruta")

rezultat = data.groupby("Judet")[["Populatie", "TotalAngajati"]].sum()

rezultat["Pondere"] = rezultat["TotalAngajati"] / rezultat["Populatie"] * 100

rezultat = rezultat.sort_values("Pondere", ascending=False)

rezultat.to_csv("Cerinta3.csv")



# 4 - Activitatea cu cei mai multi angajati la nivel de judet

data = industrie.merge(populatie, on="Siruta")

rezultat = data.groupby("Judet")[industrii].sum()

rezultat["ActivitateDominanta"] = rezultat[industrii].idxmax(axis=1)

print(rezultat["ActivitateDominanta"])

rezultat[["ActivitateDominanta"]].to_csv("Cerinta4.csv")

#5 - numărul mediu de angajați pe fiecare activitate la nivel de regiune
#Se va calcula media ponderată, folosind ca pondere populația localităților.

# 5 - media ponderata pe regiune
data = industrie.merge(populatie, on="Siruta")
data = data.merge(judete, left_on="Judet", right_on="IndicativJudet")

for activitate in industrii:
    data[activitate] = data[activitate] * data["Populatie"]

rezultat = data.groupby("Regiune")[industrii].sum()
pop_regiune = data.groupby("Regiune")["Populatie"].sum()

rezultat = rezultat.div(pop_regiune, axis=0)
rezultat.to_csv("Cerinta5.csv")

# 6 - indici de localizare pe judet si activitate
data = industrie.merge(populatie, on="Siruta")

ang_judet = data.groupby("Judet")[industrii].sum()   # angajati pe judet si activitate
pop_judet = data.groupby("Judet")["Populatie"].sum() # populatia fiecarui judet

ang_nat = ang_judet.sum()   # angajati pe activitate, la nivel national
pop_nat = pop_judet.sum()   # populatia tarii

pondere_ang = ang_judet.div(ang_nat, axis=1)   # ponderea judetului in activitate
pondere_pop = pop_judet / pop_nat              # ponderea judetului in populatie

indici = pondere_ang.div(pondere_pop, axis=0)
indici.to_csv("Cerinta6.csv")
