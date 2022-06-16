from dataclasses import dataclass

# ref: https://github.com/ArjanCodes/2021-config/blob/7c2c3babb0fb66d69eac81590356fae512c5e784/after/conf/config.yaml
@dataclass
class data:
    class raw:
        path: str
        format: str
        separator: str
        header: str
        skip_rows: int


@dataclass
class logs:
    path: str
    fileFormat: str


@dataclass
class MarketBasketConfig:
    raw_data: data.raw
    logs: logs
