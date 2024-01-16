import json
import requests
from src.api_request_handler import ApiRequestHandler
from utils.config_info import ConfigInfo

class Board:
    __api_handler = None
    __app_context = "boards"
    __endpoint = ""


    def __init__(self):
        self.__api_handler = ApiRequestHandler()
        self.__build_endpoint()

    def create_board(self, name):
        self.__api_handler.set_query_params('name', name)
        response = requests.post(self.__endpoint, params=self.__api_handler.get_query_params())
        self.__board_id = response.json()['id']
        self.__name_board = response.json()['name']
        self.__id_organization = response.json()['idOrganization']
        return response
    def update_name_board(self, updated_name):
        self.__api_handler.set_query_params('name', updated_name)
        response = requests.put("{}{}".format(self.__endpoint,self.__board_id), params=self.__api_handler.get_query_params())
        return response
    def delete_board(self):
        self.__api_handler.delete_query_param('name')
        return requests.delete("{}{}".format(self.__endpoint,self.__board_id),params=self.__api_handler.get_query_params())

    def __build_endpoint(self):
        self.__endpoint = "{}/{}/".format(self.__api_handler.build_api_call(), self.__app_context)
