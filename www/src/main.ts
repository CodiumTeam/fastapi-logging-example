import * as Sentry from "@sentry/vue";
import { BrowserTracing } from "@sentry/tracing";

import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

const app = createApp(App);

Sentry.init({
  app,
  dsn: import.meta.env.VITE_PUBLIC_SENTRY_DSN,
  integrations: [
    new BrowserTracing({
      tracePropagationTargets: ["my-site-url.com", /^\//],
    }),
  ],
  tracesSampleRate: 1.0,
});

app.mount('#app')