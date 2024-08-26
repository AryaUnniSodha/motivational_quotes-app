from django.shortcuts import render
from django.http import JsonResponse  # Import JsonResponse
from .utils import get_random_quote  # Import the function from utils

def home(request):
    quote_text, quote_author = get_random_quote()
    print(f"Quote Text: {quote_text}")
    print(f"Quote Author: {quote_author}")
    return render(request, 'quotes/home.html', {'quote_text': quote_text, 'quote_author': quote_author})

def get_quote(request):
    quote_text, quote_author = get_random_quote()
    return JsonResponse({'quote_text': quote_text, 'quote_author': quote_author})
