from matematica.formas import Retangulo, Quadrado, Triangulo, Circulo
from matematica.fracao import Fracao

retangulo1 = Retangulo(50, 10)
print("Área do retângulo:", retangulo1.calcular_area())  
print("Perímetro do retângulo:", retangulo1.calcular_perimetro())  

fracao1 = Fracao(30, 40)
print("Valor decimal da fração:", fracao1.calcular_valor_decimal()) 
