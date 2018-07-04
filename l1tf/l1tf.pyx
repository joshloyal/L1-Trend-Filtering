import numpy as np
cimport numpy as np


cdef extern from "l1tf.h":
    int l1tf(const int n, const double *y, const double alpha,
             double *x, int verbose) nogil;
    double l1tf_lambdamax(const int n, double *y) nogil;


np.import_array()


def l1_trend_filter(np.ndarray[np.float64_t, ndim=1, mode='c'] y,
                    double alpha=1.0,
                    int verbose=0):
    cdef int n_samples = y.shape[0]
    cdef np.ndarray[np.float64_t, ndim=1, mode='c'] trend = \
        np.empty(n_samples, dtype=np.float64)

    with nogil:
        l1tf(n_samples, <double*>y.data, alpha, <double*>trend.data, verbose)

    return trend


def l1_alpha_max(np.ndarray[np.float64_t, ndim=1, mode='c'] y):
    cdef int n_samples = y.shape[0]
    cdef double alpha_max

    alpha_max = l1tf_lambdamax(n_samples, <double*>y.data)

    return alpha_max
