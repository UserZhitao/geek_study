import pytest

@pytest.fixture
def first_entry():
    return "a"

@pytest.fixture
def order(first_entry):
    return []

# 自动生效： 有点类似于开关。
# 如果需要数据变化，则把开关打开。
# 如果不需要，则把开关关闭。
@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(order, first_entry):
    assert order == [first_entry]

def test_string_and_int(order, first_entry):
    order.append(2)
    assert order == [first_entry, 2]