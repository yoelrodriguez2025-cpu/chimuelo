# Main.py
from Pokemon import Pokemon
from SuperHero import SuperHero
from Weather import Weather

class Main:
    def __init__(self):
        self.pokemon_service = Pokemon()
        self.hero_service = SuperHero()
        self.weather_service = Weather()
    
    def menu(self):
        print("=" * 50)
        print("       WEB SERVICES INFORMATION CENTER")
        print("=" * 50)
        print()
        
        # Get user input
        favorite_pokemon = input("Enter your favorite Pokemon: ").strip().lower()
        favorite_hero = input("Enter your favorite Super Hero: ").strip()
        city = input("Enter your city of residence: ").strip()
        
        print()
        print("=" * 50)
        print("              FETCHING INFORMATION...")
        print("=" * 50)
        print()
        
        # 1. Pokemon Information
        print("-" * 40)
        print("POKEMON INFORMATION")
        print("-" * 40)
        self._get_pokemon_info(favorite_pokemon)
        
        print()
        
        # 2. Super Hero Information
        print("-" * 40)
        print("SUPER HERO INFORMATION")
        print("-" * 40)
        self._get_hero_info(favorite_hero)
        
        print()
        
        # 3. Weather Information
        print("-" * 40)
        print("WEATHER INFORMATION")
        print("-" * 40)
        self._get_weather_info(city)
        
        print()
        print("=" * 50)
        print("              PROCESS COMPLETED")
        print("=" * 50)
    
    def _get_pokemon_info(self, pokemon_name):
        try:
            if not pokemon_name:
                print("Error: No Pokemon name provided.")
                return
            
            # This now prints info AND returns the sprite URL
            sprite_url = self.pokemon_service.get_pokemon(pokemon_name)
            
            if sprite_url:
                file_name = f"{pokemon_name}.png"
                self.pokemon_service.get_image(sprite_url, file_name)
            else:
                print(f"Error: Could not retrieve data for '{pokemon_name}'")
                
        except Exception as e:
            print(f"Error fetching Pokemon information: {e}")
    
    def _get_hero_info(self, hero_name):
        try:
            if not hero_name:
                print("Error: No hero name provided.")
                return
            
            # Pass the hero_name to the method!
            result = self.hero_service.get_heroes(hero_name)
            
            if result is None:
                print(f"Could not retrieve data for '{hero_name}'")
                
        except Exception as e:
            print(f"Error fetching hero information: {e}")
    
    def _get_weather_info(self, city):
        try:
            if not city:
                print("Error: No city provided.")
                return
            
            # Check if API key is set
            api_key = "2419bb362c43bc6ec3b78de6045acbba"            
            if not api_key:
                print("Error: Weather API key is required.")
                print("Get your free API key at: https://openweathermap.org/api")
                return
            
            self.weather_service.get_weather(city, api_key)
            
        except Exception as e:
            print(f"Error fetching weather information: {e}")

# Entry point
if __name__ == "__main__":
    main_app = Main()
    main_app.menu()