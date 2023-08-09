class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def calcular_valor_decimal(self):
        return self.numerador / self.denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"