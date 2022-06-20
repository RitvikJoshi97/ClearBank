from django.shortcuts import render
from django.http import HttpResponse, request
import requests
import json

# Create your views here.
def main(request):
    cat_call = requests.get("https://api.thecatapi.com/v1/images/search").json()#f9980f5f-6855-4620-9be2-4bcbb1cd2f80 
    #print(json.loads(cat_call))
    cat_call = json.dumps(cat_call)
    json_data = json.loads(cat_call)[0]
    print(json.loads(cat_call))
    id = json_data['id']
    print(id)
    jpg = json_data['url']
    #print(json.loads(cat_call.json()[0]))
    return HttpResponse("<h1>This is working</h1> <img src='%s' height=100px width=100px>" %jpg)


# [{'breeds': [{'weight': {'imperial': '6 - 12', 'metric': '3 - 5'}, 'id': 'soma', 'name': 'Somali', 'cfa_url': 'http://cfa.org/Breeds/BreedsSthruT/Somali.aspx', 'vetstreet_url': 'http://www.vetstreet.com/cats/somali', 'vcahospitals_url': 'https://vcahospitals.com/know-your-pet/cat-breeds/somali', 'temperament': 'Mischievous, Tenacious, Intelligent, Affectionate, Gentle, Interactive, Loyal', 'origin': 'Somalia', 'country_codes': 'SO', 'country_code': 'SO', 'description': 'The Somali lives life to the fullest. He climbs higher, jumps farther, plays harder. Nothing escapes the notice of this highly intelligent and inquisitive cat. Somalis love the company of humans and other animals.', 'life_span': '12 - 16', 'indoor': 0, 'alt_names': 'Fox Cat, Long-Haired Abyssinian', 'adaptability': 5, 'affection_level': 5, 'child_friendly': 3, 'dog_friendly': 4, 'energy_level': 5, 'grooming': 3, 'health_issues': 2, 'intelligence': 5, 'shedding_level': 4, 'social_needs': 5, 'stranger_friendly': 5, 'vocalisation': 1, 'experimental': 0, 'hairless': 0, 'natural': 0, 'rare': 0, 'rex': 0, 'suppressed_tail': 0, 'short_legs': 0, 'wikipedia_url': 'https://en.wikipedia.org/wiki/Somali_(cat)', 'hypoallergenic': 0, 'reference_image_id': 'EPF2ejNS0'}], 'id': 'MuIB88nqJ', 'url': 'https://cdn2.thecatapi.com/images/MuIB88nqJ.jpg', 'width': 750, 'height': 750}]