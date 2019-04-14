import copy


class TestBasicTypeOne:

    def test_0_type_string(self,fixture_get_some_fruit_1, fixture_module):
        """Test for string concatenate"""
        salad = 'orange'
        assert fixture_get_some_fruit_1 + ' ' + salad == 'kiwi orange'

    def test_1_type_string(self, fixture_get_some_fruit_2):
        """Test double word length"""
        fruit = fixture_get_some_fruit_2 * 2
        assert len(fruit) == 10

    def test_3_type_number(self, fixture_get_num):
        """Test division by zero"""
        num = fixture_get_num
        try:
            result = num / 0
            assert False
        except ZeroDivisionError:
            assert True

    def test_4_type_number(self, fixture_get_num):
        """Test check for even numbers"""
        assert fixture_get_num % 2 == 0

    def test_5_type_list(self, fixture_get_list):
        """Test number in the list"""
        assert (5 in fixture_get_list) is True

    def test_6_type_list(self, fixture_get_list):
        """Test append value in list"""
        data = fixture_get_list
        data.append(7)
        assert (7 in data) is True

    def test_7_type_dict(self, fixture_get_dict):
        """Test get value from dict"""
        data = fixture_get_dict
        assert data.get('color') == 'black'

    def test_8_type_dict(self,fixture_get_dict):
        """Test check key after delete key,value from dict"""
        data = copy.deepcopy(fixture_get_dict)
        data.pop('color')
        assert list(data.keys()) == ['car', 'price']
