#!/usr/bin/python3
# 09 - Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).

temperaturaF = int(input("Digite a temperatura em Farenheit: "))
temperaturaCelsius = 5 * (temperaturaF - 32) / 9
print("A temperatura em Farenheit: %s convertida para Celsius ficou: %s" %(temperaturaF, temperaturaCelsius))