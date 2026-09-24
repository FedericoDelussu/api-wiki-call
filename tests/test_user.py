from api_wiki_call import compute
from api_wiki_call.user import User

def make_user(monkeypatch, birth, death, title="Someone"):
    '''
    build a User without calling the API, using fake birth/death years
    '''
    monkeypatch.setattr(compute, "get_year_birth", lambda title: birth)
    monkeypatch.setattr(compute, "get_year_death", lambda title: death)
    return User(title)


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


def test_compare_method(monkeypatch):
    user1 = make_user(monkeypatch, birth=1990, death=None, title='user1')
    user2 = make_user(monkeypatch, birth=2000, death=None, title='user2')
    assert user1.compare(user2) == "user1 is older 10 years than user2"
