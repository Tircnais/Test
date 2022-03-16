"""
Dada una cadena formada sólo por caracteres en minúscula,
cree dos métodos que filtren todas las consonantes y vocales de la palabra dada.
Deben conservar el orden original de los caracteres en el resultado.
"""

def FiltroVocales(cadena: str, vocales: list):
    encontradas = []
    encontradas.extend([letra for letra in cadena if letra in vocales])
    return "".join(encontradas)

def FiltroConsonantes(cadena: str, vocales: list):
    encontradas = []
    encontradas.extend([letra for letra in cadena if letra not in vocales])
    return "".join(encontradas).replace(" ", "")


S= "funeraria Jaramillo"
S= S.lower()
vocales = ['a', 'e', 'i', 'o', 'u']
print(f"Cade a evaluar, {S}")
f_vocales = FiltroVocales(S, vocales)
print(f"Vocales encontradas: {f_vocales}")
f_consonantes = FiltroConsonantes(S, vocales)
print(f"Consonantes encontradas: {f_consonantes}")
