class TestBasicTypeTwo:

    def test_9_type_tuple(self, fixture_get_tuple, fixture_module):
        """Test check type tuple"""
        data = fixture_get_tuple
        assert type(data) is tuple

    def test_10_type_tuple(self, fixture_get_tuple):
        """Test cannot delete items from tuple"""
        data = fixture_get_tuple
        try:
            del data[0]
            assert False
        except TypeError:
            assert True

    def test_11_type_tuple(self, fixture_get_set):
        """Test check type tuple"""
        data = fixture_get_set
        assert type(data) is set

    def test_12_typ_tuple(self,fixture_get_set):
        """Test intersection of two sets"""
        data = fixture_get_set
        set_2 = {1, 2, 3}
        assert (data & set_2) == {1, 2, 3}
