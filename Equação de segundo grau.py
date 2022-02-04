a = float(input('Digite o valor do A: '))
b = float(input('Digite o valor do B: '))
c = float(input('Digite o valor do C: '))
Delta = (b ** 2) - (4 * a * c)
if Delta < 0:
    print('Não existem raizes reais!')
elif Delta == 0:
    umaRaiz = (-b +  (Delta**0.5))/(2*a)
    print('Existe uma raiz real e ela é: '+ str(umaRaiz))
else:
    xmais = (-b +  (Delta**0.5))/(2*a)
    xmenos = (-b - (Delta**0.5))/(2*a)
    print('Existem duas raizes reais e elas são X¹: '+ str(round(xmais, 2)) + ' e X²: ' + str(round(xmenos, 2)))
