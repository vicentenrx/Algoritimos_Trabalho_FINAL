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
        if not quantidade.isdigit():
            console.print("[red]Quantidade deve ser número![/red]")
            input("ENTER...")
            return

        quantidade = int(quantidade)

        resp_prod = requests.get(f"{BASE_URL}/produtos/{produto_id}")

        if resp_prod.status_code != 200:
            console.print("[red]Produto não encontrado![/red]")
            input("ENTER...")
            return
        
        produto = resp_prod.json()

        estoque_atual = int(produto.get("estoque", 0))

        if quantidade > estoque_atual:
            console.print(
                f"[red]Estoque insuficiente! Disponível: {estoque_atual}[/red]"
            )
            input("ENTER...")
            return

        novo_estoque = estoque_atual - quantidade

        produto_atualizado = {
            "nome": produto["nome"],
            "categoria": produto["categoria"],
            "preco": produto["preco"],
            "estoque": novo_estoque
        }


        resp_put = requests.put(
            f"{BASE_URL}/produtos/{produto_id}",
            json=produto_atualizado
        )

        if resp_put.status_code != 200:
            console.print("[red]Erro ao atualizar estoque![/red]")
            input("ENTER...")
            return


        nova_venda = {
            "produtoId": produto_id,   
            "quantidade": quantidade
        }

        resp_venda = requests.post(f"{BASE_URL}/vendas", json=nova_venda)

        if resp_venda.status_code == 201:
            console.print(f"[green]Venda registrada! Novo estoque: {novo_estoque}[/green]")
        else:
            console.print("[red]Erro ao registrar venda![/red]")

    except Exception as e:
        console.print(f"[bold red]Erro: {e}[/bold red]")

    input("ENTER para continuar...")



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
