// EN/ZH language toggle. Default = EN. State persisted in localStorage.
(function() {
  const KEY = 'heart_lang';
  const root = document.documentElement;
  function set(lang) {
    root.setAttribute('data-lang', lang);
    try { localStorage.setItem(KEY, lang); } catch(e) {}
    document.querySelectorAll('.lang-toggle button').forEach(b => {
      b.classList.toggle('active', b.dataset.lang === lang);
    });
  }
  // Apply saved (default EN) before paint
  const saved = (() => { try { return localStorage.getItem(KEY); } catch(e) { return null; } })();
  set(saved === 'zh' ? 'zh' : 'en');
  // Wire buttons after DOM ready
  window.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.lang-toggle button').forEach(b => {
      b.addEventListener('click', () => set(b.dataset.lang));
    });
    // Mark initial state again (in case nav rendered late)
    set(root.getAttribute('data-lang'));
  });
  // Expose for inline callers
  window.HEART_LANG = { set, get: () => root.getAttribute('data-lang') || 'en' };
})();
