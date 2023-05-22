def contar_vogais(v1: str ) -> int:
    contagem = 0
    vogais = ["a", "e", "i", "o", "u"]
    for x in v1:
        if x in vogais:
            contagem += 1
        
    return contagem 

texto = input("Digite uma palavra: ")
quantidade = contar_vogais(texto)

print("A quantidade foi: ", quantidade)