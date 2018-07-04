import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class BaseTrendFilter(object):
    def fit(self, df):
        if ('ds' not in df) or ('y' not in df):
            raise ValueError(
                "Dataframe must have columns 'ds' and 'y' with the dates and "
                "values respectively."
            )

        self.history_ = df[df['y'].notnull()].copy()
        self.history_dates_ = pd.to_datetime(df['ds']).sort_values()

        return self

    def make_future_dataframe(self, periods, freq='D', include_history=True):
        if self.history_dates_ is None:
            raise Exception('Model must be fit before this can be used.')

        last_date = self.history_dates_.max()
        dates = pd.date_range(
            start=last_date,
            periods=periods + 1,
            freq=freq)
        dates = dates[dates > last_date]
        dates = dates[:periods]

        if include_history:
            dates = np.concatenate((np.array(self.history_dates_), dates))

        return pd.DataFrame({'ds': dates})

    def plot(self, df, ax=None):
        if ax is None:
            fig = plt.figure(facecolor='w', figsize=(10, 6))
            ax = fig.add_subplot(111)
        else:
            fig = ax.get_figure()

        fcst_t = df['ds'].dt.to_pydatetime()
        ax.plot(self.history_['ds'].dt.to_pydatetime(), self.history_['y'], 'k.')
        ax.plot(fcst_t, df['trend'], ls='-', c='#0072B2', lw=2)

        ax.grid(True, which='major', c='gray', ls='-', lw=1, alpha=0.2)
        ax.set_xlabel('ds')
        ax.set_ylabel('y')
        fig.tight_layout()

        return fig
