import requests
from urllib.parse import quote

HEADERS = {"User-Agent": "api-wiki-call/0.1 (federico.delussu@gmail.com)"}

def get_wiki_full_page(title: str) -> str:
      params = {
          "action": "query",
          "prop": "extracts",
          "explaintext": 1,
          "titles": title,
          "format": "json",
          "formatversion": 2,
      }
      response = requests.get("https://en.wikipedia.org/w/api.php", 
                              params=params,
                              headers=HEADERS, timeout=10)
      response.raise_for_status()
      return response.json()#["query"]["pages"][0]["extract"]

def get_wiki_page(title: str) -> dict:
    '''
    get summary of a wiki page
    '''
    link = f"https://en.wikipedia.org/api/rest_v1/page/summary/{quote(title.replace(' ', '_'))}"
    response = requests.get(link, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return response.json()

def get_property(title: str, property: str) -> dict:
    '''
    get the property of a wiki page
    '''
    qid = get_wiki_page(title)["wikibase_item"]
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json"
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    response = response.json()["entities"][qid]["claims"]
    response = response[property][0]
    return response
