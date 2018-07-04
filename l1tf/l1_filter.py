from .base import BaseTrendFilter
from .l1tf import l1_trend_filter, l1_alpha_max


__all__ = ['l1_trend_filter', 'l1_alpha_max', 'L1TrendFilter']


class L1TrendFilter(BaseTrendFilter):
    def __init__(self, alpha=1600, prop=None, verbose=False):
        self.alpha = alpha
        self.prop = prop
        self.verbose = verbose

    def fit(self, df):
        super(L1TrendFilter, self).fit(df)

        y = df['y'].values

        if self.prop is not None:
            self.alpha = l1_alpha_max(y) * self.prop

        print(self.alpha)
        self.history_['trend'] = l1_trend_filter(
            y, alpha=self.alpha, verbose=self.verbose)

        return self

    def predict(self, df=None):
        if df is None:
            df = self.history_.copy()
        else:
            if df.shape[0] == 0:
                raise ValueError('Dataframe has no rows.')

        return df
