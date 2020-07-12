from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("""
        <html><title>烂柯游艺社</title></html>
    """)
