"""
Imprecisão de ponto flutuante
- Imprecisão de ponto flutuante
- Números decimais não são representados com precisão exata em binário.
- Por isso, operações com float podem gerar resultados inesperados.
- Usamos Decimal, round ou formatação para controlar a precisão.
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))