from django.urls import path
from .views import user_login, dashboard

urlpatterns = [
	path('dashboard/', dashboard, name='dashboard'),
	path('', user_login, name='login'),
		
]