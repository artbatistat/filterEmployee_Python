'''
Lista1 = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trabalham durante o dia
Lista3 = Funcionários que não tem carro
'''

funcionarios = set(['Ana','Marcos','Alice','Pedro','Sophia','Bruno','Melissa'])
turno_dia = set(['Ana','Marcos','Alice','Melissa'])
turno_noite = set(['Pedro','Sophia','Bruno'])
tem_carro = set(['Marcos','Alice','Bruno','Melissa'])

lista1 = set(tem_carro).intersection(turno_noite)
lista2 = set(tem_carro).intersection(turno_dia)
lista3 = set(funcionarios).difference(tem_carro)

print(f'Funcionários com carro e que trabalham a noite: {lista1}')
print(f'Funcionários com carro e que trabalham durante o dia: {lista2}')
print(f'Funcionários que não tem carro: {lista3}')



