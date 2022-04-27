# 1. Pergunte ao usuário em qual cidade e o estado em que ele(a) mora
cidade = input('Qual é o sua cidade?')
print(cidade)
estado = input('Qual é o seu estado?')
print(estado)
# 2. Imprima uma mensagem diga a cidade em que o usuário mora. 
#    O nome da cidade deve estar todo em letras maiúsculas.
Cidade_maiu = cidade.upper()
print('A sua cidade é ' + Cidade_maiu)

# 3. Imprima uma mensagem diga o estado em que o usuário mora. 
#    O nome do estado deve estar todo em letras maiúsculas.
#    Utilize uma forma de formatação de string diferente da que foi usada no item 2.
Estado_que_mora = 'O seu estado é {} '.format(estado)
print(Estado_que_mora)