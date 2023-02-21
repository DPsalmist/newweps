from django.shortcuts import render, redirect
from .models import Club, News, Leadership
from django.http import HttpResponse

# Create your views here.
def test_view(request):
	context = {}
	#return HttpResponse('<h1>TEST VIEW</h1>')
	return render(request, 'test.html', context)

def index_view(request):
	clubs = Club.objects.all()
	news = News.objects.all()[:3]
	leadership = Leadership.objects.all()
	context = {'clubs':clubs, 'news':news, 'leadership':leadership}
	return render(request, 'index.html', context)

def about_view(request):
	leadership = Leadership.objects.all()
	context = {'leadership':leadership}
	return render(request, 'about.html', context)

def eyfs_academics_view(request):
	context = {}
	return render(request, 'eyfs.html', context)

def pry_academics_view(request):
	context = {}
	return render(request, 'pry_school.html', context)

def sec_academics_view(request):
	context = {}
	return render(request, 'sec_school.html', context)

def news_view(request):
	news = News.objects.all()[:3]
	context = { 'news':news,}
	return render(request, 'news.html', context)

def news_detail_view(request, pk):
	news_detail = News.objects.get(pk=pk)
	context = {'news_detail':news_detail}
	return render(request, 'news_detail.html', context)

def admissions_view(request):
	context = {}
	return render(request, 'admissions.html', context)

def contact_view(request):
	context = {}
	return render(request, 'contact.html', context)