<script setup lang="ts">
import { reactive } from "vue";
import { ref } from "vue";
import { RouterLink, RouterView } from "vue-router";



const searchInput = reactive({
  text: '',
  locale: 'de',
  sortBy: 'publishedAt'
})
const articles = ref();
const totalResults = ref();

const handleClick = async () => {
  console.log('search', searchInput.text)

  if (searchInput.text === '') return 'enter a query'
  const response = await fetch(`http://127.0.0.1:5000/search?query=${searchInput.text}&locale=${searchInput.locale}&sortBy=${searchInput.sortBy}`)
  if (response) {

  }
  const data = await response.json();
  console.log('data', data)
  articles.value = data.articles
  totalResults.value = data.totalResults
}

</script>

<template>
  <header>
    <meta name="referrer" content="no-referrer" />

  </header>
  <section className="container mx-auto h-full ">
    <div className="flex flex-1 flex-col items-center justify-center w-full mt-4">

      <div className="items-center justify-center w-full flex-col flex">
        <div className="flex flex-row justify-center w-full">
          <input name="search" className="border-2 border-solid border-gray-600 p-2 w-1/2" v-model="searchInput.text"
            @keyup.enter="handleClick" />
          <button @click="handleClick"
            className="bg-gray-500 pt-2 pb-2 pl-4 pr-4 flex items-center justify-center h-11">
            <div className="text-xl text-white">{{searchInput.locale == 'de' ? 'Suche' : 'Search'}}</div>
          </button>

        </div>
        <div className="flex flex-row items-center">
        <label>{{ searchInput.locale === 'de'  ? 'Sprache' : 'Language'}}</label>
        <select v-model="searchInput.locale" >
            <option value="de">de</option>
            <option value="en">en</option>
            

        </select>
        <label className="ml-2">{{ searchInput.locale === 'de'  ? 'Sortiern nach' : 'Sort By'}}</label>
        <select v-model="searchInput.sortBy" >
            <option value="publishedAt">{{ searchInput.locale === 'de'  ? 'Datum' : 'Date'}}</option>
            <option value="relevancy">{{ searchInput.locale === 'de'  ? 'Relevanz' : 'Relevancy'}}</option>
            <option value="popularity">{{ searchInput.locale === 'de'  ? 'Beliebtheit' : 'Popularity'}}</option>
          </select>
        </div>

      </div>

      <div v-if="articles" className="m-4 ml-10 flex flex-col container">
        <p className="m-4"> {{ searchInput.locale === 'de' ? totalResults + " Artikel gefunden. Zeige die ersten " + articles.length + " Artikel" : totalResults + " articles found. Show first " + articles.length + " results"}} </p>
        <div className="flex flex-row m-4" v-for="article in articles" :key="article.source.id">
          <a :href="`${article.url}`" className="flex flex-row" target="_blank">
            <div className="w-40 flex flex-col items-start" v-if="article.urlToImage != null">

              <img :src="`${article.urlToImage}`" className="object-contain" />

            </div>
            <div className="flex flex-col ml-2">
              <div className="flex flex-row items-center">
                <h2 className="text-lg font-bold">{{ article.title }} </h2>
                <p>- {{ article.source.name }}</p>

              </div>
              <span className="font-light text-xs">{{ new Date(article.publishedAt).toLocaleDateString() + " " + new Date(article.publishedAt).toLocaleTimeString() }}</span>

              <p className="font-light">{{ article.description }}</p>

              <a :href="`${article.url}`" target="_blank">{{ article.url }}</a>
            </div>

          </a>

        </div>

      </div>
      <div v-if="articles">
        {{ articles[0] }}
      </div>
    </div>
  </section>


</template>

<style>
#app {
  height: 100vh;
}

html,
body {
  margin: 0;
  padding: 0;
  height: 100%;
}
</style>