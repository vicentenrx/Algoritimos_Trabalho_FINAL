from rich.console import Console
from funcoes.gerais import titulo

from Produtos.Cadastro import (
    criar_produto,
    listar_produtos,
    buscar_produto_por_id,
    atualizar_produto,
    deletar_produto
)

from Graficos.Graf_Produtos import (
    grafico_produtos_por_categoria
)

from Vendas.Venda import (
    criar_venda,
    listar_vendas,
    buscar_venda_por_id,
    atualizar_venda,
    deletar_venda
)

from Graficos.Graf_Vendas import (
    grafico_vendas_por_produto
)


from Pesquisa.Pesquisa_Produtos import (
    pesquisa_produtos_avancada
)
console = Console()
# --------------------------- MENU PRINCIPAL ---------------------------

def main():
    while True:
        titulo("Sistema de Controle — Loja Estrada")

        console.print("""
[cyan]1[/cyan] - Produtos
[cyan]2[/cyan] - Vendas
[cyan]3[/cyan] - Pesquisa Avançada
[cyan]4[/cyan] - Gráficos            
[red]0[/red] - Sair
""")

        op = input("Escolha uma opção: ")

        if op == "1":
            menu_produtos()
        elif op == "2":
            menu_vendas()
        elif op == "3":
            menu_pesquisa()
        elif op == "4":
            menu_graficos()
        elif op == "0":
            console.print("[green]Saindo do sistema...[/green]")
            break
        else:
            console.print("[red]Opção inválida![/red]")


# --------------------------- MENU PRODUTOS ---------------------------

def menu_produtos():
    while True:
        titulo("Menu de Produtos")

        console.print("""
[cyan]1[/cyan] - Cadastrar Produto
[cyan]2[/cyan] - Listar Produtos
[cyan]3[/cyan] - Buscar Produto por ID
[cyan]4[/cyan] - Atualizar Produto
[cyan]5[/cyan] - Deletar Produto
[red]0[/red] - Voltar
""")

        op = input("Escolha uma opção: ")

        if op == "1":
            criar_produto()
        elif op == "2":
            listar_produtos()
        elif op == "3":
            buscar_produto_por_id()
        elif op == "4":
            atualizar_produto()
        elif op == "5":
            deletar_produto()
        elif op == "0":
            break
        else:
            console.print("[red]Opção inválida![/red]")

# --------------------------- MENU VENDAS ---------------------------

def menu_vendas():
    while True:
        titulo("Menu de Vendas")

        console.print("""
[cyan]1[/cyan] - Registrar Venda
[cyan]2[/cyan] - Listar Vendas
[cyan]3[/cyan] - Buscar Venda por ID
[cyan]4[/cyan] - Atualizar Venda
[cyan]5[/cyan] - Deletar Venda
[red]0[/red] - Voltar
""")

        op = input("Escolha uma opção: ")

        if op == "1":
            criar_venda()
        elif op == "2":
            listar_vendas()
        elif op == "3":
            buscar_venda_por_id()
        elif op == "4":
            atualizar_venda()
        elif op == "5":
            deletar_venda()
        elif op == "0":
            break
        else:
            console.print("[red]Opção inválida![/red]")

# --------------------------- MENU GRAFICOS ---------------------------

def menu_graficos():
    while True:
        titulo("Menu de Gráficos")

        console.print("""
[cyan]1[/cyan] - Produtos por Categoria
[cyan]2[/cyan] - Vendas por Produto
[red]0[/red] - Voltar
""")

        op = input("Escolha uma opção: ")

        if op == "1":
            grafico_produtos_por_categoria()
        elif op == "2":
            grafico_vendas_por_produto()
        elif op == "0":
            break
        else:
            console.print("[red]Opção inválida![/red]")

# --------------------------- MENU PESQUISA ---------------------------

def menu_pesquisa():
    while True:
        titulo("Menu de Pesquisa")

        console.print("""
[cyan]1[/cyan] - Pesquisa Avançada (Nome + Categoria)
[red]0[/red] - Voltar
""")

        op = input("Escolha uma opção: ")

        if op == "1":
            pesquisa_produtos_avancada()
        elif op == "0":
            break
        else:
            console.print("[red]Opção inválida![/red]")

if __name__ == "__main__":
    main()