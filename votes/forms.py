from django.forms import ModelForm
import datetime
from .models import Candidate, Position, Vote

class VoteModelForm(ModelForm):
    class Meta:
        model = Candidate
        exclude = ['position', 'birthdate', 'platform']
