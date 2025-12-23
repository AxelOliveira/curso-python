"""📥 1. Entrada de dado
Peça ao usuário:
Nome (string)
Idade (string → converter para int)
Senha (string)
Nota 1 (string → converter para float)
Nota 2 (string → converter para float)

🧱 2. Constantes
Crie constantes para:
IDADE_MINIMA = 18
TAMANHO_MIN_SENHA = 8
PALAVRA_PROIBIDA = "123"

🧪 3. Tratamento de erros (try / except)
Use try/except somente nas linhas que podem gerar erro:
Conversão de idade
Conversão das notas
Trate pelo menos:
ValueError

📊 4. Cálculo
Calcule a média das notas usando:
(media = (nota1 + nota2) / 2)

🧠 5. Regras de negócio (use operadores lógicos)
✔️ Situação do aluno
Média ≥ 6 → "Aprovado"
Média ≥ 4 e < 6 → "Recuperação"
Média < 4 → "Reprovado"
✔️ Status de idade
Maior ou igual à idade mínima → "Maior de idade"
Caso contrário → "Menor de idade"
✔️ Validação da senha
A senha será válida se:
Tiver 8 ou mais caracteres
Não contiver "123"
Use len(), not in, and

✂️ 6. Manipulação de string
Mostre os 3 primeiros caracteres do nome
Mostre o tamanho do nome usando len()
🧠 7. Comparações e identidade
Crie duas variáveis:
a = 10
b = 10
Mostre:
a == b
a is b
Use id(a) e id(b)
Explique em comentário o resultado

🖨️ 8. Saída formatada
Exiba tudo no final usando f-string OU .format():
Exemplo de modelo (adapte):
Nome: X
Idade: Y
Status idade: Z
Média: W
Situação: RESULTADO
Senha válida: True/False
Primeiras letras do nome: ABC
Tamanho do nome: N

🐞 9. Debug (obrigatório)
No VS Code:
Coloque breakpoints:
Antes da conversão de tipos
Antes do cálculo da média
Antes da validação final
Use:
F5 (iniciar debug)
F10 (Step Over)
Observe:
Valores no painel Variables
Fluxo entrando ou não no except

🧹 10. Qualidade do código
O código deve:
Ter nomes de variáveis claros
Ter comentários curtos e objetivos
Não colocar tudo dentro do try
Ser fácil de debugar
"""
