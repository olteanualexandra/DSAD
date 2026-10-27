
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# SERIE DE TIMP
fig, ax = plt.subplots(figsize=(10, 5))#plot-ul gol

ax.set_title('Serie de timp')#titlul
ax.set_xlabel('zi')
ax.set_ylabel('valoare')

zile = ["L", "Ma", "Mi", "J", "V", "S", "D"]
valori = [12, 15, 11, 15, 22, 11, 11]

ax.plot(zile, valori, marker="o", color='red',
        label='Valori zilnice')#adauga datele
ax.legend()

plt.tight_layout()
plt.show()


# CORELATIE
r = np.array([
    [1.0, 0.72, -0.15],
    [0.72, 1.0, 0.31],
    [-0.15, 0.31, 1.0]
])

labels = ["x", "y", "z"]

t_r = pd.DataFrame(r, index=labels, columns=labels)

fig, ax = plt.subplots(figsize=(7, 6))

sns.heatmap(t_r, annot=True, cmap='RdYlGn',
           ax=ax)

ax.set_title("Corelograma exemplu")

plt.tight_layout()
plt.show()


# HEATMAP VALORI PE ZILE
matrice = np.array(valori).reshape(1, 7)

fig, ax2 = plt.subplots(figsize=(10, 3))

sns.heatmap(
    matrice,
    annot=True,
    cmap='coolwarm',
    xticklabels=zile,
    yticklabels=['Valori'],
    ax=ax2
)

ax2.set_title('Heatmap', color='green')
ax2.set_xlabel('Zi')
ax2.set_ylabel('')

plt.tight_layout()
plt.show()


#PCA
#o comb lin de coef -PC1
# PC2- o sa fie perpendiculara pe PC1 si tot asa
#PC1+PC2 > 90% din variatia setului de date

#1 - preluarea de date
df = pd.read_csv('iris.csv')
print(df.head())
#2 - selecteaza val numerice
x=df[["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]]
#selecteaza val numerice din cele 4 coloane

#3 - standardizare - a aduce la ac unitate
x_scaled = StandardScaler().fit_transform(x)

#4 - PCA: reducem de la 4 var la 2 CP
pca= PCA(n_components=2)
X_pca=pca.fit_transform(x_scaled)

#5 - cream un nou DataFrame cu noile rez
result = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
result["Species"] = df["Species"]

#6 - Cat de mult capteaza din varianta initiala
print("Explained variance ", pca.explained_variance_ratio_)
print("Total variance: ", pca.explained_variance_ratio_.sum())

#7 - Vizualizarea rezultatelor
for species, group in result.groupby("Species"):
    plt.scatter(group["PC1"], group["PC2"], label=species)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("PCA - Iris dataset")
plt.legend()
plt.show()


