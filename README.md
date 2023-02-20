# News Search

## Folder structure 

```
.
├── frontend                   # Contains vue.js frontend bundled with vite 
├── backend                    # Contains flask backend 
├── task                       # Contains original task description
└── README.md
```
##  Setup 

Please follow the setup steps in `./backend` and `.frontend` sequentially. 

## Explantion 

The project uses https://newsapi.org/ as API for the articles. Note: The free version allows 100 REST calls per day. 

## Features

1. Searchbar with multilanguage support (de/en)
2. Articles can be sorted by different options 
3. Article preview shows title, source, date, short description and the url. On click arcticles are opened in a new tab 
4. Vite as alternative to webpack is used to bundle the project 
 

### Frontend 

Vuejs together with Tailwindcss and TypeScript.

### Backend 

As backend python3 with flask is used.
