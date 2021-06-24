from .models import Player
from django.http import JsonResponse
import json


def searchPlayer(request):
	print(request.GET)
	d = request.GET.get('data', None)
	if d:
		print('qqqqq')
	data = json.loads(d)
	print(data)
	return JsonResponse(data)