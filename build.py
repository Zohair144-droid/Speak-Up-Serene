#!/usr/bin/env python3
"""Generates index.html (students) and council/index.html from one template."""

APP_URL = "https://script.google.com/macros/s/AKfycbz6Lda5iH9Ry-ffO895_J3mQSvv6Qps6ypzGgIpHIPdcKmD-RkPx4VDydBZ4FVygSJlcw/exec"

TPL = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{TITLE}</title>

<!-- =======================================================================
     THE ONLY LINE YOU EVER NEED TO CHANGE.
     If the Google Apps Script link changes, paste the new one here,
     and in the other index.html too.
     ======================================================================= -->
<script>
  var APP_URL = "{APP_URL}";
  var PAGE = "{PAGE}";
</script>

<link rel="manifest" href="manifest.webmanifest">
<meta name="theme-color" content="{THEME}">
<link rel="icon" href="icon-192.png">
<link rel="apple-touch-icon" href="icon-192.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="{TITLE}">
<meta name="mobile-web-app-capable" content="yes">
{ROBOTS}
<style>
  :root {{
    --bg: {BG}; --card: #ffffff; --ink: {INK}; --muted: {MUTED};
    --line: {LINE}; --go: {GO}; --goink: {GOINK}; --accent: {THEME};
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --bg: {BGD}; --card: {CARDD}; --ink: {INKD}; --muted: {MUTEDD}; --line: {LINED}; }}
  }}
  * {{ box-sizing: border-box; }}
  [hidden] {{ display: none !important; }}
  html, body {{ margin: 0; height: 100%; background: var(--bg);
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif; }}
  #app {{ display: block; border: 0; width: 100%; height: 100%; }}

  #load {{ position: fixed; inset: 0; display: grid; place-items: center; align-content: center;
    gap: 16px; color: var(--muted); text-align: center; padding: 24px; }}
  #load img {{ width: 84px; height: 84px; border-radius: 21px; }}
  #load p {{ margin: 0; font-size: .95rem; }}
  #load a {{ color: inherit; }}

  /* ---- creator credit ---- */
  #credit {{ position: fixed; right: 10px; z-index: 25; pointer-events: none;
    bottom: calc(8px + env(safe-area-inset-bottom, 0px));
    padding: 3px 10px; border-radius: 999px; font-size: 11px; line-height: 1.4;
    background: var(--card); color: var(--muted); border: 1px solid var(--line);
    opacity: .9; box-shadow: 0 2px 8px rgba(0,0,0,.12); }}
  body:has(#bar.on) #credit {{ bottom: calc(112px + env(safe-area-inset-bottom, 0px)); }}

  /* ---- always-visible install bar ---- */
  #bar {{ position: fixed; left: 0; right: 0; bottom: 0; z-index: 20;
    display: none; align-items: center; gap: 12px;
    padding: 11px 14px calc(11px + env(safe-area-inset-bottom, 0px));
    background: var(--card); color: var(--ink);
    border-top: 1px solid var(--line); box-shadow: 0 -6px 20px rgba(0,0,0,.16); }}
  #bar.on {{ display: flex; }}
  #bar .ico {{ width: 40px; height: 40px; border-radius: 10px; flex: none; }}
  #bar .t {{ flex: 1; min-width: 0; font-size: .82rem; line-height: 1.3; color: var(--muted); }}
  #bar .t b {{ display: block; font-size: .95rem; color: var(--ink); }}
  .go {{ flex: none; border: 0; border-radius: 999px; padding: 10px 20px; font: inherit;
    font-weight: 700; background: var(--go); color: var(--goink); cursor: pointer; }}

  /* ---- steps sheet ---- */
  #back {{ position: fixed; inset: 0; z-index: 30; background: rgba(8,10,20,.6); display: none; }}
  #back.on {{ display: block; }}
  #sheet {{ position: fixed; left: 0; right: 0; bottom: 0; z-index: 31; display: none;
    max-width: 560px; margin: 0 auto; background: var(--card); color: var(--ink);
    border-radius: 20px 20px 0 0; max-height: 92vh; overflow: auto;
    padding: 20px 20px calc(20px + env(safe-area-inset-bottom, 0px));
    box-shadow: 0 -10px 40px rgba(0,0,0,.3); }}
  #sheet.on {{ display: block; }}
  #sheet h2 {{ margin: 0; font-size: 1.15rem; }}
  .hd {{ display: flex; align-items: center; justify-content: space-between; gap: 12px; }}
  .x {{ border: 0; background: none; color: var(--muted); font-size: 1.6rem;
    line-height: 1; cursor: pointer; padding: 2px 6px; }}
  .lead {{ display: flex; align-items: center; gap: 14px; margin: 16px 0; }}
  .lead img {{ width: 56px; height: 56px; border-radius: 14px; flex: none; }}
  .lead p {{ margin: 0; font-size: .9rem; color: var(--muted); }}
  .tabs {{ display: flex; gap: 8px; margin-bottom: 16px; }}
  .tabs button {{ flex: 1; border: 1px solid var(--line); background: var(--bg); color: var(--ink);
    border-radius: 10px; padding: 9px 10px; font: inherit; font-weight: 600; cursor: pointer; }}
  .tabs button[aria-pressed="true"] {{ background: var(--go); color: var(--goink); border-color: var(--go); }}
  ol.steps {{ list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 14px; }}
  ol.steps li {{ display: flex; gap: 13px; align-items: center; font-size: 1rem; line-height: 1.45; }}
  ol.steps .n {{ width: 32px; height: 32px; border-radius: 50%; flex: none; display: grid;
    place-items: center; background: var(--go); color: var(--goink); font-weight: 700; font-size: .95rem; }}
  ol.steps svg {{ width: 21px; height: 21px; vertical-align: -5px; margin: 0 2px; padding: 2px;
    border: 1px solid var(--line); border-radius: 6px; box-sizing: content-box; }}
  #native {{ display: none; margin: 0 0 16px; width: 100%; padding: 14px; font-size: 1.05rem; }}
  #native.on {{ display: block; }}
  .note {{ margin: 16px 0 0; font-size: .82rem; color: var(--muted); }}
</style>
</head>
<body>

<div id="load">
  <img src="icon-192.png" alt="">
  <p>{LOADING}</p>
  <p id="slow" hidden><a id="direct" href="#">Taking too long? Tap here to open it directly.</a></p>
</div>

<iframe id="app" title="{TITLE}" allow="clipboard-write" hidden></iframe>
<div id="credit">Created by Zohair Khalid</div>

<div id="bar">
  <img class="ico" src="icon-192.png" alt="">
  <p class="t"><b>Add to home screen</b>Open {TITLE} in one tap, like an app.</p>
  <button class="go" id="open" type="button">Add</button>
</div>

<div id="back"></div>
<div id="sheet" role="dialog" aria-modal="true" aria-labelledby="st">
  <div class="hd"><h2 id="st">Add to your home screen</h2>
    <button class="x" id="close" type="button" aria-label="Close">&times;</button></div>
  <div class="lead"><img src="icon-192.png" alt="">
    <p>This icon appears next to your other apps and opens <b>{TITLE}</b> in one tap.</p></div>

  <button class="go" id="native" type="button">Install now</button>

  <div class="tabs" role="group" aria-label="Choose your phone">
    <button type="button" data-os="android" aria-pressed="true">Android</button>
    <button type="button" data-os="iphone" aria-pressed="false">iPhone</button>
    <button type="button" data-os="laptop" aria-pressed="false">Laptop</button>
  </div>

  <ol class="steps" data-for="android">
    <li><span class="n">1</span><span>In <b>Chrome</b>, tap the menu
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/></svg>
      at the top right.</span></li>
    <li><span class="n">2</span><span>Tap <b>Add to Home screen</b>.</span></li>
    <li><span class="n">3</span><span>Tap <b>Install</b>, then <b>Install</b> again. Done.</span></li>
  </ol>

  <ol class="steps" data-for="iphone" hidden>
    <li><span class="n">1</span><span>Open this page in <b>Safari</b>. Only Safari can do this on iPhone.</span></li>
    <li><span class="n">2</span><span>Tap <b>Share</b>
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 15V3M8 7l4-4 4 4"/><path d="M7 11H6a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-6a2 2 0 0 0-2-2h-1"/></svg>
      at the bottom of the screen.</span></li>
    <li><span class="n">3</span><span>Scroll down, tap <b>Add to Home Screen</b>, then <b>Add</b>. Done.</span></li>
  </ol>

  <ol class="steps" data-for="laptop" hidden>
    <li><span class="n">1</span><span>In <b>Chrome</b>, click the menu
      <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/></svg>
      at the top right.</span></li>
    <li><span class="n">2</span><span>Click <b>Cast, save and share</b>, then <b>Install page as app…</b></span></li>
    <li><span class="n">3</span><span>Click <b>Install</b>. Done.</span></li>
  </ol>

  <p class="note">Once it is added, this bar disappears by itself.</p>
</div>

<script>
(function () {{
  var $ = function (id) {{ return document.getElementById(id); }};
  var url = APP_URL + (PAGE === 'council' ? '?page=council' : '');

  /* ---- load the suggestion box ---- */
  var f = $('app'), load = $('load');
  $('direct').href = url;
  f.addEventListener('load', function () {{ f.hidden = false; load.style.display = 'none'; }});
  f.src = url;
  setTimeout(function () {{ if (f.hidden) $('slow').hidden = false; }}, 6000);

  /* ---- install bar: ALWAYS shown unless already installed ---- */
  var standalone = (navigator.standalone === true) ||
      (window.matchMedia && matchMedia('(display-mode: standalone)').matches);
  var ua = navigator.userAgent || '';
  var isIOS = /iPhone|iPad|iPod/i.test(ua) ||
      (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  var isPhone = isIOS || /Android/i.test(ua);
  var deferred = null;

  if (!standalone) $('bar').classList.add('on');

  function setOS(os) {{
    var t = document.querySelectorAll('.tabs button');
    for (var i = 0; i < t.length; i++) {{
      t[i].setAttribute('aria-pressed', String(t[i].getAttribute('data-os') === os));
    }}
    var l = document.querySelectorAll('ol.steps');
    for (var j = 0; j < l.length; j++) {{
      l[j].hidden = l[j].getAttribute('data-for') !== os;
    }}
  }}
  setOS(isIOS ? 'iphone' : (isPhone ? 'android' : 'laptop'));
  document.querySelector('.tabs').addEventListener('click', function (e) {{
    var b = e.target.closest('button'); if (b) setOS(b.getAttribute('data-os'));
  }});

  function open_() {{ $('back').classList.add('on'); $('sheet').classList.add('on');
    document.body.style.overflow = 'hidden'; $('close').focus(); }}
  function close_() {{ $('back').classList.remove('on'); $('sheet').classList.remove('on');
    document.body.style.overflow = ''; }}
  $('open').addEventListener('click', open_);
  $('close').addEventListener('click', close_);
  $('back').addEventListener('click', close_);
  document.addEventListener('keydown', function (e) {{
    if (e.key === 'Escape' && $('sheet').classList.contains('on')) close_();
  }});

  /* one-tap install where the browser allows it */
  window.addEventListener('beforeinstallprompt', function (e) {{
    e.preventDefault(); deferred = e; $('native').classList.add('on');
  }});
  $('native').addEventListener('click', function () {{
    if (!deferred) return;
    deferred.prompt();
    deferred.userChoice.then(function () {{ deferred = null;
      $('native').classList.remove('on'); close_(); }});
  }});
  window.addEventListener('appinstalled', function () {{
    $('bar').classList.remove('on'); close_();
  }});
}})();
</script>
</body>
</html>
"""

LIGHT = dict(BG="#fff6dc", INK="#111111", MUTED="#4a4a55", LINE="#e3e0d4",
             BGD="#15122b", CARDD="#231f3f", INKD="#f6f1e4", MUTEDD="#c9c4d8", LINED="#3a3460")
NAVY = dict(BG="#f8f9fb", INK="#18213a", MUTED="#5f6880", LINE="#e2e6ee",
            BGD="#0d1322", CARDD="#151d31", INKD="#e8ecf5", MUTEDD="#a0a9c0", LINED="#26304a")

student = dict(TITLE="Speak Up Serene", PAGE="student", THEME="#ffd23f",
               GO="#ffd23f", GOINK="#111111", ROBOTS="",
               LOADING="Opening Speak Up Serene…", APP_URL=APP_URL, **LIGHT)
council = dict(TITLE="Serene Council", PAGE="council", THEME="#1b2d55",
               GO="#1b2d55", GOINK="#ffffff",
               ROBOTS='<meta name="robots" content="noindex, nofollow">',
               LOADING="Opening the council dashboard…", APP_URL=APP_URL, **NAVY)

open("index.html", "w").write(TPL.format(**student))
open("council/index.html", "w").write(TPL.format(**council))
print("built index.html and council/index.html")
