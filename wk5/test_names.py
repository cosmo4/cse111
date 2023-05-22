# Author: Luke Warner

from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    # Test the make_full_name()
    full_name = make_full_name("Sally", "Brown")
    assert full_name == "Brown; Sally"

    full_name = make_full_name("Luke", "Warner")
    assert full_name == "Warner; Luke"

    full_name = make_full_name("Maria", "Gimenez-Vidal")
    assert full_name == "Gimenez-Vidal; Maria"

def test_extract_family_name():
    #Test the extract_family_name()
    family_name = extract_family_name("Brown; Sally")
    assert family_name == "Brown"
    assert extract_family_name("Warner; Luke") == "Warner"
    assert extract_family_name("Gimenez-Vidal; Maria") == "Gimenez-Vidal"

def test_extract_given_name():
    # Test the extract_given_name
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name('Warner; Luke') == 'Luke'
    assert extract_given_name('Gimenez-Vidal; Maria') == 'Maria'

# Use pytest to test our code
pytest.main(["-v", "--tb=line", "-rN", __file__])