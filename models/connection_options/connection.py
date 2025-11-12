# Estabelece a conexão com o banco de dados MongoDB:
from pymongo import MongoClient

# Importando as informações de conexão que estão em mongo_db_infos
from .mongo_db_configs import mongo_db_infos


# Classe para gerenciar a string de conexão com o banco de dados:
# exemplo sem credenciais "mongodb://localhost:27017"
class DBconnectionHandler:
    # Montando a string de conexão:
    def __init__(self):
        self.__conection_string = "mongodb://{}:{}/".format(
            mongo_db_infos["HOST"],
            mongo_db_infos["PORT"],
        )
        # Salvando a instância do cliente MongoDB:
        self.__database_name = mongo_db_infos["DB_NAME"]
        self.__client = None
        self.__db_connection = None

    # Conectando ao banco de dados MongoDB:
    def connect_to_db(self):
        self.__client = MongoClient(self.__conection_string)
        self.__db_connection = self.__client[self.__database_name]

    # Obtendo a conexão com o banco de dados:
    def get_db_connecion(self):
        return self.__db_connection

    # Obtendo o cliente MongoDB:
    def get_db_client(self):
        return self.__client
