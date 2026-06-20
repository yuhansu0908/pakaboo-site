#!/usr/bin/env python3
"""
帕咔布托嬰中心 — 零依賴靜態網站產生器（CMS 層）。
讀取 Decap CMS 編輯的內容：
  content/news/*.md     → 最新消息列表 news.html + 各篇文章 news/<slug>.html
  content/events/*.md   → 活動・講座 events.html（即將舉行 / 已結束）
  content/gallery.yml   → 注入「園區生活 → 環境實景」照片
同時把兩個導覽項目（最新消息、活動）注入既有 5 頁，輸出整包到 ./build/。

執行：python3 build.py     （需 pyyaml）
"""
import os, re, shutil, html, datetime, urllib.parse
import yaml

ROOT = os.path.dirname(os.path.abspath(__file__))     # .../Pakaboo Website/cms
SITE = os.path.dirname(ROOT)                           # .../Pakaboo Website  (index.html, assets/)
OUT  = os.path.join(ROOT, "build")
TODAY = datetime.date.today()

def esc(s): return html.escape(str(s) if s is not None else "", quote=False)

ARROW = '<svg class="ca" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# ---------- content loaders ----------
def load_md(folder):
    items = []
    d = os.path.join(ROOT, "content", folder)
    if not os.path.isdir(d): return items
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md"): continue
        raw = open(os.path.join(d, fn), encoding="utf-8").read()
        m = re.match(r"^---\n(.*?)\n---\n?(.*)$", raw, re.S)
        if not m: continue
        meta = yaml.safe_load(m.group(1)) or {}
        meta["body"] = m.group(2).strip()
        meta["slug"] = os.path.splitext(fn)[0]
        items.append(meta)
    return items

def to_date(v):
    if isinstance(v, datetime.datetime): return v.date()
    if isinstance(v, datetime.date): return v
    try: return datetime.date.fromisoformat(str(v)[:10])
    except Exception: return datetime.date(1970,1,1)

def load_gallery():
    f = os.path.join(ROOT, "content", "gallery.yml")
    if not os.path.exists(f): return []
    data = yaml.safe_load(open(f, encoding="utf-8").read()) or {}
    return data.get("photos") or []

# ---------- shared shell ----------
def nav(active, root=""):
    def hl(name, page, label):
        cur = ' style="color:var(--accent)"' if active==name else ''
        return f'<li><a href="{root}{page}"{cur} class="nav-hl">{label}</a></li>' if name=="contact" \
               else f'<li><a href="{root}{page}"{cur}>{label}</a></li>'
    return f'''<header id="hdr">
  <div class="wrap nav">
    <a href="{root}index.html" class="brand" aria-label="帕咔布托嬰中心"><img src="{root}assets/logo.png" alt="帕咔布托嬰中心 PaKaBoo Nursery"></a>
    <ul class="menu" id="menu">
      <li>
        <button class="mtrig">關於{ARROW}</button>
        <div class="sub">
          <a href="{root}about.html">關於帕咔布</a>
          <a href="{root}about.html#story">品牌故事</a>
          <a href="{root}about.html#voice">我想對您說</a>
          <a href="{root}about.html#attach">分離焦慮</a>
          <a href="{root}about.html#letter">給家長的一封信</a>
        </div>
      </li>
      <li>
        <button class="mtrig">課程{ARROW}</button>
        <div class="sub">
          <a href="{root}courses.html#sensory">感官課程 · 英國</a>
          <a href="{root}courses.html#music">音樂教育 · 美國</a>
          <a href="{root}courses.html#ot">專業領航 · OT</a>
          <a href="{root}courses.html#golden">黃金三角</a>
        </div>
      </li>
      <li>
        <button class="mtrig">園區生活{ARROW}</button>
        <div class="sub">
          <a href="{root}life.html#day">一日作息</a>
          <a href="{root}life.html#gallery">環境實景</a>
          <a href="{root}life.html#menu">當月菜單</a>
        </div>
      </li>
      <li>
        <button class="mtrig"{' style="color:var(--accent)"' if active in ("news","events") else ''}>最新動態{ARROW}</button>
        <div class="sub">
          <a href="{root}news.html">最新消息</a>
          <a href="{root}events.html">活動・講座</a>
        </div>
      </li>
      <li><a href="{root}contact.html" class="nav-hl">聯絡我們</a></li>
    </ul>
    <button class="burger" id="burger" aria-label="選單"><span></span><span></span><span></span></button>
  </div>
</header>'''

def footer(root=""):
    return f'''<footer>
  <div class="wrap">
    <img class="flogo" src="{root}assets/logo.png" alt="帕咔布托嬰中心">
    <div class="fmenu">
      <a href="{root}index.html">首頁</a>
      <a href="{root}about.html">關於</a>
      <a href="{root}courses.html">課程</a>
      <a href="{root}life.html">園區生活</a>
      <a href="{root}news.html">最新消息</a>
      <a href="{root}events.html">活動・講座</a>
      <a href="{root}contact.html">聯絡我們</a>
    </div>
    <div class="fsocial" aria-label="社群連結">
      <a href="https://www.instagram.com/pakaboodaycarecenter/" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.3" cy="6.7" r="1.1" fill="currentColor" stroke="none"/></svg></a>
      <a href="https://www.facebook.com/profile.php?id=61588390091838" target="_blank" rel="noopener" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12.06C22 6.5 17.52 2 12 2S2 6.5 2 12.06c0 5 3.66 9.15 8.44 9.94v-7.03H7.9v-2.9h2.54V9.85c0-2.52 1.5-3.91 3.78-3.91 1.1 0 2.24.2 2.24.2v2.47h-1.26c-1.24 0-1.63.78-1.63 1.57v1.88h2.78l-.44 2.9h-2.34V22c4.78-.79 8.44-4.94 8.44-9.94z"/></svg></a>
      <a href="https://line.me/R/ti/p/@284vivvj" target="_blank" rel="noopener" aria-label="LINE"><svg viewBox="0 0 24 24"><rect x="2" y="2.5" width="20" height="19" rx="5.5" fill="currentColor"/><text x="12" y="14.9" text-anchor="middle" font-size="6.4" font-weight="800" font-family="Arial, sans-serif" style="fill:var(--badgefg,#6E4F33)">LINE</text></svg></a>
    </div>
    <div class="fdiv"></div>
    <div class="fnote">
      <p>帕咔布托嬰中心　PaKaBoo Nursery　·　Since May 2026　·　以愛為本，以幼為先</p>
      <p>台中市西屯區福雅路 128 巷 19 號　·　<a href="tel:0424616698">04-2461-6698</a>　·　官方 LINE @284vivvj</p>
      <p class="fcopy">© 2026 PaKaBoo Nursery. All Rights Reserved.</p>
      <p class="fcopy">※ 立案字號、團體保險與政府補助等資訊將依正式立案文件補充公告。</p>
    </div>
  </div>
</footer>'''

def page(title, desc, body, active, root=""):
    return f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;500;600;700&family=Noto+Sans+TC:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/site.css">
</head>
<body>{nav(active, root)}
{body}
{footer(root)}
<script src="{root}assets/site.js"></script>
</body>
</html>'''

def md_to_html(body):
    out = []
    for p in (body or "").split("\n\n"):
        p = p.strip()
        if not p: continue
        t = esc(p).replace(chr(10), "<br>")
        t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
        out.append(f'<p>{t}</p>')
    return "\n".join(out)

def img_src(v, root=""):
    v = str(v or "")
    if not v: return v
    if v.startswith("http"): return v
    # URL-encode spaces/special chars in the path so any filename works (keep slashes)
    if v.startswith("/"): return urllib.parse.quote(v, safe="/")
    return urllib.parse.quote(root + v, safe="/")

# ---------- NEWS ----------
def order_news(news):
    o = sorted(news, key=lambda n: to_date(n.get("date")), reverse=True)
    return sorted(o, key=lambda n: 0 if n.get("pinned") else 1)

def news_card(n, root=""):
    cover = f'<div class="ph"><img src="{esc(img_src(n.get("cover"), root))}" alt=""></div>' if n.get("cover") else ''
    pin = '<span class="pin">置頂</span>' if n.get("pinned") else ''
    return f'''      <a class="ncard reveal" href="{root}news/{esc(n["slug"])}.html">
        {cover}
        <div class="tx"><span class="ndate">{esc(to_date(n.get("date")).isoformat())} {pin}</span><h3>{esc(n["title"])}</h3><p>{esc(n.get("summary",""))}</p></div>
      </a>'''

def build_news(news):
    cards = [news_card(n) for n in order_news(news)]
    empty = '<p class="lead center" style="margin:0 auto">目前尚無消息，敬請期待。</p>' if not cards else ''
    body = f'''<section class="phero" data-spark="14"><div class="inner">
  <span class="chap">News</span><h1>最新消息<span class="en">PaKaBoo News</span></h1>
  </div></section>
<section class="sec"><div class="wrap">
  <div class="newsgrid">
{chr(10).join(cards)}
  </div>{empty}
</div></section>'''
    return page("最新消息｜帕咔布托嬰中心 PaKaBoo Nursery", "帕咔布托嬰中心最新消息與動態。", body, "news")

def build_article(n):
    cover = f'<div class="art-cover"><img src="{esc(img_src(n.get("cover"),"../"))}" alt=""></div>' if n.get("cover") else ''
    body = f'''<section class="phero" data-spark="12"><div class="inner">
  <span class="chap">News · {esc(to_date(n.get("date")).isoformat())}</span>
  <h1>{esc(n["title"])}</h1></div></section>
<section class="sec"><div class="wrap" style="max-width:760px">
  {cover}
  <article class="article">
    {md_to_html(n.get("body","")) or ('<p>'+esc(n.get("summary",""))+'</p>')}
  </article>
  <p style="margin-top:34px"><a class="btn-link" href="../news.html">← 返回最新消息</a></p>
</div></section>'''
    return page(f'{n["title"]}｜帕咔布托嬰中心', n.get("summary",""), body, "news", root="../")

# ---------- EVENTS ----------
TYPE_LABEL = {"activity":"活動", "talk":"講座", "other":"活動"}
def event_card(e):
    d = to_date(e.get("date"))
    typ = TYPE_LABEL.get(e.get("type","activity"), "活動")
    su = e.get("signup_url")
    if su:
        link = f'<a class="btn line" href="{esc(su)}" target="_blank" rel="noopener">我要報名</a>'
    else:
        link = f'<a class="btn line" href="https://line.me/R/ti/p/@284vivvj" target="_blank" rel="noopener">LINE 詢問報名</a>'
    summ = f'<p class="esum">{esc(e.get("summary",""))}</p>' if e.get("summary") else ''
    body = f'<div class="ebody">{md_to_html(e.get("body",""))}</div>' if e.get("body") else ''
    cover = e.get("cover")
    meta_parts = [x for x in [e.get("time"), e.get("location")] if x]
    if cover:
        meta_parts = [d.isoformat()] + meta_parts
        left = f'<a class="ecover" href="{esc(img_src(cover))}" target="_blank" rel="noopener"><img src="{esc(img_src(cover))}" alt="{esc(e["title"])} 活動海報"></a>'
        rowcls = "eventrow has-cover reveal"
    else:
        left = f'<div class="edate"><span class="d">{d.day:02d}</span><span class="m">{d.year} · {d.month:02d}月</span></div>'
        rowcls = "eventrow reveal"
    meta = " · ".join(meta_parts)
    return f'''      <div class="{rowcls}">
        {left}
        <div class="einfo">
          <span class="etype">{esc(typ)}</span>
          <h3>{esc(e["title"])}</h3>
          <p class="emeta">{esc(meta)}</p>
          {summ}
          {body}
          <div class="eact">{link}</div>
        </div>
      </div>'''

def build_events(events):
    up = sorted([e for e in events if to_date(e.get("date"))>=TODAY], key=lambda e: to_date(e.get("date")))
    pa = sorted([e for e in events if to_date(e.get("date"))< TODAY], key=lambda e: to_date(e.get("date")), reverse=True)
    def block(title, en, xs, empty):
        rows = "\n".join(event_card(e) for e in xs) if xs else f'      <p class="lead" style="margin:0">{empty}</p>'
        return f'''  <div class="ev-block">
    <div class="sec-head"><span class="chap">{en}</span><h2 class="t serif">{title}</h2></div>
    <div class="events">
{rows}
    </div>
  </div>'''
    body = f'''<section class="phero" data-spark="14"><div class="inner">
  <span class="chap">Events</span><h1>活動・講座<span class="en">Events &amp; Talks</span></h1>
  <p>假日寶貝探索趣、親子講座與各式活動。歡迎報名參加。</p></div></section>
<section class="sec"><div class="wrap">
{block("即將舉行", "Upcoming", up, "目前沒有即將舉行的活動，敬請期待。")}
  <div style="height:46px"></div>
{block("已結束", "Past", pa, "尚無已結束的活動。")}
</div></section>'''
    return page("活動・講座｜帕咔布托嬰中心 PaKaBoo Nursery", "帕咔布托嬰中心的活動與講座行事曆。", body, "events")

# ---------- inject into static pages ----------
def inject_nav(src):
    """加入『最新消息 / 活動』兩個選單項目到既有頁面（注入到聯絡我們之前）。"""
    target = '      <li><a href="contact.html" class="nav-hl">聯絡我們</a></li>'
    extra = ('      <li><a href="news.html">最新消息</a></li>\n'
             '      <li><a href="events.html">活動・讲座</a></li>\n').replace("讲","講")
    if target in src and "news.html" not in src.split('<div class="fmenu"')[0]:
        src = src.replace(target, extra + target, 1)
    # footer menu: add 最新消息/活動 before 聯絡我們
    ftar = '      <a href="contact.html">聯絡我們</a>'
    fext = '      <a href="news.html">最新消息</a>\n      <a href="events.html">活動・講座</a>\n'
    if ftar in src and 'href="news.html">最新消息' not in src.split('<div class="fmenu"')[-1].split('</div>')[0]:
        src = src.replace(ftar, fext + ftar, 1)
    return src

def inject_gallery(src, photos):
    if not photos: return src
    tiles = []
    for p in photos:
        img = img_src(p.get("image"))
        cap = p.get("caption","")
        caphtml = f'<figcaption>{esc(cap)}</figcaption>' if cap else ''
        tiles.append(f'      <figure class="gtile photo"><img src="{esc(img)}" alt="{esc(cap)}">{caphtml}</figure>')
    block = '<div class="gallery reveal d2">\n' + "\n".join(tiles) + '\n    </div>'
    return re.sub(r'<!--CMS:GALLERY-->.*?<!--/CMS:GALLERY-->',
                  '<!--CMS:GALLERY-->\n    ' + block + '\n    <!--/CMS:GALLERY-->',
                  src, flags=re.S)

def inject_latest_news(src, news):
    latest = order_news(news)[:3]
    if latest:
        inner = '<div class="newsgrid home3">\n' + "\n".join(news_card(n) for n in latest) + '\n    </div>'
    else:
        inner = '<p class="lead center" style="margin:24px auto 0">目前尚無消息，敬請期待。</p>'
    return re.sub(r'<!--CMS:LATESTNEWS-->.*?<!--/CMS:LATESTNEWS-->',
                  '<!--CMS:LATESTNEWS-->\n    ' + inner + '\n    <!--/CMS:LATESTNEWS-->',
                  src, flags=re.S)

# ---------- main ----------
def main():
    news = load_md("news")
    events = load_md("events")
    photos = load_gallery()

    os.makedirs(os.path.join(OUT, "news"), exist_ok=True)
    # assets (+ uploads) and admin
    shutil.copytree(os.path.join(SITE, "assets"), os.path.join(OUT, "assets"), dirs_exist_ok=True)
    shutil.copytree(os.path.join(ROOT, "admin"), os.path.join(OUT, "admin"), dirs_exist_ok=True)

    # generated pages
    open(os.path.join(OUT,"news.html"),"w",encoding="utf-8").write(build_news(news))
    open(os.path.join(OUT,"events.html"),"w",encoding="utf-8").write(build_events(events))
    for n in news:
        open(os.path.join(OUT,"news",n["slug"]+".html"),"w",encoding="utf-8").write(build_article(n))

    # static pages (nav/footer already include 最新消息/活動 from the base template)
    for fn in ["index.html","about.html","courses.html","life.html","contact.html"]:
        src = open(os.path.join(SITE, fn), encoding="utf-8").read()
        if fn == "index.html":
            src = inject_latest_news(src, news)
        if fn == "life.html":
            src = inject_gallery(src, photos)
        open(os.path.join(OUT, fn),"w",encoding="utf-8").write(src)

    print(f"Built → {OUT}")
    print(f"  news: {len(news)} 篇　events: {len(events)} 場（upcoming/past 依今天 {TODAY}）　gallery photos: {len(photos)}")
    print("  pages:", sorted(os.listdir(OUT)))

if __name__ == "__main__":
    main()
