import requests
import shutil
import json

class Pokemon():
    def get_image(self, url, file_name):
        res = requests.get(url, stream=True)
        if 200 == res.status_code:
            with open(file_name, 'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print(f'Image downloaded: {file_name}')
        else:
            print('Image download failed')
    
    def get_pokemon(self, pokemon):
        url = 'https://pokeapi.co/api/v2/pokemon/'
        try:
            r = requests.get(url + pokemon.lower())
            
            if r.status_code != 200:
                print(f'Pokemon "{pokemon}" not found (Status: {r.status_code})')
                return None
            
            obj = json.loads(r.content)
            
            # Print Pokemon information
            print(f"\n--- POKEMON INFO ---")
            print(f"Name: {obj['name'].title()}")
            print(f"ID: {obj['id']}")
            print(f"Height: {obj['height']} decimetres")
            print(f"Weight: {obj['weight']} hectograms")
            
            # Types
            types = [t['type']['name'] for t in obj['types']]
            print(f"Type(s): {', '.join(types)}")
            
            # Stats
            print("Stats:")
            for stat in obj['stats']:
                stat_name = stat['stat']['name']
                stat_value = stat['base_stat']
                print(f"  {stat_name}: {stat_value}")
            
            # Abilities
            abilities = [a['ability']['name'] for a in obj['abilities']]
            print(f"Abilities: {', '.join(abilities)}")
            
            # Return sprite URL for image download
            return obj['sprites']['front_default']
            
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None
        except (KeyError, json.JSONDecodeError) as e:
            print(f"Error parsing Pokemon data: {e}")
            return None

