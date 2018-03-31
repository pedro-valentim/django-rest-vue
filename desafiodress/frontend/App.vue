<template>
    <div id="app">

        <img src="./assets/logo.png">
        <h1>{{ msg }}</h1><br>
        <div class="elevation-demo">
            <md-content class="md-elevation-1">1</md-content>
            <md-content class="md-elevation-2">2</md-content>
            <md-content class="md-elevation-3">3</md-content>
            <md-content class="md-elevation-4">4</md-content>
            <md-content class="md-elevation-5">5</md-content>
            <md-content class="md-elevation-6">6</md-content>
            <md-content class="md-elevation-7">7</md-content>
            <md-content class="md-elevation-8">8</md-content>
            <md-content class="md-elevation-9">9</md-content>
            <md-content class="md-elevation-10">10</md-content>
            <md-content class="md-elevation-11">11</md-content>
            <md-content class="md-elevation-12">12</md-content>
            <md-content class="md-elevation-13">13</md-content>
            <md-content class="md-elevation-14">14</md-content>
            <md-content class="md-elevation-15">15</md-content>
            <md-content class="md-elevation-16">16</md-content>
            <md-content class="md-elevation-17">17</md-content>
            <md-content class="md-elevation-18">18</md-content>
            <md-content class="md-elevation-19">19</md-content>
            <md-content class="md-elevation-20">20</md-content>
            <md-content class="md-elevation-21">21</md-content>
            <md-content class="md-elevation-22">22</md-content>
            <md-content class="md-elevation-23">23</md-content>
            <md-content class="md-elevation-24">24</md-content>
        </div>
    </div>
</template>

<script>
export default {
    name: 'app',
    data () {
        return {
            msg: 'Welcome to Your Vue.js App',
        }
    }
}
</script>

<style>
#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}

[class^=md-elevation] {
    padding: 15px;
}

h1, h2 {
    font-weight: normal;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    display: inline-block;
    margin: 0 10px;
}

a {
    color: #42b983;
}
</style>
