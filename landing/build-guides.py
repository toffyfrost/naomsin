# -*- coding: utf-8 -*-
"""
สร้างหน้าคู่มือ 2 หน้า: landing/tax.html (ภาษีเข้าใจง่าย) และ landing/missions.html (ภารกิจ)
รายการค่าลดหย่อนดึงจาก supabase/functions/naomsin/taxguide.ts (ส่งออกเป็น JSON ก่อน) เพื่อให้ตรงกับที่บอทคำนวณ
รัน: python3 landing/build-guides.py <path/ded.json>
"""
import html, json, os, sys, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
OA = '@943axyqp'
ask = lambda q: 'https://line.me/R/oaMessage/' + OA + '/?' + urllib.parse.quote(q)
esc = html.escape
money = lambda n: '{:,.0f}'.format(n)

HEAD = """<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#E3F0FF">
<link rel="icon" type="image/png" sizes="32x32" href="img/brand/favicon-32.png">
<link rel="apple-touch-icon" href="img/brand/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Thai:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {{ --bg:#F5F9FF; --ink:#0B2545; --sub:#4A6485; --dim:#8196B0; --line:rgba(28,126,214,.14); --blue:#1C7ED6; --blue-d:#1864AB; --mint:#0CA678;
    --mint-s:#E6FCF5; --soft:#EAF4FF; --warn:#FFF4E6; --grad:linear-gradient(135deg,#1864AB 0%,#1C7ED6 45%,#4DABF7 100%);
    --shadow:0 1px 2px rgba(11,37,69,.05),0 16px 40px -22px rgba(24,100,171,.30); --line-green:#06C755; }}
  * {{ box-sizing:border-box; }}
  html {{ scroll-behavior:smooth; }}
  body {{ margin:0; font-family:'Noto Sans Thai',sans-serif; color:var(--ink); line-height:1.75; font-size:17px;
    background:linear-gradient(180deg,#E3F0FF 0,#F5F9FF 600px,#fff 1400px); -webkit-font-smoothing:antialiased; }}
  a {{ color:var(--blue); }}
  img {{ max-width:100%; display:block; }}
  .wrap {{ max-width:900px; margin:0 auto; padding:0 20px; }}
  header {{ position:sticky; top:0; z-index:20; background:rgba(245,249,255,.88); backdrop-filter:blur(14px); border-bottom:1px solid var(--line); }}
  header .wrap {{ display:flex; align-items:center; justify-content:space-between; height:64px; }}
  .logo {{ display:flex; align-items:center; gap:10px; font-weight:800; letter-spacing:.04em; text-decoration:none; color:var(--ink); }}
  .logo img {{ width:36px; height:36px; border-radius:50%; }}
  .btn {{ display:inline-flex; align-items:center; gap:8px; padding:12px 22px; border-radius:999px; font-weight:700; font-size:16px; text-decoration:none; border:0; }}
  .btn.line {{ background:var(--line-green); color:#fff; box-shadow:0 10px 24px -10px rgba(6,199,85,.7); }}
  .btn.ghost {{ background:#fff; color:var(--blue); border:1px solid rgba(28,126,214,.28); }}
  .btn.sm {{ padding:8px 16px; font-size:14px; }}
  .hero {{ display:grid; grid-template-columns:1.3fr 1fr; gap:20px; align-items:center; padding:40px 0 20px; }}
  .hero h1 {{ font-size:clamp(32px,5vw,50px); line-height:1.2; margin:10px 0; }}
  .hero p {{ color:var(--sub); font-size:18px; margin:0 0 20px; }}
  .grad {{ background:var(--grad); -webkit-background-clip:text; background-clip:text; color:transparent; }}
  .eyebrow {{ display:inline-block; font-size:13px; font-weight:700; letter-spacing:.12em; color:var(--blue); background:var(--soft); padding:4px 12px; border-radius:999px; }}
  .tocwrap {{ position:sticky; top:64px; z-index:10; padding:8px 0 14px; background:linear-gradient(180deg,rgba(245,249,255,.97) 75%,rgba(245,249,255,0)); }}
  .toc {{ display:flex; gap:6px; overflow-x:auto; scrollbar-width:none; -ms-overflow-style:none; scroll-behavior:smooth; padding:6px;
    background:rgba(255,255,255,.72); backdrop-filter:saturate(1.6) blur(14px); -webkit-backdrop-filter:saturate(1.6) blur(14px);
    border:1px solid rgba(15,59,125,.08); border-radius:999px; box-shadow:0 8px 28px rgba(15,59,125,.10), inset 0 1px 0 rgba(255,255,255,.9);
    -webkit-mask-image:linear-gradient(90deg,transparent 0,#000 22px,#000 calc(100% - 22px),transparent 100%); mask-image:linear-gradient(90deg,transparent 0,#000 22px,#000 calc(100% - 22px),transparent 100%); }}
  .toc::-webkit-scrollbar {{ display:none; }}
  .toc a {{ flex:0 0 auto; white-space:nowrap; font-size:14px; font-weight:600; text-decoration:none; color:var(--blue-d); padding:8px 16px; border-radius:999px; transition:background .25s,color .25s,box-shadow .25s; }}
  .toc a:first-child {{ margin-left:10px; }} .toc a:last-child {{ margin-right:10px; }}
  .toc a:hover {{ background:var(--soft); }}
  .toc a.on {{ background:var(--grad); color:#fff; box-shadow:0 4px 14px rgba(37,99,235,.35); }}
  @media (min-width:900px) {{ .toc {{ width:max-content; max-width:100%; margin:0 auto; }} .toc a {{ padding:8px 14px; }} }}
  section {{ padding:26px 0; scroll-margin-top:120px; }}
  h2 {{ font-size:clamp(24px,3.4vw,32px); line-height:1.3; margin:0 0 6px; }}
  h3 {{ font-size:19px; margin:0 0 4px; }}
  .lead {{ color:var(--sub); margin:0 0 16px; }}
  .card {{ background:#fff; border-radius:22px; padding:20px 22px; box-shadow:var(--shadow); border:1px solid var(--line); margin:12px 0; }}
  .grid {{ display:grid; grid-template-columns:repeat(2,1fr); gap:12px; }}
  .grid3 {{ display:grid; grid-template-columns:repeat(3,1fr); gap:12px; }}
  .formula {{ display:flex; flex-wrap:wrap; align-items:center; gap:8px; font-weight:700; }}
  .formula span {{ background:var(--soft); padding:8px 14px; border-radius:14px; }}
  .formula b {{ color:var(--blue); font-size:20px; }}
  table {{ width:100%; border-collapse:collapse; font-size:15px; }}
  th, td {{ text-align:left; padding:9px 10px; border-bottom:1px solid var(--line); }}
  th {{ color:var(--blue-d); background:var(--soft); }}
  td.r, th.r {{ text-align:right; }}
  .step {{ display:grid; grid-template-columns:44px 1fr; gap:12px; margin:14px 0; }}
  .step .n {{ width:44px; height:44px; border-radius:14px; background:var(--grad); color:#fff; font-weight:800; display:flex; align-items:center; justify-content:center; font-size:19px; }}
  .say {{ display:grid; grid-template-columns:90px 1fr; gap:14px; align-items:center; background:linear-gradient(135deg,var(--soft),var(--mint-s)); border-radius:22px; padding:14px 18px; }}
  .say img {{ width:90px; }}
  .chat {{ display:inline-block; background:#E9FBEF; color:#085F2E; border-radius:12px 12px 2px 12px; padding:2px 10px; font-weight:600; font-size:15px; }}
  .tag {{ display:inline-block; font-size:12px; font-weight:700; padding:1px 9px; border-radius:999px; background:var(--soft); color:var(--blue-d); }}
  .tag.mint {{ background:var(--mint-s); color:var(--mint); }} .tag.warn {{ background:var(--warn); color:#9A4C00; }}
  .ded {{ padding:12px 0; border-bottom:1px dashed var(--line); display:grid; grid-template-columns:1fr auto; gap:6px 14px; }}
  .ded:last-child {{ border-bottom:0; }}
  .ded .cap {{ font-weight:800; color:var(--blue); white-space:nowrap; }}
  .ded p {{ margin:2px 0 0; color:var(--sub); font-size:15px; grid-column:1 / 3; }}
  details {{ background:#fff; border:1px solid var(--line); border-radius:18px; padding:14px 18px; margin:10px 0; }}
  summary {{ cursor:pointer; font-weight:700; }}
  .note {{ background:var(--warn); border-radius:16px; padding:12px 16px; font-size:15px; color:#6B3A00; }}
  .fab {{ position:fixed; right:16px; bottom:16px; z-index:30; }}
  footer {{ border-top:1px solid var(--line); margin-top:30px; padding:24px 0 90px; color:var(--dim); font-size:14px; }}
  @media (max-width:720px) {{ .hero, .grid, .grid3 {{ grid-template-columns:1fr; }} .hero img {{ max-width:240px; margin:0 auto; }} body {{ font-size:16px; }} .say {{ grid-template-columns:64px 1fr; }} .say img {{ width:64px; }} }}
</style>
</head>
<body>
<header><div class="wrap"><a class="logo" href="index.html"><img src="img/brand/logo.webp" alt="">N'AOMSIN</a>
  <a class="btn line sm" href="{ask}">💬 ถามน้องออมสิน</a></div></header>
"""

FOOT = """<a class="btn line fab" href="{ask}">💬 ถามน้องออมสินใน LINE</a>
<footer><div class="wrap">{extra}<br>© N'AOMSIN · ผู้ช่วยจดรายรับรายจ่ายใน LINE · <a href="index.html">หน้าแรก</a> · <a href="features.html">ฟีเจอร์ทั้งหมด</a> · <a href="tax.html">คู่มือภาษี</a> · <a href="missions.html">คู่มือภารกิจ</a></div></footer>
<script>(function(){{var nav=document.querySelector('.toc');if(!nav||!('IntersectionObserver'in window))return;var links=[].slice.call(nav.querySelectorAll('a'));
function on(id){{links.forEach(function(a){{var h=a.getAttribute('href')==='#'+id;a.classList.toggle('on',h);if(h&&nav.scrollWidth>nav.clientWidth)nav.scrollTo({{left:a.offsetLeft-nav.clientWidth/2+a.offsetWidth/2}});}});}}
var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting)on(e.target.id);}});}},{{rootMargin:'-45% 0px -50% 0px'}});
links.forEach(function(a){{var el=document.querySelector(a.getAttribute('href'));if(el)io.observe(el);}});}})();</script>
</body></html>"""


def tax_page(data):
    groups, deds = data['groups'], data['deductions']
    def cap(d):
        if d.get('per'): return '฿' + money(d['per']) + '/คน'
        if d.get('max'): return 'สูงสุด ฿' + money(d['max'])
        return 'ไม่เกิน 10%'
    ded_html = ''
    for g in groups:
        items = [d for d in deds if d['group'] == g['id']]
        rows = ''.join(f"""<div class="ded"><b>{esc(d['name'])}{' <span class="tag warn">เฉพาะปี 2567</span>' if d.get('years') else ''}</b><span class="cap">{cap(d)}</span>
          <p>{esc(d['simple'])}{(' · 💡 ' + esc(d['tip'])) if d.get('tip') else ''}</p></div>""" for d in items)
        ded_html += f"""<details {'open' if g['id'] in ('family','insurance') else ''}><summary>{g['icon']} {esc(g['title'])} <span class="tag">{len(items)} รายการ</span></summary>{rows}</details>"""

    body = f"""
<div class="wrap">
  <div class="hero">
    <div><span class="eyebrow">คู่มือภาษีฉบับเข้าใจง่าย</span>
      <h1>ภาษีไม่ยาก<br><span class="grad">ถ้ามีน้องออมสินช่วย</span></h1>
      <p>ไม่ต้องรู้เรื่องภาษีมาก่อน ไม่ว่าจะเป็นพนักงาน ฟรีแลนซ์ หรือพ่อค้าแม่ค้าในตลาด แค่จดรายรับในแชท น้องออมสินช่วยคิด ช่วยเตือน และบอกทีละขั้นว่าต้องทำอะไร</p>
      <a class="btn line" href="{ask('สรุปภาษี')}">💬 ดูภาษีของฉันใน LINE</a> <a class="btn ghost" href="#howto">ใช้งานยังไง</a></div>
    <img src="img/mascot/guide.webp" alt="น้องออมสิน">
  </div>
  <div class="tocwrap"><nav class="toc"><a href="#simple">ภาษีคิดยังไง</a><a href="#must">ต้องยื่นไหม</a><a href="#income">รายได้ของฉันแบบไหน</a><a href="#shop">🏪 พ่อค้าแม่ค้า</a><a href="#deduct">ค่าลดหย่อน</a><a href="#howto">ใช้กับน้องออมสิน</a><a href="#file">วิธียื่น</a><a href="#faq">ถามบ่อย</a></nav></div>

  <section id="simple"><h2>ภาษีคิดยังไง (แบบ 1 นาที)</h2><p class="lead">ภาษีไม่ได้คิดจากรายได้ทั้งหมด แต่คิดจาก "เงินที่เหลือ" หลังหักสิ่งที่กฎหมายให้หัก</p>
    <div class="card"><div class="formula"><span>รายได้ทั้งปี</span><b>−</b><span>ค่าใช้จ่าย</span><b>−</b><span>ค่าลดหย่อน</span><b>=</b><span style="background:var(--mint-s);color:var(--mint)">เงินได้สุทธิ</span></div>
      <p style="margin:14px 0 6px">แล้วเอาเงินได้สุทธิไปคิดตามขั้นบันได <b>150,000 บาทแรกไม่เสียภาษีเลย</b></p>
      <table><tr><th>เงินได้สุทธิ</th><th class="r">อัตรา</th></tr>
        <tr><td>0 – 150,000</td><td class="r">ยกเว้น</td></tr><tr><td>150,001 – 300,000</td><td class="r">5%</td></tr><tr><td>300,001 – 500,000</td><td class="r">10%</td></tr>
        <tr><td>500,001 – 750,000</td><td class="r">15%</td></tr><tr><td>750,001 – 1,000,000</td><td class="r">20%</td></tr><tr><td>1,000,001 – 2,000,000</td><td class="r">25%</td></tr>
        <tr><td>2,000,001 – 5,000,000</td><td class="r">30%</td></tr><tr><td>มากกว่า 5,000,000</td><td class="r">35%</td></tr></table></div>
    <div class="say"><img src="img/mascot/thumbsup.webp" alt=""><div>ทุกคนได้ <b>ลดหย่อนส่วนตัว 60,000 บาท</b> อัตโนมัติ น้องออมสินใส่ให้แล้ว ส่วนค่าลดหย่อนอื่นๆ (ประกันสังคม ประกัน ลูก พ่อแม่) บอกน้องออมสินเพิ่มได้ ยิ่งใส่ครบ ยิ่งเสียภาษีน้อยลงค่ะ</div></div></section>

  <section id="must"><h2>ต้องยื่นภาษีไหม?</h2><p class="lead">ถ้ารายได้ทั้งปีเกินตัวเลขนี้ ต้องยื่นแบบ (แม้สุดท้ายจะไม่ต้องจ่ายภาษีก็ตาม)</p>
    <div class="grid"><div class="card"><h3>💼 มีแต่เงินเดือน</h3><p>โสด: เกิน <b>120,000</b> บาท/ปี<br>มีคู่สมรส: เกิน <b>220,000</b> บาท/ปี<br><span class="tag">แบบ ภ.ง.ด.91</span></p></div>
      <div class="card"><h3>🏪 มีรายได้อื่น (ขายของ ฟรีแลนซ์)</h3><p>โสด: เกิน <b>60,000</b> บาท/ปี<br>มีคู่สมรส: เกิน <b>120,000</b> บาท/ปี<br><span class="tag">แบบ ภ.ง.ด.90</span></p></div></div>
    <div class="note">💡 ถูกหักภาษี ณ ที่จ่ายไว้ (เช่น ค่าจ้างฟรีแลนซ์ถูกหัก 3%) แต่รายได้ไม่ถึงเกณฑ์เสียภาษี → <b>ยื่นแบบเพื่อขอเงินคืนได้</b> น้องออมสินจะบอกว่าคุณอาจได้คืนเท่าไหร่</div></section>

  <section id="income"><h2>รายได้ของฉันเป็นแบบไหน?</h2><p class="lead">แต่ละแบบหักค่าใช้จ่ายไม่เท่ากัน น้องออมสินช่วยจัดให้จากหมวดที่คุณจด (พิมพ์ <span class="chat">จัดประเภทรายรับ</span>)</p>
    <div class="grid">
      <div class="card"><h3>💼 เงินเดือน / โบนัส</h3><span class="tag">40(1)</span><p>เงินที่นายจ้างจ่ายประจำ หักค่าใช้จ่ายเหมา 50% (รวมกับรับจ้างไม่เกิน 100,000 บาท)</p></div>
      <div class="card"><h3>🧑‍💻 รับจ้าง / ฟรีแลนซ์</h3><span class="tag">40(2)</span><p>ค่าจ้างงานเป็นครั้ง ค่าคอมมิชชั่น หักเหมา 50% (รวมกับเงินเดือนไม่เกิน 100,000 บาท)</p></div>
      <div class="card"><h3>🏪 ขายของ / ค้าขาย</h3><span class="tag mint">40(8)</span><p>ขายอาหาร ขายของตลาด ขายออนไลน์ <b>หักค่าใช้จ่ายเหมา 60%</b> ไม่ต้องเก็บใบเสร็จ</p></div>
      <div class="card"><h3>🚫 ไม่ใช่รายได้</h3><span class="tag">ไม่นำมาคิด</span><p>เพื่อนคืนเงิน เงินยืม ย้ายเงินระหว่างบัญชีตัวเอง ไม่ต้องเอามาคิดภาษี</p></div></div></section>

  <section id="shop"><h2>🏪 พ่อค้าแม่ค้า อ่านตรงนี้</h2><p class="lead">ขายของหักค่าใช้จ่ายได้ถึง 60% โดยไม่ต้องมีใบเสร็จ แม่ค้าส่วนใหญ่จึงเสียภาษีน้อยกว่าที่คิด</p>
    <div class="grid">
      <div class="card"><h3>ตัวอย่าง 1: ขายส้มตำ เดือนละ 30,000</h3>
        <table><tr><td>ยอดขายทั้งปี</td><td class="r">360,000</td></tr><tr><td>หักค่าใช้จ่ายเหมา 60%</td><td class="r">−216,000</td></tr>
          <tr><td>หักลดหย่อนส่วนตัว</td><td class="r">−60,000</td></tr><tr><th>เงินได้สุทธิ</th><th class="r">84,000</th></tr>
          <tr><th>ภาษีที่ต้องจ่าย</th><th class="r" style="color:var(--mint)">0 บาท 🎉</th></tr></table>
        <p class="lead" style="margin-top:8px;font-size:15px">ยอดขายเกิน 60,000 บาท ต้องยื่นแบบ แต่ไม่ต้องจ่ายภาษี</p></div>
      <div class="card"><h3>ตัวอย่าง 2: ร้านขายของ เดือนละ 100,000</h3>
        <table><tr><td>ยอดขายทั้งปี</td><td class="r">1,200,000</td></tr><tr><td>หักค่าใช้จ่ายเหมา 60%</td><td class="r">−720,000</td></tr>
          <tr><td>หักลดหย่อนส่วนตัว</td><td class="r">−60,000</td></tr><tr><th>เงินได้สุทธิ</th><th class="r">420,000</th></tr>
          <tr><th>ภาษีขั้นบันได</th><th class="r">19,500</th></tr></table>
        <p class="lead" style="margin-top:8px;font-size:15px">ยังต้องเทียบ "วิธีที่ 2" (0.5% ของยอดขาย = 6,000) แล้วจ่ายตัวที่มากกว่า น้องออมสินเทียบให้อัตโนมัติ</p></div></div>
    <div class="card"><h3>✅ สิ่งที่พ่อค้าแม่ค้าควรทำ</h3>
      <div class="step"><div class="n">1</div><div><b>จดยอดขายทุกวัน</b> พิมพ์ในแชท เช่น <span class="chat">ขายส้มตำได้ 1,200</span> หรือเปิด <span class="chat">เปิดโหมดร้านค้า</span> ดูกำไรด้วย</div></div>
      <div class="step"><div class="n">✦</div><div><b>ไม่อยากพิมพ์? ส่งสลิปอย่างเดียว</b> พิมพ์ <span class="chat">เปิดโหมดร้านค้า</span> แล้วส่งสลิปที่ลูกค้าโอนมา น้องออมสินบันทึกเป็น <b>ยอดขาย</b> ให้เลย · ซื้อวัตถุดิบส่งสลิป/ใบเสร็จแล้วกด <b>📦 ต้นทุนร้าน</b> ครั้งแรก ครั้งต่อไปโอนให้ร้านเดิมจะนับเป็น <b>ต้นทุน</b> อัตโนมัติ</div></div>
      <div class="step"><div class="n">2</div><div><b>ยื่นครึ่งปี (ภ.ง.ด.94)</b> รายได้ ม.ค.–มิ.ย. ยื่นภายใน 30 ก.ย. แล้วยื่นเต็มปี (ภ.ง.ด.90) ช่วง ม.ค.–มี.ค. ปีถัดไป</div></div>
      <div class="step"><div class="n">3</div><div><b>ลดหย่อนเพิ่มได้</b> เช่น ออมกับ กอช. (ไม่เกิน 30,000) ประกันสังคมมาตรา 40 ประกันชีวิต/สุขภาพ</div></div>
      <a class="btn line" href="{ask('ภาษีแม่ค้า')}">💬 ถามน้องออมสินเรื่องภาษีร้านค้า</a></div></section>

  <section id="deduct"><h2>ค่าลดหย่อน ลดอะไรได้บ้าง</h2><p class="lead">ในแอปเรียกว่า <b>"ข้อมูลภาษีเพิ่มเติม"</b> เลือกข้อที่คุณมี แล้วบอกจำนวนเงิน น้องออมสินคิดเพดานให้เอง (ตามเอกสารกรมสรรพากร)</p>
    {ded_html}
    <div class="note">กลุ่มเกษียณ (กองทุนสำรองเลี้ยงชีพ RMF SSF ประกันบำนาญ กบข. กอช.) รวมกันไม่เกิน 500,000 บาท · ประกันชีวิต+ประกันสุขภาพตัวเอง รวมไม่เกิน 100,000 บาท · น้องออมสินคิดให้แล้ว</div>
    <p style="margin-top:14px">บันทึกในแชทได้ทันที เช่น <span class="chat">ลดหย่อน ประกันสังคม 9000</span> <span class="chat">ลดหย่อน ลูก 2 คน</span> <span class="chat">ลดหย่อน คู่สมรส</span> <span class="chat">ลดหย่อน ประกันสุขภาพ 18000</span></p></section>

  <section id="howto"><h2>ใช้กับน้องออมสินยังไง</h2><p class="lead">ทำตามนี้ ครั้งแรกใช้เวลาไม่ถึง 10 นาที</p>
    <div class="card">
      <div class="step"><div class="n">1</div><div><b>จดรายรับในแชทตามปกติ</b><br><span class="chat">เงินเดือนเข้า 25000</span> <span class="chat">ได้ค่าจ้างออกแบบ 5000 หัก 3%</span> <span class="chat">ขายของได้ 1500</span></div></div>
      <div class="step"><div class="n">2</div><div><b>ให้น้องออมสินจัดประเภท</b> พิมพ์ <span class="chat">จัดประเภทรายรับ</span> ตัวไหนไม่แน่ใจ แตะเลือกเองในหน้าภาษี</div></div>
      <div class="step"><div class="n">3</div><div><b>ใส่ข้อมูลภาษีเพิ่มเติม</b> พิมพ์ <span class="chat">ข้อมูลภาษีเพิ่มเติม</span> เลือกค่าลดหย่อนที่มี หรือพิมพ์ <span class="chat">ลดหย่อน ประกันสังคม 9000</span></div></div>
      <div class="step"><div class="n">4</div><div><b>ดูผล</b> พิมพ์ <span class="chat">สรุปภาษี</span> รู้ทันทีว่าต้องจ่ายเพิ่มหรือได้เงินคืน พร้อมคำแนะนำ</div></div>
      <div class="step"><div class="n">5</div><div><b>เก็บหลักฐาน</b> พิมพ์ <span class="chat">เก็บหลักฐานภาษี</span> แล้วส่งรูปหนังสือรับรองหัก ณ ที่จ่าย/ใบเสร็จประกัน เก็บเป็นไฟล์ส่วนตัว</div></div>
      <a class="btn line" href="{ask('ข้อมูลภาษีเพิ่มเติม')}">💬 เริ่มใส่ข้อมูลภาษีใน LINE</a></div></section>

  <section id="file"><h2>วิธียื่นภาษีออนไลน์ (e-Filing)</h2><p class="lead">ยื่นเองได้ที่เว็บกรมสรรพากร ใช้ตัวเลขจาก "สรุปเตรียมยื่น" ของน้องออมสิน</p>
    <div class="card">
      <div class="step"><div class="n">1</div><div>ในหน้าภาษีของแดชบอร์ด กด <b>"ดาวน์โหลดสรุปเตรียมยื่น"</b> (ไฟล์จะเปิดในเบราว์เซอร์หลัก)</div></div>
      <div class="step"><div class="n">2</div><div>เข้า <a href="https://efiling.rd.go.th/" target="_blank" rel="noopener">efiling.rd.go.th</a> ล็อกอินด้วยเลขบัตรประชาชน หรือแอป ThaID</div></div>
      <div class="step"><div class="n">3</div><div>เลือกแบบ <b>ภ.ง.ด.91</b> (มีแต่เงินเดือน) หรือ <b>ภ.ง.ด.90</b> (มีรายได้อื่น)</div></div>
      <div class="step"><div class="n">4</div><div>กรอกรายได้แต่ละประเภท ภาษีหัก ณ ที่จ่าย และค่าลดหย่อน ตามสรุป แล้วตรวจยอดภาษีให้ตรงกับน้องออมสิน</div></div>
      <div class="step"><div class="n">5</div><div>กดยื่นแบบ ถ้าต้องจ่ายเพิ่มชำระออนไลน์ได้ (ผ่อน 3 งวดได้ถ้ายอดตั้งแต่ 3,000 บาท) ถ้าได้คืนรอเงินโอนเข้าพร้อมเพย์ที่ผูกเลขบัตร</div></div>
      <p class="lead" style="font-size:15px">📅 ยื่นปีภาษีนี้ได้ ม.ค.–มี.ค. ของปีถัดไป (ยื่นออนไลน์มักขยายถึงต้นเมษายน) · น้องออมสินเตรียมข้อมูลให้ แต่ไม่ได้ยื่นแทนคุณ</p></div></section>

  <section id="faq"><h2>คำถามที่พบบ่อย</h2>
    <details><summary>ไม่รู้เรื่องภาษีเลย ใช้ได้ไหม?</summary><p>ได้เลยค่ะ แค่จดรายรับในแชทตามปกติ แล้วพิมพ์ "สรุปภาษี" น้องออมสินจะบอกทีละขั้นว่าต้องทำอะไรต่อ หรือพิมพ์ถามได้ทุกเรื่อง เช่น "ประกันสุขภาพลดหย่อนได้เท่าไหร่"</p></details>
    <details><summary>น้องออมสินยื่นภาษีให้ได้ไหม?</summary><p>ยังไม่ได้ค่ะ น้องออมสินช่วยคำนวณ เตรียมตัวเลข และสรุปให้ คุณนำไปกรอกและกดยื่นเองที่ e-Filing ของกรมสรรพากร</p></details>
    <details><summary>ตัวเลขแม่นแค่ไหน?</summary><p>เป็นการประมาณจากข้อมูลที่คุณบันทึก ตามหลักเกณฑ์กรมสรรพากร ถ้าจดรายรับครบและใส่ค่าลดหย่อนถูก ตัวเลขจะใกล้เคียงของจริง ควรตรวจอีกครั้งในระบบ e-Filing ก่อนกดยื่น</p></details>
    <details><summary>ข้อมูลภาษีของฉันปลอดภัยไหม?</summary><p>ข้อมูลทั้งหมดเข้ารหัสก่อนเก็บ ใช้ได้เฉพาะสมุดส่วนตัว ไม่แสดงในสมุดกลุ่ม และไฟล์หลักฐานเก็บแบบส่วนตัว เปิดผ่านลิงก์ชั่วคราวเท่านั้น</p></details>
    <details><summary>ขายของออนไลน์/ในตลาด ต้องจดทะเบียนอะไรไหม?</summary><p>ภาษีเงินได้ยื่นในชื่อตัวเองได้เลย ถ้ายอดขายเกิน 1.8 ล้านบาทต่อปี ต้องจดทะเบียนภาษีมูลค่าเพิ่ม (VAT) ควรปรึกษากรมสรรพากรหรือนักบัญชีเพิ่มเติม</p></details></section>

  <p class="lead" style="font-size:14px">อ้างอิง: <a href="https://www.rd.go.th/26218.html" target="_blank" rel="noopener">กรมสรรพากร: การคำนวณภาษี</a> · <a href="https://www.rd.go.th/59668.html" target="_blank" rel="noopener">โครงสร้างอัตราภาษี</a> · เอกสาร "ผู้มีเงินได้มีสิทธิหักลดหย่อนอะไรได้บ้าง?" · หลักเกณฑ์อาจเปลี่ยนทุกปี ตรวจสอบกับกรมสรรพากรก่อนยื่น</p>
</div>"""
    return HEAD.format(title='คู่มือภาษีเข้าใจง่าย · N\'AOMSIN', desc='ภาษีเงินได้บุคคลธรรมดาแบบเข้าใจง่าย ค่าลดหย่อน 28 รายการ ภาษีพ่อค้าแม่ค้า และวิธียื่นทีละขั้น กับน้องออมสิน', ask=ask('สรุปภาษี')) + body + FOOT.format(ask=ask('ถามเรื่องภาษี'), extra='คู่มือนี้ช่วยให้เข้าใจภาพรวม ไม่ใช่คำแนะนำทางภาษีเฉพาะบุคคล')


def missions_page():
    stickers = [('hello', 'เริ่มต้นจด', 'จดรายการวันแรก'), ('calendar', 'นักจดประจำ', 'จด 5 วันในสัปดาห์'), ('celebrate', 'ไฟต่อเนื่อง', 'จดต่อเนื่อง 7 วัน'),
                ('thumbsup', 'พิชิตเป้า', 'ออมครบเป้าหมาย'), ('guide', 'นักสืบรายจ่าย', 'ทายหมวดรายจ่ายถูก')]
    cards = ''.join(f"""<div class="card" style="text-align:center"><img src="img/mascot/{i}.webp" alt="" style="width:110px;margin:0 auto"><h3>{n}</h3><p class="lead" style="margin:0;font-size:15px">{h}</p></div>""" for i, n, h in stickers)
    body = f"""
<div class="wrap">
  <div class="hero">
    <div><span class="eyebrow">คู่มือภารกิจ</span>
      <h1>จดเงินให้สนุก<br><span class="grad">สะสมแต้ม แลกรางวัล</span></h1>
      <p>ทุกครั้งที่จดรายรับรายจ่าย ออมเงินครบเป้า หรือเล่นเกมทายหมวด คุณจะได้แต้มและการ์ดสะสมน้องออมสิน แล้วนำแต้มไปแลกรางวัลได้</p>
      <a class="btn line" href="{ask('ภารกิจ')}">🎮 ดูภารกิจของฉันใน LINE</a> <a class="btn ghost" href="#points">ได้แต้มยังไง</a></div>
    <img src="img/mascot/celebrate.webp" alt="น้องออมสิน">
  </div>
  <div class="tocwrap"><nav class="toc"><a href="#points">ได้แต้มยังไง</a><a href="#cards">การ์ดสะสม</a><a href="#game">เกมทายหมวด</a><a href="#rewards">แลกรางวัล</a><a href="#assistant">ผู้ช่วยส่วนตัว</a><a href="#faq">ถามบ่อย</a></nav></div>
  <section id="points"><h2>ได้แต้มยังไง</h2><p class="lead">ทำตามปกติก็ได้แต้มแล้ว ไม่ต้องทำอะไรพิเศษ</p>
    <div class="card"><table><tr><th>ภารกิจ</th><th class="r">แต้ม</th><th>ได้บ่อยแค่ไหน</th></tr>
      <tr><td>📒 จดรายการวันนี้</td><td class="r"><b>+3</b></td><td>วันละ 1 ครั้ง</td></tr>
      <tr><td>🗓️ จดครบ 5 วันในสัปดาห์</td><td class="r"><b>+8</b></td><td>สัปดาห์ละ 1 ครั้ง</td></tr>
      <tr><td>🔥 จดต่อเนื่อง 7 วัน</td><td class="r"><b>+10</b></td><td>ครั้งแรกครั้งเดียว</td></tr>
      <tr><td>🎯 ออมครบเป้าหมาย</td><td class="r"><b>+5</b></td><td>เดือนละ 1 ครั้ง</td></tr>
      <tr><td>🔎 ทายหมวดรายจ่ายถูก</td><td class="r"><b>+4</b></td><td>สัปดาห์ละ 1 ครั้ง</td></tr></table>
      <p class="lead" style="margin:10px 0 0;font-size:15px">พิมพ์ <span class="chat">ภารกิจ</span> ในแชทเพื่อดูแต้มคงเหลือและแต้มสะสมทั้งหมด · แก้ไขรายการย้อนหลังไม่ได้แต้มเพิ่ม</p></div></section>
  <section id="cards"><h2>การ์ดสะสมน้องออมสิน</h2><p class="lead">ทำภารกิจครั้งแรกได้การ์ด 1 ใบ สะสมครบ 5 ใบ · พิมพ์ <span class="chat">การ์ด</span></p><div class="grid3">{cards}</div></section>
  <section id="game"><h2>🔎 เกมทายหมวดรายจ่าย</h2>
    <div class="say"><img src="img/mascot/guide.webp" alt=""><div>พิมพ์ <span class="chat">เล่นเกมทายหมวด</span> น้องออมสินจะให้ทายว่า 7 วันที่ผ่านมา คุณใช้เงินกับหมวดไหนมากที่สุด (3 ตัวเลือก) ทายถูกได้ +4 แต้ม เล่นได้สัปดาห์ละครั้ง เป็นวิธีง่ายๆ ให้รู้ตัวว่าเงินไปไหนค่ะ</div></div></section>
  <section id="rewards"><h2>🎁 แลกรางวัล</h2><p class="lead">พิมพ์ <span class="chat">รางวัล</span> เพื่อดูรางวัลที่เปิดให้แลกตอนนี้</p>
    <div class="grid"><div class="card"><h3>💎 โค้ด Pro</h3><p>แลกแต้มเป็นโค้ดใช้ Pro ฟรีตามจำนวนวัน ระบบออกโค้ดให้ทันทีและผูกกับบัญชีคุณ</p></div>
      <div class="card"><h3>🎀 ของรางวัลพิเศษ</h3><p>ของที่ระลึกหรือสิทธิ์จากพาร์ตเนอร์ แอดมินจะติดต่อส่งมอบให้ ดูสถานะได้ในแชท</p></div></div>
    <div class="note">รางวัลมีจำนวนจำกัด แต่ละรางวัลแลกได้คนละ 1 ครั้ง แต้มจะถูกหักเมื่อแลกสำเร็จเท่านั้น</div></section>
  <section id="assistant"><h2>🐷 ผู้ช่วยส่วนตัว</h2><p class="lead">ให้น้องออมสินช่วยดูแลเงินแบบที่คุณชอบ · พิมพ์ <span class="chat">ตั้งค่าผู้ช่วย</span></p>
    <div class="card">
      <div class="step"><div class="n">1</div><div><b>เลือกน้ำเสียง</b> <span class="chat">ตั้งโหมดอ่อนโยน</span> <span class="chat">ตั้งโหมดขี้เล่น</span> <span class="chat">ตั้งโหมดเข้มงวด</span></div></div>
      <div class="step"><div class="n">2</div><div><b>ให้น้องออมสินทักก่อน</b> <span class="chat">เปิดผู้ช่วย</span> เตือนเมื่องบใกล้หมดหรือเกินงบ (ปิดได้ด้วย <span class="chat">ปิดผู้ช่วย</span>)</div></div>
      <div class="step"><div class="n">3</div><div><b>เตือนเมื่อเงินเหลือน้อย</b> <span class="chat">เตือนเงินต่ำกว่า 1000</span></div></div>
      <div class="step"><div class="n">4</div><div><b>เวลาห้ามรบกวน</b> <span class="chat">พักแจ้งเตือน 22-8</span> (ไม่ทักช่วง 22:00–08:00)</div></div></div></section>
  <section id="faq"><h2>คำถามที่พบบ่อย</h2>
    <details><summary>แต้มหมดอายุไหม?</summary><p>ไม่หมดอายุค่ะ สะสมไว้แลกรางวัลเมื่อไหร่ก็ได้</p></details>
    <details><summary>จดในกลุ่ม LINE ได้แต้มไหม?</summary><p>ภารกิจนับจากสมุดส่วนตัวของคุณค่ะ</p></details>
    <details><summary>ทำไมจดแล้วไม่ได้แต้ม?</summary><p>ภารกิจ "จดรายการวันนี้" ได้วันละครั้ง และต้องเป็นรายการของวันนี้ รายการที่แก้ไขย้อนหลังจะไม่ได้แต้มเพิ่ม</p></details></section>
</div>"""
    return HEAD.format(title="คู่มือภารกิจ · N'AOMSIN", desc='สะสมแต้ม การ์ดน้องออมสิน เกมทายหมวด แลกรางวัล และตั้งค่าผู้ช่วยส่วนตัว', ask=ask('ภารกิจ')) + body + FOOT.format(ask=ask('ภารกิจ'), extra='กติกาและรางวัลอาจเปลี่ยนแปลงตามที่แอดมินประกาศในแชท')


def shop_page():
    body = f"""
<div class="wrap">
  <div class="hero">
    <div><span class="eyebrow">คู่มือโหมดร้านค้า</span>
      <h1>ขายของเหนื่อยแล้ว<br><span class="grad">ให้น้องออมสินจดให้</span></h1>
      <p>สำหรับพ่อค้าแม่ค้า ตลาดนัด หน้าร้าน และร้านออนไลน์ จดยอดขาย ต้นทุน ดูกำไรรายวัน แล้วเอาไปใช้ยื่นภาษีได้ทันที โดยไม่ต้องมีสมุดบัญชี</p>
      <a class="btn line" href="{ask('เปิดโหมดร้านค้า')}">🏪 เปิดโหมดร้านค้าใน LINE</a> <a class="btn ghost" href="#start">เริ่มยังไง</a></div>
    <img src="img/mascot/slip.webp" alt="น้องออมสิน">
  </div>
  <div class="tocwrap"><nav class="toc"><a href="#start">เริ่มใช้</a><a href="#cash">ขายเงินสด</a><a href="#scan">ลูกค้าสแกนจ่าย</a><a href="#sms">SMS อัตโนมัติ</a><a href="#online">ขายออนไลน์</a><a href="#cost">ต้นทุน & ร้านส่ง</a><a href="#profit">ดูกำไร</a><a href="#tax">ภาษี</a><a href="#faq">ถามบ่อย</a></nav></div>

  <section id="start"><h2>เริ่มใช้ใน 10 วินาที</h2><p class="lead">พิมพ์คำเดียวในแชทน้องออมสิน</p>
    <div class="card">
      <div class="step"><div class="n">1</div><div>พิมพ์ <span class="chat">เปิดโหมดร้านค้า</span> (ฟีเจอร์ Pro)</div></div>
      <div class="step"><div class="n">2</div><div>ระบบเพิ่มหมวด <b>ขายของ/ธุรกิจ</b> (ยอดขาย) และ <b>ต้นทุนสินค้า</b> ให้เอง</div></div>
      <div class="step"><div class="n">3</div><div>เลือกวิธีจดที่เหมาะกับร้านคุณด้านล่าง ใช้ผสมกันได้ทุกวิธี · ปิดเมื่อไหร่ก็ได้ด้วย <span class="chat">ปิดโหมดร้านค้า</span></div></div></div></section>

  <section id="cash"><h2>💵 ลูกค้าจ่ายเงินสด</h2><p class="lead">พิมพ์เครื่องหมายบวกตามด้วยยอด เร็วที่สุด ไม่ต้องบอกว่าขายอะไร</p>
    <div class="grid"><div class="card"><h3>ขาย 1 ออร์เดอร์</h3><p><span class="chat">+50</span></p></div>
      <div class="card"><h3>รวบหลายออร์เดอร์ทีเดียว</h3><p><span class="chat">+50 +35 +120</span> = 3 ออร์เดอร์</p></div></div>
    <div class="note">อยากรู้ว่าอะไรขายดี? พิมพ์แบบมีชื่อสินค้า เช่น <span class="chat">ขายส้มตำ 3 จาน 150</span> น้องออมสินจะจัดอันดับสินค้าขายดีให้</div></section>

  <section id="scan"><h2>📲 ลูกค้าสแกนจ่ายหน้าร้าน</h2><p class="lead">ลูกค้าไม่ได้ส่งสลิปให้เรา ใช้หน้าจอมือถือของแม่ค้าเองได้เลย</p>
    <div class="grid"><div class="card"><h3>แคปแชท LINE ธนาคาร</h3><p>เปิดแชทธนาคารที่มีการ์ด "เงินเข้า" แคปหน้าจอ ส่งมา 1 รูปได้หลายรายการ ส่งทีละหลายรูปก็ได้</p></div>
      <div class="card"><h3>แคปประวัติรายการ</h3><p>ปิดร้านตอนเย็น แคปหน้า "รายการเดินบัญชี" ในแอปธนาคาร ได้ครบทั้งวันในไม่กี่รูป</p></div></div>
    <div class="note">น้องออมสินจำเวลาและยอดของแต่ละรายการ <b>แคปซ้ำไม่บันทึกซ้ำ</b> ตรวจแล้วกดยืนยันครั้งเดียว</div></section>

  <section id="sms"><h2>📩 SMS เงินเข้า → จดเองอัตโนมัติ</h2><p class="lead">ตั้งครั้งเดียว ทุกครั้งที่มี SMS เงินเข้า น้องออมสินบันทึกยอดขายและทักบอกยอดรวมวันนี้</p>
    <div class="card">
      <div class="step"><div class="n">1</div><div>พิมพ์ <span class="chat">เชื่อม SMS</span> รับลิงก์ส่วนตัว (ห้ามให้คนอื่น)</div></div>
      <div class="step"><div class="n">2</div><div><b>iPhone:</b> แอป "คำสั่งลัด" → ระบบอัตโนมัติ → ข้อความ → "ข้อความมี" เงินเข้า → เรียกใช้ทันที → "รับเนื้อหาของ URL" แบบ POST ส่งช่อง <b>text</b> = ข้อความ</div></div>
      <div class="step"><div class="n">3</div><div><b>Android:</b> แอป MacroDroid → ทริกเกอร์ "SMS ที่ได้รับ" (SMS จริง ไม่ใช่ RCS หรือแจ้งเตือนแอปธนาคาร) → HTTP Request แบบ POST ไปที่ลิงก์</div></div>
      <div class="step"><div class="n">4</div><div>เลิกใช้: <span class="chat">ยกเลิก SMS</span> ลิงก์เดิมใช้ไม่ได้ทันที</div></div></div>
    <div class="note">SMS เงินออกจะถูกข้าม · iPhone อ่านได้เฉพาะ SMS (อ่านแจ้งเตือนแอปธนาคารไม่ได้) ถ้าธนาคารไม่ส่ง SMS ใช้วิธีแคปหน้าจอแทน</div></section>

  <section id="online"><h2>🛍️ ขายออนไลน์</h2><p class="lead">ลูกค้าส่งสลิปมาในแชทร้าน? ส่งต่อรูปสลิปนั้นให้น้องออมสิน</p>
    <div class="say"><img src="img/mascot/guide.webp" alt=""><div>สลิปเงินเข้าจะถูกบันทึกเป็น <b>ยอดขาย</b> ทันทีโดยไม่ต้องตอบคำถาม พร้อมบอกยอดขายรวมวันนี้ ถ้าไม่ใช่ยอดขาย พิมพ์ <span class="chat">ไม่ใช่ยอดขาย</span> น้องออมสินจะลบแล้วถามใหม่ค่ะ</div></div></section>

  <section id="cost"><h2>📦 ต้นทุน & ร้านส่ง</h2><p class="lead">ซื้อวัตถุดิบ ของมาขาย บรรจุภัณฑ์ นับเป็นต้นทุน ให้เห็นกำไรจริง</p>
    <div class="card">
      <div class="step"><div class="n">1</div><div>ส่งสลิป/ใบเสร็จตอนซื้อของเข้าร้าน แล้วกดปุ่ม <b>📦 ต้นทุนร้าน</b> ครั้งแรกครั้งเดียว</div></div>
      <div class="step"><div class="n">2</div><div>น้องออมสินจำร้านนั้นเป็น <b>ร้านส่ง</b> ครั้งต่อไปโอนให้ร้านเดิม = ต้นทุนอัตโนมัติ (ใบเสร็จหลายรายการก็เช่นกัน)</div></div>
      <div class="step"><div class="n">3</div><div>ดูรายชื่อ <span class="chat">ร้านส่ง</span> · ลบ <span class="chat">ลบร้านส่ง แม็คโคร</span> · บันทึกผิด <span class="chat">ไม่ใช่ต้นทุน</span></div></div>
      <div class="step"><div class="n">4</div><div>พิมพ์เองก็ได้ <span class="chat">ซื้อหมูมาทำลูกชิ้น 800</span></div></div></div></section>

  <section id="profit"><h2>📊 ดูกำไร</h2><p class="lead">ยอดขาย − ต้นทุน = กำไร พร้อมอัตรากำไร วันที่ขายดีที่สุด และสินค้าขายดี 5 อันดับ</p>
    <div class="grid3"><div class="card"><p><span class="chat">สรุปร้านวันนี้</span></p></div><div class="card"><p><span class="chat">สรุปร้านเดือนนี้</span></p></div><div class="card"><p><span class="chat">สรุปร้านปีนี้</span></p></div></div></section>

  <section id="tax"><h2>🧾 เชื่อมกับภาษีให้เอง</h2>
    <div class="say"><img src="img/mascot/thumbsup.webp" alt=""><div>ยอดขายทั้งหมดถูกนับเป็นรายได้ประเภท <b>"ค้าขาย" (40(8))</b> หักค่าใช้จ่ายเหมา 60% โดยไม่ต้องใช้ใบเสร็จ พิมพ์ <span class="chat">สรุปภาษี</span> ดูว่าต้องยื่นหรือเสียเท่าไหร่ · <a href="tax.html#shop">อ่านภาษีสำหรับแม่ค้า</a></div></div></section>

  <section id="faq"><h2>คำถามที่พบบ่อย</h2>
    <details><summary>เงินส่วนตัวโอนเข้าบัญชีเดียวกัน จะถูกนับเป็นยอดขายไหม?</summary><p>สลิปเงินเข้าจะถูกนับเป็นยอดขายอัตโนมัติ ถ้าไม่ใช่ พิมพ์ <span class="chat">ไม่ใช่ยอดขาย</span> หรือ <span class="chat">ลบล่าสุด</span> · ถ้าโอนเข้าบัญชีตัวเอง (ชื่อผู้โอนผู้รับตรงกัน) น้องออมสินจะถามก่อน</p></details>
    <details><summary>ใช้ในกลุ่ม LINE ได้ไหม?</summary><p>โหมดร้านค้าใช้ในแชทส่วนตัวเท่านั้นค่ะ</p></details>
    <details><summary>น้องออมสินอ่านรูปในมือถือเองได้ไหม?</summary><p>LINE ไม่อนุญาตให้บอทเปิดอัลบั้มหรือ SMS ในเครื่อง ต้องส่งรูปมาเอง หรือใช้ระบบ SMS อัตโนมัติด้านบน</p></details>
    <details><summary>ข้อมูลร้านปลอดภัยไหม?</summary><p>ข้อมูลถูกเข้ารหัสและเห็นได้เฉพาะเจ้าของบัญชี ลิงก์ SMS ยกเลิกได้ทุกเมื่อ</p></details></section>
</div>"""
    return HEAD.format(title="คู่มือโหมดร้านค้า · N'AOMSIN", desc='จดยอดขาย ต้นทุน กำไร สำหรับพ่อค้าแม่ค้า ตลาดนัด หน้าร้าน และออนไลน์ กับน้องออมสิน', ask=ask('เปิดโหมดร้านค้า')) + body + FOOT.format(ask=ask('สรุปร้านวันนี้'), extra='ฟีเจอร์โหมดร้านค้าเป็นส่วนหนึ่งของแพ็กเกจ Pro')


def sms_page():
    dl = 'https://ihgdueeaslmfkbdaxqlm.supabase.co/functions/v1/naomsin/dl/'
    body = """
<style>
  .sx {{ max-width:520px; margin:0 auto; }}
  .sx .steps {{ background:#fff; border-radius:22px; padding:8px 18px; box-shadow:0 10px 30px rgba(15,59,125,.08); }}
  .sx .st {{ display:flex; gap:14px; align-items:flex-start; padding:16px 0; border-bottom:1px solid #EEF2F7; }}
  .sx .st:last-child {{ border-bottom:0; }}
  .sx .no {{ flex:0 0 30px; height:30px; border-radius:50%; background:var(--grad); color:#fff; font-weight:700; font-size:15px; display:flex; align-items:center; justify-content:center; margin-top:2px; }}
  .sx .tx {{ flex:1; min-width:0; font-size:16px; line-height:1.55; color:var(--ink); }}
  .sx .tx b {{ font-weight:700; }}
  .sx .hint {{ display:block; font-size:13.5px; color:#6B7280; margin-top:4px; }}
  .sx .act {{ display:inline-flex; align-items:center; gap:6px; margin-top:10px; padding:10px 18px; border-radius:999px; font-size:15px; font-weight:700; text-decoration:none; white-space:nowrap; border:0; cursor:pointer; font-family:inherit; }}
  .sx .act.pri {{ background:#06C755; color:#fff; box-shadow:0 6px 16px rgba(6,199,85,.28); }}
  .sx .act.sec {{ background:#EEF5FF; color:var(--blue-d); }}
  .sx video {{ width:100%; border-radius:18px; display:block; background:#EAF3FF; }}
  .sx .ext {{ background:#FFF7E6; border:1px solid #FFE1A8; border-radius:16px; padding:14px 16px; font-size:15px; margin:14px 0; display:none; }}
  .sx .setting {{ display:block; background:#F1F7FF; border:1px solid #DCEBFC; border-radius:12px; padding:9px 12px; margin-top:8px; font-size:14px; line-height:1.6; }}
  .sx .setting b {{ color:#1864AB; }}
  .sx .test-result {{ font-size:14px; margin:8px 0 0; }}
  .sx .shot-row {{ display:flex; gap:12px; overflow-x:auto; scroll-snap-type:x mandatory; padding:12px 2px 8px; margin-top:6px; }}
  .sx .shot {{ flex:0 0 min(68vw,210px); margin:0; scroll-snap-align:start; }}
  .sx .shot img {{ display:block; width:100%; aspect-ratio:1080/2193; object-fit:cover; object-position:top; border:1px solid #DCE6F3; border-radius:12px; background:#202936; }}
  .sx .shot figcaption {{ font-size:13px; line-height:1.4; color:#355276; margin-top:6px; }}
  .sx .shot-tip {{ display:block; font-size:12px; color:#65748A; margin-top:4px; }}
  .sx .lang-note {{ background:#EFF8F0; border:1px solid #CFEDD2; border-radius:14px; padding:11px 14px; margin:0 0 14px; font-size:13.5px; line-height:1.55; }}
</style>
<div class="wrap sx">
  <div style="text-align:center;padding:14px 0 4px"><img src="img/mascot/slip.webp" alt="" style="width:96px;margin:0 auto">
    <h1 style="font-size:26px;margin:6px 0 4px">ให้น้องออมสินจดเงินโอน</h1>
    <p class="lead" style="margin:0 0 14px;font-size:15.5px"><b>ทำครั้งเดียวจบ</b> ต่อไปลูกค้าโอนมา ระบบจดยอดขายให้เอง</p></div>
  <div id="ext" class="ext">⚠️ เบราว์เซอร์ใน LINE ดาวน์โหลดไฟล์ไม่ได้ <a id="extLink" href="#" style="font-weight:700">แตะที่นี่เพื่อเปิดใน Chrome / Safari</a></div>
  <div id="bad" class="note" style="display:none">ลิงก์ไม่ครบ กรุณากดปุ่มจากแชทน้องออมสินอีกครั้งค่ะ</div>

  <div id="ios" style="display:none">
    <div id="safari" class="ext" style="display:none">💡 เปิดใน <b>Safari</b> จะติดตั้งง่ายกว่า (ไม่ต้องผ่านแอปไฟล์) <a id="safLink" class="act sec" href="#">🧭 เปิดใน Safari</a></div>
    <video src="DLios.mp4?v=2" controls playsinline muted autoplay loop preload="metadata"></video>
    <p class="lead" style="text-align:center;margin:8px 0 14px;font-size:13.5px">🎬 วิดีโอจากหน้าจอ iPhone จริง ดูแล้วทำตามได้เลย</p>
    <div class="steps">
      <div class="st"><div class="no">1</div><div class="tx"><b>คัดลอกรหัสร้าน</b><br><button class="act pri cp">📋 คัดลอก</button></div></div>
      <div class="st"><div class="no">2</div><div class="tx"><b>ติดตั้งตัวช่วยจด</b><span class="hint">กด "ตั้งค่าคำสั่งลัด" → กดค้างในช่อง แล้วกด "วาง" → กด "เพิ่มคำสั่งลัด"</span><a class="act sec" href="DLios.shortcut">➕ ติดตั้ง</a></div></div>
      <div class="st"><div class="no">3</div><div class="tx"><b>กด ▶ 1 ครั้ง</b> แล้วกด <b>อนุญาต</b><span class="hint">iPhone ถามแค่ครั้งแรก</span></div></div>
      <div class="st"><div class="no">4</div><div class="tx">แอป <b>คำสั่งลัด</b> → <b>ระบบอัตโนมัติ</b> → <b>＋</b> → <b>ข้อความ</b></div></div>
      <div class="st"><div class="no">5</div><div class="tx">"ข้อความมี" พิมพ์ <b>เงินเข้า</b> → <b>เรียกใช้ทันที</b> → เลือก <b>น้องออมสินจดเงินเข้า</b> ✅</div></div></div></div>

  <div id="android" style="display:none">
    <video src="android-macrodroid.mp4?v=3" poster="android-macrodroid-poster.png?v=3" controls playsinline muted autoplay loop preload="metadata" aria-label="วิดีโอสอนตั้งค่า SMS บน Android ด้วย MacroDroid จากภาพหน้าจอจริง"></video>
    <p class="lead" style="text-align:center;margin:8px 0 14px;font-size:13.5px">🎬 วิดีโอจากภาพหน้าจอ MacroDroid จริง หยุดภาพเพื่อทำตามทีละขั้นได้</p>
    <div class="lang-note">ภาพหน้าจอเป็นเมนูภาษาอังกฤษ หากแอปของคุณเป็นภาษาไทย ให้ดูคำแปลในวงเล็บหลังชื่อเมนู ตำแหน่งหรือคำแปลอาจต่างกันตามรุ่นของแอป</div>
    <div class="steps">
      <div class="st"><div class="no">1</div><div class="tx"><b>ติดตั้ง MacroDroid</b><span class="hint">เปิดแอปและอนุญาตสิทธิ์ SMS เมื่อระบบถาม วิธีนี้ใช้กับ SMS จริงที่เข้าเครื่องนี้</span><a class="act pri" href="https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid">⬇️ เปิด Play Store</a></div></div>
      <div class="st"><div class="no">2</div><div class="tx"><b>ตรวจและคัดลอกลิงก์ร้าน</b><span class="hint">ทดสอบลิงก์ก่อน ระบบจะไม่จดรายการหรือหักแต้ม</span><button class="act pri test-sms" type="button">🔌 ทดสอบลิงก์ร้าน</button> <button class="act sec cpu" type="button">📋 คัดลอกลิงก์</button><p class="test-result" role="status" aria-live="polite"></p></div></div>
      <div class="st"><div class="no">3</div><div class="tx"><b>สร้างมาโครใหม่</b> หน้าแรกแตะ <b>Add Macro (เพิ่มมาโคร)</b> แล้วแตะ ＋ ในกรอบ <b>Triggers (ทริกเกอร์)</b><div class="shot-row"><figure class="shot"><a href="img/sms-guide/home.jpg" target="_blank" rel="noopener"><img src="img/sms-guide/home.jpg" loading="lazy" alt="หน้าแรก MacroDroid มีปุ่ม Add Macro"></a><figcaption>1. Add Macro (เพิ่มมาโคร)</figcaption></figure><figure class="shot"><a href="img/sms-guide/new-macro.jpg" target="_blank" rel="noopener"><img src="img/sms-guide/new-macro.jpg" loading="lazy" alt="หน้าสร้างมาโครมีกรอบ Triggers และ Actions"></a><figcaption>2. Triggers ＋ (เพิ่มทริกเกอร์)</figcaption></figure></div><span class="shot-tip">แตะภาพเพื่อขยาย · เลื่อนภาพไปทางซ้ายเพื่อดูภาพถัดไป</span></div></div>
      <div class="st"><div class="no">4</div><div class="tx"><b>ตั้ง SMS Received (ได้รับ SMS)</b> เลือก <b>Call/SMS (โทรศัพท์/SMS)</b> → <b>SMS Received (ได้รับ SMS)</b> → <b>Any Number (ทุกหมายเลข)</b><span class="setting">ในหน้า <b>SMS Content (เนื้อหา SMS)</b> เปลี่ยนจาก <b>Any (ทั้งหมด)</b> เป็น <b>Contains (มีคำว่า)</b> แล้วใส่คำที่มีใน SMS เงินเข้าของธนาคารจริง เช่น <b>เงินเข้า</b> หรือ <b>รับโอน</b> จากนั้นแตะ OK</span><div class="shot-row"><figure class="shot"><a href="img/sms-guide/trigger-category.jpg" target="_blank" rel="noopener"><img src="img/sms-guide/trigger-category.jpg" loading="lazy" alt="เมนู Add Trigger แสดงหมวด Call/SMS"></a><figcaption>Call/SMS (โทรศัพท์/SMS)</figcaption></figure><figure class="shot"><a href="img/sms-guide/sms-trigger.jpg" target="_blank" rel="noopener"><img src="img/sms-guide/sms-trigger.jpg" loading="lazy" alt="หมวด Call/SMS แสดง SMS Received"></a><figcaption>SMS Received (ได้รับ SMS)</figcaption></figure><figure class="shot"><a href="img/sms-guide/sender.jpg" target="_blank" rel="noopener"><img src="img/sms-guide/sender.jpg" loading="lazy" alt="ตัวเลือกผู้ส่ง Any Number"></a><figcaption>Any Number (ทุกหมายเลข)</figcaption></figure><figure class="shot"><a href="img/sms-guide/sms-content.jpg" target="_blank" rel="noopener"><img src="img/sms-guide/sms-content.jpg" loading="lazy" alt="หน้า SMS Content แสดง Any ที่เลือกอยู่และ Contains ที่ต้องเลือก"></a><figcaption>เปลี่ยน Any เป็น Contains (มีคำว่า)</figcaption></figure></div><span class="hint">ภาพหน้า SMS Content ยังเลือก Any อยู่ ให้แตะ Contains เอง คู่มือนี้ใช้กับ SMS จริง ไม่ใช่ RCS หรือการแจ้งเตือนในแอปธนาคาร</span></div></div>
      <div class="st"><div class="no">5</div><div class="tx"><b>ตั้ง HTTP Request (คำขอ HTTP)</b> แตะ ＋ ในกรอบ <b>Actions (การกระทำ)</b> แล้วใช้รูปแว่นขยายค้นหา <b>HTTP Request</b><span class="setting"><b>Settings (ตั้งค่า):</b> เปลี่ยน Request method จาก <b>GET เป็น POST</b> และวางลิงก์ร้านจากขั้นที่ 2 ในช่อง <b>Enter url (ใส่ URL)</b><br><b>Content Body (เนื้อหาคำขอ):</b> เลือกชนิด <b>text/plain</b> แล้วในช่องข้อความแตะปุ่ม <b>… / Magic Text (ข้อความพิเศษ)</b> เลือก <b>Incoming SMS message (ข้อความ SMS ที่ได้รับ)</b></span><div class="shot-row"><figure class="shot"><a href="img/sms-guide/actions.jpg" target="_blank" rel="noopener"><img src="img/sms-guide/actions.jpg" loading="lazy" alt="หน้า Add Action มีปุ่มค้นหามุมขวาบน"></a><figcaption>Actions ＋ แล้วค้นหา HTTP Request</figcaption></figure><figure class="shot"><a href="img/sms-guide/http-settings.jpg" target="_blank" rel="noopener"><img src="img/sms-guide/http-settings.jpg" loading="lazy" alt="หน้า HTTP Request ยังแสดง GET ค่าเริ่มต้นและช่อง Enter url"></a><figcaption>เปลี่ยน GET → POST แล้ววางลิงก์</figcaption></figure><figure class="shot"><a href="img/sms-guide/sms-magic.jpg" target="_blank" rel="noopener"><img src="img/sms-guide/sms-magic.jpg" loading="lazy" alt="เมนู Magic Text มี Incoming SMS message เป็นตัวเลือกแถวที่สอง"></a><figcaption>เลือก Incoming SMS message แถวที่ 2</figcaption></figure></div><span class="hint">ภาพ Settings ยังเป็น GET และภาพ Magic Text ยังเลือก Incoming SMS contact อยู่ ให้เปลี่ยนตามคำอธิบายด้านบน อย่าใส่ลิงก์ร้านใน body และอย่าพิมพ์คำว่า sms_message แทนการเลือก Magic Text</span></div></div>
      <div class="st"><div class="no">6</div><div class="tx"><b>บันทึกและเปิดมาโคร</b> ตั้งชื่อ “น้องออมสินจดเงินเข้า” → แตะเครื่องหมายถูกเพื่อบันทึก → ตรวจว่า MacroDroid และมาโครเปิดใช้งานอยู่ → อนุญาตสิทธิ์ที่แอปถามให้ครบ<div class="shot-row"><figure class="shot"><a href="img/sms-guide/macro-ready.jpg" target="_blank" rel="noopener"><img src="img/sms-guide/macro-ready.jpg" loading="lazy" alt="หน้าสรุปมาโครแสดง SMS from Any Number และ HTTP Request POST"></a><figcaption>หน้าสรุปควรมี Trigger SMS และ Action POST</figcaption></figure></div></div></div>
      <div class="st"><div class="no">7</div><div class="tx"><b>ลองรับ SMS เงินเข้าจริง</b> ให้มีเงินโอนเข้าบัญชีร้าน แล้วดูข้อความตอบใน LINE<span class="hint">การกด Run/Test มาโครเองไม่สร้างข้อความ SMS สำหรับ Magic Text ต้องให้ทริกเกอร์ SMS ทำงานจริง</span></div></div>
    </div>
    <details><summary>ตั้งแล้วไม่จด? ตรวจทีละจุด</summary><ol><li>เปิด <b>System Log</b> ใน MacroDroid ถ้าไม่เห็นมาโครทำงาน ให้ตรวจคำในทริกเกอร์ สิทธิ์ SMS และว่าเป็น SMS จริงหรือแจ้งเตือนจากแอป</li><li>ถ้ามาโครทำงานแต่ไม่จด ตรวจว่า HTTP Request เป็น POST, URL มี <b>?t=รหัสร้าน</b>, Content Body เป็น text/plain และใช้ Magic Text ของ SMS</li><li>ถ้าขึ้น <b>invalid token</b> ให้พิมพ์ “เชื่อม SMS” ใน LINE แล้วคัดลอกลิงก์ใหม่; ถ้าขึ้น <b>shop mode off</b> ให้เปิดโหมดร้านค้าและตรวจสิทธิ์ Pro</li><li>ถ้าระบบแจ้งว่าไม่ใช่เงินเข้า ตรวจว่า SMS มีคำเงินเข้าและยอดเงินจริงที่ระบบอ่านได้</li></ol></details>
  </div>

  <div class="say" style="margin-top:16px"><img src="img/mascot/guide.webp" alt=""><div style="font-size:15px">ลองให้ใครโอนมา 1 บาท น้องออมสินจะทักใน LINE ว่า <b>"เชื่อม SMS สำเร็จ"</b></div></div>
</div>
<script>(function(){{var t=(location.hash.match(/t=([a-z0-9]+)/i)||[])[1];if(!t){{document.getElementById('bad').style.display='block';return;}}
var ua=navigator.userAgent,ios=/iPhone|iPad|iPod/.test(ua)||(/Mac/.test(ua)&&'ontouchend'in document);
if(/ Line\\//i.test(ua)){{var u=location.origin+location.pathname+'?openExternalBrowser=1'+location.hash;
  if(!/openExternalBrowser=1/.test(location.search)){{location.replace(u);}}
  document.getElementById('extLink').href=u;document.getElementById('ext').style.display='block';}}
document.getElementById(ios?'ios':'android').style.display='block';
if(ios&&/CriOS|FxiOS|EdgiOS/.test(ua)){{document.getElementById('safLink').href='x-safari-'+location.origin+location.pathname+location.hash;document.getElementById('safari').style.display='block';}}
var su='https://ihgdueeaslmfkbdaxqlm.supabase.co/functions/v1/naomsin/sms?t='+t;
[].forEach.call(document.querySelectorAll('.test-sms'),function(b){{b.onclick=async function(){{var out=document.querySelector('.test-result');b.disabled=true;out.textContent='กำลังตรวจลิงก์ร้าน…';try{{var res=await fetch(su,{{method:'POST',headers:{{'Content-Type':'text/plain'}},body:'N AOMSIN connection check'}});var j=await res.json();out.textContent=j.ok?'✅ ลิงก์ร้านใช้ได้แล้ว ต่อไปตั้ง MacroDroid':'❌ '+(j.reason==='invalid token'?'รหัสร้านใช้ไม่ได้ ให้กด “เชื่อม SMS” ใน LINE ใหม่':j.reason==='shop mode off'?'โหมดร้านค้าปิดอยู่หรือสิทธิ์ Pro ยังไม่พร้อม':'ตรวจลิงก์ร้านและลองอีกครั้ง');}}catch(e){{out.textContent='❌ ติดต่อระบบไม่ได้ ตรวจอินเทอร์เน็ตแล้วลองใหม่';}}finally{{b.disabled=false;}}}};}});
[].forEach.call(document.querySelectorAll('.cpu'),function(b){{b.onclick=function(){{navigator.clipboard.writeText(su).then(function(){{b.textContent='✅ คัดลอกแล้ว';}}).catch(function(){{window.prompt('คัดลอกลิงก์ร้าน',su);}});}};}});
[].forEach.call(document.querySelectorAll('.cp'),function(b){{b.onclick=function(){{navigator.clipboard.writeText(t).then(function(){{b.textContent='✅ คัดลอกแล้ว';}});}};}});}})();</script>"""
    body = body.replace('DL', dl).replace('{{', '{').replace('}}', '}')
    return HEAD.format(title="เชื่อม SMS · N'AOMSIN", desc='ให้น้องออมสินจดเงินโอนเข้าร้านอัตโนมัติ', ask=ask('สรุปร้านวันนี้')) + body + FOOT.format(ask=ask('สรุปร้านวันนี้'), extra='รหัสร้านเป็นความลับ อย่าส่งให้คนอื่น')

if __name__ == '__main__':
    data = json.load(open(sys.argv[1], encoding='utf-8'))
    open(os.path.join(HERE, 'tax.html'), 'w', encoding='utf-8').write(tax_page(data))
    open(os.path.join(HERE, 'missions.html'), 'w', encoding='utf-8').write(missions_page())
    open(os.path.join(HERE, 'shop.html'), 'w', encoding='utf-8').write(shop_page())
    open(os.path.join(HERE, 'sms.html'), 'w', encoding='utf-8').write(sms_page())
    print('ok')
