"""

"""
import pytest

from common.conftest import login_data
from testcase.default.conftest import login_user


class TestUserLogin():
    @pytest.mark.parametrize(" username, password, rememberMe",
                             login_data["test_login_user"])
    def test_login(self, username, password, rememberMe):
        res = login_user(username, password, rememberMe)
        print(type(res))







