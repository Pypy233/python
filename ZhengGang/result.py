from __future__ import print_function
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import statsmodels.api as sm

dta2 = [408149, 473300, 171955, 165504, 498158, 163309, 592468, 762256, 237764, 531882]
dta2 = np.array(dta2, dtype=np.float)
# predict situation graph
dta2 = pd.Series(dta2)
dta2.index = pd.Index(sm.tsa.datetools.dates_from_range('2018', '2027'))
fig = plt.figure(figsize=(12, 8))
plt.show()
