import pytest


@pytest.fixture(scope='session')
def fixture_get_some_fruit_1():
    print('test start session')
    yield 'kiwi'
    print('test end session')


@pytest.fixture(scope='function')
def fixture_get_some_fruit_2():
    print('test start function')
    yield 'melon'
    print('test end function')


@pytest.fixture(scope='module')
def fixture_module():
    print('test start module')
    yield 'melon'
    print('test end module')


@pytest.fixture(scope='class')
def fixture_get_num():
    print('test start function')
    yield 100
    print('test end function')


@pytest.fixture(scope='function')
def fixture_get_list():
    print('test start function')
    yield [1, 2, 3, 4, 5]
    print('test end function')


@pytest.fixture(scope='function')
def fixture_get_dict():
    print('test start function')
    yield {'car': 'mersedes', 'color': 'black', 'price': 1000000 }
    print('test end function')


@pytest.fixture(scope='function')
def fixture_get_tuple():
    print('test start function')
    yield (1, 2, 3, 4, 5, 6, 7, 8, 10)
    print('test end function')

@pytest.fixture(scope='function')
def fixture_get_set():
    print('test start function')
    yield {1, 2, 3, 4, 5, 6, 7, 8, 10}
    print('test end function')
