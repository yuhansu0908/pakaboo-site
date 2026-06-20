# -*- coding: utf-8 -*-
import os
HERE=os.path.dirname(os.path.abspath(__file__))

ARROW='<svg class="ca" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def NAV(active):
    def cls(p): return ' style="color:var(--accent)"' if p==active else ''
    return '''
<header id="hdr">
  <div class="wrap nav">
    <a href="index.html" class="brand" aria-label="帕咔布托嬰中心"><img src="assets/logo.png" alt="帕咔布托嬰中心 PaKaBoo Nursery"></a>
    <ul class="menu" id="menu">
      <li>
        <button class="mtrig">關於''' + ARROW + '''</button>
        <div class="sub">
          <a href="about.html">關於帕咔布</a>
          <a href="about.html#story">品牌故事</a>
          <a href="about.html#voice">我想對您說</a>
          <a href="about.html#attach">分離焦慮</a>
          <a href="about.html#letter">給家長的一封信</a>
        </div>
      </li>
      <li>
        <button class="mtrig">課程''' + ARROW + '''</button>
        <div class="sub">
          <a href="courses.html#sensory">感官課程 · 英國</a>
          <a href="courses.html#music">音樂教育 · 美國</a>
          <a href="courses.html#ot">專業領航 · OT</a>
          <a href="courses.html#golden">黃金三角</a>
        </div>
      </li>
      <li>
        <button class="mtrig">園區生活''' + ARROW + '''</button>
        <div class="sub">
          <a href="life.html#day">一日作息</a>
          <a href="life.html#gallery">環境實景</a>
          <a href="life.html#menu">當月菜單</a>
        </div>
      </li>
      <li>
        <button class="mtrig">最新動態''' + ARROW + '''</button>
        <div class="sub">
          <a href="news.html">最新消息</a>
          <a href="events.html">活動・講座</a>
        </div>
      </li>
      <li><a href="contact.html" class="nav-hl">聯絡我們</a></li>
    </ul>
    <button class="burger" id="burger" aria-label="選單"><span></span><span></span><span></span></button>
  </div>
</header>'''

FOOTER='''
<footer>
  <div class="wrap">
    <img class="flogo" src="assets/logo.png" alt="帕咔布托嬰中心">
    <div class="fmenu">
      <a href="index.html">首頁</a>
      <a href="about.html">關於</a>
      <a href="courses.html">課程</a>
      <a href="life.html">園區生活</a>
      <a href="news.html">最新消息</a>
      <a href="events.html">活動・講座</a>
      <a href="contact.html">聯絡我們</a>
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

def page(fn,title,desc,active,main):
    html='''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>''' + title + '''</title>
<meta name="description" content="''' + desc + '''">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;500;600;700&family=Noto+Sans+TC:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>''' + NAV(active) + main + FOOTER + '''
<script src="assets/site.js"></script>
</body>
</html>'''
    open(os.path.join(HERE,fn),'w').write(html)
    print('wrote',fn,len(html))

# ---------- INDEX ----------
index_main='''
<section class="hero" data-spark="26">
  <div class="inner">
    <img class="logo" src="assets/logo.png" alt="帕咔布托嬰中心 PaKaBoo Nursery">
    <div class="kick">PaKaBoo Nursery · Since May 2026</div>
    <h1 class="serif">笑出第一聲，爬出第一步<br>迎接每一個驚喜的<em>「帕咔布！」</em></h1>
    <p class="sub">台中西屯 0–2 歲專業托嬰中心。以愛為本、以幼為先，<br>結合英國感官、美國音樂與職能治療師入園守護。</p>
    <div class="cta-row">
      <a class="btn" href="contact.html">預約參觀</a>
      <a class="btn ghost" href="about.html">認識帕咔布</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap split">
    <div class="art reveal"><img src="assets/logo.png" alt="帕咔布小熊"></div>
    <div>
      <span class="chap reveal">Our Story</span>
      <h2 class="t serif reveal d1">名字，來自一聲「躲貓貓」</h2>
      <p class="body reveal d2">「帕咔布」的名字，來自寶寶最喜歡的遊戲 <b>Peekaboo</b>（躲貓貓）。當寶寶看到大人從小手後面探出笑臉的那一瞬間，那份驚喜、信任與安心，就是我們想給每一個孩子的感受。</p>
      <p class="reveal d3" style="margin-top:24px"><a class="btn-link" href="about.html">了解我們的理念與承諾 →</a></p>
    </div>
  </div>
</section>

<section class="sec tint" data-spark="12">
  <div class="wrap">
    <div class="sec-head center">
      <span class="chap reveal">Our Curriculum</span>
      <h2 class="t serif reveal d1">全人發展的三大課程<span class="en">感官 · 音樂 · 專業守護</span></h2>
    </div>
    <div class="fcards">
      <div class="fcard reveal d1">
        <div class="ph"><img src="assets/course_sensory.jpg" alt="英國感官課程"></div>
        <div class="tx"><span class="badge">英國 · 感官啟蒙</span><h4>Babies Music Sensory Together</h4><p>以高品質感官刺激，在大腦發展黃金期建立神經連結，讓孩子在驚奇探索中起飛。</p></div>
      </div>
      <div class="fcard reveal d2">
        <div class="ph"><img src="assets/course_music.jpg" alt="美國音樂教育"></div>
        <div class="tx"><span class="badge">美國 · 音樂教育</span><h4>Music Together 音樂系統</h4><p>節奏與律動同時刺激左右腦，促進語言爆發、強化感統，並穩定情緒、建立自信。</p></div>
      </div>
      <div class="fcard reveal d3">
        <div class="ph"><img src="assets/course_ot.jpg" alt="職能治療師入園觀察"></div>
        <div class="tx"><span class="badge">專業 · 領航守護</span><h4>職能治療師 (OT) 入園觀察</h4><p>建立專業觀察防護網，讓孩子在發展黃金期得到最完善的專業支持。</p></div>
      </div>
    </div>
    <div class="center" style="margin-top:40px"><a class="btn-link reveal" href="courses.html">看完整課程介紹 →</a></div>
  </div>
</section>

<section class="sec dark" data-spark="16">
  <div class="wrap center">
    <span class="chap reveal">The Golden Triangle</span>
    <h2 class="t serif reveal d1">全人發展的黃金三角<span class="en">三大核心，最穩固的成長基礎</span></h2>
    <div class="tri reveal d2" style="text-align:left;margin-top:30px">
      <div><b>神經連結 × 深度啟蒙</b><p>英國感官課程，以高品質刺激建立大腦高速連結，讓孩子在探索中起飛。</p></div>
      <div><b>情緒認知 × 能力激活</b><p>美國音樂律動，以歌謠與韻律強化語言與邏輯，提升智力潛能。</p></div>
      <div><b>專業守護 × 預防科學</b><p>職能治療師入園觀察，確保肢體、感官與社會能力穩定前進。</p></div>
    </div>
  </div>
</section>

<section class="sec tint" data-spark="12" id="latest">
  <div class="wrap">
    <div class="news-head reveal">
      <div><span class="chap">News</span><h2 class="t serif">最新消息</h2></div>
      <a class="btn-link" href="news.html">看全部消息 →</a>
    </div>
    <!--CMS:LATESTNEWS-->
    <p class="lead center" style="margin:24px auto 0">目前尚無消息，敬請期待。</p>
    <!--/CMS:LATESTNEWS-->
  </div>
</section>

<section class="sec" data-spark="12">
  <div class="wrap center">
    <span class="chap reveal">Visit Us</span>
    <h2 class="t serif reveal d1">帶寶貝來一場半日體驗</h2>
    <p class="body reveal d2" style="max-width:560px;margin:6px auto 26px">歡迎預約參觀，一起認識帕咔布的溫暖環境與課程。</p>
    <div class="reveal d3"><a class="btn" href="contact.html">預約參觀</a></div>
  </div>
</section>'''
page('index.html','帕咔布托嬰中心 PaKaBoo Nursery｜台中西屯 0–2 歲專業托嬰',
     '帕咔布托嬰中心 PaKaBoo Nursery，台中市西屯區 0–2 歲專業托嬰。以愛為本、以幼為先，結合英國感官課程、美國 Music Together 音樂教育與職能治療師入園觀察。',
     'home', index_main)

# ---------- ABOUT ----------
about_main='''
<section class="phero" data-spark="14">
  <div class="inner">
    <span class="chap">About PaKaBoo</span>
    <h1>關於帕咔布<span class="en">以愛為本 · 以幼為先</span></h1>
    <p>從一聲「躲貓貓」開始，我們想給每個孩子驚喜、信任與安心。</p>
  </div>
</section>

<section class="sec" id="story">
  <div class="wrap split">
    <div class="art reveal"><img src="assets/logo.png" alt="帕咔布小熊"></div>
    <div>
      <span class="chap reveal">Our Story</span>
      <h2 class="t serif reveal d1">品牌故事 — 來自 Peekaboo</h2>
      <p class="body reveal d2">「帕咔布」的名字，來自寶寶最喜歡的遊戲 <b>Peekaboo</b>（躲貓貓）。當寶寶看到大人從小手後面探出笑臉的那一瞬間，那份驚喜、信任與安心，就是我們想給每一個孩子的感受。</p>
      <p class="body reveal d3">每一次微笑、每一聲咿呀，都被細細珍惜；如同護理媽媽陪玩 Peekaboo 一樣，我們不斷以愛與互動陪伴孩子成長。帕咔布是寶寶的第一個小世界，也是家長最安心的溫暖後盾。</p>
    </div>
  </div>
</section>

<section class="sec tint" data-spark="12">
  <div class="wrap center">
    <span class="chap reveal">We Believe</span>
    <h2 class="t serif reveal d1">每個孩子，都是一個奇妙小宇宙<span class="en">以愛為本 · 以幼為先</span></h2>
    <blockquote class="reveal d2" style="max-width:680px;margin:18px auto 34px">每個孩子，都是正在展開的奇妙小宇宙，<br>需要被溫柔看見，也需要被細心等待。</blockquote>
    <div class="mcards reveal d3" style="text-align:left">
      <div class="mcard">
        <h4><svg class="ic" viewBox="0 0 24 24"><path d="M12 21s-7-4.5-9.5-9A5.5 5.5 0 0 1 12 6a5.5 5.5 0 0 1 9.5 6c-2.5 4.5-9.5 9-9.5 9z"/></svg>宗旨</h4>
        <p>秉持「以愛為本、以幼為先」之理念，提供安全、溫馨且充滿關懷的成長環境，讓每一位嬰幼兒在被尊重與理解中快樂學習、健康成長，並重視親師之間的溝通與合作。</p>
      </div>
      <div class="mcard">
        <h4><svg class="ic" viewBox="0 0 24 24"><path d="M12 22c4-3 7-6.5 7-11a7 7 0 0 0-14 0c0 4.5 3 8 7 11z"/><path d="M12 11V3"/></svg>設立目的</h4>
        <p>為 0–2 歲嬰幼兒提供安全、健康且充滿關懷的托育環境，協助家長在工作與家庭之間取得平衡，減輕育兒壓力，成為家庭最安心的支持後盾。</p>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="voice">
  <div class="wrap">
    <div class="sec-head center"><span class="chap reveal">Mom &amp; Dad, I want to tell you</span>
    <h2 class="t serif reveal d1">爸爸媽媽，我想對您說</h2></div>
    <div class="vcard reveal d2">
      <button class="varr" id="vPrev" aria-label="上一則"><svg class="ic" viewBox="0 0 24 24"><path d="M15 6l-6 6 6 6"/></svg></button>
      <div class="vstage"><div class="vinner" id="vInner"><div class="vnum serif" id="vNum">01</div><p class="vtext" id="vText"></p></div></div>
      <button class="varr" id="vNext" aria-label="下一則"><svg class="ic" viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"/></svg></button>
    </div>
    <div class="vcount reveal d3"><span id="vCur">01</span> / 10</div>
    <div class="vdots reveal d3" id="vDots"></div>
  </div>
</section>

<section class="sec tint" data-spark="12" id="attach">
  <div class="wrap">
    <div class="sec-head center"><span class="chap reveal">Secure Attachment</span>
    <h2 class="t serif reveal d1">幼兒分離焦慮的形成<span class="en">理解，是溫柔陪伴的開始</span></h2></div>
    <p class="lead reveal d2 center" style="margin:0 auto 30px">分離焦慮的成因，很大程度取決於孩子的外部環境與條件。為孩子創造良好、溫馨和諧的環境，是改善分離焦慮的先決條件。我們從三個面向理解它：</p>
    <div class="factors reveal d3">
      <div class="factor"><h5><b>一</b>環境的變化</h5><p>從熟悉的家，進入全新的團體環境，本身就是孩子需要時間適應的轉變。穩定、可預期的作息，能幫助孩子重新建立安全感。</p></div>
      <div class="factor"><h5><b>二</b>家長的因素</h5><p>過度代勞會影響孩子的自理與獨立；過度保護、限制同儕互動，會減少社會接觸。送托時若反覆擁抱、依依不捨，或以威嚇方式，都容易加重孩子的不安。家長的一言一行，都深深影響孩子的情緒與安全感。</p></div>
      <div class="factor"><h5><b>三</b>嬰幼兒的因素</h5><p>當孩子還無法自己穿脫衣物、用餐，日常中容易感到挫折；性格內向的孩子依附情緒較強。我們以耐心觀察與漸進引導，陪孩子一點一點長出自己的能力。</p></div>
    </div>
  </div>
</section>

<section class="sec" id="letter">
  <div class="wrap">
    <div class="sec-head center"><span class="chap reveal">A Letter to Parents</span>
    <h2 class="t serif reveal d1">給新入園家長的一封信</h2></div>
    <div class="letter reveal d2">
      <p>親愛的家長：</p>
      <p>誠摯邀請您的孩子進入帕咔布入托，並感謝您對我們的信任與支持。在寶貝入托的最初幾天，是他踏入對外界環境信任感的關鍵期；這段期間的經驗，將影響孩子未來對團體生活的安全感。透過爸媽的緊密配合，我們能共同幫助寶貝在充滿安全感的環境中，順利度過「適應期」。</p>
      <p>離開熟悉的照顧者，對孩子是一大挑戰，難免有焦躁或不安；而家長感到不捨與擔憂，也是非常正常的。為了協助寶貝輕鬆度過，以下幾件事，請與我們一起配合：</p>
      <div class="tips">
        <div class="tip"><span class="k">1</span><div><b>準時的接送</b>　給孩子可預期的盼望，是最安定的力量。</div></div>
        <div class="tip"><span class="k">2</span><div><b>溫柔而堅定的告別</b>　好好道別、明確地離開，短暫的不捨勝過拖延的不安，請避免不告而別。</div></div>
        <div class="tip"><span class="k">3</span><div><b>回家後的親密陪伴</b>　孩子適應新環境用了許多心力，回家後用心的陪伴有助穩定情緒。</div></div>
        <div class="tip"><span class="k">4</span><div><b>規律的作息與飲食</b>　在家維持一致的節奏，並用正向的話語陪孩子預演入園的美好。</div></div>
      </div>
      <p class="sign">— 執行長　Jocelyn Wu</p>
    </div>
  </div>
</section>'''
page('about.html','關於帕咔布｜品牌故事與理念 — PaKaBoo Nursery',
     '帕咔布托嬰中心的品牌故事、教育理念、給新入園家長的一封信與分離焦慮的溫柔陪伴。以愛為本、以幼為先。',
     'about', about_main)

# ---------- COURSES ----------
courses_main='''
<section class="phero" data-spark="14">
  <div class="inner">
    <span class="chap">Our Curriculum</span>
    <h1>課程介紹<span class="en">感官 · 音樂 · 專業守護</span></h1>
    <p>在寶寶大腦發展的黃金時期，給予最溫暖、最有力量的啟蒙。</p>
  </div>
</section>

<section class="sec" id="sensory">
  <div class="wrap course-row">
    <div class="cphoto reveal"><img src="assets/course_sensory.jpg" alt="英國 Babies Music Sensory Together 感官課程"><span class="cphoto-num">01</span></div>
    <div class="course-txt">
      <span class="chap reveal">Curriculum 01</span>
      <span class="badge reveal d1">英國 · 感官啟蒙</span>
      <h3 class="reveal d1">Babies Music<br>Sensory Together</h3>
      <p class="reveal d2">抓握柔軟的布料、聆聽清脆的鈴聲、觀察繽紛的色彩，讓神經元在快樂中突觸連結。奇幻開場、主題探索、親密連結，在寶寶大腦發展的黃金時期，給予最溫暖、最有力量的感官啟蒙。</p>
    </div>
  </div>
</section>

<section class="sec tint" id="music" data-spark="12">
  <div class="wrap course-row flip">
    <div class="cphoto reveal"><img src="assets/course_music.jpg" alt="美國 Music Together 音樂教室"><span class="cphoto-num">02</span></div>
    <div class="course-txt">
      <span class="chap reveal">Curriculum 02</span>
      <span class="badge reveal d1">美國 · 音樂教育</span>
      <h3 class="reveal d1">Music Together<br>音樂教育系統</h3>
      <p class="reveal d2">音樂，是給大腦最好的營養。透過節奏與律動同時刺激左右腦：<b>開發腦潛能</b>、<b>強化感統協調</b>、<b>促進語言爆發</b>、<b>穩定情緒</b>，建立孩子自信與健康的社交安全感。</p>
    </div>
  </div>
</section>

<section class="sec" id="ot">
  <div class="wrap course-row">
    <div class="cphoto reveal"><img src="assets/course_ot.jpg" alt="職能治療師 OT 入園觀察・感統教室"><span class="cphoto-num">03</span></div>
    <div class="course-txt">
      <span class="chap reveal">Curriculum 03</span>
      <span class="badge reveal d1">專業 · 領航守護</span>
      <h3 class="reveal d1">職能治療師 (OT)<br>入園觀察服務</h3>
      <p class="reveal d2">帕咔布正式導入職能治療師入園觀察。我們不只提供溫暖的照顧，更建立專業的觀察防護網，讓孩子在發展的黃金期，得到最完善的專業支持。</p>
    </div>
  </div>
</section>

<section class="sec dark" id="golden" data-spark="16">
  <div class="wrap center">
    <span class="chap reveal">The Golden Triangle</span>
    <h2 class="t serif reveal d1">全人發展的黃金三角<span class="en">三大核心，最穩固的成長基礎</span></h2>
    <div class="tri reveal d2" style="text-align:left;margin-top:30px">
      <div><b>神經連結 × 深度啟蒙</b><p>英國 Babies Music Sensory Together，以高品質感官刺激建立大腦高速連結，讓孩子在驚奇探索中起飛。</p></div>
      <div><b>情緒認知 × 能力激活</b><p>美國 Music Together 親子音樂律動，以歌謠與韻律強化語言與邏輯，科學證實有效提升智力潛能。</p></div>
      <div><b>專業守護 × 預防科學</b><p>職能治療師 (OT) 入園觀察，確保每位寶寶的肢體、感官與社會能力都在正軌穩定前進。</p></div>
    </div>
  </div>
</section>'''
page('courses.html','課程介紹｜感官・音樂・專業守護 — 帕咔布托嬰中心',
     '帕咔布三大課程：英國 Babies Music Sensory Together 感官啟蒙、美國 Music Together 音樂教育、職能治療師 (OT) 入園觀察，以及全人發展的黃金三角。',
     'courses', courses_main)

# ---------- LIFE ----------
life_main='''
<section class="phero" data-spark="14">
  <div class="inner">
    <span class="chap">A Day at PaKaBoo</span>
    <h1>園區生活<span class="en">作息 · 健康 · 安全 · 飲食</span></h1>
    <p>規律的節奏，是孩子最大的安全感。</p>
  </div>
</section>

<section class="sec" id="day">
  <div class="wrap">
    <div class="sec-head center"><span class="chap reveal">Daily Rhythm</span>
    <h2 class="t serif reveal d1">托嬰中心一日作息<span class="en">規律的節奏，是孩子最大的安全感</span></h2></div>
    <div class="sched reveal d2">
      <div class="row"><div class="tm">08:00–09:00</div><div class="ct"><b>晨間入園與檢查</b><span>量體溫、手口足檢查、更換尿布、家長交接</span></div></div>
      <div class="row"><div class="tm">09:00–10:00</div><div class="ct"><b>營養補給與小點</b><span>早點心、喝水、換尿布；月齡較小者彈性調整</span></div></div>
      <div class="row"><div class="tm">10:00–11:30</div><div class="ct"><b>適性發展活動</b><span>感官統合、大肌肉躍動、繪本欣賞或主題探索</span></div></div>
      <div class="row"><div class="tm">11:30–12:30</div><div class="ct"><b>午餐時間</b><span>練習生活自理、餐後清潔與刷牙</span></div></div>
      <div class="row"><div class="tm">12:30–15:00</div><div class="ct"><b>安穩午休時光</b><span>穩定情緒、培養良好午睡習慣</span></div></div>
      <div class="row"><div class="tm">15:00–16:00</div><div class="ct"><b>起床與下午點心</b><span>儀容整理、下午點心、故事閱讀</span></div></div>
      <div class="row"><div class="tm">16:00–17:30</div><div class="ct"><b>靜態活動與回顧</b><span>自由探索、家長接送、親師溝通當日狀況</span></div></div>
    </div>
  </div>
</section>

<section class="sec tint" data-spark="12">
  <div class="wrap">
    <div class="sec-head center"><span class="chap reveal">Care &amp; Wellbeing</span>
    <h2 class="t serif reveal d1">園區生活與安心守護<span class="en">飲食 · 健康 · 安全</span></h2></div>
    <div class="grid3 reveal d2">
      <div class="info">
        <div class="hd"><svg class="ic" viewBox="0 0 24 24"><path d="M12 21c5-3 8-7 8-11a5 5 0 0 0-8-4 5 5 0 0 0-8 4c0 4 3 8 8 11z"/></svg><h4>天然飲食規劃</h4></div>
        <ul><li>每月公告當月菜單，五週循環供餐</li><li>依月齡提供副食品與適齡餐點</li><li>當季新鮮食材，營養均衡把關</li><li>用餐同時練習生活自理能力</li></ul>
      </div>
      <div class="info">
        <div class="hd"><svg class="ic" viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg><h4>健康保健</h4></div>
        <ul><li>幼兒發燒 37.5℃ 以上請就醫並居家觀察</li><li>每日晨間量測體溫與手口足檢查</li><li>傳染病須痊癒後返園</li><li>定期環境清潔消毒，守護群體健康</li></ul>
      </div>
      <div class="info">
        <div class="hd"><svg class="ic" viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.5-7 8-7s8 3 8 7"/></svg><h4>收托對象與時間</h4></div>
        <ul><li>滿 2 個月至滿 2 歲（最晚就讀至滿 3 歲前一天）</li><li>每日服務：上午 8:00 – 下午 17:30</li><li>上半年 2/1–7/31、下半年 8/1–翌年 1/31</li><li>每學期前安排課程準備與消毒日</li></ul>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="gallery">
  <div class="wrap">
    <div class="sec-head center"><span class="chap reveal">Our Space</span>
    <h2 class="t serif reveal d1">園區實景<span class="en">像雲朵一樣柔軟 · 像家一樣溫暖</span></h2>
    <p class="lead reveal d2 center" style="margin:0 auto">以下為照片版位，可隨時替換成園區實拍照片。</p></div>
    <!--CMS:GALLERY-->
    <div class="gallery reveal d2">
      <div class="gtile"><svg class="ic" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="11" r="2"/><path d="M3 17l5-4 4 3 3-2 6 4"/></svg><span>溫暖入口</span><small>照片版位</small></div>
      <div class="gtile"><svg class="ic" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="11" r="2"/><path d="M3 17l5-4 4 3 3-2 6 4"/></svg><span>遊戲區</span><small>照片版位</small></div>
      <div class="gtile"><svg class="ic" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="11" r="2"/><path d="M3 17l5-4 4 3 3-2 6 4"/></svg><span>睡眠室</span><small>照片版位</small></div>
      <div class="gtile"><svg class="ic" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="11" r="2"/><path d="M3 17l5-4 4 3 3-2 6 4"/></svg><span>用餐區</span><small>照片版位</small></div>
      <div class="gtile"><svg class="ic" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="11" r="2"/><path d="M3 17l5-4 4 3 3-2 6 4"/></svg><span>感官教具</span><small>照片版位</small></div>
      <div class="gtile"><svg class="ic" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="11" r="2"/><path d="M3 17l5-4 4 3 3-2 6 4"/></svg><span>閱讀角</span><small>照片版位</small></div>
      <div class="gtile"><svg class="ic" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="11" r="2"/><path d="M3 17l5-4 4 3 3-2 6 4"/></svg><span>盥洗區</span><small>照片版位</small></div>
      <div class="gtile"><svg class="ic" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="11" r="2"/><path d="M3 17l5-4 4 3 3-2 6 4"/></svg><span>戶外活動</span><small>照片版位</small></div>
    </div>
    <!--/CMS:GALLERY-->
  </div>
</section>

<section class="sec tint" id="menu" data-spark="12">
  <div class="wrap">
    <div class="sec-head center"><span class="chap reveal">Monthly Menu</span>
    <h2 class="t serif reveal d1">菜單參考表<span class="en">分齡供餐 · 五週循環 · 當季新鮮</span></h2></div>
    <div class="menuwrap reveal d2"><img src="assets/menu.jpg" alt="帕咔布托嬰中心 五週循環營養菜單參考表"></div>
    <div class="menucap reveal d3">
      <span><b>分齡供餐</b>　6–8 個月 / 8–12 個月 / 12 個月以上</span>
      <span><b>午餐 + 午點</b>　當季新鮮食材，營養均衡</span>
      <span><b>每月更新</b>　實際菜色依當月公告為準</span>
    </div>
  </div>
</section>'''
page('life.html','園區生活｜一日作息・環境・菜單 — 帕咔布托嬰中心',
     '帕咔布托嬰中心的一日作息、天然飲食規劃、健康保健、收托對象與時間、園區實景與五週循環菜單參考表。',
     'life', life_main)

# ---------- CONTACT ----------
contact_main='''
<section class="phero" data-spark="16">
  <div class="inner">
    <span class="chap">Visit Us</span>
    <h1>聯絡我們 · 預約參觀<span class="en">PaKaBoo Nursery</span></h1>
    <p>歡迎帶寶貝來「半日體驗」，一起認識帕咔布的溫暖環境與課程。</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="cgrid reveal">
      <div class="cinfo">
        <p><svg class="ic" viewBox="0 0 24 24"><path d="M12 21s-7-5.5-7-11a7 7 0 0 1 14 0c0 5.5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg><span>台中市西屯區福雅路 128 巷 19 號</span></p>
        <p><svg class="ic" viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L17 13l4 1v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg><span>中心專線：<a href="tel:0424616698">04-2461-6698</a><br><small>請於上午 9:00 前或下午 4:30 後來電</small></span></p>
        <p><svg class="ic" viewBox="0 0 24 24"><path d="M21 11.5a8.38 8.38 0 0 1-8.5 8.5 8.5 8.5 0 0 1-3.8-.9L3 21l1.9-5.7A8.38 8.38 0 0 1 4 11.5 8.5 8.5 0 0 1 12.5 3 8.38 8.38 0 0 1 21 11.5z"/></svg><span>官方 LINE：<a href="https://line.me/R/ti/p/@284vivvj">@284vivvj</a></span></p>
        <p><svg class="ic" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg><span>信箱：<a href="mailto:pakaboodaycarecenter@gmail.com">pakaboodaycarecenter@gmail.com</a></span></p>
        <p style="margin-top:10px"><a href="https://line.me/R/ti/p/@284vivvj" class="btn line">加入 LINE 預約參觀</a></p>
      </div>
      <div class="map"><iframe loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=台中市西屯區福雅路128巷19號&output=embed"></iframe></div>
    </div>
    <div class="social reveal d2" aria-label="社群連結">
      <a href="https://www.instagram.com/pakaboodaycarecenter/" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.3" cy="6.7" r="1.1" fill="currentColor" stroke="none"/></svg></a>
      <a href="https://www.facebook.com/profile.php?id=61588390091838" target="_blank" rel="noopener" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12.06C22 6.5 17.52 2 12 2S2 6.5 2 12.06c0 5 3.66 9.15 8.44 9.94v-7.03H7.9v-2.9h2.54V9.85c0-2.52 1.5-3.91 3.78-3.91 1.1 0 2.24.2 2.24.2v2.47h-1.26c-1.24 0-1.63.78-1.63 1.57v1.88h2.78l-.44 2.9h-2.34V22c4.78-.79 8.44-4.94 8.44-9.94z"/></svg></a>
      <a href="https://line.me/R/ti/p/@284vivvj" target="_blank" rel="noopener" aria-label="LINE"><svg viewBox="0 0 24 24"><rect x="2" y="2.5" width="20" height="19" rx="5.5" fill="currentColor"/><text x="12" y="14.9" text-anchor="middle" font-size="6.4" font-weight="800" font-family="Arial, sans-serif" style="fill:var(--badgefg,#6E4F33)">LINE</text></svg></a>
    </div>
  </div>
</section>'''
page('contact.html','聯絡我們・預約參觀｜帕咔布托嬰中心 PaKaBoo Nursery',
     '帕咔布托嬰中心｜台中市西屯區福雅路 128 巷 19 號。電話 04-2461-6698、官方 LINE @284vivvj。歡迎預約參觀與半日體驗。',
     'contact', contact_main)

print('ALL DONE')
