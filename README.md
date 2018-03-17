# Python-vPic

A simple wrapper around the vPic API.

## To install:
pip install python-vpic

## To use:
```
from vpic import vpic

# Single VIN lookup
vehicle = vpic.lookup_vin('5FYD4FS147B031975')
print('Make:', vehicle.make)
print('Model:', vehicle.model)
print('Year:', vehicle.model_year)

# Bulk VIN lookup
vehicles = vpic.lookup_vins(
    [{'vin': '5FYD4FS147B031975', 'year': 2006}, {'vin': '4V4WDBPFSCN735320'}]
)
# ...
```
