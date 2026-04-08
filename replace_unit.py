import re

with open('D:/Claudecodeworkspace/projects/fe-bridge-game/fe_bridge_v3.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = """  unit(u,sel,t){
    if(u.dead) return;
    const c=this.ctx;
    const bob=Math.sin(t*2+u.bob)*1.5;
    const px=u.px, py=u.py+bob;
    const sc=u.attackScale||1;
    c.save();
    c.translate(px,py); c.scale(sc,sc); c.translate(-px,-py);
    c.fillStyle='rgba(0,0,0,.25)'; c.beginPath(); c.ellipse(px,py+15,11,2.5,0,0,7); c.fill();
    if(sel){c.shadowColor='#fbbf24'; c.shadowBlur=12;}
    if(u.flash>0){c.fillStyle=`rgba(255,255,255,${u.flash*0.1})`;c.beginPath();c.arc(px,py,21,0,7);c.fill();}
    c.fillStyle='#080c14'; c.beginPath(); c.arc(px,py,17,0,7); c.fill();
    if(!u.done){c.fillStyle=u.isPlayer?'rgba(59,130,246,.1)':'rgba(239,68,68,.1)';c.beginPath();c.arc(px,py,16,0,7);c.fill();}
    c.lineWidth=2; c.strokeStyle=u.done?'#4b5563':(u.isPlayer?'#3b82f6':'#ef4444'); c.beginPath(); c.arc(px,py,16,0,7); c.stroke(); c.shadowBlur=0;
    const faces={'p1':'🧑‍🎤','p2':'🛡️','p3':'🏇','p4':'🏹','e1':'🧙','e2':'⚔️','e3':'🗡️','e4':'🎯'};
    c.font='22px sans-serif'; c.textAlign='center'; c.textBaseline='middle'; c.fillText(faces[u.id]||'❓',px,py+1);
    c.font='10px serif'; c.textAlign='left'; c.fillText(u.wp.i,px+14,py-5);
    const hp=u.hp/u.mhp;
    c.fillStyle='#0f172a'; c.fillRect(px-11,py+20,22,3);
    c.fillStyle=hp>0.5?'#22c55e':hp>0.25?'#eab308':'#ef4444'; c.fillRect(px-11,py+20,22*hp,3);
    c.restore();
  },"""

new = """  unit(u,sel,t){
    if(u.dead) return;
    const c=this.ctx;
    const bob=Math.sin(t*2+u.bob)*1.5;
    const px=u.px, py=u.py+bob;
    const sc=u.attackScale||1;
    c.save();
    c.translate(px,py); c.scale(sc,sc); c.translate(-px,-py);

    // shadow
    c.fillStyle='rgba(0,0,0,.3)'; c.beginPath(); c.ellipse(px,py+16,12,3,0,0,7); c.fill();

    // hit flash
    if(u.flash>0){c.fillStyle=`rgba(255,255,255,${u.flash*0.15})`;c.beginPath();c.arc(px,py,20,0,7);c.fill();}

    // breathing selection border
    if(sel){
      const pulse=0.5+Math.sin(t*4)*0.5;
      c.strokeStyle=`rgba(251,191,36,${pulse})`; c.lineWidth=3;
      c.beginPath(); c.arc(px,py,20,0,7); c.stroke();
      c.shadowColor='#fbbf24'; c.shadowBlur=15;
    }

    // bg circle
    c.fillStyle='#0d1117'; c.beginPath(); c.arc(px,py,17,0,7); c.fill();

    // aura for units not yet acted
    if(!u.done){
      c.fillStyle=u.isPlayer?'rgba(59,130,246,.15)':'rgba(239,68,68,.15)';
      c.beginPath(); c.arc(px,py,16,0,7); c.fill();
    }

    // border
    c.strokeStyle=u.done?'#374151':(u.isPlayer?'#3b82f6':'#ef4444'); c.lineWidth=2;
    c.beginPath(); c.arc(px,py,16,0,7); c.stroke(); c.shadowBlur=0;

    // geometric icon
    this._drawUnitIcon(c,u,px,py);

    // HP bar (thicker)
    const hp=u.hp/u.mhp;
    c.fillStyle='#1f2937'; c.fillRect(px-12,py+21,24,4);
    c.fillStyle=hp>0.5?'#22c55e':hp>0.25?'#eab308':'#ef4444';
    c.fillRect(px-12,py+21,24*hp,4);
    c.strokeStyle='rgba(255,255,255,.1)'; c.lineWidth=0.5;
    c.strokeRect(px-12,py+21,24,4);

    c.restore();
  },
  _drawUnitIcon(c,u,px,py){
    const j=u.job, wk=u.wk, p=u.isPlayer;
    const base=p?'#60a5fa':'#f87171';
    const acc=p?'#fbbf24':'#fcd34d';
    c.lineWidth=1.5; c.lineCap='round'; c.lineJoin='round';

    if(j==='领主'||j==='剑士'){
      // shield
      c.fillStyle=base; c.strokeStyle=acc; c.lineWidth=1;
      c.beginPath();
      c.moveTo(px-7,py-8); c.lineTo(px+7,py-8);
      c.lineTo(px+7,py+2); c.lineTo(px,py+10); c.lineTo(px-7,py+2);
      c.closePath(); c.fill(); c.stroke();
      c.strokeStyle=acc; c.lineWidth=1;
      c.beginPath(); c.moveTo(px,py-5); c.lineTo(px,py+6); c.stroke();
      c.beginPath(); c.moveTo(px-4,py); c.lineTo(px+4,py); c.stroke();
    } else if(j==='重甲'){
      // armor circle
      c.fillStyle='#4b5563'; c.strokeStyle=base; c.lineWidth=2;
      c.beginPath(); c.arc(px,py,12,0,7); c.fill(); c.stroke();
      // axe
      c.strokeStyle=acc; c.lineWidth=2;
      c.beginPath(); c.moveTo(px,py-9); c.lineTo(px,py+9); c.stroke();
      c.fillStyle=acc;
      c.beginPath(); c.moveTo(px-8,py-6); c.lineTo(px,py-1); c.lineTo(px+8,py-6); c.closePath(); c.fill();
    } else if(j==='骑士'){
      // triangle
      c.fillStyle=base; c.strokeStyle=acc; c.lineWidth=1;
      c.beginPath(); c.moveTo(px,py-11); c.lineTo(px+11,py+9); c.lineTo(px-11,py+9); c.closePath(); c.fill(); c.stroke();
      // lance
      c.strokeStyle=acc; c.lineWidth=1.5;
      c.beginPath(); c.moveTo(px,py-14); c.lineTo(px,py+6); c.stroke();
      c.fillStyle=acc;
      c.beginPath(); c.moveTo(px-3,py-14); c.lineTo(px,py-20); c.lineTo(px+3,py-14); c.closePath(); c.fill();
    } else if(j==='弓手'){
      // diamond
      c.fillStyle=base; c.strokeStyle=acc; c.lineWidth=1;
      c.beginPath(); c.moveTo(px,py-12); c.lineTo(px+9,py); c.lineTo(px,py+12); c.lineTo(px-9,py); c.closePath(); c.fill(); c.stroke();
      // bow arc
      c.strokeStyle=acc; c.lineWidth=1.5;
      c.beginPath(); c.arc(px,py,7,-Math.PI*0.7,-Math.PI*0.3); c.stroke();
      c.beginPath();
      c.moveTo(px+7*Math.cos(-Math.PI*0.7),py+7*Math.sin(-Math.PI*0.7));
      c.lineTo(px+7*Math.cos(-Math.PI*0.3),py+7*Math.sin(-Math.PI*0.3)); c.stroke();
    }
  },"""

if old in content:
    content = content.replace(old, new)
    with open('D:/Claudecodeworkspace/projects/fe-bridge-game/fe_bridge_v3.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Replaced unit renderer')
else:
    print('String not found, searching...')
    idx = content.find("unit(u,sel,t)")
    print(f"Found at index: {idx}")
    print(repr(content[idx:idx+300]))
