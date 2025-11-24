from rich.console import Console
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn
import requests
from collections import Counter
from funcoes.gerais import titulo

console = Console()
BASE_URL = "http://localhost:3000"


def grafico_produtos_por_categoria():
    titulo("Gráfico — Produtos por Categoria")

    try:
        resp = requests.get(f"{BASE_URL}/produtos")

        if resp.status_code != 200:
            console.print("[red]Erro ao buscar produtos![/red]")
            input("ENTER para continuar...")
            return

        produtos = resp.json()

        if not produtos:
            console.print("[yellow]Nenhum produto encontrado![/yellow]")
            input("ENTER para continuar...")
            return

        categorias = [p["categoria"] for p in produtos]
        contagem = Counter(categorias)

        console.print("[bold deep_pink3]Quantidade de Produtos por Categoria[/bold deep_pink3]\n")


        for categoria, qtd in contagem.items():
            console.print(
                f"[cyan]{categoria:<15}[/cyan] "
                + "[green]" + ("█" * qtd * 2) + f"[/green] {qtd}"
            )

    except Exception as e:
        console.print(f"[red]Erro ao gerar gráfico: {e}[/red]")

    input("\nENTER para continuar...")
