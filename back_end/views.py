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

class Monsters_info_v1(APIView):
    def get(self, request):
        base = get_json()
        return Response(base)