from .api import get_property

def get_year_birth(title: str) -> int:
    property =  get_property(title, "P569")
    time = property["mainsnak"]["datavalue"]["value"]["time"]
    return int(time[:5])

def get_year_death(title:str) -> int: 
    property =  get_property(title, "P570")
    time = property["mainsnak"]["datavalue"]["value"]["time"]
    return int(time[:5])

