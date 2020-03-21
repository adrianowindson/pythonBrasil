#!/usr/bin/python3
# 4 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input("Insira a nota do 1º Bimestre: "))
nota2 = float(input("Insira a nota do 2º Bimestre: "))
nota3 = float(input("Insira a nota do 3º Bimestre: "))
nota4 = float(input("Insira a nota do 4º Bimestre: "))

mediaAluno = (nota1 + nota2 + nota3 + nota4) / 4

print("A média do Aluno foi: %s" %(mediaAluno))