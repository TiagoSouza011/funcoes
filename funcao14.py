def calcular_raiz_quadrada(numero, preciso=0.0001):
raiz =numero/2
while abs(numero  - raiz**2) > precisao:
      raiz = (raiz + numero)