<script setup lang="ts">
import * as Sentry from "@sentry/vue";
import {ref} from 'vue';

defineProps<{ msg: string }>()

function randomId() {
  return Math.floor(Math.random() * 100) + '-' + Date.now()
}

function randomUser() {
  const choices = [
      "Alice", "Bob", "Chris", "Dilan", "Edgar", "Frank",
  ];
  var index = Math.floor(Math.random() * choices.length);
  return choices[index];
}

const sessionId = ref(randomId());
const userName = ref(randomUser());

Sentry.setUser({
  name: userName.value,
  email: `${userName.value.toLowerCase()}@example.com`
});

Sentry.configureScope(scope => {
    scope.setTag("session_id", sessionId.value);
});

async function fetchWrapper(url: string) {
  const uniqueRequestId = randomId();

  Sentry.configureScope(scope => {
      scope.setTag("correlation_id", uniqueRequestId);
  });

  return fetch(url, {
    headers: {
      'X-User-ID': userName.value,
      'X-Session-ID': sessionId.value,
      'X-Correlation-ID': uniqueRequestId,
    },
  });
}

function request() {
  fetchWrapper("http://localhost:8000").then(
    response => response.json()
  ).then(json => {
    alert(json.message)
  })
}

function generateError() {
  fetchWrapper("http://localhost:8000/error").then(
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
  <div class="card">
    <button type="button" @click="generateError">Error</button>
  </div>
</template>

