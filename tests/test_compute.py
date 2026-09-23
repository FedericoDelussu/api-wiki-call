from api_wiki_call import compute
from api_wiki_call.compute import User, _years_between


def make_user(monkeypatch, birth, death):
    '''
    build a User without calling the API, using fake birth/death years
    '''
    monkeypatch.setattr(compute, "get_year_birth", lambda title: birth)
    monkeypatch.setattr(compute, "get_year_death", lambda title: death)
    return User("Someone")

def test_years_between():
    
    assert _years_between(1879, 1955) == 76


def test_years_between_bc_to_ad():
    # there is no year 0: from 10 BC to 10 AD is 19 years
    assert _years_between(-10, 10) == 19


def test_dead_user(monkeypatch):
    user = make_user(monkeypatch, birth=1879, death=1955)
    assert not user.is_alive
    assert user.lifespan == 76
    assert user.age is None


def test_alive_user(monkeypatch):
    user = make_user(monkeypatch, birth=2000, death=None)
    assert user.is_alive
    assert user.lifespan is None
    assert user.age > 0
