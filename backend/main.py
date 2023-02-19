from flask import Flask
from flask import request
from newsapi import NewsApiClient
from flask import jsonify
from markupsafe import escape
from flask_cors import CORS
import os 

app = Flask(__name__)
CORS(app)
api = NewsApiClient(api_key=os.environ.get("NEWS_API_KEY"))

# index route will display the 
@app.route('/', methods=['GET'])
def hello():
    if request.method == 'POST':
            return '504: Method not allowed'
    
    top_headlines = api.get_top_headlines(language='de')

    print('top headlines', top_headlines)

    return jsonify(top_headlines)

@app.route('/search', methods=['GET'])
def search():
      query = request.args.get('query', default='', type=str)
      locale = request.args.get('locale', default='de', type=str)
      sortBy = request.args.get('sortBy', default='publishedAt', type=str)


      print('query', query)
      print('locale', locale)
      results = api.get_everything(q=query, language=locale, sort_by=sortBy)
      print('results', results)
      print('sortBy', sortBy)

      return jsonify(results)