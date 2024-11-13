import requests
import pytest

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "52ac9979326cd22743c069cb8d76bc74"
HEADER = {"Content-Type": "application/json", "trainer_token": TOKEN }
TRAINER_ID = "7444"

def test_status_code():

    response = requests.get(url = f"{URL}/trainers", params = {"trainer_id": TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response(): 
      response_get = requests.get(url = f"{URL}/trainers", params = {"trainer_id": TRAINER_ID})  
      assert response_get.json()["data"][0]["trainer_name"] == "Бульбазавр"

@pytest.mark.parametrize('key, value', ['trainer_name','Tor'), ('id',f'[TRAINER_ID]')] 
def test_parametrize(key,value):
    response_parametrize = requests.get(url= f'{URL}/trainers',params = {'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value