from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

""" create a get function for the search engine """
@api_view(['GET'])
def search(request):
    API_KEY='AIzaSyBEwBPZfUcxo0_n2S2YLpN5vU1NNTm85Fc'
    SEARCH_ENGINE_ID='b367e8f23498c4442'
     # get the query from the request
    query = request.GET.get('query')
    if query is None:
        raise Http404("No query found")

    # get the page number from the request, default to 1
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404("Invalid page number")

    # calculate the start index based on the page number
    start = (page - 1) * 10 + 1

    # construct the API URL
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

    # make the API request and handle errors
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Http404("Error making API request") from e

    # parse the search results and handle errors
    try:
        data = response.json()
        search_items = data.get("items")
        if search_items is None:
            raise Http404("No search results found")
    except (ValueError, KeyError):
        raise Http404("Error parsing search results")

    # iterate over the search results and return a list of dictionaries
    results = []
    for i, search_item in enumerate(search_items, start=start):
        try:
            title = search_item['title']
            link = search_item['link']
            snippet = search_item['snippet']
            html_snippet = search_item['htmlSnippet'].replace("<b>","").replace("</b>","")
            long_description = search_item['pagemap']['metatags'][0]['og:description']
        except (KeyError, IndexError):
            continue

        result_dict = {
            'title': title,
            'link': link,
            'snippet': snippet,
            'html_snippet': html_snippet,
            'long_description': long_description
        }
        results.append(result_dict)

    return Response({'results': results})
    
    
    