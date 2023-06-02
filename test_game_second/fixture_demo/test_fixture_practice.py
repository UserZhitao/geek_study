import pytest

my_dict = {
    'A': True,
    'B': False,
}

@pytest.fixture(params=list(my_dict.items()), ids=lambda item: f"{item[0]}={item[1]}")
def my_fixture(request):
    return request.param

def test_my_fixture(my_fixture):
    print(list(my_dict.items()))
    # key, value = my_fixture
    # print(f"测试 {key}: {value}")

pytest.main([__file__])


# # 测试账号数据
# import pytest
# test_user = ["admin1", "admin2"]
# test_psw = ["11111", "22222"]
#
#
# @pytest.fixture(scope="module")
# def input_user(request):
#     user = request.param
#     print("登录账户：%s" % user)
#     return user
#
#
# @pytest.fixture(scope="module")
# def input_psw(request):
#     psw = request.param
#     print("登录密码：%s" % psw)
#     return psw
#
#
# @pytest.mark.parametrize("input_user", test_user, indirect=True)
# @pytest.mark.parametrize("input_psw", test_psw, indirect=True)
# # 1) 当 indirect=False 时，argnames 参数被当成普通变量；
# # 2) 当 indirect=True 时，parametrize 中的 argnames 参数被当成函数执行，且 argvalues 值作为 argnames函数中的参数传参
# def test_login(input_user, input_psw):
#     """登录用例"""
#     a = input_user
#     b = input_psw
#     print("测试数据a-> %s， b-> %s" % (a, b))
#     assert b