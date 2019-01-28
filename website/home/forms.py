from django import forms

class SearchForm(forms.Form):
    '''
    Define the search form
    '''
    search_item = forms.CharField(label="Search", max_length=256)
