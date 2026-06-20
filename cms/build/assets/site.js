/* ===== PaKaBoo Nursery — shared script (multi-page) ===== */
(function(){
  // header scrolled state
  var hdr=document.getElementById('hdr');
  if(hdr){window.addEventListener('scroll',function(){hdr.classList.toggle('scrolled',window.scrollY>40);});}

  // mobile burger
  var burger=document.getElementById('burger'), menu=document.getElementById('menu');
  if(burger&&menu){
    burger.addEventListener('click',function(){menu.classList.toggle('open');});
    menu.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){menu.classList.remove('open');});});
  }

  // gold sparkles on every [data-spark] host
  [].forEach.call(document.querySelectorAll('[data-spark]'),function(host){
    if(getComputedStyle(host).position==='static') host.style.position='relative';
    var box=document.createElement('div'); box.className='sparkles';
    var n=parseInt(host.getAttribute('data-spark'),10)||14;
    for(var i=0;i<n;i++){
      var s=document.createElement('span'); s.className='spark';
      var sz=3+Math.random()*12;
      s.style.left=(Math.random()*100)+'%'; s.style.top=(Math.random()*100)+'%';
      s.style.width=sz+'px'; s.style.height=sz+'px';
      s.style.animationDuration=(2.4+Math.random()*3.4)+'s';
      s.style.animationDelay=(Math.random()*3.8)+'s';
      box.appendChild(s);
    }
    host.insertBefore(box, host.firstChild);
  });

  // reveal on scroll
  var io=new IntersectionObserver(function(es){es.forEach(function(e){
    if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}
  });},{threshold:.14});
  document.querySelectorAll('.reveal').forEach(function(el){io.observe(el);});

  // "爸爸媽媽，我想對您說" flip carousel
  (function(){
    var msgs=[
      "我的小手還很小，畫畫常常越過了線，請多給我一點包容。我的步伐還很慢，請牽著我溫暖的手，陪我一步一步走。",
      "我眼中的世界和您看到的很不一樣，請放心讓我安全地去冒險、去好奇地探索，別給我太多束縛。",
      "家事似乎永遠做不完，但我需要的其實不多——只要您願意撥點時間，輕輕為我說個故事，我就好滿足。",
      "我的心很敏感，請多留意我的感受、用溫柔回應我，就像您也希望被理解、被尊重一樣，這讓我無比安心。",
      "請用心珍惜我，陪我學習為自己負責；當我做得不夠好時，請用溫暖的方式提醒我、引導我、陪伴我。",
      "成長路上，我最需要的是您的鼓勵與肯定；若有需要改進的地方，請用簡單溫和的話語，陪我一起把事情做好。",
      "請讓我試著選擇自己喜歡的事，也允許我在過程中犯錯、在失敗中學習；因為總有一天，我要為自己的人生做決定。",
      "請多肯定我的努力，不必急著糾正每個小細節，也別拿我和別人比較；有了您的信任，我會更勇敢、更有信心。",
      "週末您想出門走走時，別為我擔心——大人和孩子都需要一點自處的空間。當您照顧好自己、情緒穩定，我也會更安心。",
      "您的一言一行都深深影響著我，請成為我的榜樣；因為在我的生命中，您是最重要、也是我的第一位老師。我好愛您。"
    ];
    var inner=document.getElementById('vInner');
    if(!inner) return;
    var num=document.getElementById('vNum'),txt=document.getElementById('vText'),
        cur=document.getElementById('vCur'),dots=document.getElementById('vDots'),i=0;
    msgs.forEach(function(_,k){var s=document.createElement('span');s.addEventListener('click',function(){go(k);});dots.appendChild(s);});
    function render(){
      num.textContent=('0'+(i+1)).slice(-2); txt.textContent=msgs[i];
      if(cur)cur.textContent=('0'+(i+1)).slice(-2);
      [].forEach.call(dots.children,function(d,k){d.classList.toggle('on',k===i);});
    }
    function go(n){
      var dir=n>i?1:-1; if(n<0)n=msgs.length-1; if(n>=msgs.length)n=0;
      inner.style.opacity=0; inner.style.transform='rotateY('+(dir>0?'-16deg':'16deg')+') translateY(8px)';
      setTimeout(function(){i=n;render();inner.style.opacity=1;inner.style.transform='none';},200);
    }
    var p=document.getElementById('vPrev'),nx=document.getElementById('vNext');
    if(p)p.addEventListener('click',function(){go(i-1);});
    if(nx)nx.addEventListener('click',function(){go(i+1);});
    render();
  })();
})();
