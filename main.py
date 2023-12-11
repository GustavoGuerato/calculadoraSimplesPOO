class Calculadora:
    def __init__(self, soma=None, divisao=None, subtracao=None, multiplicacao=None):
        self.soma = soma
        self.divisao = divisao
        self.substracao = subtracao
        self.multiplicacao = multiplicacao

    def soma(self, x, y):
        soma = x + y
        return soma

    def divisao(self, x, y):
        divisao = x / y
        return divisao

    def substracao(self, x, y):
        subtracao = x - y
        return subtracao

    def multiplicacao(self, x, y):
        multiplicacao = x * y
        return multiplicacao


conta = input('1-soma, 2-divisao, 3-subtstracao, 4-multiplicaçao')

valor_x = float(input("Digite o valor de x: "))
valor_y = float(input("Digite o valor de y: "))

calculadora = Calculadora()
if conta == '1':
    resultado = calculadora.soma(valor_x, valor_y)
elif conta == '2':
    resultado = calculadora.divisao(valor_x, valor_y)
elif conta == '3':
    resultado = calculadora.substracao(valor_x, valor_y)
elif conta == '4':
    resultado = calculadora.multiplicacao(valor_x, valor_y)
else:
    print("Operação inválida")


print(f"O resultado da {conta} de {valor_x} e {valor_y} é {resultado}")
