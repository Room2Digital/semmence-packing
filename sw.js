/* The app moved. Unregister, bin the old caches, and let the pointer page
   through — otherwise a phone with this installed keeps serving the packing
   app from cache and never sees that it has gone. */
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => {
  e.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.map(k => caches.delete(k)));
    await self.clients.claim();
    await self.registration.unregister();
    const cs = await self.clients.matchAll({type: 'window'});
    cs.forEach(c => c.navigate(c.url));
  })());
});
