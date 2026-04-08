import re

with open('D:/Claudecodeworkspace/projects/fe-bridge-game/fe_bridge_v3.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the terrain rendering block using regex
# Match from "if(g===T.FOREST)" to the closing "}" before "else if(g===T.MOUNTAIN)"
pattern = r"      if\(g===T\.FOREST\)\{.*?\n      else if\(g===T\.BRIDGE\)\{.*?\}\n    \}"

match = re.search(pattern, content, re.DOTALL)
if match:
    print(f"Found terrain block at {match.start()}-{match.end()}")
    print("First 100 chars:", repr(match.group()[:100]))
else:
    print("Pattern not found")
    # Try simpler search
    idx = content.find('if(g===T.FOREST)')
    print(f"'if(g===T.FOREST)' found at: {idx}")
