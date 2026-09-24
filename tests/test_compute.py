from api_wiki_call.compute import _years_between

def test_years_between():
    assert _years_between(1879, 1955) == 76

def test_years_between_bc_to_ad():
    # there is no year 0: from 10 BC to 10 AD is 19 years
    assert _years_between(-10, 10) == 19
