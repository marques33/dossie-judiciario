#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { marked } = require('marked');

marked.setOptions({ gfm: true });

const BASE = __dirname;
const OUTPUT = path.join(BASE, 'estudo.html');

// --------------- Scan .md files ---------------
function scanFiles(dir, rel) {
  rel = rel || '';
  const results = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true })
    .sort(function(a, b) { return a.name.localeCompare(b.name); });
  for (var i = 0; i < entries.length; i++) {
    var entry = entries[i];
    if (entry.name.startsWith('.') || entry.name === 'node_modules') continue;
    var full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      var sub = rel ? rel + '/' + entry.name : entry.name;
      results.push.apply(results, scanFiles(full, sub));
    } else if (entry.name.endsWith('.md')) {
      var raw = fs.readFileSync(full, 'utf-8');
      var m = raw.match(/^#\s+(.+)/m);
      var title = m ? m[1].trim() : entry.name.replace('.md', '');
      results.push({
        id: (rel ? rel + '/' : '') + entry.name.replace(/\.md$/, ''),
        folder: rel || null,
        filename: entry.name,
        title: title,
        html: marked.parse(raw)
      });
    }
  }
  return results;
}

var files = scanFiles(BASE);
console.log('Found ' + files.length + ' markdown files');

// --------------- Helpers ---------------
function escH(s) {
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
function folderLabel(f) {
  return f.replace(/^\d+-/, '').replace(/-/g, ' ');
}

// --------------- Build sidebar HTML ---------------
var folderOrder = [];
var folderMap = {};
files.forEach(function(f) {
  var key = f.folder || '_root';
  if (!folderMap[key]) { folderMap[key] = []; folderOrder.push(key); }
  folderMap[key].push(f);
});

var sidebarHTML = '';
folderOrder.forEach(function(key) {
  var list = folderMap[key];
  if (key === '_root') {
    list.forEach(function(f) {
      sidebarHTML += '<div class="file-item" data-id="' + f.id + '">'
        + '<span class="file-title">' + escH(f.title) + '</span>'
        + '<span class="ann-badge" style="display:none"></span></div>\n';
    });
  } else {
    sidebarHTML += '<div class="folder-group"><div class="folder-header" onclick="toggleFolder(this)">'
      + '<span class="folder-icon">\u25B8</span> ' + escH(folderLabel(key))
      + '</div><div class="folder-files">\n';
    list.forEach(function(f) {
      sidebarHTML += '<div class="file-item" data-id="' + f.id + '">'
        + '<span class="file-title">' + escH(f.title) + '</span>'
        + '<span class="ann-badge" style="display:none"></span></div>\n';
    });
    sidebarHTML += '</div></div>\n';
  }
});

// --------------- Build folder filter checkboxes ---------------
var folderOptionsHTML = '';
folderOrder.forEach(function(key) {
  if (key === '_root') return;
  folderOptionsHTML += '<label class="filter-label"><input type="checkbox" class="folder-filter" value="'
    + escH(key) + '" checked> ' + escH(folderLabel(key)) + '</label>\n';
});

// --------------- Read CSS ---------------
var CSS = `
* { margin:0; padding:0; box-sizing:border-box; }
html { font-size:16px; }
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; color:#1a1a1a; background:#f0f2f5; height:100vh; display:flex; flex-direction:column; overflow:hidden; }

/* Toolbar */
#toolbar { display:flex; align-items:center; gap:12px; padding:8px 20px; background:#fff; border-bottom:1px solid #d0d7de; flex-shrink:0; z-index:100; }
#toolbar h1 { font-size:1rem; font-weight:700; color:#0d1117; white-space:nowrap; }
.toolbar-spacer { flex:1; }
.tb-btn { padding:6px 14px; border:1px solid #d0d7de; border-radius:6px; background:#fff; cursor:pointer; font-size:.8125rem; color:#24292f; transition:background .15s; }
.tb-btn:hover { background:#f3f4f6; }
.tb-btn.active { background:#0969da; color:#fff; border-color:#0969da; }
.tb-btn.active:hover { background:#0550ae; }

/* Layout */
#app { display:flex; flex:1; overflow:hidden; }

/* Sidebar */
#sidebar { width:280px; min-width:280px; background:#fff; border-right:1px solid #d0d7de; display:flex; flex-direction:column; overflow:hidden; }
#sidebar-header { padding:12px 16px; border-bottom:1px solid #d0d7de; }
#search { width:100%; padding:6px 10px; border:1px solid #d0d7de; border-radius:6px; font-size:.8125rem; outline:none; }
#search:focus { border-color:#0969da; box-shadow:0 0 0 3px rgba(9,105,218,.15); }
#progress-bar { margin-top:8px; font-size:.75rem; color:#57606a; }
#progress-fill { height:4px; background:#0969da; border-radius:2px; transition:width .3s; }
#progress-track { height:4px; background:#e1e4e8; border-radius:2px; margin-top:4px; }
#file-tree { flex:1; overflow-y:auto; padding:8px 0; }
.folder-group { margin-bottom:2px; }
.folder-header { padding:6px 16px; font-size:.8125rem; font-weight:600; color:#57606a; cursor:pointer; display:flex; align-items:center; gap:6px; user-select:none; }
.folder-header:hover { background:#f6f8fa; }
.folder-icon { font-size:.625rem; transition:transform .2s; display:inline-block; }
.folder-group.collapsed .folder-icon { transform:rotate(0deg); }
.folder-group:not(.collapsed) .folder-icon { transform:rotate(90deg); }
.folder-group.collapsed .folder-files { display:none; }
.file-item { padding:5px 16px 5px 32px; font-size:.8125rem; cursor:pointer; display:flex; align-items:center; gap:6px; border-left:3px solid transparent; }
.file-item:hover { background:#f6f8fa; }
.file-item.active { background:#ddf4ff; border-left-color:#0969da; font-weight:600; }
.ann-badge { background:#0969da; color:#fff; font-size:.625rem; padding:1px 5px; border-radius:8px; font-weight:700; flex-shrink:0; }

/* Main content */
#main { flex:1; overflow-y:auto; background:#fff; }
#main-content { max-width:860px; margin:0 auto; padding:32px 40px 80px; line-height:1.75; }
#main-content h1 { font-size:1.75rem; font-weight:700; color:#0d1117; margin:0 0 16px; padding-bottom:8px; border-bottom:1px solid #d8dee4; }
#main-content h2 { font-size:1.375rem; font-weight:600; color:#0d1117; margin:28px 0 12px; }
#main-content h3 { font-size:1.125rem; font-weight:600; color:#24292f; margin:24px 0 8px; }
#main-content h4 { font-size:1rem; font-weight:600; color:#24292f; margin:20px 0 8px; }
#main-content p { margin:0 0 16px; }
#main-content ul, #main-content ol { margin:0 0 16px; padding-left:2em; }
#main-content li { margin:4px 0; }
#main-content li > ul, #main-content li > ol { margin:4px 0 4px; }
#main-content strong { font-weight:700; color:#0d1117; }
#main-content blockquote { border-left:4px solid #d0d7de; padding:8px 16px; margin:0 0 16px; color:#57606a; background:#f6f8fa; border-radius:0 6px 6px 0; }
#main-content table { width:100%; border-collapse:collapse; margin:0 0 16px; font-size:.875rem; }
#main-content th { background:#f6f8fa; font-weight:600; text-align:left; padding:8px 12px; border:1px solid #d0d7de; }
#main-content td { padding:8px 12px; border:1px solid #d0d7de; vertical-align:top; }
#main-content tr:hover td { background:#f6f8fa; }
#main-content code { background:#eff1f3; padding:2px 6px; border-radius:4px; font-size:.875em; font-family:"SFMono-Regular",Consolas,"Liberation Mono",Menlo,monospace; }
#main-content pre { background:#f6f8fa; padding:16px; border-radius:6px; overflow-x:auto; margin:0 0 16px; border:1px solid #d0d7de; }
#main-content pre code { background:none; padding:0; font-size:.8125rem; }
#main-content hr { border:none; border-top:1px solid #d8dee4; margin:24px 0; }
#main-content details { margin:0 0 16px; border:1px solid #d0d7de; border-radius:6px; padding:8px 12px; }
#main-content summary { cursor:pointer; font-weight:600; }
#main-content a { color:#0969da; text-decoration:none; }
#main-content a:hover { text-decoration:underline; }

/* Highlights */
mark.hl { border-radius:2px; cursor:pointer; position:relative; }
mark.hl-yellow { background:rgba(255,235,59,.45); }
mark.hl-green { background:rgba(76,175,80,.35); }
mark.hl-blue { background:rgba(66,165,245,.35); }
mark.hl-pink { background:rgba(236,64,122,.3); }
mark.hl.has-comment::after { content:"\\1F4AC"; font-size:.625rem; position:absolute; top:-8px; right:-6px; }

/* Highlight popup */
#hl-popup { position:fixed; display:none; background:#fff; border:1px solid #d0d7de; border-radius:8px; padding:6px; box-shadow:0 4px 12px rgba(0,0,0,.15); z-index:200; gap:4px; }
#hl-popup.visible { display:flex; }
.hl-color-btn { width:28px; height:28px; border:2px solid transparent; border-radius:50%; cursor:pointer; transition:transform .1s; }
.hl-color-btn:hover { transform:scale(1.2); }
.hl-color-btn[data-color="yellow"] { background:#ffe033; }
.hl-color-btn[data-color="green"] { background:#4caf50; }
.hl-color-btn[data-color="blue"] { background:#42a5f5; }
.hl-color-btn[data-color="pink"] { background:#ec407a; }

/* Highlight edit popup */
#hl-edit { position:fixed; display:none; background:#fff; border:1px solid #d0d7de; border-radius:8px; padding:12px; box-shadow:0 4px 12px rgba(0,0,0,.15); z-index:200; width:280px; }
#hl-edit.visible { display:block; }
#hl-edit textarea { width:100%; height:60px; border:1px solid #d0d7de; border-radius:6px; padding:6px 8px; font-size:.8125rem; resize:vertical; margin:8px 0; font-family:inherit; }
#hl-edit .hl-edit-colors { display:flex; gap:6px; margin-bottom:8px; }
#hl-edit .hl-edit-actions { display:flex; gap:6px; justify-content:flex-end; }
.small-btn { padding:4px 10px; border:1px solid #d0d7de; border-radius:6px; background:#fff; cursor:pointer; font-size:.75rem; }
.small-btn:hover { background:#f3f4f6; }
.small-btn.danger { color:#cf222e; border-color:#cf222e; }
.small-btn.danger:hover { background:#ffebe9; }
.small-btn.primary { background:#0969da; color:#fff; border-color:#0969da; }
.small-btn.primary:hover { background:#0550ae; }

/* Right panel */
#right-panel { width:320px; min-width:320px; background:#fff; border-left:1px solid #d0d7de; display:flex; flex-direction:column; overflow:hidden; }
#right-panel.hidden { display:none; }
#right-header { padding:12px 16px; border-bottom:1px solid #d0d7de; font-size:.875rem; font-weight:600; color:#0d1117; display:flex; align-items:center; justify-content:space-between; }
#right-header .close-btn { background:none; border:none; cursor:pointer; font-size:1.1rem; color:#57606a; }
#annotations-list { flex:1; overflow-y:auto; padding:8px; }
.ann-item { padding:8px 10px; border:1px solid #e1e4e8; border-radius:6px; margin-bottom:6px; font-size:.8125rem; cursor:pointer; }
.ann-item:hover { border-color:#0969da; }
.ann-item .ann-text { display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; margin-bottom:4px; }
.ann-item .ann-comment { color:#57606a; font-style:italic; font-size:.75rem; }
.ann-color-dot { display:inline-block; width:10px; height:10px; border-radius:50%; margin-right:6px; vertical-align:middle; }
.ann-color-dot.yellow { background:#ffe033; }
.ann-color-dot.green { background:#4caf50; }
.ann-color-dot.blue { background:#42a5f5; }
.ann-color-dot.pink { background:#ec407a; }
#note-section { border-top:1px solid #d0d7de; padding:12px; }
#note-section label { font-size:.8125rem; font-weight:600; color:#57606a; display:block; margin-bottom:6px; }
#note-area { width:100%; height:100px; border:1px solid #d0d7de; border-radius:6px; padding:8px; font-size:.8125rem; resize:vertical; font-family:inherit; }
#note-area:focus { border-color:#0969da; outline:none; box-shadow:0 0 0 3px rgba(9,105,218,.15); }

/* Review mode */
#review-container { display:none; flex:1; overflow:hidden; }
#review-container.visible { display:flex; }
#review-filters { width:240px; min-width:240px; background:#fff; border-right:1px solid #d0d7de; padding:16px; overflow-y:auto; }
#review-filters h3 { font-size:.875rem; font-weight:600; color:#0d1117; margin-bottom:8px; }
.filter-group { margin-bottom:16px; }
.filter-group h4 { font-size:.8125rem; font-weight:600; color:#57606a; margin-bottom:6px; }
.filter-label { display:block; font-size:.8125rem; padding:3px 0; cursor:pointer; }
.filter-label input { margin-right:6px; }
#review-list { flex:1; overflow-y:auto; padding:24px; background:#f6f8fa; }
.review-item { background:#fff; border:1px solid #d0d7de; border-radius:8px; padding:16px; margin-bottom:12px; }
.review-item .review-source { font-size:.75rem; color:#57606a; margin-top:8px; }
.review-item .review-source a { color:#0969da; cursor:pointer; text-decoration:none; }
.review-item .review-source a:hover { text-decoration:underline; }
.review-item .review-text { font-size:.9375rem; line-height:1.6; border-left:4px solid #d0d7de; padding-left:12px; margin-bottom:6px; }
.review-item .review-text.yellow { border-left-color:#ffe033; }
.review-item .review-text.green { border-left-color:#4caf50; }
.review-item .review-text.blue { border-left-color:#42a5f5; }
.review-item .review-text.pink { border-left-color:#ec407a; }
.review-item .review-comment { font-size:.8125rem; color:#57606a; font-style:italic; margin-top:6px; padding-left:12px; }
.review-note-item { background:#fffbdd; }
.review-note-item .review-text { border-left-color:#d4a72c; }
.review-stats { font-size:.8125rem; color:#57606a; margin-bottom:16px; padding:8px 12px; background:#fff; border-radius:6px; border:1px solid #d0d7de; }

/* Empty states */
.empty-state { text-align:center; padding:40px 20px; color:#57606a; }
.empty-state .icon { font-size:2rem; margin-bottom:8px; }

/* Modal */
#modal-overlay { position:fixed; inset:0; background:rgba(0,0,0,.4); z-index:300; display:none; align-items:center; justify-content:center; }
#modal-overlay.visible { display:flex; }
#modal { background:#fff; border-radius:12px; padding:24px; max-width:500px; width:90%; max-height:80vh; overflow-y:auto; }
#modal h2 { font-size:1.125rem; margin-bottom:12px; }
#modal input[type=file] { margin:12px 0; }

/* Responsive */
@media(max-width:1100px) { #right-panel { display:none; } }
@media(max-width:768px) {
  #sidebar { position:fixed; left:-280px; top:0; bottom:0; z-index:150; transition:left .2s; }
  #sidebar.open { left:0; }
  #sidebar-overlay { position:fixed; inset:0; background:rgba(0,0,0,.3); z-index:140; display:none; }
  #sidebar-overlay.visible { display:block; }
  .menu-btn { display:inline-flex !important; }
  #main-content { padding:20px 16px 60px; }
}
@media(min-width:769px) { .menu-btn { display:none !important; } #sidebar-overlay { display:none !important; } }
`;

// --------------- Read app.js ---------------
var appJS = fs.readFileSync(path.join(BASE, 'app.js'), 'utf-8');

// --------------- Body HTML ---------------
var BODY = `
<div id="toolbar">
  <button class="tb-btn menu-btn" onclick="toggleSidebar()" title="Menu">&#9776;</button>
  <h1>Estudo &mdash; C&acirc;mara dos Deputados</h1>
  <div class="toolbar-spacer"></div>
  <button class="tb-btn" id="btn-panel" onclick="toggleRightPanel()" title="Painel de anota\u00e7\u00f5es">\u270D Anota\u00e7\u00f5es</button>
  <button class="tb-btn" id="btn-review" onclick="toggleReview()" title="Modo revis\u00e3o">\uD83D\uDCD6 Revis\u00e3o</button>
  <button class="tb-btn" onclick="exportData()" title="Exportar anota\u00e7\u00f5es">\u2B07 Exportar</button>
  <button class="tb-btn" onclick="importData()" title="Importar anota\u00e7\u00f5es">\u2B06 Importar</button>
</div>
<div id="app">
  <div id="sidebar-overlay" onclick="toggleSidebar()"></div>
  <nav id="sidebar">
    <div id="sidebar-header">
      <input type="text" id="search" placeholder="Buscar arquivo..." oninput="filterFiles()">
      <div id="progress-bar"><span id="progress-text"></span><div id="progress-track"><div id="progress-fill" style="width:0%"></div></div></div>
    </div>
    <div id="file-tree">${sidebarHTML}</div>
  </nav>
  <main id="main"><div id="main-content"></div></main>
  <aside id="right-panel" class="hidden">
    <div id="right-header"><span>Anota\u00e7\u00f5es</span><button class="close-btn" onclick="toggleRightPanel()">&times;</button></div>
    <div id="annotations-list"></div>
    <div id="note-section">
      <label for="note-area">Nota livre</label>
      <textarea id="note-area" placeholder="Escreva notas sobre este arquivo..." oninput="saveNote()"></textarea>
    </div>
  </aside>
  <div id="review-container">
    <div id="review-filters">
      <h3>Filtros</h3>
      <div class="filter-group"><h4>Cor</h4>
        <label class="filter-label"><input type="checkbox" class="color-filter" value="yellow" checked> Amarelo</label>
        <label class="filter-label"><input type="checkbox" class="color-filter" value="green" checked> Verde</label>
        <label class="filter-label"><input type="checkbox" class="color-filter" value="blue" checked> Azul</label>
        <label class="filter-label"><input type="checkbox" class="color-filter" value="pink" checked> Rosa</label>
      </div>
      <div class="filter-group"><h4>Pasta</h4>
        <label class="filter-label"><input type="checkbox" id="folder-all" checked onchange="toggleAllFolders(this.checked)"> Todas</label>
        ${folderOptionsHTML}
      </div>
      <div class="filter-group"><label class="filter-label"><input type="checkbox" id="show-notes" checked> Incluir notas livres</label></div>
    </div>
    <div id="review-list"></div>
  </div>
</div>
<div id="hl-popup">
  <button class="hl-color-btn" data-color="yellow" title="Amarelo"></button>
  <button class="hl-color-btn" data-color="green" title="Verde"></button>
  <button class="hl-color-btn" data-color="blue" title="Azul"></button>
  <button class="hl-color-btn" data-color="pink" title="Rosa"></button>
</div>
<div id="hl-edit"></div>
<div id="modal-overlay" onclick="closeModal()"><div id="modal" onclick="event.stopPropagation()"></div></div>
`;

// --------------- Assemble HTML ---------------
var html = '<!DOCTYPE html>\n<html lang="pt-BR">\n<head>\n'
  + '<meta charset="UTF-8">\n'
  + '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
  + '<title>Estudo \u2014 C\u00e2mara dos Deputados</title>\n'
  + '<style>\n' + CSS + '\n</style>\n'
  + '</head>\n<body>\n'
  + BODY + '\n'
  + '<script>\nvar FILES = ' + JSON.stringify(files).replace(/<\//g, '<\\/') + ';\n'
  + appJS + '\n'
  + '<\/script>\n</body>\n</html>';

fs.writeFileSync(OUTPUT, html, 'utf-8');
console.log('Generated: estudo.html (' + (html.length / 1024).toFixed(1) + ' KB)');
