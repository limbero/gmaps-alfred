#!/usr/bin/env python
import sys, webbrowser

modes = {
  'bike': 'b',
  'transit': 'r',
  'drive': 'd',
  'walk': 'w'
}

query = sys.argv[1]


mode, locations = query.split(' from ');
f, t = locations.split(' to ');

gmapsurl = 'https://www.google.com/maps/preview?saddr={f}&daddr={t}&dirflg={mode}'

webbrowser.get().open_new_tab(gmapsurl.format(mode=modes[mode], f=f, t=t))
