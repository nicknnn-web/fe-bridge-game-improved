with open('D:/Claudecodeworkspace/projects/fe-bridge-game/fe_bridge_v3.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = """      if(g===T.FOREST){
        // 3棵细化的树
        const trees=[
          {cx:16,cy:26,tr:3,trh:10,fr:7},
          {cx:28,cy:22,tr:2.5,trh:12,fr:8},
          {cx:38,cy:26,tr:3,trh:10,fr:7}
        ];
        trees.forEach(tr=>{
          // 树干
          c.fillStyle='#3d2b1f';c.fillRect(x*TS+tr.cx-tr.tr,y*TS+tr.cy-tr.h,tr.tr*2,tr.trh+4);
          // 树冠阴影
          c.fillStyle='#0d2818';c.beginPath();c.arc(x*TS+tr.cx,y*TS+tr.cy,tr.fr+1,0,7);c.fill();
          // 树冠亮部
          c.fillStyle='#1e4d2b';c.beginPath();c.arc(x*TS+tr.cx-1,y*TS+tr.cy-1,tr.fr-1,0,7);c.fill();
          // 树冠高光
          c.fillStyle='#2a6b3a';c.beginPath();c.arc(x*TS+tr.cx-2,y*TS+tr.cy-3,tr.fr-3,0,7);c.fill();
        });
      }
      else if(g===T.BLUE_CASTLE){
        // 蓝色城堡塔楼
        c.fillStyle='#0d1f3c';c.fillRect(x*TS+4,y*TS+4,TS-8,TS-8);
        // 塔身
        c.fillStyle='#1a3050';c.fillRect(x*TS+8,y*TS+10,TS-16,TS-18);
        // 垛口
        for(let i=0;i<4;i++){
          c.fillStyle='#243d5c';
          c.fillRect(x*TS+8+i*9,y*TS+4,6,6);
        }
        // 城门拱
        c.fillStyle='#0a1525';c.beginPath();c.arc(x*TS+22,y*TS+30,5,Math.PI,0);c.fill();c.fillRect(x*TS+17,y*TS+30,10,8);
        // 窗
        c.fillStyle='rgba(59,130,246,.3)';c.fillRect(x*TS+11,y*TS+14,4,4);c.fillRect(x*TS+29,y*TS+14,4,4);
        // 蓝色高光边
        c.strokeStyle='rgba(59,130,246,.25)';c.lineWidth=1;c.strokeRect(x*TS+4,y*TS+4,TS-8,TS-8);
      }
      else if(g===T.RED_CASTLE){
        // 红色城堡塔楼
        c.fillStyle='#3c0d0d';c.fillRect(x*TS+4,y*TS+4,TS-8,TS-8);
        // 塔身
        c.fillStyle='#501a1a';c.fillRect(x*TS+8,y*TS+10,TS-16,TS-18);
        // 垛口
        for(let i=0;i<4;i++){
          c.fillStyle='#5c2020';
          c.fillRect(x*TS+8+i*9,y*TS+4,6,6);
        }
        // 城门拱
        c.fillStyle='#250a0a';c.beginPath();c.arc(x*TS+22,y*TS+30,5,Math.PI,0);c.fill();c.fillRect(x*TS+17,y*TS+30,10,8);
        // 窗
        c.fillStyle='rgba(239,68,68,.3)';c.fillRect(x*TS+11,y*TS+14,4,4);c.fillRect(x*TS+29,y*TS+14,4,4);
        // 红色高光边
        c.strokeStyle='rgba(239,68,68,.25)';c.lineWidth=1;c.strokeRect(x*TS+4,y*TS+4,TS-8,TS-8);
      }
      else if(g===T.MOUNTAIN){c.fillStyle='#22222a';c.beginPath();c.moveTo(x*TS+10,y*TS+34);c.lineTo(x*TS+22,y*TS+8);c.lineTo(x*TS+34,y*TS+34);c.fill();}
      else if(g===T.RIVER){const wv=Math.sin(t*2+x)*3;c.strokeStyle='rgba(56,189,248,.12)';c.lineWidth=2;c.beginPath();c.moveTo(x*TS+4,y*TS+22+wv);c.lineTo(x*TS+TS-4,y*TS+22+wv);c.stroke();}
      else if(g===T.BRIDGE){
        // 木桥底板阴影
        c.fillStyle='#1a1206';c.fillRect(x*TS+2,y*TS+2,TS-4,TS-4);
        // 桥面木板
        for(let p=0;p<4;p++){
          c.fillStyle=p%2===0?'#4a3820':'#3d2e18';
          c.fillRect(x*TS+3,y*TS+4+p*10,TS-6,9);
          // 木板纹理线
          c.strokeStyle='rgba(0,0,0,.3)';c.lineWidth=0.5;
          c.beginPath();c.moveTo(x*TS+3,y*TS+8+p*10);c.lineTo(x*TS+TS-3,y*TS+8+p*10);c.stroke();
        }
        // 护栏
        c.strokeStyle='rgba(180,140,60,.6)';c.lineWidth=2;
        c.strokeRect(x*TS+2,y*TS+2,TS-4,TS-4);
        // 栏杆柱
        c.fillStyle='#5a4428';
        c.fillRect(x*TS+3,y*TS+2,3,TS-4);c.fillRect(x*TS+TS-6,y*TS+2,3,TS-4);
        // 铆钉
        c.fillStyle='rgba(200,160,80,.5)';
        c.beginPath();c.arc(x*TS+4.5,y*TS+4.5,1.5,0,7);c.fill();
        c.beginPath();c.arc(x*TS+TS-4.5,y*TS+4.5,1.5,0,7);c.fill();
        c.beginPath();c.arc(x*TS+4.5,y*TS+TS-4.5,1.5,0,7);c.fill();
        c.beginPath();c.arc(x*TS+TS-4.5,y*TS+TS-4.5,1.5,0,7);c.fill();
      }"""

new = """      if(g===T.FOREST){
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

if old in content:
    content = content.replace(old, new)
    with open('D:/Claudecodeworkspace/projects/fe-bridge-game/fe_bridge_v3.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Replaced terrain renderer')
else:
    print('Still not found - checking exact bytes')
    idx = content.find('// 3棵细化的树')
    if idx >= 0:
        snippet = content[idx-20:idx+50]
        print(f'Found at {idx}: {repr(snippet)}')
    else:
        print('String not found at all')
