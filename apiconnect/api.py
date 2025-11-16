import requests

base_url = "https://pokeapi.co/api/v2/"


def get_pokemon(pokemon_name):
    url = f"{base_url}pokemon/{pokemon_name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data   # <-- IMPORTANT: return the data
    else:
        print(f"Pokemon not found! Status: {response.status_code}")
        return None


pokemon_name = input("Enter the name of the Pokemon: ").lower()

pokemon_info = get_pokemon(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")
    print("Abilities:")
    for ability in pokemon_info['abilities']:
        print(f"- {ability['ability']['name']}")
        
else:
    print("No information available.")
