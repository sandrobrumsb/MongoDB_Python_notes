# possibilita as conexoes com o banco de dados do MongoDB:
from pymongo import MongoClient

# Criando a String de conexao com o banco, nesse caso nao tem usuario e senha:
# Com credenciais de conexao: connection_string = "mongodb://admin:password@localhost:27017/authSource=admin"
connection_string = "mongodb://localhost:27017"
# conectando o banco apartir da string de conexao:
client = MongoClient(connection_string)
# apontando o "client" para o banco criando no mongoDB Compass:
db_connection = client["meuBanco"]

# Monstrando o resultado da conexao com o mongoDB:
print(db_connection)
print("----------------------------")

# usando o db_connection para referenciar a coleção:
# está pegando uma coleção chamada "minhaCollection" dentro de um banco de dados do MongoDB.
collection = db_connection.get_collection("minhaCollection")

# Monstrando os dados de conexao da coleção
print(collection)
print("----------------------------")


# Fazendo um filtro: busca todo campo "ola" que tiver "mundo":
search_filter = {"estou": "aqui"}

# Buscando as informaçoes (dados) do BD:
response = collection.find(search_filter)
# retorna uma responsta no formato cursor:
print(response)

# Lendo a resposta e fazndro o print do registro(dados):
for registry in response:
    print(registry)


# Fazendo uma inserção:
collection.insert_one({
    "estou": "inserindo",
    "numeros":[123,456,789]
})

