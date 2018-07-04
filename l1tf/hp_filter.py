import numpy as np
import scipy.sparse as sparse
import scipy.linalg as linalg
import warnings

from .base import BaseTrendFilter


__all__ = ['hp_filter', 'HPTrendFilter']


def solve_banded_dia(A, b):
    """solve the linear system Ax = b where A is a sparse DIA matrix."""
    if sparse.isspmatrix(b):
        raise ValueError("`b` in solve_banded_dia must be dense.")

    b_ = np.asarray(b)
    overwrite_b = b_ is not b

    if len(A.offsets) == 0:
        l, u = 0, 0
    else:
        l = max(0, -A.offsets.min())
        u = max(0, A.offsets.max())

    # create the ab matrix expected by solved_banded
    if np.array_equal(A.offsets, np.arange(u, l - 1, -1)):
        ab = A.data
        overwrite_ab = False
    else:
        ab = np.zeros((l + u + 1, b.shape[0]))
        ab[u - A.offsets, :A.data.shape[1]] = A.data
        overwrite_ab = True

    try:
        x = linalg.solve_banded((l, u), ab, b_,
                                overwrite_ab=overwrite_ab,
                                overwrite_b=overwrite_b)
    except linalg.LinAlgError:
        warnings.warn("Matrix is exactly singular", MatrixRankWarning)
        x = np.empty_like(b_, dtype=np.float64)
        x.fill(np.nan)

    if x.ndim == 2 and x.shape[1] == 1:
        x = x.ravel()

    return x


def hp_filter(y, alpha=1600, solve_banded=True):
    # build the second-order difference matrix
    n_samples = y.shape[0]

    data = np.repeat([[1.], [-2.], [1.]], n_samples, axis=1)
    D = sparse.dia_matrix((data, [0, 1, 2]),
                          shape=(n_samples - 2, n_samples))

    X = sparse.eye(n_samples) + 2 * alpha * D.T.dot(D)

    if solve_banded:
        return solve_banded_dia(sparse.dia_matrix(X), y)
    else:
        return sparse.linalg.spsolve(X, y, use_umfpack=True)


class HPTrendFilter(BaseTrendFilter):
    """Hodrick-Prescott Filter."""
    def __init__(self, alpha=1600):
        self.alpha = alpha

    def fit(self, df):
        super(HPTrendFilter, self).fit(df)

        y = df['y'].values
        self.history_['trend'] = hp_filter(y, alpha=self.alpha)

        return self

    def predict(self, df=None):
        if df is None:
            df = self.history_.copy()
        else:
            if df.shape[0] == 0:
                raise ValueError('Dataframe has no rows.')

        return df
