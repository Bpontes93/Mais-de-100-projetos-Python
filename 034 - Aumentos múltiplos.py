#Escreva um programa que pergunte o salário de um funcionário e calcule seu aumento.
#Para sálario superiores a R$1.250,00 o aumento será de 10%, para inferiores ou iguais o aumento é de 15%.
sl = float(input("Insira seu salário: "))

if sl <= 1250.00:
    print("Seu aumento será de R${:0.2f}\nTendo R${:0.2f} como novo salário".format(sl*0.15, sl*1.15))

else: print("Seu aumento será de R${:0.2f}\nTendo R${:0.2f} como novo salário".format(sl*0.10, sl*1.10))