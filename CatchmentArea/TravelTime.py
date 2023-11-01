"""
Travel Catchment Area using Travel Time
Create 30 minutes isochrones map to arrive at Melbourne Central at 8:30
For public transport, 15 mintues range allowed for waiting time
"""

import traveltimepy as ttpy
import os
from datetime import datetime

output = []

arrival_search = {
  'id': "Melbourne Central",
  'arrival_time':  "2023-03-16T08:30:00.000Z",
  'travel_time': 1800,
  'coords': {'lat': -37.8097547589978, 'lng': 144.962592276797},
  'transportation': {'type': "public_transport"},
  'range': {'enabled': True, 'width': 900}
} 
area = ttpy.time_map(arrival_searches=[arrival_search], limit=3000)
output.append(response_to_geojson(area))
