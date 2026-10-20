nome: str = input("Adicione o seu nome: ")
idade: int = int(input("Adicione a sua idade: "))
pretensao: float = float(input("Adicione a sua pretensão salarial: "))
r_casado: bool = input("Atualmente está casado? ").lower()

casado: bool 
if r_casado == "sim":
    casado = True
else:
    casado = False