from hashlib import md5
from requests import get
from datetime import datetime

class SuperHero:
    """
    Information about the service:
    https://superheroapi.com/index.html
    """
    token = 'fea72302f4b828aa4ebc007d6616412b'
    
    def get_heroes(self, hero_name=None):
        if not self.token:
            print("Error: API token not configured. Add your token in SuperHero.py")
            return None
        
        if not hero_name:
            print("Error: No hero name provided")
            return None
            
        try:
            # Search for the specific hero name
            search_url = f'https://www.superheroapi.com/api.php/{self.token}/search/{hero_name}'
            result = get(search_url)
            data = result.json()
            
            print(f"Searching for: {hero_name}")
            print(f"API Status: {data.get('response', 'unknown')}")
            
            if data.get('response') == 'success':
                heroes = data.get('results', [])
                if heroes:
                    # Find exact match or closest match
                    matched_hero = None
                    for hero in heroes:
                        if hero['name'].lower() == hero_name.lower():
                            matched_hero = hero
                            break
                    
                    # If no exact match, use first result
                    if not matched_hero:
                        matched_hero = heroes[0]
                        print(f"No exact match, showing closest: {matched_hero['name']}")
                    
                    print(f"\n--- HERO INFORMATION ---")
                    print(f"Name: {matched_hero.get('name')}")
                    print(f"Full Name: {matched_hero.get('biography', {}).get('full-name', 'N/A')}")
                    print(f"Publisher: {matched_hero.get('biography', {}).get('publisher', 'N/A')}")
                    print(f"Alignment: {matched_hero.get('biography', {}).get('alignment', 'N/A')}")
                    print(f"Intelligence: {matched_hero.get('powerstats', {}).get('intelligence', 'N/A')}")
                    print(f"Strength: {matched_hero.get('powerstats', {}).get('strength', 'N/A')}")
                    print(f"Speed: {matched_hero.get('powerstats', {}).get('speed', 'N/A')}")
                    return matched_hero
                else:
                    print(f"No heroes found matching '{hero_name}'")
                    return None
            else:
                print(f"Error from API: {data.get('error', 'Unknown error')}")
                return None
                
        except Exception as e:
            print(f"Error fetching hero information: {e}")
            return None