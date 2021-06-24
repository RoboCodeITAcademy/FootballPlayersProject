from django.shortcuts import render, redirect
from django.views.generic import (
	TemplateView, 
	ListView,
	UpdateView,
	DetailView
	)
from django.views.generic.edit import CreateView
from .forms import  AddPlayerForm
from .models import Player
from django.http import JsonResponse
from django.urls import reverse

class PC(CreateView):
	model = Player
	fields = '__all__'
	# form_class = AddPlayerForm
	template_name = 'player/player_create.html'
	success_url = '/'

# Create your views here.
class PlayerListView(ListView):
	model = Player
	template_name = 'players_list.html'
	context_object_name = 'players'

class PlayerUpdateView(UpdateView):
	model = Player
	fields = '__all__'
	# template_name = 'index.html'
	success_url = '/'

class PlayerDetailView(DetailView):
	model = Player
	
	# template_name = ''

def searchPage(request):
	return render(request, 'search.html')

def searchPlayer(request):
	import json
	print(request.GET)
	if request.GET['player'] and request.GET.get('player'):
		d = request.GET.get('player')
		# data = json.dumps(d)
		queryset = Player.objects.filter(name__icontains=d).values()
		
		response = {
		 'is_naydeno':list(queryset)
		}	
		return JsonResponse(response)
	return JsonResponse({'ok':200})