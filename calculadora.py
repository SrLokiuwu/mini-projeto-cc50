import time
print("bem-vindo á calculadora inteligente")
time.sleep(1)
print("aqui você pode conseguir a tabuada de qualquer número até o 20, ou multiplicar qualquer número especifico")
time.sleep(1)
pergunta = input("gostaria de usar a tabuada ou a calculadora? ")
if pergunta == "tabuada":
    nt = int(input("número: "))
    print(" 1 x {} = {}".format(nt, nt * 1))
    time.sleep(1)
    print(" 2 x {} = {}".format(nt, nt * 2))
    time.sleep(1)
    print(" 3 x {} = {}".format(nt, nt * 3))
    time.sleep(1)
    print(" 4 x {} = {}".format(nt, nt * 4))
    time.sleep(1)
    print(" 5 x {} = {}".format(nt, nt * 5))
    time.sleep(1)
    print(" 6 x {} = {}".format(nt, nt * 6))
    time.sleep(1)
    print(" 7 x {} = {}".format(nt, nt * 7))
    time.sleep(1)
    print(" 8 x {} = {}".format(nt, nt * 8))
    time.sleep(1)
    print(" 9 x {} = {}".format(nt, nt * 9))
    time.sleep(1)
    print(" 10 x {} = {}".format(nt, nt * 10))
    time.sleep(1)
    print(" 11 x {} = {}".format(nt, nt * 11))
    time.sleep(1)
    print(" 12 x {} = {}".format(nt, nt * 12))
    time.sleep(1)
    print(" 13 x {} = {}".format(nt, nt * 13))
    time.sleep(1)
    print(" 14 x {} = {}".format(nt, nt * 14))
    time.sleep(1)
    print(" 15 x {} = {}".format(nt, nt * 15))
    time.sleep(1)
    print(" 16 x {} = {}".format(nt, nt * 16))
    time.sleep(1)
    print(" 17 x {} = {}".format(nt, nt * 17))
    time.sleep(1)
    print(" 18 x {} = {}".format(nt, nt * 18))
    time.sleep(1)
    print(" 19 x {} = {}".format(nt, nt * 19))
    time.sleep(1)
    print(" 20 x {} = {}".format(nt, nt * 20))

elif pergunta == "calculadora":
    n1 = int(input("primeiro número: "))
    n2 = int(input("segundo número: "))
    print("{} x {} = {}".format(n1, n2, n1 * n2))
