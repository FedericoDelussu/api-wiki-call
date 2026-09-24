from api_wiki_call import compute
from api_wiki_call.user import User
from api_wiki_call.compare import compare_users


def make_user(monkeypatch, title, birth, death):
    '''
    build a User without calling the API, using fake birth/death years
    '''
    monkeypatch.setattr(compute, "get_year_birth", lambda title: birth)
    monkeypatch.setattr(compute, "get_year_death", lambda title: death)
    return User(title)

def test_compare_living_users(monkeypatch):

    user1 = make_user(monkeypatch, title='user1', birth=2000, death=None)
    user2 = make_user(monkeypatch, title='user2', birth=2000, death=None)
    assert compare_users(user1, user2) == "user1 and user2 are the same age"

    user1 = make_user(monkeypatch, title='user1', birth=1990, death=None)
    user2 = make_user(monkeypatch, title='user2', birth=2000, death=None)
    assert compare_users(user1, user2) == "user1 is older 10 years than user2"

