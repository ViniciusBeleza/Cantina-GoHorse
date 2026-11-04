# 🥪 Cantina CESAR — Versão Go-Horse (Entrega 1)

App de linha de comando para **pedido antecipado na cantina**: o aluno monta o pedido, paga
(Pix, cartão ou carteira), entra na fila e é avisado quando o pedido está **pronto** — sem perder
os 15 minutos do intervalo na fila.

Esta é a **versão go-horse**: foi feita rápido, **funciona**, mas é frágil de propósito (ou por
pressa). Ela é o "antes" do projeto; a versão refatorada com princípios de projeto está na
**Entrega 2** (repositório `cantina-cesar`).

Só biblioteca padrão do Python 3.10+ (sem instalar nada).

## Como rodar
```bash
python demo_go_horse.py     # fluxo: 3 pedidos (Pix, carteira, cartão recusado) e a cozinha chamando a fila
python demo_dores.py        # as 5 dores da versão go-horse, uma por uma
python -m unittest          # testes de fumaça (3)
```

## Como funciona
Tudo está em **`cantina_go_horse.py`** (2 funções + 2 variáveis globais):

| Peça | O que é |
|---|---|
| `processa_pedido(aluno, itens, tipo_pagamento, dados_pagamento)` | Calcula preços, aplica desconto, cobra e põe na fila. **Tudo numa função.** |
| `prepara_proximo()` | Tira o primeiro da fila e avisa que está pronto. |
| `fila` | Lista global e **pública** com os pedidos. |
| `saldos` | Dict global e **público** com o saldo da carteira de cada aluno. |

Itens do cardápio: coxinha (R$ 6), suco (R$ 5), pão de queijo (R$ 4), café (R$ 3).
Desconto: coxinha + suco = −R$ 2. Cada pedido espera ~2 min por posição na fila.

## O que está errado (e dá para provar)
Medido com o `metricas.py` da Entrega 2 (complexidade ciclomática = decisões + 1):

| Métrica | Valor |
|---|---|
| Funções | 2 |
| `processa_pedido` | **CC = 14**, 44 linhas |
| CC média por função | 8,0 |

`python demo_dores.py` reproduz cada problema:

| # | Dor | Por quê | Princípio violado |
|---|---|---|---|
| 1 | Aceitar um novo meio de pagamento exige **editar** `processa_pedido` | pagamento é um `if/elif` dentro da função | Aberto/Fechado |
| 2 | Qualquer código corrompe a fila (`fila.append("lixo")` e o `prepara_proximo` quebra) | `fila` é global e pública | Ocultamento de informação |
| 3 | O mesmo cartão paga duas vezes além do limite | a função só compara, nunca debita o cartão | responsabilidades misturadas |
| 4 | Combo só vale para coxinha + suco | a regra está escrita direto no `if` | Aberto/Fechado |
| 5 | Item inválido só imprime "item invalido" e devolve `None` | sem exceção, quem chama não sabe o motivo | tratamento de erro |

Além disso, a função mistura **preço, desconto, pagamento, fila e mensagens** (viola
Responsabilidade Única) e é difícil de testar, porque as mensagens saem por `print` e o
estado é global.

## Limitações conhecidas (não são bugs escondidos)
- Os nomes precisam ser idênticos: `saldos["ana"]` não vale para `"Ana"`.
- Os itens são strings sem acento (`"pao de queijo"`, `"cafe"`).
- Só existe saldo inicial para `"ana"` (os demais precisam ser cadastrados em `saldos`).

## Estrutura
```
cantina_go_horse.py   a versão go-horse (tudo aqui)
demo_go_horse.py      fluxo completo
demo_dores.py         as 5 dores, uma por uma
test_smoke.py         3 testes de fumaça
ROTEIRO_VIDEO.md      roteiro do vídeo (3:00)
```

## Equipe
_(preencher: nomes e papéis)_
