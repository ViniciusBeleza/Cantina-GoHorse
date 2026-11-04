"""As DORES da versão go-horse: cada bloco mostra um problema real (e reproduzível).
Rode: python demo_dores.py"""
import cantina_go_horse as cantina


def titulo(t):
    print(f"\n=== {t} ===")


titulo("1) Novo meio de pagamento (voucher) NÃO cabe sem editar a função")
cantina.processa_pedido("Duda", ["coxinha"], "voucher", {"codigo": "CESAR-123"})
print("   -> para aceitar 'voucher' é preciso abrir processa_pedido e criar mais um elif.")

titulo("2) Fila global e pública: qualquer um corrompe")
cantina.fila.append("lixo")          # nada impede isso
try:
    cantina.prepara_proximo()
except TypeError as e:
    print("   -> quebrou:", e)
cantina.fila.clear()

titulo("3) Cartão não debita o limite: o mesmo cartão paga duas vezes")
cartao = {"limite": 10}
cantina.processa_pedido("Eva", ["coxinha", "suco"], "cartao", cartao)   # total 9
cantina.processa_pedido("Eva", ["coxinha", "suco"], "cartao", cartao)   # total 9 de novo
print("   -> limite de R$ 10 aprovou R$ 18 (o limite nunca diminui).")
cantina.fila.clear()

titulo("4) Combo só existe para coxinha+suco (regra escrita no if)")
cantina.processa_pedido("Fábio", ["pao de queijo", "cafe"], "pix", {"chave": "f@pix"})
print("   -> lanche+bebida deveria ter desconto; aqui pagou R$ 7 cheio.")
cantina.fila.clear()

titulo("5) Item com acento é 'invalido' e o erro é só um print")
r = cantina.processa_pedido("Gabi", ["pão de queijo"], "pix", {"chave": "g@pix"})
print("   -> retorno:", r, "(quem chamou nem sabe o motivo; não há exceção)")
