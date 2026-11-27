# Research: AST base e nós de expressão

Meia página; só o que muda a implementação. Fontes: `docs/01` §6, `docs/05`, `docs/03`.

## D1 — Estrutura dos nós

- **Decisão**: `@dataclass(frozen=True)` por nó, campos de domínio + `line`/`column`.
- **Rationale**: D-02 (dados puros + visitantes); imutável desde a criação (T1);
  `eq` estrutural e `repr` de graça, exigidos pelo "Pronto quando".
- **Alternativas**: `NamedTuple` (perde `frozen` explícito e legibilidade de
  campos-chave); classes com `__slots__` manuais (boilerplate sem ganho didático).

## D2 — Campo `tipo` (VarDecl/ArrayDecl/Convert)

- **Decisão**: `CliteType = Literal["int", "float", "char", "bool"]` declarado em `nodes.py`.
- **Rationale**: validação estática sem runtime; `types.py` (`IntType`...) é
  território do ticket de semântica; o ticket fixa os arquivos tocados.
- **Alternativas**: `str` solto (mypy não protege); definir tipos agora (estoura
  o escopo do ticket).

## D3 — Posição com padrão

- **Decisão**: `line: int = 0, column: int = 0` ao fim de cada nó; `0` = não informado.
- **Rationale**: o exemplo da issue constrói nós sem posição, logo os campos
  precisam de padrão; campos padrão devem vir depois dos obrigatórios
  (regra de dataclass); `0`/`1` são as únicas literais numéricas liberadas pela
  regra de números mágicos — nenhuma constante extra necessária.
- **Alternativas**: posição obrigatória (quebra o exemplo do ticket); `None`
  (propaga `Optional` para as fases sem necessidade).

## D4 — Hierarquia

- **Decisão**: aliases de união (`Declaration`, `Command`, `Expression`), sem ABC.
- **Rationale**: nós continuam dados puros; o checker/avaliador farão despacho
  por visitante depois; uniões fechadas dão exaustividade em `match`.
- **Alternativas**: classes base abstratas (adicionam acoplamento e nada de
  comportamento agora); `Protocol` (desnecessário sem métodos).

## D5 — `If` sem `else`

- **Decisão**: `else: Command | None = None`, campo após `then`.
- **Rationale**: §6 marca `senão?` como opcional; ordem de campos respeita
  dataclass (padrões por último).
- **Alternativas**: nó `Skip` como else sintético (esconde informação do §6).

## D6 — ArrayDecl.tamanho

- **Decisão**: `size: int` puro, não um nó `IntLiteral`.
- **Rationale**: §6 fixa "literal inteiro na declaração, não expressão"; o nó de
  declaração já carrega a posição.
- **Alternativas**: `IntLiteral` (adicionaria nó dentro de declaração sem uso).
