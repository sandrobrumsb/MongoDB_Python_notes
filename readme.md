# MongoDB com Python

## Introdução

Python pode ser usado em aplicações de banco de dados.
Um dos bancos de dados NoSQL mais populares é o MongoDB.
O MongoDB armazena dados em documentos do tipo JSON, o que torna o banco de dados muito flexível e escalável.

## Pré-requisitos

Para usar o MongoDB com Python, você precisa instalar a biblioteca PyMongo:

```bash
python -m pip install pymongo
```

## MongoDB Compass

Manipule seu banco de dados facilmente com o Compass, a interface gráfica do usuário (GUI) para MongoDB.

## Conteúdo Estudado

### 1. Conexão com MongoDB

- Estabelecimento de conexão com servidor MongoDB local
- Uso da URL padrão `mongodb://localhost:27017/`

### 2. Gerenciamento de Banco de Dados

- Criação e acesso a bancos de dados
- Verificação de bancos existentes
- Listagem de bancos disponíveis

### 3. Gerenciamento de Coleções

- Criação e acesso a coleções (equivalentes a tabelas)
- Verificação de coleções existentes
- Listagem de coleções em um banco
- Exclusão de coleções (drop)

### 4. Operações CRUD

#### Create (Inserção)

- Inserção de documento único (insert_one)
- Inserção de múltiplos documentos (insert_many)
- Inserção com IDs personalizados

#### Read (Leitura)

- Busca de um único documento (find_one)
- Busca de múltiplos documentos (find)
- Filtragem de campos específicos
- Consultas com filtros
- Uso de expressões regulares em consultas
- Ordenação de resultados (sort)
- Limitação de resultados (limit)

#### Update (Atualização)

- Atualização de um documento (update_one)
- Atualização de múltiplos documentos (update_many)
- Uso de operadores de atualização ($set)

#### Delete (Exclusão)

- Exclusão de um documento (delete_one)
- Exclusão de múltiplos documentos (delete_many)
- Exclusão com base em critérios
- Exclusão de todos os documentos de uma coleção

### 5. Recursos Avançados

- Consultas avançadas com operadores ($gt, $regex)
- Projeções de campos (inclusão/exclusão de campos específicos)
- Ordenação de resultados (crescente/decrescente)
- Paginação de resultados com limit()

## Boas Práticas

1. Sempre verificar a existência de bancos/coleções antes de operá-los
2. Usar try-except para tratamento de erros de conexão
3. Fechar conexões após o uso
4. Utilizar nomes descritivos para bancos de dados e coleções
5. Validar dados antes da inserção
6. Usar índices para otimizar consultas frequentes
