# Importando a classe DBconnectionHandler, que gerencia a conexão com o banco de dados MongoDB
from models.connection_options.connection import DBconnectionHandler
from models.repository.minhaCollection_repository import MinhaCollectionRepository

from datetime import datetime, timedelta

# Criando uma instância da classe DBconnectionHandler para gerenciar a conexão:
db_handle = DBconnectionHandler()

# Estabelecendo a conexão com o banco de dados MongoDB chamando o método connect_to_db:
db_handle.connect_to_db()
db_connection = db_handle.get_db_connecion()  # Obtendo a conexão  ao banco de dados
# print(db_connection)

minhaCollection_repository = MinhaCollectionRepository(db_connection)

# ==================== OPERAÇÕES DE INSERÇÃO ====================

# Realizando inserção de um documento:
documento = {
    "nome": "Namikaze Minato",
    "idade": 30,
    "data_de_criacao": datetime.utcnow() - timedelta(hours=3),
}
minhaCollection_repository.insert_document(documento)

# Realizando inserção de listas de documentos:
Order = {
    "name": "Sandro",
    "Endereço": "Konoha",
    "Pedidos": {"Sushi": 30, "Refrigerante": 2},
}

minhaCollection_repository.insert_document(Order)

list_of_documents = [
    {"Capitao": "Luffy"},
    {"Navegadora": "Nami"},
    {"Atirador": "Usopp"},
    {"Imediato": "Zoro"},
    {"Cozinheiro": "Sanji"},
    {"Historiadora": "Robin"},
    {"Medico": "Chopper"},
    {"Carpinteiro": "Franky"},
    {"Musico": "Brook"},
    {"Timoneiro": "Jimbei"},
]

minhaCollection_repository.insert_list_of_documents(list_of_documents)

# ==================== OPERAÇÕES DE CONSULTA ====================

# Buscando um único documento com o filtro name = "Sandro":
response2 = minhaCollection_repository.select_one({"name": "Sandro"})
print(response2)
print()

# Buscando múltiplos documentos com o filtro name = "Sandro":
response = minhaCollection_repository.select_many({"name": "Sandro"})
print(response)
print()

# Busca documentos onde uma propriedade específica existe na coleção:
minhaCollection_repository.select_if_property_exists()

# Busca múltiplos documentos com ordenação aplicada:
minhaCollection_repository.select_many_order()

# Busca documentos usando operador OR (retorna registros que atendem uma OU outra condição):
minhaCollection_repository.select_or()

# Busca documentos pelo seu ObjectId (identificador único do MongoDB):
minhaCollection_repository.select_by_object_id()

# ==================== OPERAÇÕES DE ATUALIZAÇÃO ====================

minhaCollection_repository.edit_registry("Sandro SB")

filtro = {"profissao": "Desenvolvedor"}
propriedades = {"profissao": "Software Developer", "apelido": "Dev"}

# Incrementando mais um dados( "idade") nas propriedades que tem {"profissao":"Software Developer"}:
filtro = {"profissao": "Software Developer"}
propriedades = {"idade": 37}

minhaCollection_repository.edit_many_registries(filtro, propriedades)

# Aumentando 3 anos na idade:
minhaCollection_repository.edit_many_increment(3)

# Decrementando 10 anos de idade:
minhaCollection_repository.edit_many_increment(-10)

# ==================== OPERAÇÕES DE EXCLUSÃO ====================

minhaCollection_repository.delet_one_registry()

minhaCollection_repository.delet_many_registries()

# ==================== OPERAÇÕES DE ÍNDICE ====================

minhaCollection_repository.create_index_ttl()
