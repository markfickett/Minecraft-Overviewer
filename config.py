# http://docs.overviewer.org/en/latest/config/
import os
from observer import JSObserver
import poi_filters

BASE = '/home/minecraft/minecraft'
WORLD_NAME = 'Naib'
UP_WORLD_NAME = 'UP'

worlds[WORLD_NAME] = os.path.join(BASE, 'server/world')
worlds[UP_WORLD_NAME] = os.path.join(BASE, 'upserver/upworld')
outputdir = os.path.join(BASE, '../public_html/overviewer')

renders['Day'] = {
  'world': WORLD_NAME,
  'title': 'Day',
  'rendermode': smooth_lighting,
  'defaultzoom': 6,
  'markers': poi_filters.ALL_MARKERS,
#  'forcerender': True,
}

renders['Night'] = {
  'world': WORLD_NAME,
  'title': 'Night',
  'rendermode': smooth_night,
  'defaultzoom': 6,
  'markers': poi_filters.ALL_MARKERS,
}

renders['Nether'] = {
  'world': WORLD_NAME,
  'title': 'Nether',
  'rendermode': nether_smooth_lighting,
  'dimension': 'nether',
  'defaultzoom': 4,
  'markers': poi_filters.ALL_MARKERS,
}

end_smooth_lighting = [Base(), EdgeLines(), SmoothLighting(strength=0.5)]
renders['End'] = {
  'world': WORLD_NAME,
  'title': 'End',
  'rendermode': end_smooth_lighting,
  'dimension': 'end',
  'defaultzoom': 3,
  'markers': poi_filters.ALL_MARKERS,
}

renders['Up'] = {
  'world': UP_WORLD_NAME,
  'title': 'Day',
  'rendermode': smooth_lighting,
  'defaultzoom': 3,
  'markers': poi_filters.ALL_MARKERS,
}

observer = JSObserver(outputdir=outputdir)
