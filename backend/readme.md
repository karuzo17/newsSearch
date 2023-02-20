# How to setup the backend part 

## API Key 

1. Get your newsapi key from https://newsapi.org/ 
2. Create a local .env file
3. Enter NEWS_API_KEY="YOUR_API_KEY"

## Create virtual environment inside the backend folder

1. Run `python3 -m venv .venv`
2. Run `source .venv/bin/activate`


## Install dependencies 

Run `pip install -r requirements.txt`


## Source venv again to make flask command available 

source .venv/bin/activate

## Run 

`flask --app main run`
