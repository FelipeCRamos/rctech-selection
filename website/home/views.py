# coding: utf-8

from django.shortcuts import render
from .forms import SearchForm
from home.models import Post

def home_page(request):
    '''
    Before the user make a search query, it displays all available posts
    '''
    posts = Post.objects.all()
    return render(request, 'home/index.html', {'object_list': posts})

def search_view(request):
    '''
    Function to manage search form queries and display to user
    '''
    if request.method == "POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            # Get all posts that the title contains 'search_query'
            search_query = form.cleaned_data['search_item']
            results = Post.objects.filter(title__icontains = search_query)

        else:
            # If query is invalid (for any reason) -> display all news
            results = Post.objects.all()

        # return the render with object_list populated with search result
        return render(request, 'home/index.html',
                      {'form': form, 'object_list': results})
    else:
        # Just declare the form to prevent errors
        form = SearchForm()

    return render(request, 'home/index.html', {'form': form})
