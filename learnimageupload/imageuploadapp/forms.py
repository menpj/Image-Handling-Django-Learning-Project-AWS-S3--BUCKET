#https://youtu.be/UcUm82jWeKc
#https://youtu.be/lKyH_ZGtvwM
from django import forms
from imageuploadapp.models import Dog

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name','image']
        widgets = {
            'image': forms.FileInput(attrs={'accept': '.png, .jpg, .jpeg, .pdf'})
        }