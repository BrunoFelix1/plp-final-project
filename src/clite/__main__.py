# ================================================= #
# MAIN - Orquestracao do interpretador CLite
# Ticket 004
# ================================================= #
from clite.cli import criar_parser, executar_comando, validar_arquivo

# ================================================= #
# Fluxo principal
# ================================================= #


def main(argv: list[str] | None = None) -> int:
    args = criar_parser().parse_args(argv)

    if not validar_arquivo(args.arquivo):
        return 2

    return executar_comando()


if __name__ == "__main__":
    raise SystemExit(main())
