"""Demo da versão go-horse (Entrega 1).
Mesmo cenário da demo da Entrega 2: Ana (Pix), Bia (carteira) e Caio (cartão recusado)."""
import cantina_go_horse as cantina

# Os saldos são um dict global e público: qualquer arquivo mexe neles.
cantina.saldos["Bia"] = 20.0  # a chave tem que bater EXATAMENTE com o nome ('ana' != 'Ana')

print("== Pedidos ==")
cantina.processa_pedido("Ana", ["coxinha", "suco"], "pix", {"chave": "ana@pix"})
cantina.processa_pedido("Bia", ["pao de queijo", "cafe"], "carteira", {})
cantina.processa_pedido("Caio", ["coxinha", "suco"], "cartao", {"limite": 3})

print("\n== Cozinha chama a fila ==")
while len(cantina.fila) > 0:  # a fila também é global e pública
    cantina.prepara_proximo()
