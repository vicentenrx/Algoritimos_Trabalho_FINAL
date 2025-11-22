import requests
import matplotlib.pyplot as plt
from collections import Counter
from rich.console import Console
from funcoes_gerais.gerais import titulo

console = Console()

BASE_URL = "http://localhost:3000"

# ============================
#   GRÁFICO — VENDAS
# ============================

def grafico_vendas_por_produto():
    titulo("Gráfico — Vendas por Produto")

    try:
        resp_vendas = requests.get(f"{BASE_URL}/vendas")

        if resp_vendas.status_code != 200:
            console.print("[red]Erro ao buscar vendas![/red]")
            input("ENTER para continuar...")
            return

        vendas = resp_vendas.json()

        if not vendas:
            console.print("[yellow]Nenhuma venda encontrada![/yellow]")
            input("ENTER para continuar...")
            return

        nomes_produtos = []

        for v in vendas:
            resp_prod = requests.get(f"{BASE_URL}/produtos/{v['produtoId']}")
            if resp_prod.status_code == 200:
                prod = resp_prod.json()
                nomes_produtos.append(prod["nome"])

        contagem = Counter(nomes_produtos)

        plt.figure(figsize=(9, 6))
        plt.bar(contagem.keys(), contagem.values())
        plt.title("Quantidade de Vendas por Produto")
        plt.xticks(rotation=45, ha='right')
        plt.xlabel("Produto")
        plt.ylabel("Vendas")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        console.print(f"[red]Erro ao gerar gráfico: {e}[/red]")

    input("ENTER para continuar...")