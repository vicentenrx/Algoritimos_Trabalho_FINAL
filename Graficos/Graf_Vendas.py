from rich.console import Console
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn
import requests
from collections import Counter
from funcoes.gerais import titulo

console = Console()
BASE_URL = "http://localhost:3000"

def grafico_vendas_por_produto():
    titulo("Gráfico — Vendas por Produto")

    try:
        resp = requests.get(f"{BASE_URL}/vendas")

        if resp.status_code != 200:
            console.print("[red]Erro ao buscar vendas![/red]")
            input("ENTER para continuar...")
            return

        vendas = resp.json()

        if not vendas:
            console.print("[yellow]Nenhuma venda encontrada![/yellow]")
            input("ENTER para continuar...")
            return

        nomes = []

        for v in vendas:
            prod = requests.get(f"{BASE_URL}/produtos/{v['produtoId']}").json()
            nomes.append(prod["nome"])

        contagem = Counter(nomes)

        console.print("[bold deep_pink3]Quantidade de Vendas por Produto[/bold deep_pink3]\n")

        for nome, qtd in contagem.items():
            console.print(
                f"[cyan]{nome:<20}[/cyan] "
                + "[magenta]" + ("█" * qtd * 2) + f"[/magenta] {qtd}"
            )

    except Exception as e:
        console.print(f"[red]Erro ao gerar gráfico: {e}[/red]")

    input("\nENTER para continuar...")
