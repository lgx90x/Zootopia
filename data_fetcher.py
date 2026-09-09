import os
from dotenv import load_dotenv
import requests


load_dotenv()
API_KEY = os.getenv('API_KEY')

def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """

  headers = {'X-Api-Key': API_KEY}
  params = {'name': animal_name}
  response = requests.get('https://api.api-ninjas.com/v1/animals', params, headers=headers)
  data = response.json()

  return data
