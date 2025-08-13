def segundo_maior(lista):
    if len(lista) < 2:
        return None 
    
    ordenar = sorted(lista)
    return ordenar [-2]
    

lista = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
segundo_maior_numero = segundo_maior(lista)

if segundo_maior_numero:
    print("O segundo maior número desta lista é: ", segundo_maior_numero)

else:
    print("A lista não tem mais de um elemento.")
