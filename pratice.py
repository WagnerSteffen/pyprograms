class Pratice:
    def __init__(self, num):
        self.num = num

    def dobro(self):
        dobro = self.num * 2
        print(f"O dobro do numero é: {dobro}")

    def triplo(self):
        triplo = self.num * 3
        print(f"O triplo do numero é: {triplo}")

    def raiz(self):
        raiz = self.num ** (1 / 2)
        print(f"A raiz quadrada do numero é: {raiz}")


while True:
    numero = int(input("Digite o numero desejado(0 - para sair): "))
    if numero == 0:
        break
    matematico = Pratice(numero)
    matematico.dobro()
    matematico.triplo()
    matematico.raiz()

print("Obrigado por participar!")
