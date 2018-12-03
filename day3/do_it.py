from collections import namedtuple, defaultdict

# import pandas as pd
# import numpy as np

coord = namedtuple('coord', ['x', 'y'])

claims = {}
fabric = defaultdict(lambda: {'count': 0, 'claims': set()})
with open('input', 'rb') as input_file:
    for line in input_file:
        tokens = line.split()
        coords = tokens[2].replace(':', '').split(',')
        size = tokens[3].split('x')
        data = {
            'x': int(coords[0]),
            'y': int(coords[1]),
            'width': int(size[0]),
            'height': int(size[1])
        }
        claims[tokens[0]] = data
        for col in range(data['x'], data['x'] + data['width']):
            for row in range(data['y'], data['y'] + data['height']):
                fabric[coord(x=col, y=row)]['count'] += 1
                fabric[coord(x=col, y=row)]['claims'] |= set([tokens[0]])

print len([v for v in fabric.values() if v['count'] > 1])

disqualified = [v['claims'] for v in fabric.values() if v['count'] > 1]
print len(disqualified)
disqualified = reduce(lambda agg, cur: agg | cur, disqualified)
print len(disqualified)
print len(set(claims.keys()))
print set(claims.keys()) - disqualified
