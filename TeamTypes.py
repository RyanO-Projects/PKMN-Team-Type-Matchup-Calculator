import requests

# Fetch type data from PokeAPI and store it in a dictionary
def fetch_type_data():
    OK = 200
    type_data = {}

    response = requests.get("https://pokeapi.co/api/v2/type/")
    if response.status_code == OK:
        types = response.json()["results"]
        for type_info in types:
            type_name = type_info["name"]
            type_response = requests.get(type_info["url"])
            if type_response.status_code == OK:
                damage_relations = type_response.json()["damage_relations"]
                super_effective = [t["name"] for t in damage_relations["double_damage_from"]]
                not_very_effective = [t["name"] for t in damage_relations["half_damage_from"]]
                no_effect = [t["name"] for t in damage_relations["no_damage_from"]]
                type_data[type_name] = {
                    "super_effective" : super_effective,
                    "not_very_effective" : not_very_effective,
                    "no_effect" : no_effect
                }
    return type_data

# Determine defensive strength/weakness to each type for each PKMN in team
def tally(pokemon, type_dict, type_data):
    for type_name in pokemon:
        type_info = type_data.get(type_name)
        if type_info:
            for key in type_dict:
                if key in type_info["super_effective"]:  #check weakness
                    type_dict[key] -= 1
                if key in type_info["not_very_effective"]:  #check resist
                    type_dict[key] += 1
                if key in type_info["no_effect"]:   #check no-effect
                    type_dict[key] += 2
    
    return type_dict

def main():
    type_data = fetch_type_data()

    type_dict = {
        'normal' : 0, 'fire' : 0, 'water' : 0, 'electric' : 0,
        'grass' : 0, 'ice' : 0, 'fighting' : 0, 'poison' : 0,
        'ground' : 0, 'flying' : 0, 'psychic' : 0, 'bug' : 0, 'rock' : 0,
        'ghost' : 0, 'dark' : 0, 'dragon' : 0, 'steel' : 0, 'fairy' : 0
        }
    
    team = (['water', 'flying'],)
    #team = (['fire'],['psychic','flying'], ['flying','poison'], ['water','flying'], ['fighting'])

    for pokemon in team:
        tally(pokemon, type_dict, type_data)

    #print(type_data)
    print(type_dict)

main()