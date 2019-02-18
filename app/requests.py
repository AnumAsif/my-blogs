import urllib.request, json
from .models import Quote


quote_url = None
def configure_request(app):
    global quote_url
    quote_url = app.config["QUOTE_API_URL"]

def get_quotes():
    '''
    Function that gets the json response
    '''
    quoteUrl= "http://quotes.stormconsultancy.co.uk/random.json"
    with urllib.request.urlopen(quoteUrl) as url:
        get_quotes_data = url.read()
        quotes_response = json.loads(get_quotes_data)    

        quote = None
        if quotes_response:
            author = quotes_response.get('author')
            quoteMsg = quotes_response.get('quote')
            quote = Quote(author, quoteMsg)
    return quote
        