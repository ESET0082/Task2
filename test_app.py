
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


# ✅ Each test function must start with 'test_'
def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_add_negative():
    assert add(-1, 1) == 0
# def test_example():
#     assert 2 == 2
