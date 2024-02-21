#1. Build a Flask app that scrapes data from multiple websites and displays it on your site.
#You can try to scrap websites like youtube , amazon and show data on output pages and deploy it on cloud 
#platform 
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    #Scrape data from Youtube
    youtube_data = scrape_youtube()

    # Scrape data from Amazon
    amazon_data = scrape_amazon()

    # Example data for testing
    youtube_data = [{'title': 'Video Title 1', 'url': 'https://www.youtube.com/watch?v=SA-toN0eXM4', 'views': 10000},]

    amazon_data = [{'name': 'Product 1', 'url': 'https://www.amazon.com/Puro-Sound-Labs-Cancelling-Headphones/dp/B087QV671C/ref=sr_1_2_sspa?crid=2BAIYVI9VPQ16&keywords=sony+headphones&qid=1706908801&sprefix=sony+headphones%2Caps%2C362&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1', 'price': '$149', 'rating': '4.5'},]

    return render_template('index.html', youtube_data=youtube_data, amazon_data=amazon_data)



def scrape_youtube():
    url = 'https://www.youtube.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')  # Parse the HTML content of the page

    # Extract relevant data from the soup (example: getting video titles)
    video_titles = [title.text for title in soup.select('.style-scope ytd-rich-grid-media #video-title')]

    return {'video_titles': video_titles}



def scrape_amazon():
    url = 'https://www.amazon.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')  # Parse the HTML content of the page

    # Extract relevant data from the soup (example: getting product names)
    product_names = [name.text for name in soup.select('.s-title-instructions')]

    return {'product_names': product_names}

if __name__ == '__main__':
    app.run(debug=True)
