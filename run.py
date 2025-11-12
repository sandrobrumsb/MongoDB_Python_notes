# Importando a classe DBconnectionHandler, que gerencia a conexão com o banco de dados MongoDB
from models.connection_options.connection import DBconnectionHandler

# Criando uma instância da classe DBconnectionHandler para gerenciar a conexão
db_handle = DBconnectionHandler()

# Obtendo a conexão do banco de dados (ainda não conectada, pois o método connect_to_db não foi chamado)
conn1 = db_handle.get_db_connecion()
print(conn1)  # neste momento, é uma conexão não estabelecida)

# Estabelecendo a conexão com o banco de dados MongoDB chamando o método connect_to_db
db_handle.connect_to_db()
conn2 = db_handle.get_db_connecion()  # Obtendo a conexão conectada ao banco de dados
print(conn2)

# pegando a coleção dentro do banco chamada minhaCollection:
collection = conn2.get_collection("minhaCollection")

# Fazendo uma inserção:
collection.insert_one({
    "estou": "inserindo",
    "numeros":[123,456,789,101112]
})
