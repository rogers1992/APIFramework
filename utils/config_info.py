import json
import os


class ConfigInfo(object):
    absolute_path = os.path.dirname(__file__)
    path = os.getcwd()
    print("Current Directory", path)

    # prints parent directory
    print(os.path.abspath(os.path.join(path, os.pardir)))
    print(absolute_path)
    print(os.listdir('.'))
    with open('../config.json', 'r') as file:
        config = json.load(file)
    _instance = None
    __base_url = config['General']['API_URL']
    __api_version = config['General']['API_VERSION']
    __API_KEY = config['Credentials']['API_KEY']
    __API_TOKEN = config['Credentials']['API_TOKEN']
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            print("creating new instance")
            cls._instance = cls.__new__(cls)
            return cls._instance

    def get_base_url(self):
        return self.__base_url

    def get_api_key(self):
        return self.__API_KEY

    def get_api_token(self):
        return self.__API_TOKEN

    def get_api_version(self):
        return self.__api_version
