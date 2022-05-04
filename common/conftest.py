"""

"""
import os
import pytest

# from common.log import logger
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


login_data = get_data("user_controller.yaml")

# @allure.step("前置步骤 ==>> 清理数据")
# def step_first():
#     logger.info("***********************")
#     logger.info("前者步骤开始 ==>> 清理数据")
#
#
# @allure.step("后置步骤 ==>> 清理数据")
# def step_last():
#     logger.info("***********************")
#     logger.info("后置步骤开始 ==>> 清理数据")
#
#
