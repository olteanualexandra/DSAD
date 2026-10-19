varsta = 20
print(varsta)

varsta= "salut"
print(varsta)

def func():
    pass

def func2():
    print("salut " + str(2))
func2()

for i in range(5):
    print (i)

fructe=["mar", "par"]
for i in fructe:
    print(fructe)

class Masina:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def merge(self):
        print("vroom")

masina = Masina(3,2);
print(masina.name)
masina.merge()

date = pd.read_csv("")
print(date)