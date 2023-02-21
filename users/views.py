from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def test_view(request):
	context = {}
	#return HttpResponse('<h1>TEST VIEW</h1>')
	return render(request, 'layout.html', context)

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if username or email is not None:
			login(request, user)

			print(f'Welcome {user.username}')
			print('Authentication successful!')
			return redirect('dashboard')
		else:
			messages.error(request, f"Please input the right credentials!")	
			print('Authentication failed!')					


def dashboard(request):
	return render(request, 'dashboard.html')

def logoutUser(request):
	logout(request)
	return redirect('login')

