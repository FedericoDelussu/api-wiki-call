from api_wiki_call.compute import get_year_birth
import sys

user1 = sys.argv[1]
user2 = sys.argv[2]

def main() -> None:
    print(get_year_birth(user1))
    print(get_year_birth(user2))

if __name__ == "__main__":
    main()
