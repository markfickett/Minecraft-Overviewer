# https://overviewer.readthedocs.org/en/latest/signs/
# POI filters to render player locations and spawn points, and sign text.
import time

_AVATAR_URL_T = 'http://overviewer.org/avatar/%s'
_TIME_FORMAT = '%Y %b %d %H:%M %Z'


def _SignText(poi):
  if poi['id'] != 'Sign':
    return
  texts = []
  for n in range(1, 5):
    t = poi.get('Text%d' % n)
    texts.append('' if t == 'null' else t)
  if any(texts):  # Omit blank signs (used for structure only).
    texts.append('y = %s' % poi['y'])
    return '\n'.join(texts).strip('\n')


def _PlayerLocation(poi):
  if poi['id'] != 'Player':
    return
  # depends on __getattr__ to trigger UUID-to-name lookup
  name = poi['EntityId']
  if not name:
      return  # probably a leftover from before the UUID change <= 2014
  poi['icon'] = _AVATAR_URL_T % name
  return 'location for %s as of %s' % (
      name, time.strftime(_TIME_FORMAT, poi['time']))


def _PlayerSpawn(poi):
  if poi['id'] != 'PlayerSpawn':
    return
  name = poi['EntityId']
  if not name:
    return
  poi['icon'] = _AVATAR_URL_T % name
  return 'spawn point for %s' % name


ALL_MARKERS = [
  {'name': 'Signs', 'filterFunction': _SignText},
  {'name': 'Players', 'filterFunction': _PlayerLocation},
  {'name': 'Spawn Points', 'filterFunction': _PlayerSpawn},
]
