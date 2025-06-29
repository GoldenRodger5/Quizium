const CACHE_NAME = 'flashcard-app-v2'; // Increment version for updates
const urlsToCache = [
  '/',
  '/static/manifest.json',
  '/static/icons/icon-192x192.png',
  '/static/icons/icon-512x512.png'
];

// Install event - cache resources and skip waiting
self.addEventListener('install', (event) => {
  console.log('🔄 Installing new service worker...');
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('📦 Caching app resources');
        return cache.addAll(urlsToCache);
      })
      .then(() => {
        // Skip waiting to activate the new service worker immediately
        return self.skipWaiting();
      })
      .catch((error) => {
        console.log('❌ Cache install failed:', error);
      })
  );
});

// Activate event - clean up old caches and claim clients
self.addEventListener('activate', (event) => {
  console.log('🚀 Activating new service worker...');
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all([
        // Delete old caches
        ...cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME) {
            console.log('🗑️ Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        }),
        // Take control of all clients immediately
        self.clients.claim()
      ]);
    }).then(() => {
      // Notify all clients about the update
      return self.clients.matchAll().then(clients => {
        clients.forEach(client => {
          client.postMessage({
            type: 'APP_UPDATED',
            message: 'App has been updated!'
          });
        });
      });
    })
  );
});

// Fetch event - network first strategy for API calls, cache first for static assets
self.addEventListener('fetch', (event) => {
  const url = new URL(event.request.url);
  
  // Network first for API calls and HTML pages
  if (event.request.method === 'POST' || 
      url.pathname.includes('/upload') || 
      url.pathname.includes('/generate-from-url') ||
      event.request.headers.get('accept')?.includes('text/html')) {
    event.respondWith(
      fetch(event.request)
        .then(response => {
          // If successful, update cache with new content
          if (response.ok && event.request.method === 'GET') {
            const responseClone = response.clone();
            caches.open(CACHE_NAME).then(cache => {
              cache.put(event.request, responseClone);
            });
          }
          return response;
        })
        .catch(() => {
          // Fallback to cache for GET requests
          if (event.request.method === 'GET') {
            return caches.match(event.request);
          }
          throw new Error('Network failed and no cache available');
        })
    );
  } else {
    // Cache first for static assets
    event.respondWith(
      caches.match(event.request)
        .then((response) => {
          return response || fetch(event.request);
        })
        .catch(() => {
          if (event.request.destination === 'document') {
            return caches.match('/');
          }
        })
    );
  }
});

// Background sync for offline actions
self.addEventListener('sync', (event) => {
  console.log('🔄 Background sync triggered:', event.tag);
  
  if (event.tag === 'background-sync') {
    event.waitUntil(
      // Perform background sync operations
      checkForUpdates()
    );
  }
});

// Check for app updates
async function checkForUpdates() {
  try {
    const response = await fetch('/', { cache: 'no-cache' });
    if (response.ok) {
      console.log('✅ App is up to date');
    }
  } catch (error) {
    console.log('❌ Update check failed:', error);
  }
}