/* ========= State ========= */
var currentFileId = null;
var data = {};
var reviewMode = false;
var pendingSelection = null;

/* ========= Data management ========= */
function loadData() {
  try { var s = localStorage.getItem("estudo_data"); if (s) data = JSON.parse(s); } catch(e) { data = {}; }
}
function saveData() {
  localStorage.setItem("estudo_data", JSON.stringify(data));
}
function fd(id) {
  if (!data[id]) data[id] = { highlights: [], note: "", lastRead: null };
  return data[id];
}
function genId() { return Date.now().toString(36) + Math.random().toString(36).substr(2, 6); }
function esc(s) { var d = document.createElement("div"); d.textContent = s; return d.innerHTML; }

/* ========= Sidebar ========= */
function toggleFolder(el) {
  el.parentElement.classList.toggle("collapsed");
}
function filterFiles() {
  var q = document.getElementById("search").value.toLowerCase();
  document.querySelectorAll(".file-item").forEach(function(el) {
    var title = el.querySelector(".file-title").textContent.toLowerCase();
    el.style.display = title.indexOf(q) !== -1 ? "" : "none";
  });
  document.querySelectorAll(".folder-group").forEach(function(g) {
    var hasVisible = false;
    g.querySelectorAll(".file-item").forEach(function(fi) {
      if (fi.style.display !== "none") hasVisible = true;
    });
    g.style.display = hasVisible ? "" : "none";
    if (q && hasVisible) g.classList.remove("collapsed");
  });
}
function updateProgress() {
  var total = FILES.length;
  var read = 0;
  var annotated = 0;
  FILES.forEach(function(f) {
    var d = data[f.id];
    if (d && d.lastRead) read++;
    if (d && ((d.highlights && d.highlights.length > 0) || d.note)) annotated++;
  });
  document.getElementById("progress-text").textContent = read + "/" + total + " lidos, " + annotated + " anotados";
  document.getElementById("progress-fill").style.width = (read / total * 100) + "%";
}
function updateBadges() {
  document.querySelectorAll(".file-item").forEach(function(el) {
    var id = el.getAttribute("data-id");
    var d = data[id];
    var badge = el.querySelector(".ann-badge");
    if (!badge) return;
    if (d && d.highlights && d.highlights.length > 0) {
      badge.textContent = d.highlights.length;
      badge.style.display = "";
    } else {
      badge.style.display = "none";
    }
  });
}

/* ========= Navigation ========= */
function navigateTo(fileId) {
  var file = FILES.find(function(f) { return f.id === fileId; });
  if (!file) return;
  currentFileId = fileId;
  localStorage.setItem("estudo_lastFile", fileId);
  document.querySelectorAll(".file-item").forEach(function(el) {
    el.classList.toggle("active", el.getAttribute("data-id") === fileId);
  });
  renderContent();
  var d = fd(fileId);
  d.lastRead = new Date().toISOString();
  saveData();
  updateProgress();
  updateBadges();
  updateRightPanel();
  document.getElementById("main").scrollTop = 0;
  if (window.innerWidth < 769) {
    document.getElementById("sidebar").classList.remove("open");
    document.getElementById("sidebar-overlay").classList.remove("visible");
  }
}
function renderContent() {
  var file = FILES.find(function(f) { return f.id === currentFileId; });
  if (!file) return;
  var mc = document.getElementById("main-content");
  mc.innerHTML = file.html;
  restoreHighlights();
}

/* ========= Highlight restore ========= */
function getTextMap(container) {
  var walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT);
  var fullText = "";
  var nodes = [];
  while (walker.nextNode()) {
    nodes.push({ node: walker.currentNode, start: fullText.length });
    fullText += walker.currentNode.textContent;
  }
  return { fullText: fullText, nodes: nodes };
}
function restoreHighlights() {
  var d = fd(currentFileId);
  if (!d.highlights || !d.highlights.length) return;
  var mc = document.getElementById("main-content");
  var map = getTextMap(mc);
  var sorted = d.highlights.slice().map(function(h) {
    var search = h.text;
    var ctx = (h.contextBefore || "") + search + (h.contextAfter || "");
    var idx = map.fullText.indexOf(ctx);
    if (idx !== -1) { idx += (h.contextBefore || "").length; }
    else { idx = map.fullText.indexOf(search); }
    return { h: h, idx: idx };
  }).filter(function(x) { return x.idx !== -1; });
  sorted.sort(function(a, b) { return b.idx - a.idx; });
  sorted.forEach(function(item) {
    applyHighlightAtPosition(item.h, item.idx, map.nodes);
  });
}
function applyHighlightAtPosition(h, idx, nodes) {
  var startOff = idx;
  var endOff = idx + h.text.length;
  var startNode = null, startNodeOff = 0, endNode = null, endNodeOff = 0;
  for (var i = 0; i < nodes.length; i++) {
    var n = nodes[i];
    var nEnd = n.start + n.node.textContent.length;
    if (!startNode && startOff < nEnd) { startNode = n.node; startNodeOff = startOff - n.start; }
    if (!endNode && endOff <= nEnd) { endNode = n.node; endNodeOff = endOff - n.start; break; }
  }
  if (!startNode || !endNode) return;
  try {
    if (startNode === endNode) {
      var range = document.createRange();
      range.setStart(startNode, startNodeOff);
      range.setEnd(endNode, endNodeOff);
      var mark = makeMark(h);
      range.surroundContents(mark);
    } else {
      wrapMultiNode(startNode, startNodeOff, endNode, endNodeOff, h);
    }
  } catch(e) { console.warn("hl restore fail", h.id, e); }
}
function wrapMultiNode(sn, so, en, eo, h) {
  var range = document.createRange();
  range.setStart(sn, so);
  range.setEnd(en, eo);
  var container = range.commonAncestorContainer;
  var walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT);
  var textNodes = [];
  while (walker.nextNode()) {
    if (range.intersectsNode(walker.currentNode)) textNodes.push(walker.currentNode);
  }
  for (var i = textNodes.length - 1; i >= 0; i--) {
    var tn = textNodes[i];
    var ws = (tn === sn) ? so : 0;
    var we = (tn === en) ? eo : tn.textContent.length;
    if (ws === we) continue;
    if (ws === 0 && we === tn.textContent.length) {
      var m = makeMark(h);
      tn.parentNode.insertBefore(m, tn);
      m.appendChild(tn);
    } else {
      var txt = tn.textContent;
      var frag = document.createDocumentFragment();
      if (ws > 0) frag.appendChild(document.createTextNode(txt.substring(0, ws)));
      var m2 = makeMark(h);
      m2.textContent = txt.substring(ws, we);
      frag.appendChild(m2);
      if (we < txt.length) frag.appendChild(document.createTextNode(txt.substring(we)));
      tn.parentNode.replaceChild(frag, tn);
    }
  }
}
function makeMark(h) {
  var m = document.createElement("mark");
  m.className = "hl hl-" + h.color + (h.comment ? " has-comment" : "");
  m.setAttribute("data-hl-id", h.id);
  m.addEventListener("click", function(e) { e.stopPropagation(); showHlEdit(h.id, e); });
  return m;
}

/* ========= Selection & highlight creation ========= */
document.addEventListener("mouseup", function(e) {
  if (reviewMode) return;
  var popup = document.getElementById("hl-popup");
  if (popup.contains(e.target)) return;
  var sel = window.getSelection();
  if (!sel || sel.isCollapsed || !sel.toString().trim()) { popup.classList.remove("visible"); return; }
  var mc = document.getElementById("main-content");
  if (!mc || !mc.contains(sel.anchorNode) || !mc.contains(sel.focusNode)) { popup.classList.remove("visible"); return; }
  var text = sel.toString().trim();
  if (text.length < 2) return;
  var map = getTextMap(mc);
  var pos = map.fullText.indexOf(text);
  if (pos === -1) { pendingSelection = null; return; }
  var ctxBefore = pos > 0 ? map.fullText.substring(Math.max(0, pos - 30), pos) : "";
  var ctxAfter = map.fullText.substring(pos + text.length, Math.min(map.fullText.length, pos + text.length + 30));
  pendingSelection = { text: text, contextBefore: ctxBefore, contextAfter: ctxAfter };
  var rect = sel.getRangeAt(0).getBoundingClientRect();
  popup.style.left = Math.max(8, rect.left + rect.width / 2 - 70) + "px";
  popup.style.top = Math.max(8, rect.top - 44) + "px";
  popup.classList.add("visible");
});
document.querySelectorAll("#hl-popup .hl-color-btn").forEach(function(btn) {
  btn.addEventListener("click", function() {
    if (!pendingSelection) return;
    var color = btn.getAttribute("data-color");
    var h = {
      id: genId(),
      text: pendingSelection.text,
      contextBefore: pendingSelection.contextBefore,
      contextAfter: pendingSelection.contextAfter,
      color: color,
      comment: "",
      createdAt: new Date().toISOString()
    };
    fd(currentFileId).highlights.push(h);
    saveData();
    window.getSelection().removeAllRanges();
    document.getElementById("hl-popup").classList.remove("visible");
    pendingSelection = null;
    renderContent();
    updateRightPanel();
    updateBadges();
  });
});
document.addEventListener("mousedown", function(e) {
  var popup = document.getElementById("hl-popup");
  if (!popup.contains(e.target)) popup.classList.remove("visible");
  var edit = document.getElementById("hl-edit");
  if (!edit.contains(e.target) && !e.target.closest("mark.hl")) edit.classList.remove("visible");
});

/* ========= Highlight edit ========= */
function showHlEdit(hlId, e) {
  var d = fd(currentFileId);
  var h = d.highlights.find(function(x) { return x.id === hlId; });
  if (!h) return;
  var edit = document.getElementById("hl-edit");
  var colors = ["yellow","green","blue","pink"];
  var colorsHtml = "";
  colors.forEach(function(c) {
    colorsHtml += '<button class="hl-color-btn' + (c===h.color?" active":"") + '" data-color="' + c + '" style="width:24px;height:24px;" onclick="changeHlColor(\'' + hlId + '\',\'' + c + '\')"></button>';
  });
  var commentVal = (h.comment||"").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
  edit.innerHTML = '<div class="hl-edit-colors">' + colorsHtml + '</div>'
    + '<textarea id="hl-comment-input" placeholder="Adicionar coment\u00e1rio...">' + commentVal + '</textarea>'
    + '<div class="hl-edit-actions">'
    + '<button class="small-btn danger" onclick="removeHl(\'' + hlId + '\')">Remover</button>'
    + '<button class="small-btn primary" onclick="saveHlComment(\'' + hlId + '\')">Salvar</button>'
    + '</div>';
  var rect = e.target.getBoundingClientRect();
  edit.style.left = Math.min(rect.left, window.innerWidth - 300) + "px";
  edit.style.top = (rect.bottom + 6) + "px";
  edit.classList.add("visible");
}
function changeHlColor(hlId, color) {
  var d = fd(currentFileId);
  var h = d.highlights.find(function(x) { return x.id === hlId; });
  if (h) { h.color = color; saveData(); renderContent(); }
  document.getElementById("hl-edit").classList.remove("visible");
  updateRightPanel();
}
function saveHlComment(hlId) {
  var d = fd(currentFileId);
  var h = d.highlights.find(function(x) { return x.id === hlId; });
  if (h) {
    h.comment = document.getElementById("hl-comment-input").value;
    saveData();
    renderContent();
  }
  document.getElementById("hl-edit").classList.remove("visible");
  updateRightPanel();
}
function removeHl(hlId) {
  var d = fd(currentFileId);
  d.highlights = d.highlights.filter(function(x) { return x.id !== hlId; });
  saveData();
  renderContent();
  document.getElementById("hl-edit").classList.remove("visible");
  updateRightPanel();
  updateBadges();
}

/* ========= Right panel ========= */
function toggleRightPanel() {
  var rp = document.getElementById("right-panel");
  rp.classList.toggle("hidden");
  document.getElementById("btn-panel").classList.toggle("active", !rp.classList.contains("hidden"));
}
function updateRightPanel() {
  if (!currentFileId) return;
  var d = fd(currentFileId);
  var list = document.getElementById("annotations-list");
  if (!d.highlights || !d.highlights.length) {
    list.innerHTML = '<div class="empty-state"><div class="icon">\uD83D\uDCDD</div><p>Selecione texto para grifar</p></div>';
  } else {
    var html = "";
    d.highlights.forEach(function(h) {
      var shortText = h.text.length > 80 ? h.text.substring(0, 80) + "..." : h.text;
      html += '<div class="ann-item" onclick="scrollToHl(\'' + h.id + '\')">'
        + '<div class="ann-text"><span class="ann-color-dot ' + h.color + '"></span>' + esc(shortText) + '</div>';
      if (h.comment) html += '<div class="ann-comment">\uD83D\uDCAC ' + esc(h.comment) + '</div>';
      html += '</div>';
    });
    list.innerHTML = html;
  }
  document.getElementById("note-area").value = d.note || "";
}
function scrollToHl(hlId) {
  var mark = document.querySelector('mark[data-hl-id="' + hlId + '"]');
  if (mark) {
    mark.scrollIntoView({ behavior: "smooth", block: "center" });
    mark.style.outline = "2px solid #0969da";
    setTimeout(function() { mark.style.outline = ""; }, 1500);
  }
}

/* ========= Notes ========= */
function saveNote() {
  if (!currentFileId) return;
  fd(currentFileId).note = document.getElementById("note-area").value;
  saveData();
}

/* ========= Review mode ========= */
function toggleReview() {
  reviewMode = !reviewMode;
  document.getElementById("btn-review").classList.toggle("active", reviewMode);
  document.getElementById("main").style.display = reviewMode ? "none" : "";
  document.getElementById("right-panel").style.display = reviewMode ? "none" : "";
  document.getElementById("sidebar").style.display = reviewMode ? "none" : "";
  var rc = document.getElementById("review-container");
  rc.classList.toggle("visible", reviewMode);
  if (reviewMode) renderReview();
  document.querySelectorAll(".color-filter, .folder-filter, #show-notes").forEach(function(el) {
    el.onchange = renderReview;
  });
}
function toggleAllFolders(checked) {
  document.querySelectorAll(".folder-filter").forEach(function(cb) { cb.checked = checked; });
  renderReview();
}
function renderReview() {
  var colors = [];
  document.querySelectorAll(".color-filter:checked").forEach(function(cb) { colors.push(cb.value); });
  var folders = [];
  document.querySelectorAll(".folder-filter:checked").forEach(function(cb) { folders.push(cb.value); });
  var showNotes = document.getElementById("show-notes").checked;
  var items = [];
  FILES.forEach(function(file) {
    if (file.folder && folders.indexOf(file.folder) === -1) return;
    var d = data[file.id];
    if (!d) return;
    if (d.highlights) {
      d.highlights.forEach(function(h) {
        if (colors.indexOf(h.color) === -1) return;
        items.push({ type: "highlight", file: file, highlight: h });
      });
    }
    if (showNotes && d.note && d.note.trim()) {
      items.push({ type: "note", file: file, note: d.note });
    }
  });
  var list = document.getElementById("review-list");
  if (!items.length) {
    list.innerHTML = '<div class="empty-state"><div class="icon">\uD83D\uDCCB</div><p>Nenhuma anota\u00e7\u00e3o encontrada com os filtros atuais</p></div>';
    return;
  }
  var html = '<div class="review-stats">' + items.length + ' iten(s) encontrado(s)</div>';
  items.forEach(function(item) {
    if (item.type === "highlight") {
      var h = item.highlight;
      html += '<div class="review-item"><div class="review-text ' + h.color + '">' + esc(h.text) + '</div>';
      if (h.comment) html += '<div class="review-comment">\uD83D\uDCAC ' + esc(h.comment) + '</div>';
      html += '<div class="review-source"><a onclick="exitReviewAndGo(\'' + item.file.id + '\')">' + esc(item.file.title) + '</a></div></div>';
    } else {
      html += '<div class="review-item review-note-item"><div class="review-text">\uD83D\uDCDD ' + esc(item.note) + '</div>';
      html += '<div class="review-source"><a onclick="exitReviewAndGo(\'' + item.file.id + '\')">' + esc(item.file.title) + '</a></div></div>';
    }
  });
  list.innerHTML = html;
}
function exitReviewAndGo(fileId) {
  if (reviewMode) toggleReview();
  navigateTo(fileId);
}

/* ========= Export / Import ========= */
function exportData() {
  var json = JSON.stringify(data, null, 2);
  var blob = new Blob([json], { type: "application/json" });
  var url = URL.createObjectURL(blob);
  var a = document.createElement("a");
  a.href = url;
  a.download = "estudo-anotacoes-" + new Date().toISOString().slice(0,10) + ".json";
  a.click();
  URL.revokeObjectURL(url);
}
function importData() {
  var modal = document.getElementById("modal");
  modal.innerHTML = '<h2>Importar anota\u00e7\u00f5es</h2>'
    + '<p style="font-size:.875rem;color:#57606a;margin-bottom:12px">Selecione um arquivo JSON exportado anteriormente. As anota\u00e7\u00f5es ser\u00e3o mescladas com as existentes.</p>'
    + '<input type="file" id="import-file" accept=".json">'
    + '<div style="margin-top:12px;display:flex;gap:8px;justify-content:flex-end">'
    + '<button class="small-btn" onclick="closeModal()">Cancelar</button>'
    + '<button class="small-btn primary" onclick="doImport()">Importar</button>'
    + '</div>';
  document.getElementById("modal-overlay").classList.add("visible");
}
function doImport() {
  var input = document.getElementById("import-file");
  if (!input.files.length) return;
  var reader = new FileReader();
  reader.onload = function(e) {
    try {
      var imported = JSON.parse(e.target.result);
      Object.keys(imported).forEach(function(key) {
        if (!data[key]) { data[key] = imported[key]; return; }
        var existing = data[key].highlights || [];
        var existingIds = existing.map(function(h) { return h.id; });
        (imported[key].highlights || []).forEach(function(h) {
          if (existingIds.indexOf(h.id) === -1) existing.push(h);
        });
        data[key].highlights = existing;
        if (!data[key].note && imported[key].note) data[key].note = imported[key].note;
      });
      saveData();
      renderContent();
      updateRightPanel();
      updateBadges();
      updateProgress();
      closeModal();
      alert("Importa\u00e7\u00e3o conclu\u00edda!");
    } catch(err) {
      alert("Erro ao importar: " + err.message);
    }
  };
  reader.readAsText(input.files[0]);
}
function closeModal() {
  document.getElementById("modal-overlay").classList.remove("visible");
}

/* ========= Mobile sidebar ========= */
function toggleSidebar() {
  document.getElementById("sidebar").classList.toggle("open");
  document.getElementById("sidebar-overlay").classList.toggle("visible");
}

/* ========= File item click handlers ========= */
document.querySelectorAll(".file-item").forEach(function(el) {
  el.addEventListener("click", function() {
    navigateTo(el.getAttribute("data-id"));
  });
});

/* ========= Init ========= */
loadData();
updateBadges();
updateProgress();
var lastFile = localStorage.getItem("estudo_lastFile");
navigateTo(lastFile && FILES.find(function(f){return f.id===lastFile;}) ? lastFile : FILES[0].id);
