# Generates brand-style SVG illustrations -> assets/img/*.svg  (swap with real photos any time)
P={'or':('#FFF4E8','#FFDDBA','#FF7A00','#6D28D9'),'pu':('#F3ECFF','#D9C8FB','#6D28D9','#00B8A5'),'te':('#E6FCF5','#BFF3E3','#00B8A5','#6D28D9')}
O='#FF7A00';PU='#6D28D9';TE='#00D2BE';N='#0A1931';G='#CBD5E8'
def R(x,y,w,h,f='#fff',r=24,s=True,o=1):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{f}" opacity="{o}"{" filter=\"url(#s)\"" if s else ""}/>'
def C(x,y,r,f,o=1):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f}" opacity="{o}"/>'
def L(x1,y1,x2,y2,c,w=4,d=''):return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" {d}/>'
def PL(pts,c,w=6):return f'<polyline points="{pts}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
def dots(x,y):return C(x,y,7,'#FF5F57')+C(x+26,y,7,'#FEBC2E')+C(x+52,y,7,'#28C840')
def laptop(a,b):
    s=R(170,110,560,370)+dots(206,150)
    for i,(x,w,c) in enumerate([(206,230,a),(206,320,G),(246,170,b),(246,270,G),(246,130,O),(206,210,G),(246,250,a)]):s+=R(x,196+i*38,w,16,c,8,False)
    return s+'<path d="M110 500h680l-44 46H154z" fill="'+N+'"/>'+R(560,330,240,130)+C(610,395,26,'#19c98c')+PL('598,395 608,406 624,384','#fff',6)+R(652,380,100,12,G,6,False)+R(652,402,70,12,G,6,False)
def chart(a,b):
    s=R(140,110,620,450);h=[90,150,120,210,250,310]
    for i,v in enumerate(h):s+=R(200+i*88,500-v,50,v,a if i%2==0 else b,14,False)
    s+=L(180,500,720,500,G,4)+PL('225,400 313,340 401,372 489,270 577,230 665,160',N,6)
    for i,(x,y) in enumerate([(225,400),(313,340),(401,372),(489,270),(577,230),(665,160)]):s+=C(x,y,9,'#fff')+C(x,y,5,O)
    return s+f'<path d="M665 160l-4 -34 30 18z" fill="{N}"/>'
def network(a,b,n=3):
    xs=[210+i*(480/(n)) for i in range(n+1)];cnt=[3,4,4,3,2][:n+1];s=R(130,100,640,480);pos=[]
    for x,c in zip(xs,cnt):pos.append([(x,170+j*(340/(c-1 if c>1 else 1))) if c>1 else (x,340) for j in range(c)])
    for l in range(n):
        for p in pos[l]:
            for q in pos[l+1]:s+=L(p[0],p[1],q[0],q[1],G,2.5)
    for l,col in enumerate(pos):
        for j,(x,y) in enumerate(col):s+=C(x,y,20,[a,b,O][(l+j)%3])+C(x,y,8,'#fff')
    return s
def tokens(a,b):
    s=R(120,100,660,290)
    for r,(row) in enumerate([[110,70,140,90,120],[150,100,80,130],[90,160,110]]):
        x=160
        for w in row:s+=R(x,140+r*80,w,44,[a,b,O,G][(x+w)%4] if (x//7)%3 else G,12,False,.9);x+=w+14
    return s+R(120,430,660,190,'#fff')+R(160,470,360,18,a,9,False)+R(160,508,520,14,G,7,False)+R(160,538,440,14,G,7,False)+R(160,568,40,18,O,4,False)+C(730,470,22,b)
def flow(a,b):
    pts=[(150,330),(340,200),(530,330),(720,200)];s=R(80,80,740,540,'#fff',30,True,.55)
    for i in range(3):s+=L(pts[i][0]+60,pts[i][1]+10,pts[i+1][0]-60,pts[i+1][1]+10,N,4,'stroke-dasharray="2 12"')
    for i,(x,y) in enumerate(pts):s+=R(x-60,y-60,120,120,'#fff',30)+C(x,y,26,[a,b,O,TE][i])+C(x,y,10,'#fff')
    return s+f'<path d="M200 520 C 330 640, 560 640, 700 520" fill="none" stroke="{b}" stroke-width="5" stroke-dasharray="3 14" stroke-linecap="round"/>'+R(330,560,240,50,'#fff',25)+C(360,585,10,'#19c98c')+R(382,577,140,16,G,8,False)
def vision(a,b):
    s=R(130,100,640,460,'#fff',30)+R(150,120,600,420,'url(#g)',22,False)+C(450,330,70,b,.9)+f'<path d="M290 540c0-110 70-150 160-150s160 40 160 150z" fill="{a}"/>'
    s+=f'<rect x="340" y="250" width="220" height="250" rx="14" fill="none" stroke="{O}" stroke-width="5" stroke-dasharray="14 10"/>'+R(340,214,130,32,O,10,False)+R(354,226,80,9,'#fff',4,False)
    return s+L(150,330,750,330,TE,3,'opacity=".7"')+C(235,215,9,TE)+C(665,445,9,TE)
def badge(a,b):
    s=R(130,110,640,470,'#fff',30,True,.6)+f'<path d="M450 140 L640 210 V350 C640 450 560 520 450 560 C340 520 260 450 260 350 V210Z" fill="{a}" filter="url(#s)"/><path d="M450 185 L605 240 V350 C605 430 540 487 450 520 C360 487 295 430 295 350 V240Z" fill="#fff" opacity=".28"/>'
    return s+PL('370,350 430,410 540,290','#fff',22)+R(160,520,200,24,G,12,False)+R(160,520,150,24,O,12,False)+C(700,170,14,TE)+C(190,200,10,PU)
def bands(a,b):
    def bd(yc,c):
        pts=[(-2.4,-1.4),(-.3,.7),(.6,.7),(2.4,2.5)];up=[(450+x*62,yc-yy*62) for x,yy in pts];dn=[(x,yy+62) for x,yy in up]
        return f'<polygon points="{" ".join(f"{x:.0f},{yy:.0f}" for x,yy in up+dn[::-1])}" fill="{c}" filter="url(#s)"/>'
    return bd(250,TE)+bd(370,'#7C3AED')+bd(490,O)+C(150,150,12,PU)+C(760,600,16,TE)+C(110,560,9,O)
def chat(a,b):
    return R(120,120,520,130,'#fff',34)+C(180,185,34,a)+R(236,160,330,16,G,8,False)+R(236,192,240,16,G,8,False)+R(260,300,520,130,a,34)+R(300,336,380,16,'#fff',8,False)+R(300,368,260,16,'#fff',8,False)+C(730,365,34,b)+R(120,480,420,100,'#fff',34)+C(180,530,26,O)+R(226,510,60,14,G,7,False)+C(310,517,6,a)+C(332,517,6,b)+C(354,517,6,O)
def kanban(a,b):
    s=''
    for i,c in enumerate([a,b,O]):
        x=130+i*215;s+=R(x,110,195,480,'#fff',26)+R(x+20,138,90,14,c,7,False)
        for j in range(3-(i==2)+(i==0)*0):s+=R(x+18,180+j*130,159,100,'#F6F8FC',18,False)+R(x+18,180+j*130,8,100,c,4,False)+R(x+40,202+j*130,100,12,G,6,False)+R(x+40,228+j*130,70,10,G,5,False)+C(x+150,262+j*130,12,c)
    return s
def team(a,b):
    s=R(130,330,640,250,'#fff',30)
    for i,v in enumerate([70,110,90,150,190]):s+=R(180+i*58,540-v,34,v,[a,b][i%2],10,False)
    for i,(x,c) in enumerate([(240,a),(450,b),(660,O)]):s+=C(x,170,52,c)+f'<path d="M{x-90} 310c0-80 40-100 {90} -100s{90} 20 {90} 100z" fill="{c}" opacity=".85"/>'
    return s+L(300,170,390,170,N,3,'stroke-dasharray="2 10"')+L(510,170,600,170,N,3,'stroke-dasharray="2 10"')+R(560,380,170,150,'#F6F8FC',20,False)+PL('580,500 620,450 650,470 710,410',O,6)
def bridge(a,b):
    s=R(70,430,240,170,a,24)+R(590,260,240,340,b,24)
    for i in range(4):s+=R(330+i*66,400-i*44,60,24,[TE,PU,O,TE][i],10)
    return s+C(210,380,26,N)+f'<path d="M180 430c0-60 60-60 60 0z" fill="{N}"/>'+C(710,210,26,O)+L(710,236,710,260,O,5)+PL('690,200 706,214 736,184','#fff',5)+L(120,430,120,380,N,4)+R(100,330,70,40,O,8,False)
def cta(a,b):return bands(a,b)+network(a,b,2)[0:0]+C(750,140,70,a,.18)+R(560,520,260,90,'#fff',28)+C(610,565,22,'#19c98c')+PL('600,565 608,574 622,556','#fff',5)+R(646,550,120,14,G,7,False)+R(646,574,80,12,G,6,False)
def svg(body,p,alt):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 700" role="img" aria-label="{alt}"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{p[0]}"/><stop offset="1" stop-color="{p[1]}"/></linearGradient><filter id="s" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="16" stdDeviation="16" flood-color="#0A1931" flood-opacity=".16"/></filter></defs><rect width="900" height="700" fill="url(#g)"/>{C(790,90,190,p[2],.14)}{C(90,650,170,p[3],.12)}{body}</svg>'
I={'t-ml':(chart,'or','Rising model accuracy chart'),'t-dl':(lambda a,b:network(a,b,4),'pu','Deep neural network layers'),'t-llm':(tokens,'te','Language model prompt and answer'),'t-agent':(flow,'or','Agentic AI workflow nodes'),'t-cv':(vision,'pu','Computer vision object detection'),
'o-tracks':(laptop,'te','Learner coding on a laptop'),'o-assess':(badge,'or','Validated skill badge'),'o-place':(bands,'pu','Upward career path'),'o-mentor':(chat,'or','Mentor conversation'),'o-projects':(kanban,'te','Project board'),'o-corp':(team,'pu','Team upskilling'),
's-train':(laptop,'pu','Train on a track'),'s-build':(kanban,'or','Build portfolio projects'),'s-validate':(badge,'te','Get validated'),'s-gap':(bridge,'pu','Close the skills gap'),'s-place':(bands,'or','Get placed'),
'v-talent':(laptop,'or','Talent learning AI'),'v-company':(team,'pu','Company hiring AI talent'),'cta':(cta,'te','Gen ZEE AI ascent')}
for k,(f,pk,alt) in I.items():
    p=P[pk];open(f'assets/img/{k}.svg','w').write(svg(f(p[2],p[3]),p,alt))
print(len(I),'images')
