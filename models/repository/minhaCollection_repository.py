from typing import Dict, List
from bson.objectid import ObjectId
from datetime import timedelta


class MinhaCollectionRepository:
    # Construtor recebe uma conexão com o banco de dados
    def __init__(self, db_connection) -> None:
        self.__collection_name = "minhaCollection"  # Nome da coleção no banco
        self.__db_connection = db_connection  # Armazena a conexão recebida

    # ==================== OPERAÇÕES DE INSERÇÃO ====================

    # Insere um único documento na coleção:
    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)  # Obtém a coleção
        collection.insert_one(document)  # Insere o documento
        return document  # Retorna o documento inserido

    # Insere uma lista de documentos na coleção
    def insert_list_of_documents(self, list_of_document: List[Dict]) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)  # Obtém a coleção
        collection.insert_many(list_of_document)  # Insere vários documentos de uma vez
        return list_of_document  # Retorna a lista inserida

    # ==================== OPERAÇÕES DE CONSULTA ====================

    # Fazendo uma busca de um único documento no MongoDB com base no filtro informado:
    def select_one(self, filter) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)  # Obtém a coleção
        response = collection.find_one(filter, {"_id": 0})
        return response

    # Fazendo uma consulta e retorna vários documentos que correspondem ao filtro informado:
    def select_many(self, filter) -> List[Dict]:
        collection = self.__db_connection.get_collection( self.__collection_name)  # Obtém a coleção
        data = collection.find(filter, {"Endereço": 0, "_id": 0} )  # Filtro da busca  # Opçoes de Retorno

        response = []  # Cria uma lista vazia para armazenar os elementos
        for elementos in data:  # Percorre cada elemento presente em 'data'
            response.append(elementos)  # Adiciona o elemento atual à lista 'response'
        return response  # Retorna a lista preenchida

    # Buscando e exibindo todos os documentos da coleção que possuem a propriedade cpf:
    def select_if_property_exists(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)  # Obtém a coleção
        data = collection.find({"cpf": {"$exists": True}})  # Busca documentos onde a propriedade 'cpf' existe.
        for elemento in data:
            print(elemento)

    # Ordenando elementos na ordem:
    def select_many_order(self):
        collection = self.__db_connection.get_collection(self.__collection_name)  # Obtém a coleção
        data = collection.find(
            {"name": "Sandro"}, #Filtro da busca
            {"Endereço":0, "_id":0} # Opçoes de Retorno
            ).sort([("Pedidos.Sushi",-1)]) # ordena os documentos e o valor -1 significa ordem decrescente

        for elementos in data: print(elementos)

    # Consulta  usando o operador lógico $or:
    def select_or(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)  # Obtém a coleção
       # Retorna todos os documentos que atendem a pelo menos UMA das condições abaixo:
        data = collection.find({"$or":[{"name": "Sandro"},{"Ola":{'$exists':True}}]}) 
        for elemento in data:
            print(elemento)
            print()

    # Realizando busca pelo ObjectId:
    def select_by_object_id(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)  # Obtém a coleção
        data = collection.find({"_id": ObjectId("691298861e5fd509a86f0fd0")}) 
        for elemento in data: print(elemento)

    # ==================== OPERAÇÕES DE ATUALIZAÇÃO ====================

    # Atualizando um único documento no BD:
    def edit_registry(self, new_name) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)  # Obtém a coleção
        data = collection.update_one(
            {"_id":ObjectId("691e1313987bb80f35408a7b")}, # Filtro -filtrando pelo ObjectId.
            {"$set": {"name":new_name}}) # Campo de Edição - atualização a ser aplicada
        print(data.modified_count)

    # Atualizando varios elementos no BD:
    def edit_many_registries(self,filtro,propriedades) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)  # Obtém a coleção
        data = collection.update_many(
            filtro,
            {"$set":propriedades}) 
            #{"profissao": "Programador"}, # Filtrando pela chave ("profissao") e valor("Programador").
            #{"$set": {"profissao":"Desenvolvedor"}}) # atualização a ser aplicada em todos quer for profissao : Programador
        print(data.modified_count)

    # Editando elementos incrementados em  def edit_many_registries():
    def edit_many_increment(self,num) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)  # Obtém a coleção
        data = collection.update_many(
            {"_id":ObjectId("691e1313987bb80f35408a7b")}, # Filtro -filtrando pelo ObjectId.
            {"$inc": {"idade":num}}) # Campo de Edição - atualização a ser aplicada
        print(data.modified_count)

    # ==================== OPERAÇÕES DE EXCLUSÃO ====================

    # Deletando um registro no BD:
    def delet_one_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)  # Obtém a coleção
        data = collection.delete_one({"_id":ObjectId("691bc08d8e689385efacfa3b")})# Filtro -filtrando e deletando pelo _id.
        print(data.deleted_count)

    # Deletando varios registros no BD:
    def delet_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)  # Obtém a coleção
        data = collection.delete_many({"profissao": "Programador"})# Filtro -filtrando e deletando pela profissao : Programador.
        print(data.deleted_count)

    # ==================== OPERAÇÕES DE ÍNDICE ====================

    # Criando um Indices TTL - usado para remover documentos no mongo apos um certo periodo de tempo:
    def create_index_ttl(self):
        collection = self.__db_connection.get_collection(self.__collection_name)  # Obtém a coleção
        tempo_de_vida = timedelta(seconds=10)  # Criando uma propriedade temporal, representando um intervalo de 10 segundos atribuindo a variavel "tempo_de_vida".
        collection.create_index("data_de_criacao", expireAfterSeconds=tempo_de_vida.seconds)  # propriedade do meu index será:"data_de_criacao"
        print("TTL Criada!!!")
