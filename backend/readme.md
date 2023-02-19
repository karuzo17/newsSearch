# How to setup the backend part 

## API Key 

1. Get your newsapi key from https://newsapi.org/ 
2. Create a local .env file
3. Enter NEWS_API_KEY="YOUR_API_KEY"

## Create virtual environment 

1. Run `python3 -m venv .venv`
2. Run `source .venv/bin/activate`


## Install dependencies 

Run `pip install -r requirements.txt`

## Run 

`flask --main app run`
