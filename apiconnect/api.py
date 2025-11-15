import requists

base_url ="https://pokeapi.co/api/v2/"

def get_pokemon(pokemon_name):
  url = f"{base_url}pokemon/{pokemon_name}"
  response = requists.get(url)
  #print(response.json())
  if(response.status_code == 200):
    #    print("data is retrived successfully")
         pokeman_data = response.json()
         print(pokeman_data)
  else:
      print(f"Pokemon not found {response.status_code}")
pokeman_name = input("Enter the name of the Pokemon: ").lower()

pokeman_info = get_pokemon(pokeman_name)

if pokeman_info:
    print(f"Name: {pokeman_info['name'].capitalize()}")
    print(f"Height: {pokeman_info['height']}")
    print(f"Weight: {pokeman_info['weight']}")
    print("Abilities:")
    for ability in pokeman_info['abilities']:
        print(f"- {ability['ability']['name']}")
