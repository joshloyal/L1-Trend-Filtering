import csv
import numpy as np
import pandas as pd

from os.path import dirname
from os.path import join


def load_sp500(return_logy=False):
    module_path = dirname(__file__)
    with open(join(module_path, 'data', 'sp500.csv')) as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        n_samples = int(temp[0])
        data = np.empty((n_samples,), dtype='datetime64[D]')
        target = np.empty((n_samples,), dtype=np.float64)

        for i, ir in enumerate(data_file):
            data[i] = np.datetime64(ir[0])
            target[i] = np.asarray(ir[-1], dtype=np.float64)

        return pd.DataFrame({'ds': data, 'y': target})
