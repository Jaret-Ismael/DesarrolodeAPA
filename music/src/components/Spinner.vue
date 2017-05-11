<template>
	<div class="loader">Loading...</div>
</template>
<script>
  exportdefault {
    name: 'spinner'
  }
</script>

<style>
.loader,
.loader:after {
  border-radius: 50%;
  width: 10em;
  height: 10em;
}
.loader {
  margin: 60px auto;
  font-size: 10px;
  position: relative;
  text-indent: -9999em;
  border-top: 1.1em solid rgba(15,111,140, 0.2);
  border-right: 1.1em solid rgba(15,111,140, 0.2);
  border-bottom: 1.1em solid rgba(15,111,140, 0.2);
  border-left: 1.1em solid #0f6f8c;
  -webkit-transform: translateZ(0);
  -ms-transform: translateZ(0);
  transform: translateZ(0);
  -webkit-animation: load8 1.1s infinite linear;
  animation: load8 1.1s infinite linear;
}
@-webkit-keyframes load8 {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@keyframes load8 {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

</style>

3.-Ir a archivo App.vue y modificarlo con este cÃ³digo:

<template lang="pug">
  <div id="app">
    <img src="./assets/logo.png">
    h1 Album Music
    select(v-model="selectedCountry")
      option(v-for="country in countries" v-bind:value="country.value") {{ country.name}}
    spinner(v-show="loading")
    ul
      artist(v-for="artist in artists" v-bind:artist="artist" v-bind:key="artist.mbid") 
    
  </div>
</template>

<script>
import Artist from './components/Artist.vue'
import Spinner from './components/Spinner.vue'
import getArtists from './api'

export default {
  name: 'app',
  data () {
    return {
      artists:[],
      countries:[
      { name:'Mexico',value:'mexico'},
      { name:'Argentina',value:'argentina'},
      { name:'Colombia',value:'colombia'},
      { name:'EspaÃ±a',value:'spain'},
      ],
      selectedCountry: 'mexico',
      loading:true
    }
  },
  components:{
    Artist,
    Spinner
  },
  methods:{
    refreshArtists(){
      const self = this
      this.loading=true
      this.artists=[]
    getArtists(this.selectedCountry)
      .then(function (artists) {
        self.loading=false
        self.artists = artists
      })

    }
  },
  mounted(){
    this.refreshArtists()
  },
  watch: {
    selectedCountry(){
      this.refreshArtists()

    }
  }
}
</script>

<style lang="stylus">
#app
    font-family 'Avenir', Helvetica, Arial, sans-serif
    -webkit-font-smoothing antialiased
    -moz-osx-font-smoothing grayscale
    text-align center
    color #2c3e50
    margin-top 60px

h1, h2
    font-weight normal

ul
    list-style-type none
    padding 0

li
    display inline-block
    margin 0 10px

a
    color #42b983
</style>