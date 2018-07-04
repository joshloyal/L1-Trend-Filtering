import csv

import numpy as np

from os.path import join


def load_data(module_path, data_file_name, is_classification=True):
    with open(join(module_path, 'data', data_file_name)) as csv_file:
        data_file = csv.reader(csv_file)
        temp = next(data_file)
        n_samples = int(temp[0])
        n_features = int(temp[1])
        data = np.empty((n_samples, n_features))

        if is_classification:
            target_dtype = np.int
        else:
            target_dtype = np.float64
        target = np.empty((n_samples,), dtype=target_dtype)

        for i, ir in enumerate(data_file):
            data[i] = np.asarray(ir[:-1], dtype=np.object)
            target[i] = np.asarray(ir[-1], dtype=target_dtype)

        return data, target
