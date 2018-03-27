from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'myblogg/index.html')

def help(request):
	return render(request, 'myblogg/help.html')