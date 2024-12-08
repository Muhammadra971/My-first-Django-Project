from django.forms import ModelForm
from . models import Moviedata

class MovieFrom(ModelForm):
    class Meta:
        model=Moviedata
        fields='__all__'