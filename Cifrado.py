def Pregunta_5 (frase, a, b):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    m = len(alfabeto) 
    texto_encriptado = ''

    for c in frase:
        if c in alfabeto:
            x = alfabeto.index(c)
            encriptado = (a * x + b) % m
            texto_encriptado += alfabeto[encriptado]
        else:
            texto_encriptado += c

    return texto_encriptado.upper()


frase = "si la gente no cree que las matematicas son simples, es solo porque no se dan cuenta de lo complicado que es la vida"
a = 11
b = 15
texto_encriptado = Pregunta_5(frase, a, b)
print (texto_encriptado)