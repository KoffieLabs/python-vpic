import requests

from .models import Vehicle


class VPicAPI(object):

    url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'

    def lookup_vin(self, vin, year=None):
        vin_info = [vin]
        if year:
            vin_info.append(year)
        data = ','.join(vin_info)
        r = requests.post(self.url, data={'DATA': data, 'format': 'JSON'})
        r.raise_for_status()
        return Vehicle(**r.json()['Results'][0])

    def lookup_vins(self, vin_lookups):
        vin_infos = []
        for vin_info in vin_lookups:
            info = [vin_info['vin']]
            year = vin_info.get('year')
            if year:
                info.append(str(year))
            vin_infos.append(','.join(info))
        data = ';'.join(vin_infos)
        response = requests.post(self.url, data={'DATA': data, 'format': 'JSON'})
        response.raise_for_status()
        return [Vehicle(**r) for r in response.json()['Results']]


vpic = VPicAPI()
