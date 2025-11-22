import requests
from rich.console import Console
from rich.table import Table
from funcoes.gerais import titulo

console = Console()

BASE_URL = "http://localhost:3000"


# ======================================================
#   PESQUISA AVANÇADA — Nome + Categoria (ou só 1 deles)
# ======================================================

def pesquisa_produtos_avancada():
    titulo("Pesquisa Avançada de Produtos")

    nome = input("Pesquisar por nome (ou deixar vazio): ").strip().lower()
    categoria = input("Pesquisar por categoria (ou deixar vazio): ").strip().lower()

    # Se nada foi digitado
    if nome == "" and categoria == "":
        console.print("[yellow]Você deve informar pelo menos um filtro![/yellow]")
        input("ENTER para continuar...")
        return

    try:
        resp = requests.get(f"{BASE_URL}/produtos")

        if resp.status_code != 200:
            console.print("[red]Erro ao buscar produtos![/red]")
            input("ENTER...")
            return

        produtos = resp.json()

        # FILTROS DINÂMICOS
        resultados = []

        for p in produtos:
            nome_match = nome in p["nome"].lower() if nome else True
            categ_match = categoria in p["categoria"].lower() if categoria else True

            if nome_match and categ_match:
                resultados.append(p)

        if not resultados:
            console.print("[yellow]Nenhum produto encontrado com os filtros informados![/yellow]")
            input("ENTER para continuar...")
            return

        table = Table(title="Resultados da Pesquisa", header_style="bold magenta")
        table.add_column("ID", style="cyan")
        table.add_column("Nome", style="deep_pink3")
        table.add_column("Categoria", style="yellow")
        table.add_column("Preço", justify="right", style="green")
        table.add_column("Estoque", justify="right")

        for p in resultados:
            table.add_row(
                str(p["id"]),
                p["nome"],
                p["categoria"],
                f"R$ {p['preco']:.2f}",
                str(p["estoque"])
            )

        console.print(table)

    except Exception as e:
        console.print(f"[red]Erro de conexão: {e}[/red]")

    input("ENTER para continuar...")
