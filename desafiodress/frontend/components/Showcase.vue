<template>
  <div class="md-layout md-gutter md-alignment-center">
    <div class="product md-layout-item md-medium-size-50 md-small-size-50 md-xsmall-size-100" v-for="product in products" v-match-heights="{el: ['.product-header']}">
      <a href="/api">
        <md-card md-with-hover>
          <md-riple>
            <md-card-media md-ratio="4:3" class="product-photo">
                <img :src="product.photo" alt="Alt Text">
              </md-card-media>
  
            <md-card-header class="product-header">
              <span class="md-title">{{ product.name }}</span>
              <span class="md-subhead">$ {{ product.price }}</span>
            </md-card-header>
          </md-riple>
        </md-card>
      </a>
    </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
    name: 'Showcase',
    data: () => ({
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
  .md-layout-item.product {
    margin-bottom: 15px;
  }
  .md-layout-item.product a {
    /*text-decoration: none !important;*/
  }
  .product-header > span {
    display: block;
  }
  .product-header > span.md-title {
    margin-bottom: 10px;
  }
  .product-header > span.md-subhead {
    bottom: 10px;
    position: absolute;
  }
</style>
