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
        array1 = np.array(d['country'])
        array2 = np.array(d['year'])
        ls2 = []
        for i in array2:
            ls2.append(i)
        print(len(ls2))
        a = set(array1)
        country_len = len(a)
        print(country_len)

        year_set = set(array2)
        print(year_set)

        data = {}
        for y in year_set:
            data.update({y: ls2.count(y)})
        print(data)
        countries = len(d['country'])
        median_number = np.median(array2)
        #print(medianNumber)
        return [countries, median_number]
        pass

s = Solution()
s.solve()