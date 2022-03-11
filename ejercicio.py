def FiltroVocales(cadena: str, vocales: list):
    cadena= list(cadena)
    encontradas = []
    for item in cadena:
        if item in vocales:
            encontradas.append(item)
    return str(encontradas)

def FiltroConsonantes(cadena: str, vocales: list):
    cadena= list(cadena)
    encontradas = []
    for item in cadena:
        if item not in vocales:
            encontradas.append(item)
    return str(encontradas)


S= "funeraria Jaramillo"
S= S.lower()
vocales = ['a', 'e', 'i', 'o', 'u']
print(f"Cade a evaluar, {S}")
f_vocales = FiltroVocales(S, vocales)
print(f"Vocales encontradas, {f_vocales}")
f_consonantes = FiltroConsonantes(S, vocales)
print(f"Consonantes encontradas, {f_consonantes}")
print(f"Tipo, {type(f_vocales)}")