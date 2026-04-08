import re

with open('D:/Claudecodeworkspace/projects/fe-bridge-game/fe_bridge_v3.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_terrain = """      if(g===T.FOREST){
        const tx=x*TS, ty=y*TS;
        // GBA风格简化树
        c.fillStyle='#5a3d2b';c.fillRect(tx+17,ty+24,6,14);
        c.fillStyle='#1a4d2b';c.beginPath();c.moveTo(tx+20,ty+8);c.lineTo(tx+32,ty+26);c.lineTo(tx+8,ty+26);c.closePath();c.fill();
        c.fillStyle='#2a6d3a';c.beginPath();c.moveTo(tx+20,ty+14);c.lineTo(tx+29,ty+26);c.lineTo(tx+11,ty+26);c.closePath();c.fill();
      }
      else if(g===T.BLUE_CASTLE){
        const tx=x*TS, ty=y*TS;
        c.fillStyle='#0d1f3c';c.fillRect(tx+3,ty+3,TS-6,TS-6);
        c.strokeStyle='rgba(59,130,246,.15)';c.lineWidth=0.5;
        for(let r=0;r<4;r++){c.beginPath();c.moveTo(tx+3,ty+7+r*11);c.lineTo(tx+TS-3,ty+7+r*11);c.stroke();}
        for(let r=0;r<4;r++){for(let col=0;col<3;col++){
          const bx=col%2===0?tx+3:tx+17;
          c.beginPath();c.moveTo(bx+r*11,ty+3+r*11);c.lineTo(bx+r*11+10,ty+3+r*11);c.stroke();
        }}
        c.fillStyle='#060e18';c.fillRect(tx+17,ty+22,16,18);
        c.fillStyle='#0a1525';c.fillRect(tx+18,ty+22,14,17);
      }
      else if(g===T.RED_CASTLE){
        const tx=x*TS, ty=y*TS;
        c.fillStyle='#3c0d0d';c.fillRect(tx+3,ty+3,TS-6,TS-6);
        c.strokeStyle='rgba(239,68,68,.15)';c.lineWidth=0.5;
        for(let r=0;r<4;r++){c.beginPath();c.moveTo(tx+3,ty+7+r*11);c.lineTo(tx+TS-3,ty+7+r*11);c.stroke();}
        for(let r=0;r<4;r++){for(let col=0;col<3;col++){
          const bx=col%2===0?tx+3:tx+17;
          c.beginPath();c.moveTo(bx+r*11,ty+3+r*11);c.lineTo(bx+r*11+10,ty+3+r*11);c.stroke();
        }}
        c.fillStyle='#200606';c.fillRect(tx+17,ty+22,16,18);
        c.fillStyle='#300a0a';c.fillRect(tx+18,ty+22,14,17);
      }
      else if(g===T.MOUNTAIN){
        c.fillStyle='#2a2a35';c.beginPath();c.moveTo(x*TS+20,y*TS+6);c.lineTo(x*TS+38,y*TS+36);c.lineTo(x*TS+2,y*TS+36);c.closePath();c.fill();
        c.fillStyle='#3a3a45';c.beginPath();c.moveTo(x*TS+20,y*TS+6);c.lineTo(x*TS+30,y*TS+20);c.lineTo(x*TS+10,y*TS+20);c.closePath();c.fill();
      }
      else if(g===T.RIVER){
        c.fillStyle='#060d1a';c.fillRect(x*TS+2,y*TS+2,TS-4,TS-4);
        c.strokeStyle='rgba(56,149,248,.2)';c.lineWidth=1;
        for(let i=0;i<3;i++){c.beginPath();c.moveTo(x*TS+4,y*TS+10+i*12);c.lineTo(x*TS+TS-4,y*TS+10+i*12);c.stroke();}
      }
      else if(g===T.BRIDGE){
        const tx=x*TS, ty=y*TS;
        c.fillStyle='#1a1206';c.fillRect(tx+2,ty+2,TS-4,TS-4);
        for(let p=0;p<4;p++){
          c.fillStyle=p%2===0?'#4a3820':'#3d2e18';
          c.fillRect(tx+3,ty+4+p*10,TS-6,9);
        }
        c.strokeStyle='rgba(180,140,60,.7)';c.lineWidth=2;
        c.strokeRect(tx+2,ty+2,TS-4,TS-4);
        c.fillStyle='#5a4428';c.fillRect(tx+3,ty+2,3,TS-4);c.fillRect(tx+TS-6,ty+2,3,TS-4);
        c.fillStyle='rgba(200,160,80,.6)';
        c.beginPath();c.arc(tx+4.5,ty+4.5,1.5,0,7);c.fill();
        c.beginPath();c.arc(tx+TS-4.5,ty+TS-4.5,1.5,0,7);c.fill();
      }"""

# Pattern to match from "if(g===T.FOREST)" through all terrain types to the closing of BRIDGE block
pattern = r"      if\(g===T\.FOREST\)\{.*?\}\n      else if\(g===T\.BRIDGE\)\{.*?\}\n    \}"

result, count = re.subn(pattern, new_terrain + '\n    }', content, count=1, flags=re.DOTALL)
if count > 0:
    with open('D:/Claudecodeworkspace/projects/fe-bridge-game/fe_bridge_v3.html', 'w', encoding='utf-8') as f:
        f.write(result)
    print(f'Replaced {count} occurrence(s)')
else:
    print('Pattern not found - checking structure')
    # Let's see what's at the FOREST block
    idx = content.find('if(g===T.FOREST)')
    print(f'FOREST at: {idx}')
    # Check what comes after BRIDGE
    idx2 = content.find('if(g===T.MOUNTAIN)')
    print(f'MOUNTAIN at: {idx2}')
    print(repr(content[idx2-200:idx2+50]))
