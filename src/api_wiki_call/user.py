from datetime import date
from api_wiki_call import compute
from api_wiki_call.compare import compare_users


class User:
    def __init__(self, title: str):
        self.title = title
        self.year_birth = compute.get_year_birth(title)
        self.year_death = compute.get_year_death(title)

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
        return compute._years_between(self.year_birth, date.today().year)

    @property
    def lifespan(self) -> int | None:
        '''
        age at death, None if the person is alive
        '''
        if self.is_alive:
            return None
        return compute._years_between(self.year_birth, self.year_death)

    @property
    def years_lived(self) -> int:
        '''
        current age if alive, age at death otherwise
        '''
        return self.age if self.is_alive else self.lifespan

    def compare(self, other: "User") -> str:
        return compare_users(self, other)

    def __repr__(self) -> str:
        return f"User({self.title!r}, born={self.year_birth}, died={self.year_death})"
