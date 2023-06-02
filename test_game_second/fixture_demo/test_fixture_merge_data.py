"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

# import pytest
#
# @pytest.fixture
# def first_entry():
#     return "a"
#
# @pytest.fixture
# def order(first_entry):
#     return []
#
# # 自动生效： 有点类似于开关。
# # 如果需要数据变化，则把开关打开。
# # 如果不需要，则把开关关闭。
# @pytest.fixture(autouse=True)
# def append_first(order, first_entry):
#     return order.append(first_entry)
#
#
# def test_string_only(order, first_entry):
#     assert order == [first_entry]
#
# def test_string_and_int(order, first_entry):
#     order.append(2)
#     assert order == [first_entry, 2]


import pytest


# 原始夹具
@pytest.fixture
def data():
    return [1, 2, 3]

@pytest.fixture
def data2():
    return ["a","b","c"]

@pytest.fixture(autouse=True)
def merge_data(data,data2):
    # data = data + data2
    data.append(data2)
    print('测试夹具：')
    # print(data)

@pytest.fixture
def data3():
    return [3,2,1]

# 有些时候需要对数据进行二次定制，
# 有些时候则是要使用原始的数据信息。
# @pytest.fixture
# def data_plus(data):
#     new_data = []
#     for i in data:
#         i = i + 1
#         new_data.append(i)
#     return new_data
# 数据的形参叫什么，夹具的函数名就必须一致。
def test_data(data, data2):
    print(data)
    print(data2)

def test_only_data(data):
    print(data)

def test_only_data2(data2):
    print(data2)

def test_data3(data3):
    print(data3)


def test_no_data():
    print(123)



'''
在你的代码中，`order` Fixture 的返回值是一个可变对象，即一个列表。当你在 `append_first` Fixture 中使用 `order.append(first_entry)` 时，实际上是对同一个列表对象进行了修改操作。因此，你可以在 `append_first` Fixture 中使用 `return` 返回该列表，而在其他地方仍然能够访问到修改后的列表。

`data` Fixture 的返回值是一个可变对象，即一个列表。当你在 `merge_data` Fixture 中使用 `data = data2 + data` 时，实际上是创建了一个新的列表对象，并将 `data` 变量指向了这个新的列表对象。然而，由于 `data` 变量是在 `merge_data` Fixture 中定义的局部变量，它的作用范围仅限于该 Fixture 内部，所以无法通过 `return` 返回修改后的列表对象。

返回 merged_data 是不会影响到 data 夹具的值的。原因是 pytest 在运行夹具函数时会将返回值视为夹具的实际值，并不会对夹具本身产生影响。

要在 merge_data 夹具中修改 data 的值，你可以通过修改夹具函数的参数方式来实现
'''