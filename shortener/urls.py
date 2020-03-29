from django.urls import path,include
from shortener.views import dashboard,create_short_url,redirect_to_long_url 
urlpatterns = [
	path("dashboard/",dashboard),
	path("create_short_url/",create_short_url),
	path("<str:hashcode>/",redirect_to_long_url),
]