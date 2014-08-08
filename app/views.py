from django.shortcuts import render
from django.http import HttpResponse
from app.models import Tweet
from django.core import serializers

def index(request):
	return render(request, 'index.html')

def tweets(request, start, quantity):
	data = serializers.serialize('json', Tweet.objects.order_by('-date')[start:int(quantity)+int(start)])
	return HttpResponse(data, content_type='application/json')


def error(request):
	return HttpResponse('<h1>404 Does Not Exist!</h1>')
