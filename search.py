import requests

API_KEY='AIzaSyBEwBPZfUcxo0_n2S2YLpN5vU1NNTm85Fc'
SEARCH_ENGINE_ID='b367e8f23498c4442'

query = "python"

#using first page of results
page=1

# constructing the URL
# doc: https://developers.google.com/custom-search/v1/using_rest
# calculating start, (page=2) => (start=11), (page=3) => (start=21)

start = (page - 1) * 10 + 1
#url = "https://www.googleapis.com/customsearch/v1?key={}&cx={}&q={}&start={}".format(API_KEY, SEARCH_ENGINE_ID, query, start)
url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"


# make the API request
data=requests.get(url).json()

# get the result items
search_items=data.get("items")


# iterate over 10 results found
for i, search_item in enumerate(search_items, start=1):
    try:
        long_description=search_item['pagemap']['metatags'][0]['og:description']
    except KeyError:
        long_description="N/A"
    # get the page title
    title=search_item['title']
    # get the page link
    link=search_item['link']
    # get the page snippet
    snippet=search_item['snippet']
    #htmlSnippet=search_item['htmlSnippet']
    htmlSnippet=search_item['htmlSnippet'].replace("<b>","").replace("</b>","")
    #print results
    print("="*10, f"Result #{i+start-1}", "="*10)
    print(f"{i}. Title: {title} Link: {link} Snippet: {snippet} HTML Snippet: {htmlSnippet} Long Description: {long_description}")
        
        