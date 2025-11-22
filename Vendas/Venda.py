import requests
from funcoes.gerais import titulo

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm

console = Console()

BASE_URL = "http://localhost:3000"

def criar_venda():
    titulo("Registrar Venda")

    produto_id = input("ID do produto: ")
    quantidade = input("Quantidade: ")

    try:
        # Verifica se o produto existe
        resp_prod = requests.get(f"{BASE_URL}/produtos/{produto_id}")

        if resp_prod.status_code != 200:
            console.print("[red]Produto não encontrado![/red]")
            input("ENTER para continuar...")
            return
        
        produto = resp_prod.json()

        nova_venda = {
            "produtoId": int(produto_id),
            "quantidade": int(quantidade)
        }

        resp = requests.post(f"{BASE_URL}/vendas", json=nova_venda)

        if resp.status_code == 201:
            console.print(f"[green]Venda registrada para o produto: {produto['nome']}[/green]")
        else:
            console.print("[red]Erro ao registrar venda![/red]")

    except Exception as e:
        console.print(f"[bold red]Erro de conexão: {e}[/bold red]")

    input("Pressione ENTER para continuar...")



def listar_vendas():
    titulo("Lista de Vendas")

    try:
        resp = requests.get(f"{BASE_URL}/vendas")

        if resp.status_code != 200:
            console.print("[red]Erro ao obter lista de vendas[/red]")
            input("ENTER para continuar...")
            return

        vendas = resp.json()

        if not vendas:
            console.print("[yellow]Nenhuma venda registrada.[/yellow]")
            input("ENTER para continuar...")
            return

        for v in vendas:
            prod = requests.get(f"{BASE_URL}/produtos/{v['produtoId']}").json()
            
            console.print(f"""
[cyan]ID da Venda:[/cyan] {v['id']}
Produto: {prod['nome']}
Quantidade: {v['quantidade']}
""")

    except Exception as e:
        console.print(f"[bold red]Erro de conexão: {e}[/bold red]")

    input("Pressione ENTER para continuar...")


def buscar_venda_por_id():
    titulo("Buscar Venda por ID")

    venda_id = input("ID da Venda: ")

    try:
        resp = requests.get(f"{BASE_URL}/vendas/{venda_id}")

        if resp.status_code != 200:
            console.print("[red]Venda não encontrada![/red]")
            input("ENTER para continuar...")
            return
        
        venda = resp.json()
        prod = requests.get(f"{BASE_URL}/produtos/{venda['produtoId']}").json()

        console.print(f"""
[deep_pink3]Venda Encontrada:[/deep_pink3]
ID: {venda['id']}
Produto: {prod['nome']}
Quantidade: {venda['quantidade']}
""")

    except Exception as e:
        console.print(f"[bold red]Erro: {e}[/bold red]")

    input("Pressione ENTER para continuar...")



def atualizar_venda():
    titulo("Atualizar Venda")

    venda_id = input("ID da Venda: ")

    try:
        resp = requests.get(f"{BASE_URL}/vendas/{venda_id}")

        if resp.status_code != 200:
            console.print("[red]Venda não encontrada![/red]")
            input("ENTER...")
            return

        venda = resp.json()

        nova_qtd = input(f"Quantidade nova ({venda['quantidade']}): ") or venda["quantidade"]
        
        novo_prod = input(f"Novo produtoId ({venda['produtoId']}): ") or venda["produtoId"]

        dados = {
            "quantidade": int(nova_qtd),
            "produtoId": int(novo_prod),
        }

        resp_up = requests.patch(f"{BASE_URL}/vendas/{venda_id}", json=dados)

        if resp_up.status_code == 200:
            console.print("[green]Venda atualizada com sucesso![/green]")
        else:
            console.print("[red]Erro ao atualizar venda![/red]")

    except Exception as e:
        console.print(f"[bold red]Erro: {e}[/bold red]")

    input("ENTER para continuar...")



def deletar_venda():
    titulo("Excluir Venda")

    venda_id = input("ID da Venda: ")

    try:
        resp = requests.get(f"{BASE_URL}/vendas/{venda_id}")

        if resp.status_code != 200:
            console.print("[red]Venda não encontrada![/red]")
            input("ENTER...")
            return

        venda = resp.json()
        console.print(f"[yellow]Confirmar a exclusão da venda ID {venda_id}?[/yellow]")
        confirmar = input("Digite S para confirmar: ").upper()

        if confirmar != "S":
            console.print("[cyan]Operação cancelada.[/cyan]")
            input("ENTER...")
            return

        resp_del = requests.delete(f"{BASE_URL}/vendas/{venda_id}")

        if resp_del.status_code == 200:
            console.print("[green]Venda excluída![/green]")
        else:
            console.print("[red]Erro ao excluir.[/red]")

    except Exception as e:
        console.print(f"[bold red]Erro: {e}[/bold red]")

    input("ENTER para continuar...")
