from django.urls import path 
from .import views
from .models import Player
from .ajax import * 

from django.views.generic.edit import DeleteView
app_name= 'player'

urlpatterns = [
	path('', views.PlayerListView.as_view(), name = 'players'),
	path('update/<pk>', views.UpdatePlayerView.as_view(), name = 'update_player'),
	#path('detail/<pk>', views.PlayerDetailView.as_view(), name = 'detail_player'),
	path('add/', views.CreatePlayerView.as_view(),name='add'),

	path('delete/<pk>', DeleteView.as_view(model=Player, success_url='/'), name='delete'),
	
	path('search/', views.searchPage, name='search'),
	path('test/', views.searchPlayer, name='searchPlayer'),

	path('all/', views.PlayerListView.as_view(), name='all')
]
