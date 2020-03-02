from ..timeseries import TimeSeries
import numpy as np
from sklearn.base import TransformerMixin
import torch


class TimeSeriesDataset(torch.utils.data.Dataset):
    def __init__(self, series: TimeSeries, scaler: TransformerMixin,
                 train_window: int = 1, label_window: int = 1):
        self.series = series.values()
        self.series = scaler.transform(self.series.reshape(-1, 1))
        self.series = torch.from_numpy(self.series).float()
        self.tw = train_window
        self.lw = label_window
        # self.sequences, self.labels = self._input_label_batch(series, train_window, label_window)
        # only if series is not too big to hold in RAM

    def __len__(self):
        return len(self.series) - self.tw - self.lw + 1
        # if series is light enough
        # return len(self.sequences)

    def __getitem__(self, index):
        sequence = self.series[index:index + self.tw]
        label = self.series[index + self.tw:index + self.tw + self.lw]
        return sequence, label[:, 0]
        # if series is light enough
        # return self.sequences[index], self.labels[index]

    @staticmethod
    def _input_label_batch(series: TimeSeries, train_window: int = 1, label_window: int = 1) -> [np.ndarray,
                                                                                                 np.ndarray]:
        sequences = []
        labels = []
        length = len(series)
        for i in range(length - train_window - label_window + 1):
            sequences.append(series.values()[i:i + train_window])
            labels.append(series.values()[i + train_window:i + train_window + label_window])
        return np.array(sequences), np.array(labels)


if __name__ == '__main__':
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler

    pd_series = pd.Series(range(100), index=pd.date_range('20130101', '20130410'))
    pd_series = pd_series.map(lambda x: np.sin(x * np.pi / 6))
    series = TimeSeries(pd_series)
    scaler = MinMaxScaler()
    scaler.fit(series.values().reshape(-1, 1))
    dataset = TimeSeriesDataset(series, scaler, 12, 2)
    train_loader = torch.utils.data.DataLoader(dataset, batch_size=60, shuffle=True,
                                               num_workers=2, pin_memory=True, drop_last=False)
    for batch_idx, (data, target) in enumerate(train_loader):
        print(data.size(), target.size())
        print(data.dtype, target.dtype)
