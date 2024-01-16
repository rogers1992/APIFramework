from utils.config_info import ConfigInfo
class ApiRequestHandler:
    __base_url = ""
    __query_params = {}
    __request_headers = {}
    __api_call = ""
    __version = ""

    def __init__(self):
        self.__base_url = ConfigInfo().get_base_url()
        self.__query_params['key'] = ConfigInfo().get_api_key()
        self.__query_params['token'] = ConfigInfo().get_api_token()
        self.__endpoint = ConfigInfo().get_base_url()
        self.__version = ConfigInfo().get_api_version()
    def set_base_url(self, base_url):
        self.__base_url = base_url
    def get_base_url(self):
        return self.__base_url
    def set_query_params(self, key, value):
        self.__query_params[key] = value
    def delete_query_param(self, key):
        self.__query_params.pop(key)
    def get_query_params(self):
        return self.__query_params
    def set_request_headers(self, key, value):
        self.__request_headers[key] = value
    def get_request_headers(self):
        return self.__request_headers
    def set_enpoint(self, endpoint):
        self.__endpoint  = endpoint
    def get_endpoint(self):
        return self.__endpoint

    def build_api_call(self):
        self.__api_call = "{}/{}".format(self.__base_url, self.__version)
        print("api call is", self.__api_call)
        return self.__api_call




    
