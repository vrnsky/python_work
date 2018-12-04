﻿import pygal
from pygal.maps.world import World

wm  = pygal.maps.world.World()
wm.title = 'North, Central, and South America'

# wm.add('North America', ['ca', 'mx', 'us'])
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', {'ca':34126000, 'us':3093490000, 'mx':113423000})

wm.render_to_file('americas.svg')