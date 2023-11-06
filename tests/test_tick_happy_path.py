from datetime import datetime
import pandas as pd
from synthetick.synthetick import Ticks

DATE_FROM: datetime = pd.to_datetime("2023-01-01 00:00:00")
DATE_TO: datetime = pd.to_datetime("2023-02-01 00:00:00")


class TestSyntheticHappyPath:

    def test_gen_tick_date_range(self):
        tick_data_generator = Ticks(trend=0.01,
                                    volatility_range=10,
                                    spread_range=[1, 2],
                                    pip_position=4,
                                    remove_weekend=True)

        tick_data_generator._compute_date_range(date_from=DATE_FROM,
                                                date_to=DATE_TO,
                                                frequency="1s",
                                                init_value=1.1300)
        tick_data_generator.price_time_series.to_csv("test_tick_happy_path.csv", index_label="date-time")

        assert tick_data_generator.price_time_series.index[0] == pd.to_datetime(DATE_FROM)
        assert tick_data_generator.price_time_series.index[-1] == pd.to_datetime(DATE_TO)
        assert pd.infer_freq(tick_data_generator.price_time_series.index) == "S"

    def test_gen_tick_with_compute(self):
        tick_data_generator = Ticks(trend=0.01,
                                    volatility_range=10,
                                    spread_range=[1, 2],
                                    pip_position=4,
                                    remove_weekend=True)

        tick_data_generator.compute(date_from=DATE_FROM,
                                    date_to=DATE_TO,
                                    frequency="1s",
                                    init_value=1.1300)
        tick_data_generator.price_time_series.to_csv("test_tick_happy_path_with_compute.csv", index_label="date-time")

        assert tick_data_generator.price_time_series.index[0] == pd.to_datetime(DATE_FROM)
        assert tick_data_generator.price_time_series.index[-1] == pd.to_datetime(DATE_TO)
        assert pd.infer_freq(tick_data_generator.price_time_series.index) == "S"
