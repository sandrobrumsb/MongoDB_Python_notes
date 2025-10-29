"""
===========================================================
   EXEMPLO DE USO BÁSICO DO MONGODB COM PYTHON (PyMongo)
===========================================================

Etapas:
1. Criar uma conexão com o MongoDB.
2. Criar um banco de dados.
3. Criar uma coleção (equivalente a uma tabela em SQL).
4. Inserir um documento (registro) na coleção.
5. Verificar bancos de dados e coleções existentes.
"""

import pymongo


# 1. Conectando ao servidor MongoDB
# A URL padrão "mongodb://localhost:27017/" conecta ao MongoDB local.
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# 2. Criando (ou acessando) um banco de dados
# O banco de dados só é criado após inserirmos dados nele.
mydb = myclient["mydatabase"]

# 3. Criando (ou acessando) uma coleção.
# No MongoDB, a coleção é equivalente a uma tabela.
# Assim como o banco, ela só é criada quando recebe conteúdo.
mycol = mydb["customers"]

# 4. Inserindo um documento na coleção.
# Criamos um dicionário representando um documento JSON.
mydict = {"name": "Sandro", "address": "Brasil"}

# Inserindo o documento na coleção "customers".
x = mycol.insert_one(mydict)

# Inserindo outro registro na coleção "customers" e retorne o valor do "_id" campo:
# OBS: Se você não especificar um _idcampo, o MongoDB adicionará um para você.
mydict = {"name": "Naruto", "address": "Konoha"}
x = mycol.insert_one(mydict)
print(x.inserted_id)

# Exibindo o ID do documento inserido.
print("Documento inserido com ID:", x.inserted_id)


# Inserindo vários documentos, usamos o metodo insert_many():
mylist = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blvd 2"},
    {"name": "Betty", "address": "Green Grass 1"},
    {"name": "Richard", "address": "Sky st 331"},
    {"name": "Susan", "address": "One way 98"},
    {"name": "Vicky", "address": "Yellow Garden 2"},
    {"name": "Ben", "address": "Park Lane 38"},
    {"name": "William", "address": "Central st 954"},
    {"name": "Chuck", "address": "Main Road 989"},
    {"name": "Viola", "address": "Sideway 1633"},
]

x = mycol.insert_many(mylist)
print(x.inserted_ids)  # imprimindo lista dos valores inseridos
"""
# Inserindo vários documentos,com IDs especificados:
mylist = [
    {"_id": 1, "name": "John", "address": "Highway 37"},
    {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
    {"_id": 3, "name": "Amy", "address": "Apple st 652"},
    {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
    {"_id": 5, "name": "Michael", "address": "Valley 345"},
    {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
    {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
    {"_id": 8, "name": "Richard", "address": "Sky st 331"},
    {"_id": 9, "name": "Susan", "address": "One way 98"},
    {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
    {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
    {"_id": 12, "name": "William", "address": "Central st 954"},
    {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
    {"_id": 14, "name": "Viola", "address": "Sideway 1633"},
]

x = mycol.insert_many(mylist)
print(x.inserted_ids)  # imprimindo lista dos valores inseridos
"""


# 5. Verificando bancos de dados existentes
print("\nBancos de dados existentes:")
print(myclient.list_database_names())

# Verificando se o banco de dados "mydatabase" existe.
if "mydatabase" in myclient.list_database_names():
    print(" O banco de dados 'mydatabase' existe.")


# 6. Verificando coleções dentro do banco de dados
print("\nColeções no banco 'mydatabase':")
print(mydb.list_collection_names())

# Verificando se a coleção "customers" existe.
if "customers" in mydb.list_collection_names():
    print(" A coleção 'customers' existe.")

# 7. Encontrando o primeiro dados em uma coleção, com o método find_one():
x = mycol.find_one()
print(x)

# Encontrando todos os dados em uma coleção, com o método find():
for x in mycol.find():
    print(x)

# Retornando apenas os "nomes" e "endereços",sem os "_ids":
for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(x)

# Retornando sem "endereço" no resultado":
for x in mycol.find({}, {"address": 0}):
    print(x)

# 8. Filtrar o resultado usando um método  de consulta find():

# Cria uma consulta (filtro) para buscar documentos na coleção.
# Aqui, queremos todos os documentos onde o campo "address" é igual a "Park Lane 38"
myquery = {"address": "Park Lane 38"}
# O método find() retorna uma lista iterável com todos os documentos que atendem ao filtro.
mydoc = mycol.find(myquery)
# Percorre cada documento retornado pela consulta e o imprime.
for x in mydoc:
    print(x)

# Consulta Avançada, você pode usar modificadores como valores no objeto de consulta.
# Encontrando documentos cujo endereço começa com a letra "S" ou superior:

myquery = {"address": {"$gt": "S"}}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

# Filtrar com expressões regulares, encontrando documentos cujo endereço começa com a letra "S":
myquery = {"address": {"$regex": "^S"}}
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

# 9. Classificar o resultado, Use o sort() para classificar o resultado em ordem crescente ou decrescente:
# Classificando o resultado em ordem alfabética por nome:
mydoc = mycol.find().sort("name")
for x in mydoc:
    print(x)

# Ordenar em ordem decrescente:
# sort("nome", 1) #crescente
# sort("nome", -1) #decrescente
mydoc = mycol.find().sort("name", -1)
for x in mydoc:
    print(x)

# 10. Excluir documento, para excluir um dado, usamos o delete_one():
myquery = {"address": "Mountain 21"}
mycol.delete_one(myquery)
for x in mycol.find():
    print(x)

# Para excluir mais de um dado, use o delete_many():
# Excluindo todos os documentos com endereço que começa com a letra S:
myquery = {"address": {"$regex": "^S"}}
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")

# Excluindo todos os dados da coleção "clientes":
x = mycol.delete_many({})
print(x.deleted_count, "documents deleted")

# 11. Você pode excluir uma tabela, ou coleção, como é chamada no MongoDB, usando o drop():
"""
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
"""
mycol.drop()

# OBS: O drop()retorna "true" se a coleção foi descartada com sucesso, e "false" se a coleção não existe.

# 12. Atualizando um registro ou documento, usando o update_one():
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

"""
myquery = {"address": "Valley 345"}
newvalues = {"$set": {"address": "Canyon 123"}}

mycol.update_one(myquery, newvalues)

# imprimindo "customers" depois do update:
for x in mycol.find():
    print(x)

# Atualizando todos os documentos cujo endereço comece com a letra "S", utilize o update_many():
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

"""
myquery = {"address": {"$regex": "^S"}}
newvalues = {"$set": {"name": "Minnie"}}

x = mycol.update_many(myquery, newvalues)
print(x.modified_count, "documents updated.")


# 13. Limitando o resultado para retornar apenas 5 documentos, usamos o limit() :
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

"""
myresult = mycol.find().limit(5)

# imprimindo o resultado:
for x in myresult:
    print(x)
