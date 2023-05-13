# Python program that uses the GITHUB search API to list the top projects by language, based on stars.

import requests

GITHUB_API_URL = "https://api.github.com/search/repositories"

def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "

    for langauge in languages:
        query += f"language:{langauge} "

    # a sample query looks like: "stars:>50 langauge:python language:javascript"
    return query
    

def repos_with_most_star(languages, sort="stars", order="desc"):
    query = create_query(languages)
    params = {"q": query, "sort": sort, "order": order}

    response = requests.get(GITHUB_API_URL, params=params)
    status_code = response.status_code

    if status_code != 200:
        raise RuntimeError(f"An error occured. HTTP Code: {status_code}")
    else: 
        response_json = response.json()
        return response_json["items"]

# Define some code that only runs when the script is run directly
if __name__ == "__main__":
    languages = ["python", "javascript", "ruby"]
    results = repos_with_most_star(languages)

    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"-> {name} is a {language} repo with {stars} stars.")