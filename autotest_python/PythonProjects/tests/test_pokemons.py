import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '23285b87e0246ac8b0719b032223e8da' 
HEADER = { 'Content-Type': 'application/json',
          'trainer_token':TOKEN}
TRAINER_ID = '37823'

## Проверка ответа статуса 200
def test_status_code():
    response=requests.get(url = f'{URL}/pokemons', headers = HEADER, params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200
## Проверка, что приходит правильное имя покемона 

def test_part_response():
    response_get=requests.get(url = f'{URL}/pokemons', headers = HEADER, params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Sirius'

## Проверка, что приходит статус 200 на инфо о тренере

def test_code_get_name():
    response_get_name=requests.get(url = f'{URL}/trainers/{TRAINER_ID}', headers = HEADER)
    print("got status:", response_get_name.status_code)
    assert response_get_name.status_code == 200


## Проверка, что приходит верное имя тренера

def test_get_trainer_name():
    response_get_trainer_name=requests.get(url = f'{URL}/trainers/{TRAINER_ID}', headers = HEADER)
    assert response_get_trainer_name.json()["trainer_name"] == 'фома киняев'


@pytest.mark.parametrize('key, value', [('name', 'Sirius'), ('trainer_id', TRAINER_ID), ('id', '375022')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', headers = HEADER, params = {'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] ==  value