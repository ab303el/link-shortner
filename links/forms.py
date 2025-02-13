from django import forms
# to link to our model we use ModelForm
from .models import Link

# class LinkForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     url = forms.URLField(max_length=200)
#     slug = forms.SlugField(required=False)

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['name' , 'url' , 'slug']