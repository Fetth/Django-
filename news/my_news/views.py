from django.shortcuts import render, redirect #redirect - перенаправление на страницу
import requests
from .models import News
BASE_URL = 'https://dummyjson.com/products'

def home(request):
    response = requests.get(f"{BASE_URL}") #GET запрос
    resp = {
        'resp': response.json()
    }
    return render(request, 'my_news/index.html', resp)