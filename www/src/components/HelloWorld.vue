<script setup lang="ts">

import {ref} from 'vue';

defineProps<{ msg: string }>()

function randomId() {
  return Math.floor(Math.random() * 100) + '-' + Date.now()
}

const sessionId = ref(randomId());

function request() {
  fetch("http://127.0.0.1:8000", {
    headers: {
      'User-ID': 'john',
      'Session-ID': sessionId.value,
      'X-Correlation-ID': randomId(),
    }
  }).then(
      response => response.json()
  ).then(json => {
    alert(json.message)
  })
}

</script>

<template>
  <h1>{{ msg }}</h1>

  <div class="card">
    <button type="button" @click="request">Request to server</button>
  </div>
</template>

