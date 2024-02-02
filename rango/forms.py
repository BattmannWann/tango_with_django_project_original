from django import forms 
from rango.models import Page, Category


class CategoryForm(forms.ModelForm):
    
    name = forms.CharField(max_length = 128, help_text = "Please enter the category name.")
    slug = forms.CharField(widget = forms.HiddenInput(), required = False)
    
    views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    likes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    
    
    class Meta:
        model = Category
        fiels = ('name')
        
        

class PageForm(forms.ModelForm):
    
    title = forms.CharField(max_length = 128, help_text = "Please enter the title of the page.")
    url = forms.URLField(max_length = 200, help_text = "PLease enter the URL of the page.")
    views = forms.IntegerField(widget = forms.HiddenInput(), intital = 0)
    
    class Meta:
        
        model = Page
        exclude = ('category')
        
        
