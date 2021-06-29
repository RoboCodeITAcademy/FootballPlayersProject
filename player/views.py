from django.shortcuts import render, redirect
from django.views.generic import (
	TemplateView, 
	ListView,
	DetailView,
	View
	)
from django.views.generic.edit import (
	CreateView,
	UpdateView,
	DeleteView
	)

# 1. controller method
# 2. controller class 
# request => WSGIRequest = example



from .forms import  AddPlayerForm
from .models import Player
from django.http import JsonResponse
from django.urls import reverse



# Create your views here.
class PlayerListView(ListView):
	model = Player
	template_name = 'players_list.html'
	context_object_name = 'players'


class PlayerDetailView(DetailView):
	model = Player
	
	# template_name = ''

def searchPage(request):
	query = request.GET.get('player_name', None)
	print(query)
	response = Player.objects.filter(name__icontains=query)
	return render(request, 'search.html',{'players':response})

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

 
class PlayerListView(View):
	
	def get(self,request):
		players = Player.objects.all()
		# form = AddPlayerForm()
		context = {
			'players':players,
			# 'form':form
		}
		return render(request, 'all.html', context)

	def post(self):
		form = AddPlayerForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			form = AddPlayerForm()
		context = {
			'form':form
		}
		return render(request, 'all.html', context)




class CreatePlayerView(CreateView):
	model = Player
	fields = '__all__'
	success_url = '/'
	# template_name = 'YOU TEMPLATE PATH'
	# or 
	# default-template = '<model_name/model_name_form.html>'

class UpdatePlayerView(UpdateView):
	model = Player
	fields = '__all__'
	success_url = '/'

