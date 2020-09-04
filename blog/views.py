from django.shortcuts import render
from django.http import HttpResponse


posts = [
	{
		'author':'peter',
		'title':'Blog post1',
		'content':'this is my first blog',
		'date_posted':'august 21,2020'
	},
	{
		'author':'potter',
		'title':'Blog post2',
		'content':'this is my secondt blog',
		'date_posted':'september 21,2020'
	}
]

def home(request):
	
	return render(request,'blog/home.html',{'posts':posts})

def about(request):
	return render(request,'blog/about.html'
		,{'title':'About'})	

# Create your views here.
