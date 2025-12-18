import os
from django.http import JsonResponse, HttpResponse

def index(request):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    index_path = os.path.join(base_dir, 'frontend', 'index.html')
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            return HttpResponse(f.read(), content_type='text/html')
    except FileNotFoundError:
        return HttpResponse('<h1>Index not found</h1>', status=404)

def optimize(request):
    balances=[5000,2000,1000]
    rates=[0.22,0.18,0.12]
    order=sorted(range(len(rates)), key=lambda i: rates[i], reverse=True)
    plan=[{"balance":balances[i],"rate":rates[i]} for i in order]
    return JsonResponse({"plan":plan})
