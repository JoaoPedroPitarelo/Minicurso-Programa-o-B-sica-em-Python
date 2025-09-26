
# Simulando uma chamada SEM laço de repetição

print("Ana?")
print("Presente!")

print("João?")
print("Presente!")

print("Maria?")
print("Presente!")

# Simulando uma chamada COM laço de repetição

# Declarando uma variável "alunos" que armazena uma lista de texto (str)
alunos = ["Ana", "João", "Maria"]

for aluno in alunos: # Para cada aluno na lista de alunos
    print(aluno + "?")
    print("Presente!")


# Outro exemplo usando While

quantidade_alunos = len(alunos) # len() -> captura o tamanho de uma lista ou texto
indice = 0

while indice < quantidade_alunos: # <- Condicional de parada | Enquanto indice for menor do que a quantidade de alunos
    print(alunos[indice] + "?")
    print("Presente!")

    indice += 1 # A cada iteração o valor de indice é incremento em 1 até que a condição seja satisfeita
