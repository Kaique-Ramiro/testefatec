print ("--- FOR ---")
for voltas in range(6):
    print(f"Número de voltas: {voltas}")

print("--- FOR LIST ---")
notas = [7.5, 8.0, 8.5, 7.0]
for nota in notas:
    print(f"Notas: {nota}")

print("--- WHILE ---")
contador: int = 1
while contador <= 5:
    print(f"Volta número: {contador}")
    contador += 1