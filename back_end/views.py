from rest_framework.views import APIView
from rest_framework.response import Response
import json
from functools import lru_cache
import requests
import random

bucket_url = 'https://pub-ed66c609d0704fa385dcef01472e6bcf.r2.dev/ss2-monsters'

@lru_cache(maxsize=1)
def get_json():
    response = requests.get(f"{bucket_url}/sprites.json")
    file = json.loads(response.text)
    
    return file

class Monsters_v1(APIView):
    def get(self, request):
        base = get_json()
        
        family = random.choice(list(base.keys()))
        monster = random.choice(list(base[family]))
        
        data = {
            "name": monster,
            "family": family,
            "sprite": f"{bucket_url}/{family}/{monster}.gif"
        }
        
        return Response(data)

class Monsters_filter_v1(APIView):
    def get(self, request, family, monster=None):
        base = get_json()
        
        if family.isdigit():
            index = int(family)
            if index >= len(base):
                return Response({"message": "ops, numero invalido"}, status=400)
            
            family_name, family_choiced = list(base.items())[index]
            monster_choiced = self.get_monster(family_choiced, monster)
            if monster_choiced is None:
                return Response({"message": "ops, monstro invalido"}, status=400)
            
        elif family in base:
            try:
                family_name = family
                family_choiced = base[family]
                monster_choiced = self.get_monster(family_choiced, monster)
                if monster_choiced is None:
                    return Response({"message": "ops, monstro invalido"}, status=400)
                
            except KeyError:
                return Response({"message": "ops, familia invalida"}, status=400) 
            
        else:
            return Response({"message": "Formato inválido"}, status=400)
        
        data = {
            "name": monster_choiced,
            "family": family_name,
            "sprite": f"{bucket_url}/{family_name}/{monster_choiced}.gif"
        }
        
        return Response(data)
    
    def rarity_definy(self, monsters_list):
        chances = []
        chance = 1
        rare_chance = 0.1
        for monster in monsters_list:
            if "rare" in monster.lower():
                chances.append(rare_chance)
                rare_chance *= 0.5
                
            else:
                chances.append(chance)
                chance *= 0.8
            
        return chances
    
    def get_monster(self, family_arr, monster=None):
        if not monster:
            return random.choices(
                        family_arr, weights=self.rarity_definy(family_arr), k=1)[0]
        
        elif monster in family_arr:
            return monster
        
        elif monster.isdigit():
            index = int(monster)
            if not index >= len(family_arr):
                return family_arr[index]
            
        return None

class Monsters_info_v1(APIView):
    def get(self, request):
        base = get_json()
        return Response(base)
    
class Monsters_filter_info_v1(APIView):
    def get(self, request, family):
        base = get_json()

        if family.isdigit():
            index = int(family)
            if index >= len(base):
                return Response({"message": "ops, numero invalido"}, status=400)
            
            family_choiced = list(base.values())[index]
            
        elif family.replace(" ", "").replace("-", "").isalpha():
            try:
                family_choiced = base[family]
                
            except KeyError:
                return Response({"message": "ops, familia invalida"}, status=400) 
            
        else:
            return Response({"message": "Formato inválido"}, status=400)

        return Response(family_choiced)