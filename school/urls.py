from django.urls import path
from .views import index_view, about_view, news_view, admissions_view, sec_academics_view, contact_view, news_detail_view, \
	pry_academics_view, eyfs_academics_view


urlpatterns = [
	path('', index_view, name='index'),
	#path('test/', test_view),
	path('about/', about_view, name='about'),
	path('school/eyfs/', eyfs_academics_view, name='eyfs-academics'),
	path('school/primary/', pry_academics_view, name='pry-academics'),
	path('school/secondary/', sec_academics_view, name='sec-academics'),
	path('news/', news_view, name='news'),
	path('news/<str:pk>/', news_detail_view, name='news-detail'),
	path('admissions/', admissions_view, name='admissions'),
	path('contact/', contact_view, name='contact'),
]