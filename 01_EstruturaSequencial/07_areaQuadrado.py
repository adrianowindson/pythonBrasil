#!/usr/bin/python3
# 07 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = int(input("Entre com o valor do lado do quadrado: "))
altura = int(input("Entre com a altura do quadrado: "))
area = lado * altura
dobroArea = area * 2
print("O valor da área é: %s" %(area))
print("O dobro dessa área é: %s" %(dobroArea))