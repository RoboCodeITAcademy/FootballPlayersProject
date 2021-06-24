from django import forms
from .models import Player
class AddPlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = '__all__'