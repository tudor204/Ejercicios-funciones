def contar_letras(palabra):
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    contador = {"vocales": 0, "consonantes": 0}
    for letra in palabra:
        if letra.isalpha():
            if letra in vocales:
                contador["vocales"] += 1
            else:
                contador["consonantes"] += 1
    return contador

print(contar_letras("Acordeón"))
