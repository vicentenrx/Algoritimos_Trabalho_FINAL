from rich.console import Console

console = Console()

def titulo(texto):
    console.clear()
    console.rule("[blue]LOJAS ESTRADA")
    console.rule(texto, style="blue")
    console.rule()

