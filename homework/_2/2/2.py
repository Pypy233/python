import requests
import zipfile
import pandas as pd
from pandas import DataFrame as df
import numpy as np


class Solution():
    def solve(self):
       # url = 'http://files.grouplens.org/datasets/movielens/ml-latest-small.zip'
       # r = requests.get(url, stream=True)
        #with open("ml-latest-small.zip", 'wb') as f:
         #   f.write(r.content)
        #azip = zipfile.ZipFile('ml-latest-small.zip')
       # azip.extractall()
        csv_path = 'ml-latest-small/movies.csv'

    #    d = df(pd.read_csv(csv_path))
    #    print(d[0][0])
    #    arr1 = np.asarray(d)
    #    ge_str = str(arr1[0][2])
    #     ge_lst = ge_str.split('|')
    #    print(len(ge_lst))
        csv_path2 = 'ml-latest-small/ratings.csv'
        d = pd.read_csv(csv_path2)
        id_arr = np.asarray(d['movieId'])
        rating_arr = np.asarray(d['rating'])
       # print(id_arr)
        id_set = set(id_arr)

      #  print(id_set)
      #  print(id_arr[0], id_arr[1])
    #  print(id_set)
        count_dict = dict(zip(id_arr, rating_arr))
        print(count_dict)

        pass


s = Solution()
s.solve()