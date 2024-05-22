# Exercício 1: Criação de variáveis para armazenar informações do funcionário
nome_funcionario = "João Silva"
idade = 30
salario = 2500.00
cargo = "Analista de Sistemas"
turno = "matutino"  # ou "noturno"
setor = "Tecnologia da Informação"

# Imprimindo informações do funcionário
print("Nome do Funcionário:", nome_funcionario)
print("Idade:", idade)
print("Salário:", salario)
print("Cargo:", cargo)
print("Turno:", turno)
print("Setor:", setor)

# Exercício 2: Criação de variáveis para armazenar informações da escola
nome_escola = "Colégio Militar"
estado = "Rio de Janeiro"
numero_professores = 50
cidade = "Rio de Janeiro"
numero_militares = 30
logradouro = "Rua das Flores"
numero_endereco = 123
numero_alunos = 500
colegio_e_militar = True  # ou False
disciplinas = ["Matemática", "Português", "História", "Geografia"]

# Imprimindo informações da escola
print("\nNome da Escola:", nome_escola)
print("Estado:", estado)
print("Número de Professores:", numero_professores)
print("Cidade:", cidade)
print("Número de Militares:", numero_militares)
print("Logradouro:", logradouro)
print("Número (Endereço):", numero_endereco)
print("Número de Alunos:", numero_alunos)
print("Colégio é Militar:", colegio_e_militar)
print("Disciplinas:", disciplinas)

# Exercício 3: Cálculo e exibição dos resultados das operações com as variáveis fornecidas
valor1 = 10
valor2 = 5
valor3 = "2"
valor4 = 8
valor5 = -5

# valor8 não foi fornecido, supondo que seja 0 para evitar erro
valor8 = 0

# Realizando e imprimindo os cálculos solicitados
print("\nvalor1 + valor2 =", valor1 + valor2)
print("valor1 + valor2 + valor4 =", valor1 + valor2 + valor4)
print("valor1 + valor2 - valor5 =", valor1 + valor2 - valor5)
print("valor1 + valor3 =", str(valor1) + valor3)  # Concatenando string com número
print("valor1 * valor2 =", valor1 * valor2)
print("(valor4 * valor2) / 2 =", (valor4 * valor2) / 2)
print("(valor1 + valor2 + valor8 + valor5) / 4 =", (valor1 + valor2 + valor8 + valor5) / 4)

# Exercício 4: Cálculo e exibição da soma e média dos valores fornecidos
v1 = 2
v2 = 3
v3 = 5
v4 = 6

soma_valores = v1 + v2 + v3 + v4
media_valores = soma_valores / 4

# Imprimindo a soma e média dos valores
print("\nSoma dos valores:", soma_valores)
print("Média dos valores:", media_valores)

# Exercício 5: Verificação de aprovação ou reprovação do aluno com base nas notas fornecidas
nota1 = 64
nota2 = 45
nota3 = 60
media = (nota1 + nota2 + nota3) / 3

# Determinando e imprimindo o status de aprovação do aluno
if media >= 60:
    print("\nAluno aprovado")
else:
    print("\nAluno reprovado")

# Exercício 6: Determinação do status de aprovação do aluno com base na média
if media >= 90:
    print("Aluno foi aprovado com certificado")
elif media >= 60:
    print("Aluno apenas aprovado")
else:
    print("Aluno reprovado")
