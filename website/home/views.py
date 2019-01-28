# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import SearchForm
from home.models import Post

def search_view(request):
    '''
    Function to manage search form queries and display to user
    '''
    if request.method == "POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            search_query = form.cleaned_data['search_item']

            print("SEARCH QUERY: ['%s']" % search_query)
            results = Post.objects.filter(title__icontains = search_query)

            # Just a console debug
            if( len(results) == 0 ):
                print("DEBUG: NO RESULTS FOUND!")
            else:
                print("DEBUG: {} RESULTS FOUND!".format(len(results)))
                print('-' * 50)
                for result in results:
                    print("\t-> %s" % result)
                print('-' * 50)

            # return the render with object_list populated with search result
            return render(request, 'home/index.html',
                          {'form': form, 'object_list': results})

        else:
            # If query is invalid (for any reason) -> display all news
            results = Post.objects.all()
            return render(request, 'home/index.html',
                          {'form': form, 'object_list': results})

    else:
        form = SearchForm()

    return render(request, 'home/index.html', {'form': form})
