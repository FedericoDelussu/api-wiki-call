from datetime import date
from .api import get_property


def _get_year(title: str, property_id: str) -> int:
    property = get_property(title, property_id)
    time = property["mainsnak"]["datavalue"]["value"]["time"]
    return int(time[:5])


def get_year_birth(title: str) -> int:
    return _get_year(title, "P569")


def get_year_death(title: str) -> int | None:
    '''
    return None if the person has no date of death (still alive)
    '''
    try:
        return _get_year(title, "P570")
    except KeyError:
        return None


def _years_between(start: int, end: int) -> int:
    '''
    Wikidata has no year 0 (1 BC is -1), so skip it when crossing BC -> AD
    '''
    years = end - start
    if start < 0 < end:
        years -= 1
    return years


class User:
    def __init__(self, title: str):
        self.title = title
        self.year_birth = get_year_birth(title)
        self.year_death = get_year_death(title)

    @property
    def is_alive(self) -> bool:
        return self.year_death is None

    @property
    def age(self) -> int | None:
        '''
        current age, None if the person is dead
        '''
        if not self.is_alive:
            return None
        return _years_between(self.year_birth, date.today().year)

    @property
    def lifespan(self) -> int | None:
        '''
        age at death, None if the person is alive
        '''
        if self.is_alive:
            return None
        return _years_between(self.year_birth, self.year_death)

    def __repr__(self) -> str:
        return f"User({self.title!r}, born={self.year_birth}, died={self.year_death})"
