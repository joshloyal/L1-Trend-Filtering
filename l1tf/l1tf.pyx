import numpy as np
cimport numpy as np


cdef extern from "l1tf.h":
    int l1tf(const int n, const double *y, const double alpha,
             double *x, int verbose) nogil;
    double l1tf_lambdamax(const int n, double *y) nogil;


np.import_array()


def l1_trend_filter(np.ndarray[np.float64_t, ndim=1, mode='c'] y,
                    double alpha=100,
                    int verbose=0):
    """Fit the l1 trend filtering algorithm using the
    primal-dual interior-point method.

    This method utilizes the C solver written by Kwangmoo Koh,
    Seung-Jean Kim and Stephen Boyd.

    Parameters
    ----------
    y : array, dtype=float64, size=[n_samples]
        Target vector

    alpha : float64, optional
        The regularization parameter

    verbose : int, optional
        Boolean that indicates whether to print information about the fit.
        Default is False.

    Returns
    -------
    trend : array, shape=[n_samples]
        The estimated trend.
    """
    cdef int n_samples = y.shape[0]
    cdef np.ndarray[np.float64_t, ndim=1, mode='c'] trend = \
        np.empty(n_samples, dtype=np.float64)

    with nogil:
        l1tf(n_samples, <double*>y.data, alpha, <double*>trend.data, verbose)

    return trend


def l1_alpha_max(np.ndarray[np.float64_t, ndim=1, mode='c'] y):
    """Estimate the maximum value for the regularization parameter (`alpha`).

    Parameters
    ----------
    y : array, dtype=float64, size=[n_samples]
        Target vector

    Returns
    -------
    alpha_max : float64
        The maximum value for the regularization parameter (`alpha`).
    """
    cdef int n_samples = y.shape[0]
    cdef double alpha_max

    with nogil:
        alpha_max = l1tf_lambdamax(n_samples, <double*>y.data)

    return alpha_max
