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
      <showcase />
    </md-content>
  </div>
</template>

<script>
import Showcase from './components/Showcase.vue';

export default {
    name: 'app',
    components: {
      'showcase': Showcase
    },
    data: () => ({
      title: 'Vitrine',
      appName: 'Desafio Dress&Go',
      showNavigation: false,
      showSidepanel: false
    })
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
</style>
