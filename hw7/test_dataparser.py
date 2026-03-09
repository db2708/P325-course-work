from dataparser import read_data

# program uses pytest to run tests on the read_data function in dataparser.py.

def test_values():
    result = read_data('good_data.txt')
    assert result == (40.25, 3.6996621467371855)

def test_badvalues():
    result = read_data('bad_data.txt')
    assert result == (40.25, 3.6996621467371855)

def test_novalues():
    result = read_data('no_data.txt')
    assert result == (None, None)