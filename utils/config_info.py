import json
class ConfigInfo(object):
    with open('../config.json', 'r') as file:
        config = json.load(file)
    _instance = None
    __base_url = config['General']['API_URL']
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

