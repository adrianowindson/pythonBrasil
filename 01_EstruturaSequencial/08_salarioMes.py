#!/usr/bin/python3
# 08 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salarioHora = float(input("Digite quanto você ganha por hora: "))
HoraTrabalhadaMes = int(input("Quantas horas trabalhadas por mês: "))

salarioMensal = salarioHora * HoraTrabalhadaMes
print("O salário mensal é: %s" %(salarioMensal))