#!/usr/bin/env python3
"""TEAM SWYK サイト v3（スリム公開版：23ページ→11ページ、重複統合・メモ削除）"""
import os, shutil

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(SRC, "site_v3")
LINE_URL = "https://line.me/ti/p/22-lX5DSVm"
WA_URL = "https://wa.me/817023172503?s=p"
EMAIL = "hirosetakuya0225@gmail.com"
from urllib.parse import quote as _q
MAIL_URL = f"mailto:{EMAIL}?subject={_q('【TEAM SWYK】お問い合わせ')}"

CSS = """
:root{--navy:#16294d;--navy2:#1f3f73;--yellow:#ffc82e;--yellow2:#ffd95e;--cream:#fffbeb;--ink:#2b2b2b;--line:#e8e2d2}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:"Hiragino Kaku Gothic ProN","Hiragino Sans","Noto Sans JP",sans-serif;color:var(--ink);background:#fff;line-height:1.85}
img{max-width:100%;display:block}
a{color:var(--navy2)}
main{max-width:1080px;margin:0 auto;padding:0 16px 64px}
section{margin-top:54px;scroll-margin-top:96px}
h2.sec{color:var(--navy);font-size:clamp(22px,4.5vw,30px);text-align:center;margin:0 0 6px}
h2.sec .en{display:block;font-size:12px;letter-spacing:.35em;color:#b3941f;font-weight:800}
h3.sub{color:var(--navy);font-size:19px;margin:26px 0 8px}
.lead{text-align:center;color:#444;max-width:780px;margin:8px auto 22px}
.lead-l{color:#444;max-width:820px;margin:8px 0 16px}
header.site{position:sticky;top:0;z-index:20;background:#fff;border-bottom:2px solid var(--yellow);box-shadow:0 2px 12px rgba(21,42,78,.08)}
header.site .in{max-width:1080px;margin:0 auto;padding:8px 16px;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
header.site a.brand{display:flex;align-items:center;gap:10px;text-decoration:none}
header.site img.logo{width:40px;height:40px;object-fit:contain}
header.site .name{font-weight:900;color:var(--navy);font-size:17px;letter-spacing:.03em;line-height:1.15}
header.site .name small{display:block;font-size:10px;color:#8a7a3a;letter-spacing:.18em}
header.site nav.main{margin-left:auto;display:flex;gap:13px;font-size:13px;font-weight:700;flex-wrap:wrap}
header.site nav.main a{color:var(--navy);text-decoration:none}
header.site nav.main a.cta{background:var(--navy);color:#fff;border-radius:999px;padding:3px 12px}
.lang{display:flex;gap:6px;margin-left:8px}
.lang a{font-size:12px;font-weight:800;text-decoration:none;border:1.5px solid var(--navy);color:var(--navy);border-radius:999px;padding:2px 10px}
.lang a.on{background:var(--yellow);border-color:var(--yellow)}
details.mnav{display:none;width:100%}
details.mnav summary{cursor:pointer;font-weight:800;color:var(--navy);padding:6px 0;list-style:none}
details.mnav nav{display:grid;gap:2px;padding:6px 0 10px}
details.mnav nav a{color:var(--navy);text-decoration:none;font-weight:700;padding:7px 10px;border-radius:8px;background:var(--cream)}
@media(max-width:900px){header.site nav.main{display:none}details.mnav{display:block}.lang{margin-left:auto}}
.hero{margin:0 -16px;background:var(--cream);padding:26px 16px 30px;border-radius:0 0 26px 26px}
.hero .photo{max-width:880px;margin:0 auto;border-radius:18px;overflow:hidden;box-shadow:0 10px 28px rgba(21,42,78,.20)}
.hero .cap{max-width:880px;margin:8px auto 0;font-size:12.5px;color:#6b6136;text-align:right}
.hero h1{color:var(--navy);text-align:center;font-size:clamp(30px,7vw,52px);margin:20px 0 6px;font-weight:900;line-height:1.35}
.hero .sub{text-align:center;color:#4a3f14;font-weight:600;max-width:760px;margin:0 auto}
.entries{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:20px}
.entry{background:#fff;border:2px solid var(--yellow);border-radius:14px;padding:16px;text-decoration:none;color:var(--ink)}
.entry b{color:var(--navy);font-size:16.5px;display:block;margin-bottom:4px}
.entry span{font-size:13.5px;color:#555}
.pagehead{margin:0 -16px;background:linear-gradient(180deg,#fff3c4,var(--yellow2));padding:34px 16px 24px;border-radius:0 0 24px 24px;text-align:center}
.pagehead h1{color:var(--navy);margin:0;font-size:clamp(25px,5.5vw,38px)}
.pagehead p{color:#4a3f14;font-weight:600;margin:6px auto 0;max-width:740px}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}
.card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:20px;box-shadow:0 3px 10px rgba(21,42,78,.05)}
.card h3{color:var(--navy);margin:0 0 8px;font-size:18px}
.card p{margin:0 0 12px;font-size:14.5px;color:#444}
.card .more{font-weight:800;text-decoration:none}
.card img{border-radius:12px;margin-bottom:12px;width:100%;height:auto}
.st{display:inline-block;font-size:11.5px;font-weight:800;border-radius:999px;padding:1px 10px;margin-bottom:8px}
.st-now{background:var(--yellow);color:var(--navy)}
.st-done{background:#e5e7eb;color:#4b5563}
.values{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-top:18px}
.values .v{background:var(--cream);border:2px solid var(--yellow);border-radius:14px;padding:16px;text-align:center}
.values .v b{font-size:26px;color:var(--navy);display:block}
.values .v span{font-weight:800;color:var(--navy);display:block}
.photo{border-radius:16px;overflow:hidden;margin:22px auto;max-width:820px;box-shadow:0 8px 22px rgba(21,42,78,.15)}
.photo img{width:100%;height:auto}
table.kv{width:100%;border-collapse:collapse;background:#fff;font-size:14.5px}
table.kv th,table.kv td{border-bottom:1px solid var(--line);padding:10px 12px;text-align:left;vertical-align:top}
table.kv th{background:#fff7dd;color:var(--navy);white-space:nowrap;width:130px}
ul.tight{margin:6px 0;padding-left:20px}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips span{background:#fff;border:1px solid var(--line);border-radius:999px;padding:4px 12px;font-size:13px}
.chips a{background:#fff;border:1.5px solid var(--navy);border-radius:999px;padding:4px 14px;font-size:13.5px;font-weight:800;text-decoration:none;color:var(--navy)}
.gallery{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:16px}
.gallery figure{margin:0;border-radius:14px;overflow:hidden;background:#fff;border:1px solid var(--line)}
.gallery img{width:100%;height:auto}
.gallery figcaption{font-size:12.5px;color:#555;padding:6px 10px}
.btn{display:inline-block;background:var(--navy);color:#fff !important;text-decoration:none;font-weight:800;border-radius:999px;padding:12px 26px}
.btn.y{background:var(--yellow);color:var(--navy) !important}
.btn.line-b{background:#06c755;color:#fff !important}
.btn.wa{background:#25d366;color:#1c4d2e !important}
.btnrow{display:flex;gap:10px;flex-wrap:wrap;justify-content:center;margin-top:14px}
.flow{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;counter-reset:step}
.flow .f{background:var(--cream);border-radius:14px;padding:16px}
.flow .f b{color:var(--navy);display:block;margin-bottom:4px}
.flow .f p{margin:0;font-size:14px;color:#444}
.diagram{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;align-items:stretch;margin-top:16px}
.diagram .node{background:#fff;border:2px solid var(--navy);color:var(--navy);font-weight:800;border-radius:14px;padding:12px 16px;text-align:center;min-width:130px}
.diagram .node small{display:block;font-weight:600;color:#555;font-size:12px}
.diagram .arr{align-self:center;color:#b3941f;font-weight:900;font-size:20px}
.cycle{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;margin-top:16px}
.cycle .c{background:#fff;border:1px solid var(--line);border-top:5px solid var(--yellow);border-radius:12px;padding:14px}
.cycle .c b{color:var(--navy)}
.timeline{max-width:780px;margin:0 auto}
.timeline .t{display:flex;gap:14px;padding:10px 0;border-bottom:1px dashed var(--line)}
.timeline .y{flex:0 0 118px;font-weight:800;color:var(--navy)}
footer.site{background:var(--navy);color:#dfe6f2;margin-top:70px}
footer.site .in{max-width:1080px;margin:0 auto;padding:28px 16px;font-size:13px}
footer.site .cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:18px}
footer.site a{color:#ffe9a8;text-decoration:none}
footer.site .name{color:#fff;font-weight:900;font-size:17px}
footer.site ul{list-style:none;margin:6px 0;padding:0}
footer.site li{margin:4px 0}
.back{display:inline-block;margin-top:26px;font-weight:700;text-decoration:none}
.quote{background:#fff;border-left:5px solid #f080a8;border-radius:0 14px 14px 0;padding:16px 18px;max-width:820px;margin:18px auto;font-size:15px}
.note{text-align:center;color:#666;font-size:13.5px;margin-top:14px}
@media(max-width:640px){.timeline .y{flex-basis:92px}table.kv th{width:96px}}
"""

NAV = [
    ("about.html", "TEAMSWYKについて"),
    ("activities.html", "活動紹介"),
    ("locations.html", "拠点・教室"),
    ("programs.html", "参加・プログラム"),
    ("work.html", "講演・仕事の依頼"),
    ("global.html", "海外活動・Brasil"),
    ("news.html", "お知らせ"),
]


def header(lang="ja"):
    nav = "".join(f'<a href="{u}">{t}</a>' for u, t in NAV)
    mnav = "".join(f'<a href="{u}">{t}</a>' for u, t in NAV + [("contact.html", "お問い合わせ"), ("pt.html", "Português（Para os brasileiros）")])
    if lang == "pt":
        lang_html = '<a href="index.html">日本語</a><a class="on" href="pt.html">Português</a>'
    else:
        lang_html = '<a class="on" href="index.html">日本語</a><a href="pt.html">Português</a>'
    return f"""<header class="site"><div class="in">
<a class="brand" href="index.html"><img class="logo" src="img/logo.png" alt="TEAM SWYK ロゴ">
<span class="name">TEAM SWYK<small>チーム さわやか</small></span></a>
<nav class="main">{nav}<a class="cta" href="contact.html">お問い合わせ</a></nav>
<div class="lang">{lang_html}</div>
<details class="mnav"><summary>☰ メニュー</summary><nav>{mnav}</nav></details>
</div></header>"""


FOOTER = f"""<footer class="site"><div class="in">
<div class="cols">
<div><div class="name">TEAM SWYK（チーム さわやか）</div>
<p>人とつながる。世界が広がる。<br>TEAMSWYK Conductor：廣瀬拓哉</p></div>
<div><b style="color:#fff">メニュー</b><ul>
<li><a href="about.html">TEAMSWYKについて</a></li>
<li><a href="activities.html">活動紹介</a></li>
<li><a href="locations.html">拠点・教室紹介</a></li>
<li><a href="programs.html">参加・プログラム</a></li>
<li><a href="work.html">講演・仕事のご依頼</a></li>
<li><a href="news.html">お知らせ</a></li>
</ul></div>
<div><b style="color:#fff">お問い合わせ</b><ul>
<li><a href="contact.html">お問い合わせについて</a></li>
<li><a href="{LINE_URL}" target="_blank" rel="noopener">LINEで相談する</a></li>
<li><a href="{WA_URL}" target="_blank" rel="noopener">WhatsAppで相談する</a></li>
<li><a href="{MAIL_URL}">メールで相談する</a></li>
</ul></div>
<div><b style="color:#fff">その他</b><ul>
<li><a href="pt.html">Português（Para os brasileiros）</a></li>
<li><a href="privacy.html">プライバシーポリシー</a></li>
</ul></div>
</div>
<p style="margin-top:18px">© 2026 TEAM SWYK</p>
</div></footer>"""


def page(title, body, desc="", lang="ja"):
    return ("<!DOCTYPE html>\n<html lang=\"ja\"><head><meta charset=\"UTF-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
            f"<title>{title}｜TEAM SWYK（チーム さわやか）</title>\n"
            f"<meta name=\"description\" content=\"{desc}\">\n"
            f"<style>{CSS}</style></head>\n<body>{header(lang)}<main>{body}</main>{FOOTER}</body></html>")


def head(title, sub):
    return f'<div class="pagehead"><h1>{title}</h1><p>{sub}</p></div>'


def cta_row():
    return ('<div class="btnrow">'
            '<a class="btn y" href="contact.html">相談・問い合わせについて</a>'
            f'<a class="btn line-b" href="{LINE_URL}" target="_blank" rel="noopener">LINEで相談する</a>'
            f'<a class="btn wa" href="{WA_URL}" target="_blank" rel="noopener">WhatsAppで相談する</a>'
            f'<a class="btn" href="{MAIL_URL}">メールで相談する</a>'
            '</div>')


VALUES = """
<div class="values">
<div class="v"><b>支え合う</b>関わる人と支え合う</div>
<div class="v"><b>分かり合う</b>それぞれの個性を知り、認め合う</div>
<div class="v"><b>やりきる</b>途中であきらめない</div>
<div class="v"><b>感動する</b>できた感動を全員で味わう</div>
</div>"""

# ---------------- トップ ----------------
index_body = """
<div class="hero">
<div class="photo"><img src="img/hero.jpg" alt="TEAMSWYK Conductor 廣瀬拓哉と、ブラジルの子どもたち"></div>
<p class="cap">TEAMSWYK Conductor 廣瀬拓哉と、ブラジルの子どもたち</p>
<h1>人とつながる。世界が広がる。</h1>
<p class="sub">TEAM SWYK（チーム さわやか）は、スポーツ・教育・地域交流・国際交流を通じて、人と人がつながり、新しい経験・学び・挑戦が生まれる活動です。</p>
<div class="entries">
<a class="entry" href="about.html"><b>TEAMSWYKを知る</b><span>理念・設立背景・コンダクター紹介</span></a>
<a class="entry" href="programs.html"><b>活動に参加する</b><span>参加できるプログラムのご案内</span></a>
<a class="entry" href="work.html"><b>講演・仕事を依頼する</b><span>学校園・自治体・企業・団体の方へ</span></a>
<a class="entry" href="global.html"><b>Brasil・海外</b><span>国際交流とブラジル向けサービスのご案内</span></a>
</div>
</div>

<section>
<h2 class="sec"><span class="en">PHILOSOPHY</span>大切にしている4つの考え方</h2>
<p class="lead">TEAM SWYKの名前は、この4つの言葉から生まれました。子ども、学生、大人がそれぞれの得意を活かして関わり、学んだ人が支える側にもなっていく。その循環を大切にしています。</p>
""" + VALUES + """
<p style="text-align:center;margin-top:16px"><a href="about.html" style="font-weight:800">理念について詳しく →</a></p>
</section>

<section>
<h2 class="sec"><span class="en">ACTIVITIES</span>活動と拠点</h2>
<p class="lead">国内の教育現場から、南米のグラウンドまで。詳しくは各ページでご紹介しています。</p>
<div class="cards">
<div class="card"><h3>活動紹介</h3><p>オンライン職業講話、放課後レッスン、ティーボール、国際交流、日本語教育、コミュニティなど、活動をまとめてご紹介します。</p><a class="more" href="activities.html">活動を見る →</a></div>
<div class="card"><h3>拠点・教室紹介</h3><p>TEAMSWYK JAPAN、奈良教室、新宮校、Brasil、松井ヶ丘保育園ティーボールスクールの5つの拠点をご紹介します。</p><a class="more" href="locations.html">拠点・教室を見る →</a></div>
<div class="card"><h3>海外活動・Brasil</h3><p>JICA海外協力隊としてのブラジル派遣をはじめ、南米での野球指導や国際交流に取り組んできました。</p><a class="more" href="global.html">海外活動を見る →</a></div>
</div>
</section>

<section>
<h2 class="sec"><span class="en">JOIN / WORK</span>参加とご依頼</h2>
<div class="cards">
<div class="card"><h3>参加できるプログラム</h3><p>ティーボールスクール、野球個別指導、日本語教育・学習支援、コミュニティイベントへの参加をご案内します。</p><a class="more" href="programs.html">プログラムを見る →</a></div>
<div class="card"><h3>講演・仕事のご依頼</h3><p>学校園での講演、国際理解教育、野球指導、教育プログラムの企画運営など、学校園・自治体・企業・団体からのご相談に対応します。</p><a class="more" href="work.html">依頼できる内容を見る →</a></div>
</div>
</section>

<section>
<h2 class="sec"><span class="en">NEWS &amp; CONTACT</span>お知らせ・お問い合わせ</h2>
<p class="lead">活動の様子や募集のお知らせは、お知らせページで発信していきます。ご相談はLINE・WhatsApp・メールからお気軽にどうぞ。</p>
<p style="text-align:center"><a class="btn" href="news.html">お知らせを見る</a></p>
""" + cta_row() + """
</section>
"""

# ---------------- TEAMSWYKについて＋コンダクター ----------------
_timeline = [
    ("2009 - 2013", "近畿大学（硬式野球部）"),
    ("2013 - 2017", "大阪府内公立中学校 社会科教員（寝屋川市立中木田中学校、枚方市立蹉跎中学校）"),
    ("2016", "TEAMSWYK（チーム さわやか）創設"),
    ("2017 - 2019", "JICA日系社会青年海外協力隊 野球隊員としてブラジルへ派遣"),
    ("2019.3", "「TEAMSWYK 日本遠征 Project」を企画・実施（ブラジルの子どもたち10人を枚方市へ）"),
    ("2019 - 2023", "履正社スポーツ専門学校 野球コース 監督・講師"),
    ("2020 -", "オンライン職業講話を開始（静岡学園高校の探究学習カリキュラムに導入）"),
    ("2021.9 -", "放課後レッスン「TEAMSWYK LESSON」開講"),
    ("2023.3", "松井ヶ丘保育園（京田辺市）TEAMSWYKティーボールスクール開校"),
    ("2024", "JICA大学連携 近畿大学 ペルー派遣コーディネーター／モンゴル・ペルーでの野球指導"),
]
_tl = "\n".join(f'<div class="t"><div class="y">{y}</div><div>{d}</div></div>' for y, d in _timeline)

about_body = head("TEAMSWYKについて", "人とつながる。世界が広がる。 ― 理念、設立背景、コンダクターをご紹介します") + """
<section style="margin-top:30px">
<h2 class="sec">理念と設立背景</h2>
<p class="lead">子どもの頃に出会う大人によって、人生が大きく変わる。ならば、出会うことができる「場」をつくりたい。TEAM SWYKは、子ども一人一人が「自分の人生はこれだ！」と自分を語れるように、きっかけをつくる活動です。</p>
<p class="lead-l">2016年、公立中学校の社会科教員だった廣瀬拓哉が創設しました。その後、JICA日系社会青年海外協力隊としてブラジルへ派遣され、言葉や文化の違う子どもたちとも、スポーツを通して心が通う経験を重ねました。国内の教育現場と海外での経験、その両方を土台に活動を広げています。</p>
""" + VALUES + """
</section>

<section>
<h2 class="sec">活動全体のつながり</h2>
<p class="lead">教育・スポーツ・国際交流・地域・仕事は、別々の活動ではなく、つながり合っています。</p>
<div class="diagram">
<div class="node">スポーツ<small>レッスン・ティーボール・野球指導</small></div><div class="arr">⇄</div>
<div class="node">教育<small>職業講話・日本語教育・学習支援</small></div><div class="arr">⇄</div>
<div class="node">地域<small>居場所づくり・コミュニティ</small></div><div class="arr">⇄</div>
<div class="node">国際交流<small>海外指導・道具の輸出・交流</small></div><div class="arr">⇄</div>
<div class="node">仕事<small>講演・企画運営・連携</small></div>
</div>
<div class="cycle">
<div class="c"><b>1. 学ぶ</b><p style="margin:6px 0 0;font-size:14px;color:#444">子ども・学生が、活動や講話を通して新しい世界や大人に出会います。</p></div>
<div class="c"><b>2. 実践する</b><p style="margin:6px 0 0;font-size:14px;color:#444">自分の「好き」や「得意」を、実際の活動の中で試していきます。</p></div>
<div class="c"><b>3. 支える</b><p style="margin:6px 0 0;font-size:14px;color:#444">学んだ人が、今度は指導や運営など、支える側に回ります。</p></div>
<div class="c"><b>4. つながる</b><p style="margin:6px 0 0;font-size:14px;color:#444">地域や世界へつながりが広がり、次の出会いと学びが生まれます。</p></div>
</div>
</section>

<section id="conductor">
<h2 class="sec"><span class="en">CONDUCTOR</span>コンダクター紹介</h2>
<p class="lead">TEAMSWYK Conductor　廣瀬 拓哉（ひろせ たくや） ― 大阪府枚方市出身。「コンダクター」は、教育・スポーツ・国際交流・地域の現場を行き来しながら、人と人、人と世界をつなぐ役割です。公立中学校の社会科教員を経てブラジルへ派遣され、帰国後は履正社スポーツ専門学校 野球コースの監督・講師を務めながら活動を広げてきました。教え子には、サンフランシスコ・ジャイアンツと契約した選手もいます。</p>
<h3 class="sub">経歴</h3>
<div class="timeline">""" + _tl + """</div>
<h3 class="sub">球歴</h3>
<p class="lead-l">枚方ホワイトイーグルス／枚方リトルシニア／近畿大学附属新宮高等学校 硬式野球部（主将）／近畿大学 体育会硬式野球部</p>
<h3 class="sub">保有資格</h3>
<div class="chips">
<span>高等学校教諭一種免許状（公民科）</span><span>中学校教諭一種免許状（社会科）</span><span>小学校教諭二種免許状</span><span>日本ティーボール協会 特別公認指導者</span><span>マックブランド 爪機能アドバイザー</span><span>スポーツネイルケアインストラクター</span><span>スリーバランスアカデミー公認心理学講師</span>
</div>
</section>
""" + cta_row()

# ---------------- 活動紹介（1ページ集約） ----------------
activities_body = head("活動紹介", "TEAM SWYKの活動を、まとめてご紹介します") + """
<section style="margin-top:26px">
<div class="chips" style="justify-content:center">
<a href="#career">オンライン職業講話</a><a href="#lesson">放課後レッスン</a><a href="#teeball">ティーボール</a><a href="#nihongo">日本語教育・学習支援</a><a href="#community">コミュニティ</a><a href="#dream">夢を形にするプロジェクト</a><a href="global.html">国際交流・海外活動 →</a>
</div>
</section>

<section id="career">
<span class="st st-now">実施中</span>
<h2 class="sec">学校授業、オンライン職業講話</h2>
<div class="photo"><img src="img/kidsfield.jpg" alt="グラウンドに集まる子どもたち"></div>
<p class="lead">コロナ禍に始めた、“大人と社会と繋がる場所”。オンラインを通して様々な生き方や価値観に触れ、将来の選択肢を増やすきっかけをつくります。私立静岡学園中学校・高等学校では探究学習のカリキュラムとして導入され延べ13回実施。その他、全国の小・中・高・大学で実施し、一般向け講話も延べ14回行ってきました。参加総数は7,550人（2025年4月時点）です。</p>
<div class="quote">「野球をしてきたおかげで、海外に行くことができた。言語も、家族と呼べる人たちもできた」というお話が心に残りました。自分の“好き”をキャリアにできること、未来を肯定してくれる考え方を、自分の人生のプラスにしていきたいです。<br><span style="color:#888;font-size:13px">（大阪府 中学2年生の感想より）</span></div>
<p class="lead">実施校の例：静岡学園高等学校・中学校、島根県立大学、京都橘大学、近畿大学附属新宮高校、大阪府立枚方高校、兵庫県立国際高校 ほか多数</p>
</section>

<section id="lesson">
<span class="st st-now">実施中</span>
<h2 class="sec">放課後レッスン、居場所づくり</h2>
<div class="photo"><img src="img/flagkids.jpg" alt="レッスンに参加する子どもたち"></div>
<p class="lead">2021年9月に開講した「TEAMSWYK LESSON」。京都府八幡市の美濃山地区で、平日に子どもたちが集まる、家・学校・習い事以外の「心の拠り所」です。現在、約56名が在籍しています。</p>
<div class="cards">
<div class="card"><h3>野球レッスン</h3><p>野球を専門的に学ぶ学生による、技術と心を育てるレッスンです。</p></div>
<div class="card"><h3>勉強レッスン</h3><p>現役の大阪大学法学部生による、オンライン・オフラインのハイブリッド型・苦手克服講座です。</p></div>
<div class="card"><h3>食育・栄養講座</h3><p>子どもの成長に欠かせない、食と栄養について学ぶ講座です。</p></div>
<div class="card"><h3>キャリア・夢講座</h3><p>いろんな人の生き方に触れ、自分の将来を考える講座です。</p></div>
</div>
<p class="lead" style="margin-top:14px">指導の中心は、将来、学校の先生や野球の指導者を志す大学生・専門学生です。子どもと関わる経験は、彼ら自身の財産にもなります。</p>
</section>

<section id="teeball">
<span class="st st-now">実施中</span>
<h2 class="sec">ティーボール、スポーツ</h2>
<div class="photo"><img src="img/certs.jpg" alt="活動に参加した子どもたち"></div>
<p class="lead">2023年3月、認定こども園 松井ヶ丘保育園（京都府京田辺市）で開校したティーボールスクール。スポンジ製のボールやバットを使って、走る・跳ねる・投げる・打つ・捕るの土台づくりを目指します。挨拶や礼儀、片付け、思いやりの心、挑戦する気持ちも育みます。指導者は全員、日本ティーボール協会の講習会を受講した指導者資格の保有者です。奈良教室も開講しています。</p>
</section>

<section id="nihongo">
<span class="st st-now">実施中</span>
<h2 class="sec">日本語教育、学習支援</h2>
<p class="lead">海外では、ブラジル・ペルー・パラグアイの日系コミュニティを中心に日本語学習の支援に携わってきました。国内では、京都・大阪の公立中学校で、日本語学習支援や総合学習の非常勤講師を務めています（2020年9月〜）。言葉が通じることで生まれる安心と、学びの土台づくりを大切にしています。</p>
</section>

<section id="community">
<span class="st st-now">実施中</span>
<h2 class="sec">コミュニティ、地域交流</h2>
<div class="photo"><img src="img/biggroup.jpg" alt="コミュニティの仲間たち"></div>
<p class="lead">2024年8月にスタートした、オンライン＆オフラインのコミュニティ「TEAM SWYK Community」。年齢・性別・国籍を問わず交われる場所で、現在54名（社会人22名／大学生13名／高校生16名／中学生3名）が参加し、Discordを中心に交流しています。大阪府枚方市・和歌山県新宮市でのマルシェ出店など、地域とつながる活動も行っています。</p>
<p class="lead">関わり方は参加するだけではありません。伝える、企画する、撮影する、デザインする、通訳する、指導するなど、それぞれの得意を活かして支える側にもなれます。参加・協力のご相談はお問い合わせから受け付けています。</p>
</section>

<section id="dream">
<span class="st st-done">実施済み</span>
<h2 class="sec">夢を形にするプロジェクト</h2>
<div class="photo"><img src="img/dream.jpg" alt="TEAMSWYKの旗を持つ選手たち"></div>
<p class="lead">「DREAM PROJECT」は、学生のデザインしたフェアトレードTシャツを、シサム工房と共に形にしたプロジェクトです（2022年3月〜2023年8月）。頭の中の「やってみたい」を実現する経験そのものが、学びになります。このプロジェクトは実施済みで、現在同じ形での募集は行っていません。</p>
""" + cta_row() + """
</section>
"""

# ---------------- 拠点・教室紹介（1ページ集約） ----------------
locations_body = head("拠点・教室紹介", "それぞれの地域で、それぞれの形の活動が育っています") + """
<section style="margin-top:30px">
<h2 class="sec">TEAMSWYK JAPAN</h2>
<div class="photo"><img src="img/biggroup.jpg" alt="TEAMSWYK JAPANの活動の様子"></div>
<p class="lead">日本国内の活動とコミュニティの拠点です。大阪府枚方市を中心に、学校での職業講話・キャリア教育、放課後レッスン、ティーボール、コミュニティ活動などを展開し、海外での経験を日本の子どもたちや地域へ還元しています。</p>
<table class="kv" style="max-width:820px;margin:0 auto"><tr><th>活動</th><td>職業講話／放課後レッスン／コミュニティ／ティーボール</td></tr><tr><th>対象者</th><td>子ども・学生・大人（活動ごとに異なります）</td></tr></table>
</section>

<section>
<h2 class="sec">松井ヶ丘保育園 TEAMSWYKティーボールスクール</h2>
<div class="photo"><img src="img/kidsfield.jpg" alt="松井ヶ丘保育園ティーボールスクールの様子"></div>
<p class="lead">認定こども園 松井ヶ丘保育園（京都府京田辺市）で2023年3月に開校したティーボールスクールです。卒園して学校が離れても、スポーツで繋がる関係が残る場を目指しています。</p>
<p style="text-align:center"><a href="activities.html#teeball" style="font-weight:800">ティーボールの活動紹介を見る →</a></p>
</section>

<section>
<h2 class="sec">TEAMSWYK奈良教室</h2>
<p class="lead">奈良県で、ティーボールなどの教室活動を行っています。走る・投げる・打つ・捕るの土台づくりと、挨拶・礼儀・思いやりを育む指導は、松井ヶ丘保育園のスクールと同じ考え方です。開催の詳しい内容は、お問い合わせ時にご案内します。</p>
</section>

<section>
<h2 class="sec">TEAMSWYK新宮校</h2>
<p class="lead">和歌山県新宮市での活動拠点です。マルシェ出店や、近畿大学附属新宮高校での職業講話の実施など、地域と学校とのつながりを育ててきました。</p>
</section>

<section>
<h2 class="sec">TEAMSWYK Brasil</h2>
<div class="photo"><img src="img/night.jpg" alt="ブラジルでの交流の様子"></div>
<p class="lead">2017年から2019年まで、JICA日系社会青年海外協力隊の野球隊員として、サンパウロ州インダイアツーバ市で日系コミュニティの子どもたちを指導したことが土台になっています。現在も、野球指導・国際交流・野球道具の環境開発を通して、ブラジルとのつながりが続いています。</p>
<div class="btnrow"><a class="btn" href="global.html">海外活動の詳細を見る</a><a class="btn y" href="pt.html">Para os brasileiros（Português）</a></div>
""" + cta_row() + """
</section>
"""

# ---------------- 参加・プログラム ----------------
programs_body = head("参加・プログラムのご案内", "参加・利用のご相談は、LINE・WhatsApp・メールから受け付けています") + """
<section style="margin-top:30px">
<div class="cards">
<div class="card"><span class="st st-now">参加相談 受付中</span><h3>ティーボールスクール</h3>
<p>スポンジ製のボールやバットを使って、走る・跳ねる・投げる・打つ・捕るの土台づくり。挨拶・礼儀・思いやりも育みます。</p>
<p>対象：園児／場所：認定こども園 松井ヶ丘保育園（京都府京田辺市）・奈良教室／対面</p>
<a class="more" href="activities.html#teeball">活動紹介を見る →</a></div>
<div class="card"><span class="st st-now">参加相談 受付中</span><h3>野球個別指導</h3>
<p>TEAMSWYK Conductor 廣瀬拓哉による、選手一人ひとりの課題に合わせた個別指導。技術だけでなく、目標の持ち方や野球との向き合い方も一緒に考えます。保護者の方のご相談も歓迎です。</p>
<p>対象：野球選手（小学生〜大人）、保護者／対面（オンライン相談も可）</p>
<a class="more" href="about.html#conductor">コンダクター紹介を見る →</a></div>
<div class="card"><span class="st st-now">参加相談 受付中</span><h3>日本語教育、学習支援</h3>
<p>国内外での日本語教育と、学校・地域での学習支援。言葉の学びを通して、安心して学べる土台をつくります。</p>
<p>対象：日本語を学ぶ子ども・学生、学習支援を希望する学校・地域の方／対面・オンライン</p>
<a class="more" href="activities.html#nihongo">活動紹介を見る →</a></div>
<div class="card"><span class="st st-now">参加相談 受付中</span><h3>コミュニティイベント・プロジェクト参加</h3>
<p>コミュニティのイベントやプロジェクトへの参加・協力。伝える、企画する、撮影する、デザインする、通訳するなど、得意を活かした関わり方ができます。</p>
<p>対象：学生・大人（年齢・国籍を問いません）／オンライン＆オフライン</p>
<a class="more" href="activities.html#community">活動紹介を見る →</a></div>
</div>
<p class="note">開催日時・料金は、プログラムや内容により異なります。お問い合わせの際にご案内いたします。<br>参加までの流れ：お問い合わせ → ご案内・ヒアリング → 日程のご相談 → 参加・実施</p>
""" + cta_row() + """
</section>
"""

# ---------------- 講演・仕事のご依頼 ----------------
work_body = head("講演・仕事のご依頼", "学校園・自治体・企業・団体からのご相談に対応します") + """
<section style="margin-top:30px">
<h2 class="sec">依頼できる内容</h2>
<div class="cards">
<div class="card"><h3>学校園での講演</h3><p>キャリア教育・職業講話など、子どもたちの将来の選択肢を広げる講演。</p></div>
<div class="card"><h3>国際理解教育、異文化交流授業</h3><p>海外での経験をもとにした、国際理解・異文化交流の授業。</p></div>
<div class="card"><h3>JICA、ブラジルでの経験に関する講演</h3><p>JICA海外協力隊としてブラジルで活動した経験からの講演。</p></div>
<div class="card"><h3>野球指導、スポーツ教室</h3><p>野球指導やスポーツ教室の実施・サポート。</p></div>
<div class="card"><h3>子どもの居場所づくり、地域活動</h3><p>放課後の居場所づくりや地域活動についての相談・講演。</p></div>
<div class="card"><h3>教育プログラム、体験活動の企画運営</h3><p>教育プログラムや体験活動の企画・運営のサポート。学校交流、地域との連携の場づくりもご相談ください。「こんなことはできる？」という段階のご相談も歓迎です。</p></div>
</div>
</section>
<section>
<h2 class="sec">対象となる方</h2>
<div class="chips" style="justify-content:center">
<span>小学校・中学校・高校・大学</span><span>幼稚園・保育園・こども園</span><span>自治体</span><span>企業</span><span>スポーツチーム・団体</span><span>地域団体</span>
</div>
<p class="lead" style="margin-top:16px">実施例：オンライン職業講話は、静岡学園中学校・高等学校の探究学習カリキュラムに導入され、全国の学校で実施してきました（参加総数7,550人・2025年4月時点）。担当は <a href="about.html#conductor">TEAMSWYK Conductor 廣瀬拓哉</a> です。</p>
</section>
<section>
<h2 class="sec">相談から実施までの流れ</h2>
<div class="flow">
<div class="f"><b>1. ご相談</b><p>LINE・WhatsApp・メールから、ご希望の内容をお知らせください。</p></div>
<div class="f"><b>2. ヒアリング</b><p>対象者・人数・日時・場所などをお聞きし、内容をご提案します。</p></div>
<div class="f"><b>3. 内容・日程の確定</b><p>ご提案内容と日程、条件を確定します。</p></div>
<div class="f"><b>4. 実施</b><p>当日、講演・授業・指導を実施します。</p></div>
</div>
""" + cta_row() + """
</section>
"""

# ---------------- 海外活動・Brasil ----------------
global_body = head("国際交流、海外での野球指導", "野球を通して、日本と世界を繋ぐ") + """
<div class="photo"><img src="img/brazilflag.jpg" alt="ブラジルの子どもたちとの集合写真"></div>
<section style="margin-top:26px">
<h2 class="sec">ブラジルでの指導と日本遠征</h2>
<p class="lead">2017年から2019年まで、JICA日系社会青年海外協力隊の野球隊員として、ブラジル・サンパウロ州インダイアツーバ市へ派遣され、日系コミュニティの子どもたちを指導しました。2019年3月には「TEAMSWYK 日本遠征 Project」を実施し、ブラジルの子どもたち10人を大阪府枚方市へ招き、野球を通して延べ約700人と交流しました。</p>
</section>
<section>
<h2 class="sec">教え子の、その後</h2>
<div class="card" style="max-width:820px;margin:0 auto">
<h3>ブラジルの教え子が、サンフランシスコ・ジャイアンツと契約</h3>
<p>2019年の日本遠征の野球教室で、当時12歳だったビニシウス選手は、近畿大学の佐藤輝明選手（現・阪神タイガース）からバットをいただきました。その喜びを力に野球を続け、ブラジル代表（U-12・U-15・U-18）に選出。2024年1月、サンフランシスコ・ジャイアンツと契約しました。</p>
</div>
</section>
<section>
<h2 class="sec">南米・世界での活動</h2>
<div class="cards">
<div class="card"><h3>ペルー</h3><p>JICA大学連携事業（近畿大学✕野球）で大学生の活動コーディネーターとして派遣され、1ヶ月で計600人への野球指導を行いました。ペルー代表キャンプのヘッドコーチも務め、大阪府在住の中学生を南米へ派遣する「南米野球留学」も実施しました。</p></div>
<div class="card"><h3>モンゴル</h3><p>2022年には日本モンゴル国交樹立50周年の友好イベントに派遣。2024年にはモンゴルの子どもたちへの野球指導を行いました。</p></div>
<div class="card"><h3>野球道具の環境開発（ZETT国際部と共に）</h3><p>ペルー・ブラジル・パラグアイ・ボリビアを回り、13都市で15の野球クリニックを開催、延べ2,000人への野球指導と道具の営業を行いました。</p></div>
</div>
<div class="gallery">
<figure><img src="img/kimono.jpg" alt="日本遠征での文化交流"><figcaption>日本遠征での文化交流（着物体験）</figcaption></figure>
<figure><img src="img/fieldflags.jpg" alt="南米のグラウンドでの集合写真"><figcaption>南米のグラウンドでの野球クリニック</figcaption></figure>
<figure><img src="img/blue.jpg" alt="現地チームとの集合写真"><figcaption>現地チームとの集合写真</figcaption></figure>
</div>
</section>
<section>
<h2 class="sec">野球道具の取り扱い・Brasilの方へ</h2>
<p class="lead">海外（主に南米）の方々への野球・ソフトボール道具の購入場所をつくるため、日本のメーカーやショップにご協力いただき、輸出の仕事に携わっています。取り扱い：ZETT／ローリングスジャパン／marucci／ケンコーティーボール（その他メーカーも相談可）。ブラジル向けのサービス案内は、ポルトガル語ページをご覧ください。</p>
<div class="btnrow"><a class="btn y" href="pt.html">Para os brasileiros（Português）</a></div>
""" + cta_row() + """
</section>
"""

# ---------------- お知らせ ----------------
news_body = head("お知らせ", "活動の様子や募集のお知らせを発信していきます") + """
<section style="margin-top:30px">
<p class="lead">TEAM SWYKの活動レポートや、プログラム・イベントの募集のお知らせは、こちらのページで順次お届けします。</p>
<div class="cards">
<div class="card"><h3>活動紹介</h3><p>現在の活動の内容は、活動紹介ページでまとめてご覧いただけます。</p><a class="more" href="activities.html">活動紹介を見る →</a></div>
<div class="card"><h3>参加・プログラム</h3><p>参加相談を受け付けているプログラムはこちらです。</p><a class="more" href="programs.html">プログラムを見る →</a></div>
<div class="card"><h3>海外活動・Brasil</h3><p>国際交流・海外活動の取り組みはこちらです。</p><a class="more" href="global.html">海外活動を見る →</a></div>
</div>
""" + cta_row() + """
</section>
"""

# ---------------- お問い合わせ ----------------
contact_body = head("お問い合わせ", "ご相談は、LINE・WhatsApp・メールから受け付けています") + f"""
<section style="margin-top:30px">
<p class="lead">活動への参加、講演・仕事のご依頼、協力・連携のご相談など、内容を問わずお気軽にご連絡ください。ブラジル・海外からのご相談は、WhatsApp（ポルトガル語対応）をご利用ください。メールでのご相談は <a href="{MAIL_URL}">{EMAIL}</a> へどうぞ。</p>
<div class="btnrow" style="margin-bottom:26px">
<a class="btn line-b" href="{LINE_URL}" target="_blank" rel="noopener">LINEで相談する</a>
<a class="btn wa" href="{WA_URL}" target="_blank" rel="noopener">WhatsAppで相談する</a>
<a class="btn" href="{MAIL_URL}">メールで相談する</a>
</div>
<h2 class="sec">ご相談の例</h2>
<div class="chips" style="justify-content:center">
<span>活動・プログラムへの参加、利用</span><span>講演、仕事のご依頼</span><span>活動への協力、連携</span><span>商品、海外サービス</span><span>その他</span>
</div>
<p class="lead" style="margin-top:18px">講演・仕事のご相談では、学校園・団体名、対象者と人数、ご希望の日時・場所をお知らせいただけますと、ご案内がスムーズです。ご連絡いただいた情報は、ご相談への対応のためにのみ使用します。取り扱いの詳細は <a href="privacy.html">プライバシーポリシー</a> をご覧ください。</p>
<p style="text-align:center"><a class="btn y" href="pt.html">Para os brasileiros（Português）</a></p>
</section>
"""

# ---------------- プライバシーポリシー ----------------
privacy_body = head("プライバシーポリシー", "個人情報の取り扱いについて") + """
<section style="margin-top:30px;max-width:820px;margin-left:auto;margin-right:auto">
<h3 class="sub">1. 事業者</h3>
<p class="lead-l">TEAM SWYK（チーム さわやか）／ TEAMSWYK Conductor 廣瀬拓哉</p>
<h3 class="sub">2. 取得する情報</h3>
<p class="lead-l">お問い合わせ・参加申込・仕事依頼の際に、お名前、連絡先、所属団体名、相談内容など、対応に必要な情報を取得します。</p>
<h3 class="sub">3. 利用目的</h3>
<p class="lead-l">取得した情報は、ご相談・お申し込みへの対応、活動やプログラムのご案内、実施に必要な連絡のためにのみ使用します。</p>
<h3 class="sub">4. 第三者への提供</h3>
<p class="lead-l">ご本人の同意がある場合、または法令に基づく場合を除き、取得した情報を第三者に提供することはありません。</p>
<h3 class="sub">5. 安全管理</h3>
<p class="lead-l">取得した情報は、不正アクセス・漏えい等を防ぐため、適切な方法で管理します。</p>
<h3 class="sub">6. 開示・訂正・削除のご請求</h3>
<p class="lead-l">ご本人からの開示・訂正・利用停止・削除のご請求には、本人確認のうえ、適切に対応します。お問い合わせページからご連絡ください。</p>
<h3 class="sub">7. 本ポリシーの変更</h3>
<p class="lead-l">本ポリシーは、必要に応じて変更することがあります。変更後の内容は、このページに掲載した時点から効力を生じます。</p>
<a class="back" href="index.html">← トップへ戻る</a>
</section>
"""

# ---------------- ポルトガル語ページ ----------------
pt_body = f"""
<div class="pagehead"><h1>TEAM SWYK</h1><p>Conectar pessoas. Expandir o mundo. ― Serviços para brasileiros, do Japão para o Brasil.</p></div>
<section style="margin-top:30px">
<h2 class="sec"><span class="en">INÍCIO</span>Bem-vindo à TEAM SWYK</h2>
<p class="lead">A TEAM SWYK é uma iniciativa japonesa que conecta pessoas por meio do esporte, da educação e do intercâmbio internacional. Nosso condutor, Takuya Hirose, atuou no Brasil como voluntário da JICA (2017–2019), ensinando beisebol para crianças da comunidade nikkei. Esta página apresenta os serviços voltados aos brasileiros.</p>
<div class="entries">
<a class="entry" href="#materiais"><b>Materiais de Beisebol</b><span>Equipamentos japoneses de beisebol e softbol</span></a>
<a class="entry" href="#produtos"><b>Produtos Japoneses</b><span>Cosméticos, beleza, matcha e outros produtos do Japão</span></a>
<a class="entry" href="#experiencias"><b>Experiências no Japão</b><span>Vivências de viagem e cultura japonesa</span></a>
<a class="entry" href="#contato"><b>Contato</b><span>Fale conosco em português</span></a>
</div>
</section>
<section id="materiais">
<h2 class="sec"><span class="en">MATERIAIS DE BEISEBOL</span>Equipamentos de Beisebol</h2>
<p class="lead">Trabalhamos com a exportação de equipamentos japoneses de beisebol e softbol, em parceria com fabricantes e lojas do Japão. Marcas como ZETT, Rawlings Japan, marucci e Kenko Tee Ball estão entre as que podemos consultar. Para catálogos, disponibilidade e pedidos, fale conosco pelo WhatsApp.</p>
<div class="btnrow"><a class="btn wa" href="{WA_URL}" target="_blank" rel="noopener">Consultar pelo WhatsApp</a></div>
</section>
<section id="produtos">
<h2 class="sec"><span class="en">PRODUTOS JAPONESES</span>Produtos do Japão</h2>
<p class="lead">Apresentaremos produtos japoneses selecionados, como cosméticos, itens de beleza e matcha. Os detalhes de cada produto serão publicados conforme forem confirmados. Se você procura algo específico do Japão, consulte-nos.</p>
<div class="btnrow"><a class="btn wa" href="{WA_URL}" target="_blank" rel="noopener">Consultar pelo WhatsApp</a></div>
</section>
<section id="experiencias">
<h2 class="sec"><span class="en">EXPERIÊNCIAS NO JAPÃO</span>Vivências no Japão</h2>
<p class="lead">Para quem visita o Japão, apresentaremos experiências como as trilhas de Kumano Kodo e vivências da cultura japonesa ligadas às nossas atividades. Roteiros e condições serão anunciados conforme forem confirmados. Conte-nos o que você gostaria de vivenciar.</p>
<div class="btnrow"><a class="btn wa" href="{WA_URL}" target="_blank" rel="noopener">Consultar pelo WhatsApp</a></div>
</section>
<section id="contato">
<h2 class="sec"><span class="en">CONTATO</span>Fale conosco</h2>
<p class="lead">Atendemos em português pelo WhatsApp e pelo LINE.</p>
<div class="btnrow">
<a class="btn wa" href="{WA_URL}" target="_blank" rel="noopener">WhatsApp</a>
<a class="btn line-b" href="{LINE_URL}" target="_blank" rel="noopener">LINE</a>
<a class="btn" href="{MAIL_URL}">E-mail</a>
</div>
</section>
"""

pages = {
    "index.html": ("トップ", index_body, "人とつながる。世界が広がる。TEAM SWYK（チーム さわやか）の公式サイト。", "ja"),
    "about.html": ("TEAMSWYKについて", about_body, "TEAM SWYKの理念・設立背景・コンダクター紹介。", "ja"),
    "activities.html": ("活動紹介", activities_body, "TEAM SWYKの活動紹介。", "ja"),
    "locations.html": ("拠点・教室紹介", locations_body, "TEAM SWYKの拠点・教室紹介。", "ja"),
    "programs.html": ("参加・プログラム", programs_body, "TEAM SWYKの参加プログラムのご案内。", "ja"),
    "work.html": ("講演・仕事のご依頼", work_body, "学校園・自治体・企業・団体からの講演・仕事のご依頼について。", "ja"),
    "global.html": ("国際交流、海外での野球指導", global_body, "TEAM SWYKの国際交流・海外活動とブラジル向け案内。", "ja"),
    "news.html": ("お知らせ", news_body, "TEAM SWYKのお知らせ。", "ja"),
    "contact.html": ("お問い合わせ", contact_body, "TEAM SWYKへのお問い合わせ。", "ja"),
    "privacy.html": ("プライバシーポリシー", privacy_body, "TEAM SWYKのプライバシーポリシー。", "ja"),
    "pt.html": ("Para os brasileiros", pt_body, "Serviços da TEAM SWYK para brasileiros.", "pt"),
}

os.makedirs(OUT, exist_ok=True)
img_src = os.path.join(SRC, "site", "img")
img_out = os.path.join(OUT, "img")
if os.path.isdir(img_src):
    if os.path.isdir(img_out):
        shutil.rmtree(img_out)
    shutil.copytree(img_src, img_out)
for name, (title, body, desc, lang) in pages.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(page(title, body, desc, lang))
    print("wrote", name)
print("total pages:", len(pages))
