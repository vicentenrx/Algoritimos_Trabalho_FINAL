import requests
from funcoes.gerais import titulo

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm

BASE_URL = "http://localhost:3000"

console = Console()


def criar_produto():
    titulo("Adicionar Produtos")

    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: "))
    estoque = int(input("Estoque: "))
    
    try:
        response = requests.post(f"{BASE_URL}/produtos", json={
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "estoque": estoque
        })

        if response.status_code == 201:
            produto = response.json()
            print(f"Produto criado com sucesso! ID: {produto['id']}")
        else:
            print("Erro ao criar produto!")

    except Exception as e:
        print(f"Erro: {e}")

    input("Pressione ENTER para continuar...")


def listar_produtos():
    titulo("Listagem de Produtos")

    try:
        response = requests.get(f"{BASE_URL}/produtos")
        if response.status_code !=200:
            console.print("Erro ao obter lista de produtos", style="bold red")
            return

        produtos = response.json()

        table = Table(show_header=True,
        header_style="bold magenta") # Trocar Cor
        table.add_column("Cód.", style="dim")
        table.add_column("Produto")
        table.add_column("Categoria")
        table.add_column("Preço", justify="right")
        table.add_column("Estoque")

        for produto in produtos:
            preco_f = f"{produto.get('preco', 0):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

            table.add_row(
                str(produto.get("id")),
                str(produto.get("nome", "")),
                str(produto.get("categoria", "")),
                f"R$ {preco_f}",
                str(produto.get("estoque", ""))
            )

        console.print(table)

    except Exception as e:
        console.print(f"Erro de conexão: {e}",
        style="bold red")

    input("Pressione ENTER para continuar..............")

def buscar_produto_por_id():
    titulo("Buscar Produto por ID")

    produto_id = input("Informe o ID do produto: ")

    try:
        resposta = requests.get(f"{BASE_URL}/produtos/{produto_id}")

        if resposta.status_code != 200:
            console.print("[red]Produto não encontrado![/red]")
            input("Pressione ENTER para continuar...")
            return

        produto = resposta.json()

        console.print("\n[bold deep_pink3]Produto localizado:[/bold deep_pink3]")
        console.print(f"[cyan]ID:[/cyan] {produto.get('id')}")
        console.print(f"[cyan]Nome:[/cyan] {produto.get('nome')}")
        console.print(f"[cyan]Categoria:[/cyan] {produto.get('categoria')}")
        console.print(f"[cyan]Preço:[/cyan] R$ {produto.get('preco'):.2f}")
        console.print(f"[cyan]Estoque:[/cyan] {produto.get('estoque')}")

    except Exception as e:
        console.print(f"[bold red]Erro ao consultar produto: {e}[/bold red]")

    input("\nPressione ENTER para continuar...")


def atualizar_produto():
    titulo("Atualizar Produto")

    produto_id = input("Informe o ID do produto a ser atualizado: ")

    try:
        resposta = requests.get(f"{BASE_URL}/produtos/{produto_id}")

        if resposta.status_code != 200:
            console.print("[red]Produto não encontrado![/red]")
            input("Pressione ENTER para continuar...")
            return

        produto = resposta.json()

        console.print("[deep_pink3]Deixe vazio para manter o valor atual.[/deep_pink3]")

        nome = input(f"Nome ({produto['nome']}): ") or produto["nome"]
        categoria = input(f"Categoria ({produto['categoria']}): ") or produto["categoria"]

        preco_input = input(f"Preço ({produto['preco']}): ")
        preco = float(preco_input) if preco_input else produto["preco"]

        estoque_input = input(f"Estoque ({produto['estoque']}): ")
        estoque = int(estoque_input) if estoque_input else produto["estoque"]

        dados_atualizados = {
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "estoque": estoque
        }

        resposta_update = requests.patch(f"{BASE_URL}/produtos/{produto_id}", json=dados_atualizados)

        if resposta_update.status_code == 200:
            console.print("[bold green]Produto atualizado com sucesso![/bold green]")
        else:
            console.print("[red]Erro ao atualizar produto![/red]")

    except Exception as e:
        console.print(f"[bold red]Erro de conexão: {e}[/bold red]")

    input("\nPressione ENTER para continuar...")



def deletar_produto():
    titulo("Excluir Produto")

    produto_id = input("Informe o ID do produto que deseja excluir: ")

    try:
        resposta = requests.get(f"{BASE_URL}/produtos/{produto_id}")

        if resposta.status_code != 200:
            console.print("[red]Produto não encontrado![/red]")
            input("Pressione ENTER para continuar...")
            return

        console.print(f"[yellow]Tem certeza que deseja excluir o produto '{resposta.json()['nome']}'?[/yellow]")
        confirm = input("Digite S para confirmar: ").upper()

        if confirm != "S":
            console.print("[cyan]Operação cancelada.[/cyan]")
            input("Pressione ENTER para continuar...")
            return

        resposta_del = requests.delete(f"{BASE_URL}/produtos/{produto_id}")

        if resposta_del.status_code == 200:
            console.print("[bold green]Produto excluído com sucesso![/bold green]")
        else:
            console.print("[red]Erro ao excluir produto![/red]")

    except Exception as e:
        console.print(f"[bold red]Erro de conexão: {e}[/bold red]")

    input("\nPressione ENTER para continuar...")
