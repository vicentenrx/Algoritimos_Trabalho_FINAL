from rich.console import Console

console = Console()

def titulo(texto):
    console.clear()
    console.rule("[dark_magenta]LOJAS ESTRADA")
    console.rule(texto, style="deep_pink3")
    console.rule()