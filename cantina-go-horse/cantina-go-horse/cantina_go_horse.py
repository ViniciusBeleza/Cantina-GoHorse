"""VERSÃO GO-HORSE (Entrega 1) - funciona, mas é frágil. Mantida só para o 'antes e depois'."""

fila = []          # global e público: qualquer um mexe
saldos = {"ana": 20.0}


def processa_pedido(aluno, itens, tipo_pagamento, dados_pagamento):
    total = 0
    for item in itens:
        if item == "coxinha":
            total += 6
        elif item == "suco":
            total += 5
        elif item == "pao de queijo":
            total += 4
        elif item == "cafe":
            total += 3
        else:
            print("item invalido")
            return None

    if "coxinha" in itens and "suco" in itens:
        total -= 2

    if tipo_pagamento == "pix":
        if dados_pagamento.get("chave"):
            print("Pix de", total, "recebido")
        else:
            print("pix recusado")
            return None
    elif tipo_pagamento == "cartao":
        if dados_pagamento.get("limite", 0) >= total:
            print("Cartao de", total, "aprovado")
        else:
            print("cartao recusado")
            return None
    elif tipo_pagamento == "carteira":
        if saldos.get(aluno, 0) >= total:
            saldos[aluno] -= total
            print("Carteira debitada em", total)
        else:
            print("saldo insuficiente")
            return None
    else:
        print("pagamento desconhecido")
        return None

    fila.append({"aluno": aluno, "itens": itens, "total": total})
    print(aluno, "esta na posicao", len(fila), "- espera aprox", len(fila) * 2, "min")
    return len(fila)


def prepara_proximo():
    if len(fila) > 0:
        p = fila.pop(0)
        print("PRONTO:", p["aluno"], "pode retirar o pedido!")
