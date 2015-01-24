from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests



def index(request):
    payload = {'u': 'random', 'login': 'f.nappez'}
    r = requests.get('https://www.blablashare.com/blablaface/api.php', params=payload)
    #import pdb;pdb.set_trace()


    data = r.json()
    url = data['user']['photo']
    names = data['other_nicknames']
    first_name = data['user']['firstname']
    full_name = data['user']['fullname']


    context = {'photo_url': url, 'names': names, 'first_name': first_name, 'full_name': full_name }
    return render(request, 'showphoto/index.html', context)

# Create your views here.
