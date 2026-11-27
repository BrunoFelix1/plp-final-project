# Data Model: Tabela de símbolos (ticket 012)

## Entidades

### Declaração (existente, #9)

Nó da AST carregado pela tabela; a tabela não cria dados novos.

| Campo | VarDecl | ArrayDecl |
| --- | --- | --- |
| name | nome declarado | nome declarado |
| type | `"int" \| "float" \| "char" \| "bool"` | idem |
| size | — | literal inteiro (validação é do parser, D-11) |
| line, column | posição 1-based; 0 = não informado | idem |

### Tabela de símbolos (nova)

Mapa plano nome → Declaração, escopo único (D-06), ordem de inserção preservada.

| Propriedade | Regra |
| --- | --- |
| Unicidade | um nome só pode ser registrado uma vez; 2º registro → `E3002` |
| Resolução | busca devolve a declaração original; ausente → `E3001` |
| Exposição | lista de declarações em ordem de inserção (contrato com #13/#14) |
| Plana | blocos não criam escopo; não há sombreamento (D-06) |

### Erro semântico (nova, local)

Diagnóstico com `code` (E3xxx), `line`, `column`, `message`; texto no formato
`erro E<NNNN> (linha L, coluna C): texto` (docs/03 §5), em português.

| Código | Quando | Posição |
| --- | --- | --- |
| `E3001` | busca de nome não registrado | referência informada na busca (0, 0 se omitida) |
| `E3002` | segundo registro do mesmo nome | nó da segunda declaração |

## Invariantes

1. Após `n` registros bem-sucedidos, a lista exposta tem exatamente `n`
   declarações, na ordem de registro.
2. Unicidade ⇒ bijeção nome → declaração; todo nome da lista aparece uma vez.
3. A tabela não muta os nós da AST (nós são `frozen`; D-02).
4. Registro que falha não persiste: erro não deixa estado parcial.
