vitorias = int(input("Vitórias: "))
derrotas = int(input("Derrotas: "))

def Classificador(saldo, rank):
    saldo = vitorias - derrotas

    if saldo >= 11 and saldo <= 20:
        rank = "Bronze"

    elif saldo > 20 and saldo <= 50:
        rank = "Prata"

    elif saldo > 50 and saldo <= 80:
        rank = "Ouro"

    elif saldo > 80 and saldo <= 90:
        rank = "Diamante"

    elif saldo > 90 and saldo <= 100:
        rank = "Lendário"

    elif saldo >= 101:
        rank = "Imortal"
        
    else:
        rank = "Sem rank"


    return print(f"Seu rank é {rank}")
 
Classificador(vitorias, derrotas)