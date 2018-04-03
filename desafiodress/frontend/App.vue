<template>
  <div class="page-container md-layout-column">
    <md-toolbar class="md-primary">
      <md-button class="md-icon-button" @click="showNavigation = true">
        <md-icon>menu</md-icon>
      </md-button>
      <span class="md-title">{{ title }}</span>

      <div class="md-toolbar-section-end">
        <md-button @click="showSidepanel = true">REST API</md-button>
      </div>
    </md-toolbar>

    <md-drawer :md-active.sync="showNavigation">
      <md-toolbar class="md-transparent" md-elevation="0">
        <span class="md-title">{{ appName }}</span>
      </md-toolbar>

      <md-list>
        <md-list-item>
          <md-icon>grid_on</md-icon>
          <span class="md-list-item-text">Vitrine</span>
        </md-list-item>
      </md-list>
    </md-drawer>

    <md-drawer class="md-right" :md-active.sync="showSidepanel">
      <md-toolbar class="md-transparent" md-elevation="0">
        <span class="md-title">REST API</span>
        <md-button class="md-icon-button md-list-action">
          <md-icon class="md-primary">code</md-icon>
        </md-button>
      </md-toolbar>

      <md-list>
        <md-list-item href="/api" target="_blank">
          <span class="md-list-item-text">/api</span>
        </md-list-item>

        <md-list-item href="/api/products" target="_blank">
          <span class="md-list-item-text">/api/products</span>
        </md-list-item>
      </md-list>
    </md-drawer>

    <md-content>
      <div class="md-layout md-gutter md-alignment-center">
        <div class="product md-layout-item md-medium-size-50 md-small-size-50 md-xsmall-size-100" v-for="product in products" v-match-heights="{el: ['.product-header']}">
          <md-card>
            <md-card-media md-ratio="4:3" class="product-photo">
                <img :src="product.photo" alt="Alt Text">
              </md-card-media>
  
            <md-card-header class="product-header">
              <span class="md-title">{{ product.name }}</span><br>
              <span class="md-subhead">$ {{ product.price }}</span>
            </md-card-header>
  
            <md-card-actions>
              <md-button>See More</md-button>
            </md-card-actions>
          </md-card>
        </div>
      </div>
    </md-content>
  </div>
</template>

<script>

import axios from 'axios';

export default {
    name: 'app',
    data: () => ({
      title: 'Vitrine',
      appName: 'Desafio Dress&Go',
      showNavigation: false,
      showSidepanel: false,
      products: [],
      errors: []
    }),
    created() {
        axios.get('/api/products?format=json').then(response => {
          this.products = response.data
        }).catch(e => {
          this.errors.push(e)
        })
    }
}
</script>

<style lang="scss" scoped>
  body {
    min-height: 100%;
  }
  .md-app {
    border: 1px solid rgba(#000, .12);
  }
  .page-container {
    min-height: 100%;
    overflow: hidden;
    position: relative;
    border: 1px solid rgba(#000, .12);
  }
  .md-drawer {
    width: 230px;
    max-width: calc(100vw - 125px);
  }
  .md-content {
    padding: 16px;
  }
  .md-layout-item.product {
    margin-bottom: 15px;
  }
</style>
