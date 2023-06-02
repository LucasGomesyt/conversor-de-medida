#Conversor de unidades

#Unidade de medidas
def converter_unidades(massa, unidade_origem, unidade_destino):
    fatores = {
        'kg': 1,
        'g': 1000,
        't': 0.001,
        'mg': 1e+6,
        'mcg': 1e+9
    }

    massa_convertida = massa * fatores[unidade_destino] / fatores[unidade_origem]
    return massa_convertida

massa = float(input('Digite a quantidade de massa: '))
unidade_origem = input("Digite a unidade de origem (kg, g, t, mg, mcg): ")
unidade_destino = input("Digite a unidade de destino (kg, g, t, mg, mcg): ")
massa_convertida = converter_unidades(massa, unidade_origem, unidade_destino)
print(f'{massa} {unidade_origem} é igual a {massa_convertida} {unidade_destino}')