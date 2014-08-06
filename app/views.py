from django.shortcuts import render
from django.http import HttpResponse
from app.models import Tweet

def index(request):
	tweets = Tweet.objects.order_by('date')[:10]
	return render(request, 'index.html', {'tweets' : tweets})

def error(request):
	return HttpResponse('<h1>404 Does Not Exist!</h1>')
