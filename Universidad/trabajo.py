def depositar(y):
    x=int(input('Valor a depositar a su cuenta: '))
    resultado=x+y
    return resultado
def girar(g):
    x=int(input('Ingrese valor a girar: '))
    resultado=g-x
    return resultado    
def trans(z):
    x=int(input('Ingrese valor a transferir: '))
    resultado=z-x
    return resultado
    

total=50000
print('1. Menu cajero...');
print('2. Deposito...');
print('3. Giros...');
print('4. Transferencia...');
print('5. Compras...');
print('6. Pagos de servicios...');
opcion=int(input('Ingrese un valor: '))
if opcion==2:
    total=depositar(total);
    print(total)
elif opcion==3:
    total=girar(total);
    print(total)
elif opcion==4:
    cuenta=int(input('Ingresa la cuenta a la quieres transferir: '))
    total=trans(total);
    print('Se transfirio un total de',total, 'a la siguiente cuenta:',cuenta)