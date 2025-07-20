# import requests

# def get_random_fact():
#     """Fetches a random fact from an API and returns it"""
#     try:
#         response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
#         response.raise_for_status()  
#         fact_data = response.json()
#         return fact_data['text']
#     except requests.exceptions.RequestException as e:
#         return f"Failed to fetch fact: {e}"

# def print_random_fact():
#     """Prints a random fact to the console"""
#     fact = get_random_fact()
#     print("\nRandom Fact:")
#     print("-" * 30)
#     print(fact)
#     print("-" * 30 + "\n")

# # Example usage
# if __name__ == "__main__":
#     print_random_fact()

import requests

def get_random_cat_fact():
    """
    Fetches a random cat fact from an external API.
    Returns:
        str: A random cat fact.
    Raises:
        Exception: If the API request fails or the response is invalid.
    """
    url = "https://catfact.ninja/fact"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        return data.get("fact", "No cat fact found.")
    except requests.RequestException as e:
        return f"Error fetching cat fact: {e}"

def print_cat_fact():
    """
    Prints a random cat fact to the console.
    """
    fact = get_random_cat_fact()
    print("\nRandom Fact:")
    print("-" * 100)
    print(f"\n🐱 Cat Fact: {fact}")
    print("-" * 100 + "\n")

# Example usage
# if __name__ == "__main__":
print_cat_fact()
