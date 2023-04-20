x = float(input())
operacao = input()
y = float(input())
if operacao == "+":
    print(f"{x} + {y} =", x + y)
elif operacao == "-":
    print(f"{x} - {y} =", x - y)
elif operacao == "*":
    print(f"{x} * {y} =", x * y)
elif operacao == "//":
    if y == 0:
        print("Divisao por 0!")
    else:
        print(f"{x} // {y} =", x // y)
elif operacao == "**":
    print(f"{x} ** {y} =", x ** y)
elif operacao == "%":
    if y == 0:
        print("Divisao por 0!")
    else:
        print(f"{x} % {y} =", x % y)
else:
    print("Operacao nao reconhecida!")
