def letterA(string):
    
    countA = string.count('A')
    counta = string.count('a')

    if countA > 0 or counta > 0:
        return f"A string ({string}) contém [{countA} A(s) maiúsculo(s)] e [{counta} a(s) minúsculo(s)]"

    return f"A string ({string}) não contém a letra 'A'"

s = input("Digite uma palavra ou uma frase: ")

print(letterA(s))