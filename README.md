# 📦 Sistema de Controle — Loja Estrada

Aplicação desenvolvida para o Trabalho #3 – Uso de Estruturas de Dados para Manipulação de APIs da disciplina Algoritmos e Estruturas de Dados I (Prof. Edécio).

O projeto implementa:

✔️ CRUD de Produtos

✔️ CRUD de Vendas

✔️ Pesquisa avançada (Nome + Categoria)

✔️ Gráficos com Matplotlib

✔️ API REST usando JSON Server

✔️ Interface estilizada com Rich

🚀 Tecnologias Utilizadas

Python 3.10+

JSON Server

Requests

Rich

Matplotlib

Collections (Counter)
```ts
📁 Estrutura do Projeto
Trabalho_API/
│
├── funcoes_gerais/
│   └── gerais.py
│
├── Produtos/
│   └── Cadastro.py
│
├── Vendas_API/
│   └── Cadastro.py
│
├── Pesquisa/
│   └── pesquisa_produtos.py
│
├── Graficos/
│   └── graficos.py
│
├── db.json
└── controle.py
```
# 🌐 API – JSON Server

A API possui duas tabelas relacionadas.
```ts
📌 Produtos (tabela principal)
{
  "id": 1,
  "nome": "Notebook Lenovo",
  "categoria": "Informática",
  "preco": 3500.00,
  "estoque": 12
}

📌 Vendas (tabela relacionada)
{
  "id": 1,
  "produtoId": 1,
  "quantidade": 2,
  "data": "2025-11-01"
}
```
# ⚙️ Rodando a API
Instalar o JSON Server:
npm install -g json-server

Executar:
json-server --watch db.json --port 3000 ou **npx json-server db.json**

# 🔗 Endpoints da API
Produtos
GET    /produtos
GET    /produtos/:id
POST   /produtos
PATCH  /produtos/:id
DELETE /produtos/:id

Vendas
GET    /vendas
GET    /vendas/:id
POST   /vendas
PATCH  /vendas/:id
DELETE /vendas/:id

🖥️ Rodando o Sistema Python
Instalar dependências:
pip install requests rich matplotlib

Executar o sistema:
python controle.py

# 🛠️ Funcionalidades do Sistema
# 🔷 CRUD – Produtos

Cadastrar

Listar

Buscar por ID

Atualizar

Deletar

# 🔷 CRUD – Vendas

Registrar venda

Listar vendas

Buscar por ID

Atualizar

Excluir

# 🔷 Pesquisa Avançada – Nome + Categoria

Permite filtrar produtos combinando:

nome

categoria

ou ambos

Exemplo:

Nome: mouse
Categoria: periféricos

# 🔷 Gráficos
# 📊 Produtos por Categoria

Barra mostrando quantos produtos existem em cada categoria.

# 📈 Vendas por Produto

Total de vendas de cada produto.

# 📚 Principais Conceitos Aplicados
Estruturas de Dados

listas

dicionários

contagem com Counter

tratamento de exceções (try/except)

APIs REST

requisições GET, POST, PATCH e DELETE

integração entre tabelas com produtoId

Organização do Código

módulos separados

funções reutilizáveis

interface amigável com Rich

# 🧪 Exemplos de Funcionalidades
✔️ Listagem de Produtos
ID | Nome             | Categoria    | Preço     | Estoque
1  | Notebook Lenovo  | Informática  | 3500.00   | 12

✔️ Pesquisa Avançada
Filtros aplicados:
Nome: mouse
Categoria: periféricos

✔️ Gráfico – Produtos por Categoria

(gerado com matplotlib)

✔️ Gráfico – Vendas por Produto

(gerado com matplotlib)

# 👨‍💻 Autor

Vicente Rochefort
Análise e Desenvolvimento de Sistemas
Ano: 2025