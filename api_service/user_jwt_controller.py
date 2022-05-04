"""


"""
import os

from common.base_api import ApiCases
from common.read_data import data


BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "conf", "config.ini")
api_root_url = data.load_ini(data_file_path)["login"]["path"]
print(api_root_url)


class UserController(ApiCases):
    def __init__(self, api_root_url, **kwargs):
        super(UserController, self).__init__(api_root_url, **kwargs)

    def login(self, **kwargs):
        return self.post("api/authenticate", **kwargs)


us = UserController(api_root_url)
