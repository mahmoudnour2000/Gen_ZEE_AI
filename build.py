import html
def band(b):
    c=[(2,b),(24,b-18),(38,b-18),(66,b-44)];t=11
    pts=[(x,y) for x,y in c]+[(x,y+t) for x,y in reversed(c)]
    return " ".join(f"{x},{y}" for x,y in pts)
LOGO=f'<svg viewBox="-2 -2 72 90" aria-hidden="true"><polygon points="{band(30)}" fill="#00D2BE"/><polygon points="{band(52)}" fill="#7C3AED"/><polygon points="{band(74)}" fill="#FF7A00"/></svg>'
NAV=[("index.html","Home"),("services.html","Services"),("blog.html","Blog"),("contact.html","Contact")]
def head(title,desc,page):
    li=""
    for h,n in NAV:
        on=' on' if h==page or (n=="Services" and page.startswith("services")) else ''
        if n=="Services":
            li+=f'<li><a class="l{on}" href="{h}">Services</a><div class="sub"><a href="services.html">Overview</a><a href="services-talents.html">For Talents</a><a href="services-companies.html">For Companies</a></div></li>'
        else: li+=f'<li><a class="l{on}" href="{h}">{n}</a></li>'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | Gen ZEE AI</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,800&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans+Arabic:wght@400;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css"></head><body><div class="sp"><i></i></div>
<header class="nav dk"><a class="brand" href="index.html">{LOGO}<span>Gen <b>ZEE</b> AI</span></a>
<button class="burger" aria-label="Menu" aria-expanded="false"><i></i><i></i><i></i></button>
<ul class="menu">{li}</ul><a class="btn b-or" href="contact.html">Get in Touch</a></header><main>'''
FOOT=f'''</main><footer class="f"><div class="wrap"><div class="fg"><div><a class="brand" href="index.html">{LOGO}<span>Gen <b>ZEE</b> AI</span></a><p>Gen ZEE AI fill the gap between academic learning and market needs through AI Expert in AI field to empower the talents.</p><p><b>outlearn, outearn, outlead</b></p></div>
<div><h4>Explore</h4><a href="index.html">Home</a><a href="services.html">Services</a><a href="services-talents.html">For Talents</a><a href="services-companies.html">For Companies</a></div>
<div><h4>Company</h4><a href="blog.html">Blog</a><a href="contact.html">Contact</a><a href="https://linkedin.com/company/genzeeai">LinkedIn</a></div>
<div><h4>Legal</h4><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a><a href="mailto:hello@genzee.ai">hello@genzee.ai</a></div></div>
<div class="copy"><span>© 2026 Gen ZEE AI. All rights reserved.</span><span>Tech &amp; Training for talent and companies</span></div></div></footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="assets/js/main.js"></script></body></html>'''
def hero(tag,h1,lead,btns,sm=False,stats=False):
    b="".join(f'<a class="btn {c}" href="{u}">{t}</a>' for t,u,c in btns)
    s='<div class="stats"><div><b data-count="150" data-suf="+">150+</b><span>Talents trained</span></div><div><b data-count="85" data-suf="%">85%</b><span>Placement rate</span></div><div><b data-count="2">2</b><span>Hiring partners</span></div><div><b data-count="8" data-suf="+">8+</b><span>Expert mentors</span></div></div>' if stats else ''
    a='<div class="ask" aria-live="polite"><span class="dot"></span><div><p class="q"></p><p class="a"></p></div></div>' if stats else ''
    return f'<section class="hero{" sm" if sm else ""}"><canvas id="stage" aria-label="Interactive 3D Gen ZEE AI logo"></canvas><div class="wrap"><div><span class="tag">{tag}</span><h1>{h1}</h1><p class="lead">{lead}</p><div class="cta">{b}</div>{a}</div><div></div>{s}</div><span class="hint">drag / move to interact</span></section>'
def sec(h,p,body,alt=False):
    return f'<section class="sec{" alt" if alt else ""}"><div class="wrap"><div class="head rv"><h2>{h}</h2><p>{p}</p></div>{body}</div></section>'
TR=["Machine Learning","Deep Learning","LLM","Agentic AI","Computer Vision"]
TS=["AI Learning Tracks","Mentorship","Skill Assessment","Career Placement"]
CS=["Pre-validated AI Talent","Role Matching","Pay on Placement","Corporate AI Training"]
def lis(a):return "<ul>"+"".join(f"<li>{x}</li>" for x in a)+"</ul>"
def hs(i,h,p,items,alt=False):
    ps="".join(f'<article class="hp"><figure><img src="assets/img/{im}.svg" alt="{al}"></figure><div class="bd">'+(f'<em>{k}</em>' if k else '')+f'<h3>{t}</h3>'+(f'<p>{d}</p>' if d else '')+'</div></article>' for im,al,k,t,d in items)
    return f'<section class="hs{" alt" if alt else ""}" id="{i}"><div class="hs-in"><div class="wrap"><div class="head"><h2>{h}</h2><p>{p}</p></div></div><div class="h-track">{ps}</div><div class="wrap"><div class="h-bar"><i></i></div></div></div></section>'
def tracks():return '<div class="tracks">'+"".join(f'<div class="track rv"><em>Track {i+1}</em><h3>{t}</h3></div>' for i,t in enumerate(TR))+'</div>'
def last():return '<section class="last"><div class="wrap cta2"><div class="rv"><span class="tag">Tech &amp; Training for talent and companies</span><h2>Ready to train talent — or hire it?</h2><p>Gen ZEE AI fills the gap between academic learning and market needs through AI experts in the field.</p><div class="cta"><a class="btn b-or" href="services-talents.html">For Talents</a><a class="btn b-pu" href="services-companies.html">For Companies</a><a class="btn b-gh" href="contact.html">Or send a message</a></div></div><figure class="cimg cp"><img src="assets/img/cta.svg" alt="Gen ZEE AI ascent"><span class="chip c1"><b>85%</b>placement rate</span><span class="chip c2"><b>150+</b>talents trained</span></figure></div></section>'
SK="Python,Machine Learning,Deep Learning,Computer Vision,NLP,LLMs,Agentic AI,PyTorch,TensorFlow,MLOps,GenAI,Prompt Engineering".split(",")
FAQ=[("What is Gen ZEE AI?","A tech and training company for talent and companies. We fill the gap between academic learning and market needs through AI experts in the field."),("Which tracks can talent join?","Machine Learning, Deep Learning, LLM, Agentic AI and Computer Vision."),("How do I get started as talent?","Send us a message and choose “Talent”. We will guide you to the right track."),("How can my company hire through Gen ZEE AI?","Contact us as a company. We match validated talent to your roles, or train your existing team."),("Do you offer corporate AI training?","Yes. We upskill the teams you already employ with the same market-aligned programs."),("What is your placement rate?","85% of our trained talent has been placed with hiring partners.")]
STORY=[("Ahmed Hassan","ML Engineer","I graduated with strong theory but froze in technical interviews. The gap roadmap showed me what the market actually expects."),("Sara Mohamed","AI Researcher","Mentorship and human validation helped me prove my skills were industry-ready, not only academic."),("Omar Khalil","Data Scientist","Practical projects and employer-facing assessment are what finally got me hired."),("Layla Ibrahim","NLP Engineer","Hands-on LLM work, code reviews and interview prep tied to what employers hire for."),("Karim Nour","AI Engineer","I saw my readiness score and fixed the weak spots my degree never covered before applying."),("Fatma Ali","Machine Learning Engineer","I was validated against industry standards, not exam grades. That clarity changed my approach.")]
POSTS=[("Industry","Why University AI Education Isn't Enough for Today's Job Market"),("Career","From Classroom to Production: What Hiring Managers Actually Look For"),("Career","The Complete AI Career Roadmap for 2026"),("Guides","LLM Engineer vs ML Engineer: Which Path Is Right for You?"),("Career","Building an AI Portfolio That Gets You Hired"),("Industry","How Partner Companies Hire AI Talent in 2026"),("Guides","What Is an AI Talent Ecosystem — and Why It Matters"),("Career","How to Close Your AI Skills Gap in 90 Days")]
pages={}
# HOME
b=hero("Tech &amp; Training for talent and companies","Tech and training that closes the gap between learning and the market.","Gen ZEE AI fills the gap between academic learning and market needs through AI experts in the field — empowering talent, and giving companies people they can hire with confidence.",[("For Talents","services-talents.html","b-or"),("For Companies","services-companies.html","b-pu")],stats=True)
b+=sec("Built for talent and companies","Two commercial paths. One standard: market-ready AI capability.",f'<div class="two"><div class="card t rv"><figure class="cimg cp"><img src="assets/img/v-talent.svg" alt="Talent learning AI"></figure><span class="k">For talent</span><h3>Training that makes you hireable</h3><p>Turn academic knowledge into a profile companies will hire. Train on the tracks the market recruits for, get mentored by AI practitioners, and enter partner pipelines with proof.</p><a class="btn b-or" href="services-talents.html">Explore talent training</a></div><div class="card c rv"><figure class="cimg cp"><img src="assets/img/v-company.svg" alt="Company hiring AI talent"></figure><span class="k">For companies</span><h3>Hire and train with less risk</h3><p>Hiring from open CVs is slow and expensive. 72% of employers cannot fill skilled roles. We deliver talent trained and validated by AI practitioners.</p><a class="btn b-pu" href="services-companies.html">Explore company solutions</a></div></div>')
b+='<div class="wrap"><div class="partners rv"><span>Mobica</span><span>BEDO</span></div></div>'
b+=sec("Closing the talent gap","Gen ZEE AI fill the gap between academic learning and market needs through AI Expert in AI field to empower the talents.",'<div class="two"><div class="prob rv"><h3>The AI skills gap is a hiring crisis</h3><ul><li>72% of employers report difficulty filling skilled roles; in 2026 AI overtook engineering and IT as the hardest skill to find.</li><li>AI job demand has grown about 21% a year since 2019; 44% of executives say missing in-house AI expertise slows adoption.</li><li>46% of leaders name skill gaps as a primary barrier to shipping AI.</li><li>Graduates leave with theory, not messy data, evaluation and deployment.</li></ul><p class="src">Sources: ManpowerGroup 2026; Bain &amp; Company 2025; McKinsey 2025.</p></div><div class="sol rv"><h3>A market-ready talent pipeline</h3><ul><li>Market-aligned tracks in ML, Deep Learning, LLM, Agentic AI and Computer Vision.</li><li>Mentorship and validation by AI practitioners — proven before the interview.</li><li>A placement path with partners such as Mobica and BEDO.</li></ul></div></div>',True)
b+=hs("tracks","AI learning tracks","Five market-aligned tracks. No filler weeks or levels — only the skills companies recruit for.",[(f"t-{k}",n,f"Track {i+1}",n,"") for i,(k,n) in enumerate(zip(["ml","dl","llm","agent","cv"],TR))])
b+='<div class="marq" aria-hidden="true"><div>'+"".join(f"<span>{s}</span>" for s in SK*2)+'</div></div>'
off=[("AI learning tracks","Five tracks mapped to the roles companies compete to fill."),("Practitioner assessment","Experts validate what talent can ship."),("Career placement","A hiring path with Mobica and BEDO."),("Mentorship","One-to-one guidance from AI practitioners."),("Market-shaped projects","Portfolio work on messy data, evaluation and deployment."),("Corporate training","Upskill the teams you already employ.")]
b+=hs("offer","What we offer","Training for talent. Hiring and upskilling for companies. One ecosystem.",[(k,t,"",t,d) for k,(t,d) in zip(["o-tracks","o-assess","o-place","o-mentor","o-projects","o-corp"],off)],True)
st=[("Train","Join a track with practitioner-reviewed projects."),("Build","Ship portfolio work that reflects production AI."),("Validate","Prove readiness through expert assessment."),("Close gaps","Follow a focused plan for what is still missing."),("Place","Enter partner hiring conversations.")]
b+=hs("how","How it works","From training to validated placement.",[(k,t,f"Step {i+1}",t,d) for i,(k,(t,d)) in enumerate(zip(["s-train","s-build","s-validate","s-gap","s-place"],st))])
b+=sec("Graduate stories","Talent who moved from academic learning to market-ready AI work.",'<div class="stories">'+"".join(f'<div class="story rv">“{q}”<footer><div class="av">{"".join(w[0] for w in n.split()[:2])}</div><div><b>{n}</b><small>{r}</small></div></footer></div>' for n,r,q in STORY)+'</div>',True)
b+=sec("Common questions","Clear answers for talent and for companies.",'<div class="faq">'+"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in FAQ)+'</div>')
pages["index.html"]=(head("Home","Tech & Training for talent and companies. Gen ZEE AI closes the gap between academic learning and market needs.","index.html")+b+last()+FOOT)
# SERVICES
b=hero("Services","Two doors. One standard.","Choose the path that fits you: train to get hired, or hire and train with less risk.",[("Not sure? Contact us","contact.html","b-gh")],sm=True)
b+=sec("What we do","Equal paths for talent and companies.",f'<div class="two"><div class="card t rv"><span class="k">Talent</span><h3>Training that makes you hireable</h3>{lis(TS)}<a class="btn b-or" href="services-talents.html">For Talents</a></div><div class="card c rv"><span class="k">Companies</span><h3>Hire and train with less risk</h3>{lis(CS)}<a class="btn b-pu" href="services-companies.html">For Companies</a></div></div>')
pages["services.html"]=head("Services","Services for AI talent and for companies.","services.html")+b+last()+FOOT
# TALENTS
j=[("Join a track",""),("Build projects",""),("Get validated",""),("Enter hiring talks","")]
b=hero("For talents","Training that makes you hireable","Turn academic knowledge into a profile companies will hire — mentored by AI practitioners.",[("Contact as talent","contact.html","b-or")],sm=True)
b+=sec("Four services","Everything you need to move from classroom to career.",'<div class="three">'+"".join(f'<div class="card t rv"><h3>{t}</h3></div>' for t in TS)+'</div>')
b+=hs("tracks","Learning tracks","Names only — the skills the market recruits for.",[(f"t-{k}",n,f"Track {i+1}",n,"") for i,(k,n) in enumerate(zip(["ml","dl","llm","agent","cv"],TR))],True)
b+=sec("How the journey works","Four steps to hiring conversations.",'<div class="steps" style="grid-template-columns:repeat(4,1fr)">'+"".join(f'<div class="step rv"><h3>{t}</h3></div>' for t,_ in j)+'</div>')
pages["services-talents.html"]=head("For Talents","AI training that makes you hireable.","services-talents.html")+b+last()+FOOT
# COMPANIES
b=hero("For companies","Hire and train with less risk","Talent trained and validated by AI practitioners — production-ready capability for your roles.",[("Talk to our team","contact.html","b-pu")],sm=True)
b+=sec("Why open-CV hiring is slow and expensive","72% of employers cannot fill skilled roles; 44% of executives say missing AI expertise delays adoption.",'<div class="three">'+"".join(f'<div class="card c rv"><h3>{t}</h3></div>' for t in CS)+'<div class="card rv" style="grid-column:1/-1"><h3>Why companies buy this</h3><p>Faster hiring · less mis-hire risk · better role fit · team upskilling</p></div></div>')
b+='<div class="wrap"><div class="partners rv"><span>Mobica</span><span>BEDO</span></div></div>'
pages["services-companies.html"]=head("For Companies","Hire and train AI talent with less risk.","services-companies.html")+b+last()+FOOT
# BLOG
b=hero("Blog","Articles on AI careers and hiring","Practical guides for talent and for the companies that hire them.",[],sm=True)
cards="".join(f'<a class="card post{" f" if i==0 else ""} rv" href="article.html"><span class="k" style="color:{"var(--mint)" if i==0 else "var(--orange)"}">{c}</span><h3>{t}</h3><div class="m"><span>Gen ZEE AI Team</span><span>6 min read</span></div></a>' for i,(c,t) in enumerate(POSTS))
b+=f'<section class="sec"><div class="wrap"><div class="posts">{cards}</div></div></section>'
pages["blog.html"]=head("Blog","Articles about AI careers and hiring.","blog.html")+b+FOOT
pages["article.html"]=head("Article","Article","blog.html")+hero("Industry",POSTS[0][1],"Gen ZEE AI Team · 6 min read",[("Back to blog","blog.html","b-gh")],sm=True)+'<section class="sec"><div class="wrap art"><p>Replace this placeholder with the article body. In WordPress this becomes single.php.</p><h2>Key takeaways</h2><p>Add summary points here.</p></div></section>'+FOOT
# CONTACT
fld=lambda l,n,t="text":f'<div><label for="{n}">{l}</label><input id="{n}" name="{n}" type="{t}" required></div>'
b=hero("Contact","Let’s talk","Tell us whether you are joining as talent or as a hiring partner. We reply in 1–2 business days.",[],sm=True)
b+=f'''<section class="sec"><div class="wrap two"><div class="rv"><h2 style="font-size:2rem;margin-bottom:18px">Reach us</h2><p style="color:var(--mut)">Email: <a href="mailto:hello@genzee.ai" style="color:var(--orange)">hello@genzee.ai</a><br>Location: Cairo, Egypt — serving talent and companies across MENA<br><a href="https://linkedin.com/company/genzeeai" style="color:var(--orange)">LinkedIn</a></p></div>
<form class="card form rv" id="cform">{fld("First name","fn")}{fld("Last name","ln")}{fld("Email","em","email")}{fld("Phone","ph","tel")}
<div class="full"><label for="as">I am contacting as</label><select id="as"><option>Talent</option><option>Company</option><option>Other</option></select></div>
<div class="full">{fld("Subject","sb")}</div><div class="full"><label for="ms">Message</label><textarea id="ms" rows="5" required></textarea></div>
<div class="full"><button class="btn b-or" type="submit">Send message</button><div class="ok">Thank you! We reply in 1–2 business days.</div></div></form></div></section>'''
pages["contact.html"]=head("Contact","Contact Gen ZEE AI.","contact.html")+b+FOOT
for n,t in(("privacy","Privacy"),("terms","Terms")):
    pages[n+".html"]=head(t,t,n+".html")+hero(t,t,"Draft text — needs full legal copy before launch.",[],sm=True)+f'<section class="sec"><div class="wrap art"><p>{t} text goes here.</p></div></section>'+FOOT
for k,v in pages.items(): open(k,"w",encoding="utf-8").write(v)
print(len(pages),"pages")
