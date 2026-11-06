def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multi(a, b):
    return a * b


def divi(a, b):
    return a / b


def pedir_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número.")


def pedir_opcao():
    while True:
        resposta = input("Deseja sair? Digite S ou N: ").strip().lower()

        if resposta == "s" or resposta == "n":
            return resposta

        print("Resposta inválida. Digite S ou N.")




opcao = ""

while opcao != "s":
    numero01 = pedir_numero("Digite o primeiro número: ")

    operacao = input("Escolha uma operação (+, -, * ou /): ")

    numero02 = pedir_numero("Digite o segundo número: ")

    if operacao == "+":
        print("Resultado =", somar(numero01, numero02))
    elif operacao == "-":
        print("Resultado =", subtrair(numero01, numero02))
    elif operacao == "*":
        print("Resultado =", multi(numero01, numero02))
    elif operacao == "/":
        try:
            print("Resultado =", divi(numero01, numero02))
        except ZeroDivisionError:
            print("Divisão por zero é inválida.")
    else:
        print("Operação inválida.")

    opcao = pedir_opcao()

print("Fim do programa.")

