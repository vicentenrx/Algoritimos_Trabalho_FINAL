import requests
import matplotlib.pyplot as plt
from collections import Counter
from rich.console import Console
from funcoes.gerais import titulo

console = Console()

BASE_URL = "http://localhost:3000"

# ============================
#   GRÁFICO — PRODUTOS
# ============================

def grafico_produtos_por_categoria():
    titulo("Gráfico — Produtos por Categoria")

    try:
        resposta = requests.get(f"{BASE_URL}/produtos")

        if resposta.status_code != 200:
            console.print("[red]Erro ao buscar produtos![/red]")
            input("ENTER para continuar...")
            return

        produtos = resposta.json()

        if not produtos:
            console.print("[yellow]Nenhum produto encontrado![/yellow]")
            input("ENTER para continuar...")
            return

        categorias = [p["categoria"] for p in produtos]
        contagem = Counter(categorias)

        plt.figure(figsize=(8, 5))
        plt.bar(contagem.keys(), contagem.values())
        plt.title("Quantidade de Produtos por Categoria")
        plt.xlabel("Categoria")
        plt.ylabel("Quantidade")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        console.print(f"[red]Erro ao gerar gráfico: {e}[/red]")

    input("ENTER para continuar...")