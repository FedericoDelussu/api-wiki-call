"""
Compare the age of different users and determine who is younger, who is older etc..
"""

from typing import Protocol


class Comparable(Protocol):
    '''
    what compare_users needs from a user (User satisfies it without importing it here)
    '''
    title: str
    is_alive: bool
    years_lived: int


def compare_users(user1: Comparable, user2: Comparable) -> str:
    """
    Compare the years lived by two users:
    - both alive: compare their current age
    - both dead: compare their lifespan
    - one alive, one dead: compare the current age of the living one
      with the lifespan of the dead one
    """
    years1, years2 = user1.years_lived, user2.years_lived
    diff = abs(years1 - years2)
    # the user who lived longer goes first in the message
    longer, shorter = (user1, user2) if years1 >= years2 else (user2, user1)

    if user1.is_alive and user2.is_alive:
        if diff == 0:
            return f"{user1.title} and {user2.title} are the same age"
        return f"{longer.title} is older {diff} years than {shorter.title}"

    if not user1.is_alive and not user2.is_alive:
        if diff == 0:
            return f"{user1.title} and {user2.title} lived the same number of years"
        return f"{longer.title} lived {diff} years longer than {shorter.title}"

    alive, dead = (user1, user2) if user1.is_alive else (user2, user1)
    if diff == 0:
        return f"{alive.title} has lived as many years as {dead.title} did"
    if longer is alive:
        return f"{alive.title} has already lived {diff} years longer than {dead.title} did"
    return f"{dead.title} lived {diff} years longer than {alive.title} has so far"
