from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts=[
# 	{
# 		'title':'blog1',
# 		"content":"asdfj",
# 		"author":"user1",
# 		"date_posted":"august 27 2000"
# 	},
# 	{
# 		'title':'blog1',
# 		"content":"asdfj",
# 		"author":"user1",
# 		"date_posted":"august 27 2000"
# 	},
# 	{
# 		'title':'blog1',
# 		"content":"asdfj",
# 		"author":"user1",
# 		"date_posted":"august 27 2000"
# 	},
# ]
def home(request):
	context ={
		'posts':Post.objects.all()
	}
	
	return render(request,'blog/home.html',context)

def about(request):
	return render(request,'blog/about.html',{'title':'About'})	

# Create your views here.
