import random
print(" desarme a bomba: ")
print(" selecione o fio certo: d1 f2 h4 j5")
bomba= random.randint(1,5)
t= 2

while True:
     fio= int(input("digite o numero do fio: "))
     
     
     if bomba == fio:
         print("a bomba foi desarmada com sucesso")
         break
     elif bomba < fio:
         t -= 1
         print(" a bomba quase explodiu tente de novo")
     elif bomba > fio:
            t -= 1
            print(" a bomba quase explodiu tente de novo")
    if t==0:
     print("explodiu")
     break