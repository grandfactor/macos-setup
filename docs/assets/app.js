/* app.js — theme toggle, mobile nav, TOC highlight, copy buttons, light syntax colouring, client-side search. No deps. */
(function () {
  'use strict';
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));

  /* ---------- theme ---------- */
  const root = document.documentElement;
  const themeBtn = $('#themeBtn');
  const order = ['auto', 'light', 'dark'];
  function currentTheme() { return root.getAttribute('data-theme') || 'auto'; }
  function applyTheme(t) {
    if (t === 'auto') root.removeAttribute('data-theme'); else root.setAttribute('data-theme', t);
    try { t === 'auto' ? localStorage.removeItem('theme') : localStorage.setItem('theme', t); } catch (e) {}
    if (themeBtn) themeBtn.textContent = t === 'light' ? '☀' : t === 'dark' ? '☾' : '◐';
  }
  if (themeBtn) {
    applyTheme(currentTheme());
    themeBtn.addEventListener('click', () => applyTheme(order[(order.indexOf(currentTheme()) + 1) % order.length]));
  }

  /* ---------- mobile sidebar ---------- */
  const menuBtn = $('#menuBtn'), sidebar = $('#sidebar');
  if (menuBtn && sidebar) {
    menuBtn.addEventListener('click', () => {
      const open = sidebar.classList.toggle('open');
      menuBtn.setAttribute('aria-expanded', String(open));
    });
    document.addEventListener('click', (e) => {
      if (sidebar.classList.contains('open') && !sidebar.contains(e.target) && !menuBtn.contains(e.target)) {
        sidebar.classList.remove('open'); menuBtn.setAttribute('aria-expanded', 'false');
      }
    });
    // scroll active nav item into view
    const active = $('.sidebar li.active');
    if (active) active.scrollIntoView({ block: 'center' });
  }

  /* ---------- TOC scroll-spy ---------- */
  const tocLinks = $$('.toc a');
  if (tocLinks.length && 'IntersectionObserver' in window) {
    const map = new Map();
    tocLinks.forEach(a => { const el = document.getElementById(decodeURIComponent(a.hash.slice(1))); if (el) map.set(el, a); });
    let current = null;
    const io = new IntersectionObserver((entries) => {
      entries.forEach(en => { if (en.isIntersecting) { if (current) current.classList.remove('active'); current = map.get(en.target); if (current) current.classList.add('active'); } });
    }, { rootMargin: '-72px 0px -70% 0px', threshold: 0 });
    map.forEach((_, el) => io.observe(el));
  }

  /* ---------- copy buttons ---------- */
  $$('.codeblock .copy').forEach(btn => {
    btn.addEventListener('click', async () => {
      const code = btn.parentElement.querySelector('code');
      let text = code.innerText;
      // strip leading "$ " prompts when copying shell snippets
      if (/language-(sh|bash|zsh|shell|console)/.test(code.className)) {
        text = text.split('\n').map(l => l.replace(/^\$ /, '')).join('\n');
      }
      try { await navigator.clipboard.writeText(text); btn.textContent = 'Copied'; btn.classList.add('done'); }
      catch (e) { btn.textContent = 'Failed'; }
      setTimeout(() => { btn.textContent = 'Copy'; btn.classList.remove('done'); }, 1600);
    });
  });

  /* ---------- tiny syntax highlighter (shell/toml/json/yaml/lua/etc.) ---------- */
  const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const KW = /\b(if|then|else|elif|fi|for|in|do|done|while|case|esac|function|return|export|local|source|alias|set|unset|eval|exec|echo|exit|sudo|brew|git|mise|uv|npm|pnpm|docker|container|defaults|xcode-select|softwareupdate|chsh|ssh|ssh-keygen|curl|mkdir|cd|ls|cat|touch|chmod|chown|ln|rm|cp|mv|tmutil|diskutil|xattr|spctl|launchctl|pmset|killall|open|true|false|null|let|const|var|import|from|require|def|class|end|fn|pub|use|mod)\b/g;
  function hl(code) {
    const lang = (code.className.match(/language-([\w-]+)/) || [])[1] || '';
    if (!lang || /^(text|txt|output|plain|diff)$/.test(lang)) return;
    const src = code.textContent;
    const out = [];
    let i = 0;
    const re = /(#[^\n]*|\/\/[^\n]*|--[^\n]*|"(?:[^"\\\n]|\\.)*"|'(?:[^'\\\n]|\\.)*'|\$\{?[A-Za-z_][\w]*\}?|--?[A-Za-z][\w-]*|\b\d+(?:\.\d+)?\b)/g;
    let m;
    while ((m = re.exec(src))) {
      out.push(esc(src.slice(i, m.index)).replace(KW, '<span class="tok-k">$1</span>'));
      const t = m[0];
      let cls = 'tok-v';
      if (t[0] === '#' || t.startsWith('//') || t.startsWith('--') && /^--\s|^--$/.test(t)) cls = 'tok-c';
      else if (t[0] === '"' || t[0] === "'") cls = 'tok-s';
      else if (t[0] === '$') cls = 'tok-v';
      else if (t[0] === '-') cls = 'tok-p';
      else cls = 'tok-n';
      // toml/yaml/ini comments only at line start or after whitespace
      if (cls === 'tok-c' && t[0] === '#' && /language-(lua|json|js|ts|swift|rust|go|c|cpp)/.test(code.className)) cls = 'tok-p';
      out.push('<span class="' + cls + '">' + esc(t) + '</span>');
      i = m.index + t.length;
    }
    out.push(esc(src.slice(i)).replace(KW, '<span class="tok-k">$1</span>'));
    code.innerHTML = out.join('');
  }
  $$('.codeblock code').forEach(hl);

  /* ---------- search ---------- */
  const modal = $('#searchModal'), input = $('#searchInput'), results = $('#searchResults'), searchBtn = $('#searchBtn');
  let index = null, sel = -1, loading = null;
  function loadIndex() {
    if (index) return Promise.resolve(index);
    if (!loading) loading = fetch('search.json').then(r => r.json()).then(d => (index = d)).catch(() => (index = []));
    return loading;
  }
  function openSearch() { if (!modal) return; modal.hidden = false; input.value = ''; results.innerHTML = ''; sel = -1; loadIndex(); setTimeout(() => input.focus(), 10); }
  function closeSearch() { if (modal) modal.hidden = true; }
  if (searchBtn) searchBtn.addEventListener('click', openSearch);
  if (modal) modal.addEventListener('click', (e) => { if (e.target === modal) closeSearch(); });
  document.addEventListener('keydown', (e) => {
    const typing = /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName);
    if ((e.key === '/' && !typing) || ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k')) { e.preventDefault(); openSearch(); }
    else if (e.key === 'Escape' && modal && !modal.hidden) closeSearch();
  });
  function tokens(q) { return q.toLowerCase().split(/\s+/).filter(Boolean); }
  function score(entry, toks) {
    const t = (entry.t || '').toLowerCase(), c = entry.c.toLowerCase(), b = entry.b.toLowerCase();
    let s = 0;
    for (const tok of toks) {
      if (t.includes(tok)) s += 12; else if (c.includes(tok)) s += 6;
      const idx = b.indexOf(tok);
      if (idx >= 0) s += 3 + Math.min(4, (b.split(tok).length - 1)); else if (!t.includes(tok) && !c.includes(tok)) return 0;
    }
    return s;
  }
  function highlight(text, toks) {
    let h = esc(text);
    toks.forEach(tok => { h = h.replace(new RegExp('(' + tok.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi'), '<mark>$1</mark>'); });
    return h;
  }
  function snippet(b, toks) {
    const low = b.toLowerCase();
    let pos = -1;
    for (const tok of toks) { const i = low.indexOf(tok); if (i >= 0 && (pos < 0 || i < pos)) pos = i; }
    if (pos < 0) return b.slice(0, 160);
    const start = Math.max(0, pos - 60);
    return (start > 0 ? '…' : '') + b.slice(start, start + 200) + (start + 200 < b.length ? '…' : '');
  }
  function render(q) {
    const toks = tokens(q);
    if (!toks.length) { results.innerHTML = ''; return; }
    const scored = index.map(e => [score(e, toks), e]).filter(x => x[0] > 0).sort((a, b) => b[0] - a[0]).slice(0, 25);
    if (!scored.length) { results.innerHTML = '<li class="search-empty">No matches. Try a different word.</li>'; return; }
    results.innerHTML = scored.map(([, e]) =>
      '<li><a href="' + e.u + '"><div class="r-ch">' + esc(e.n ? e.n + ' · ' : '') + esc(e.c) + '</div>' +
      (e.t ? '<div class="r-title">' + highlight(e.t, toks) + '</div>' : '') +
      '<div class="r-body">' + highlight(snippet(e.b, toks), toks) + '</div></a></li>').join('');
    sel = -1;
  }
  if (input) {
    input.addEventListener('input', () => loadIndex().then(() => render(input.value)));
    input.addEventListener('keydown', (e) => {
      const items = $$('li', results);
      if (e.key === 'ArrowDown') { e.preventDefault(); sel = Math.min(items.length - 1, sel + 1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); sel = Math.max(0, sel - 1); }
      else if (e.key === 'Enter') { const a = (items[sel] || items[0]) && (items[sel] || items[0]).querySelector('a'); if (a) location.href = a.href; return; }
      else return;
      items.forEach((li, i) => li.classList.toggle('sel', i === sel));
      if (items[sel]) items[sel].scrollIntoView({ block: 'nearest' });
    });
  }

  /* ---------- external links get ↗ ---------- */
  $$('.prose a[target="_blank"]').forEach(a => { if (!a.querySelector('img') && !a.classList.contains('card')) a.insertAdjacentHTML('beforeend', '<span aria-hidden="true" style="font-size:.75em;opacity:.6"> ↗</span>'); });
})();
