import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '23285b87e0246ac8b0719b032223e8da' 
HEADER = { 'Content-Type': 'application/json',
          'trainer_token':TOKEN}
body_create_pokemon = {
    "name": "Bulba",
    "photo_id": 5
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response_create.text)

pokemon_id=response_create.json()['id']
print(pokemon_id)

body_change_name = {
    "pokemon_id": pokemon_id,
    "name": "Sirius",
    "photo_id": 2
}

body_add_pokeball = {
    "pokemon_id": pokemon_id
}

response_change_name= requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)

response_add_pokeball= requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)
