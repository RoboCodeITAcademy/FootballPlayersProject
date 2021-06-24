from django.urls import path 
from .import views
from .ajax import * 

app_name= 'player'

urlpatterns = [
	path('', views.PlayerListView.as_view(), name = 'players'),
	path('update/<pk>', views.PlayerUpdateView.as_view(), name = 'update_player'),
	path('detail/<pk>', views.PlayerDetailView.as_view(), name = 'detail_player'),
	
	path('search/', views.searchPage, name='search'),
	path('test/', views.searchPlayer, name='searchPlayer'),
]