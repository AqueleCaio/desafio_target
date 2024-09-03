def fibonacci(number):
    a = 0
    b = 1

    # Gera números de Fibonacci ser maior ou menor que o valor digitado
    while a <= number:
        if a == number:
            return f"O número {number} pertence à sequência de Fibonacci."
        a, b = b, a + b

    return f"O número {number} não pertence à sequência de Fibonacci."

x = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

print(fibonacci(x))