# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import requests
import zipfile
import pandas as pd
import numpy as np


def get_data():
    url = 'https://www.imf.org/external/pubs/ft/wp/2008/Data/wp08266.zip'
    r = requests.get(url, stream=True)
    with open("wp08266.zip", 'wb') as f:
        f.write(r.content)
    azip = zipfile.ZipFile('wp08266.zip')
    azip.extractall()


class Solution():
    def solve(self):
        get_data()
        dta_path = 'Financial Reform Dataset Dec 2008.dta'
        d = pd.read_stata(dta_path)
        print(d)
        movieName = 's'
        return movieName
        pass


s = Solution()
s.solve()