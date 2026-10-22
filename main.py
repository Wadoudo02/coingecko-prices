import numpy as np
import pandas as pd
from pull import get_coingecko_prices

FILE = "Api_URLs.txt"
CURRENCY_ORDER = ["gbp", "usd", "eur"]

# Pulls the URL for the API from a txt file, so more can be added in the future without changing the code. 

df = pd.read_csv("Api_URLs.txt", sep=r"\s+")

for url in df["url"]:
    data = get_coingecko_prices(url)
    if data is None:
        continue  # skip this URL if the request failed

    for coin, prices in data.items():
        coin_df = pd.DataFrame(list(prices.items()), columns=["currency", "price"])
        # Reorder columns to match CURRENCY_ORDER
        coin_df = coin_df.set_index("currency").reindex(CURRENCY_ORDER).reset_index()
        coin_df.to_csv(f"{coin}.csv", index=False)


