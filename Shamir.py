import random
from sympy import symbols, simplify

def generar_polinomio(n, constante):
    coeficientes = [random.randint(0, 1000) for _ in range(n-1)]  # Genera n-1 coeficientes aleatorios
    
    polynomial_terms = [f"{coeficientes[i]}x^{n-i-1}" for i in range(n-1)]
    polynomial_str = " + ".join(polynomial_terms)
    
    polynomial_str += f" + {constante}"  # Agregar el coeficiente constante
    
    return polynomial_str

def evaluar_polinomio(polinomio, x):
    # Separar el polinomio en términos
    polynomial_terms = polinomio.split(" + ")
    
    resultado = []
    for x in x:
        resultado = 0
        for term in polynomial_terms:
            if 'x^' in term:
                coefficient, power = term.split("x^")  # Separar coeficiente y potencia
                coefficient = int(coefficient)
                power = int(power)
                resultado += coefficient * (x ** power)  # Calcular el término
            else:
                constant = int(term)
                resultado += constant  # Sumar el coeficiente constante
        resultado.append(resultado)
    
    return resultado

def lagrange_interpolacion(points):
    x = symbols('x')
    n = len(points)
    polynomial = 0
    for i in range(n):
        xi, yi = points[i]
        term = yi
        for j in range(n):
            if j != i:
                xj, _ = points[j]
                term *= (x - xj) / (xi - xj)
        polynomial += term
    return simplify(polynomial)

# Ejemplo de uso
points = [(6, 349123),(2, 15211),(3,39109), (8, 967399), (10, 2184987), (1, 6663)]  # Puntos para la interpolación de Lagrange
polinomio = lagrange_interpolacion(points)
print("Polinomio interpolante de Lagrange:", polinomio)

# Ejemplo de uso
n = 10  # Número mínimo requerido para reconstruir el secreto
constante = 45622323  # Coeficiente constante definido
print ("Secreto: ", constante)
polinomio = generar_polinomio(n, constante) #crear polinomio de n-1 grados
print("Polinomio generado:", polinomio)
valor_x = list(range(1, 31)) 
resultado = evaluar_polinomio(polinomio, valor_x)

x_valores = [1,2,3,4,5,6,7,8,9,10]  # Valor de x para evaluar el polinomio
#result = evaluate_polynomial(polynomial, x_value)
#print("Resultado de evaluar el polinomio en x =", x_value, ":", result)
puntosaEvaluar = [1,3,5,4,10,11,19,2,6,14,7,8,20,17,24,28,9]
print ("Puntos para reconstruir secreto: ",puntosaEvaluar)
puntos_evaluados = evaluar_polinomio(polinomio, puntosaEvaluar)
points =  list(zip(puntosaEvaluar, puntos_evaluados)) # Lista de tuplas (x, y) para la interpolación de Lagrange
polinomioLagrange = lagrange_interpolacion(points)
print("Polinomio:", polinomioLagrange)