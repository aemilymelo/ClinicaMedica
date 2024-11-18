const CACHE_NAME = 'meu-app-cache-v1';
const urlsToCache = [
  '/',
  '/static/css/styles.css',  // Substitua com o caminho real do seu CSS
  '/static/js/main.js',      // Substitua com o caminho real do seu JS
  '/static/icons/icon-192x192.png',
  '/static/icons/icon-512x512.png'
];

// Instalando o service worker
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(urlsToCache);
    })
  );
});

// Ativando o service worker
self.addEventListener('activate', (event) => {
  const cacheWhitelist = [CACHE_NAME];
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (!cacheWhitelist.includes(cacheName)) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// Interceptando requisições para servir conteúdo do cache
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      return cachedResponse || fetch(event.request);
    })
  );
});
