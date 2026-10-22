import pandas as pd
from urllib.parse import urlparse, parse_qs
import os

from pull import get_coingecko_prices

if __name__ == "__main__": 

    # Pulls the URL for the API from a txt file, so more can be added in the future without changing the code.
    config = pd.read_csv("Api_URLs.txt", sep=r"\s+")
 
    os.makedirs("output", exist_ok=True)

    results = {}  # holds each coin's DataFrame until every coin has passed

    for coin, url in zip(config["coin"], config["url"]):
        # The API returns currencies in no guaranteed order, so read the order
        # requested in the URL's vs_currencies part (e.g. "gbp,usd,eur") instead
        url_order = parse_qs(urlparse(url).query)["vs_currencies"][0].lower().split(",")

        data = get_coingecko_prices(url)
        if data is None:
            raise RuntimeError(f"Request failed for {url}")

        # Check the response has this coin and a numeric price for every currency asked for
        prices = data.get(coin, {})
        missing = [c for c in url_order if not isinstance(prices.get(c), (int, float))]
        if missing:
            raise ValueError(f"{coin}: missing or non-numeric price for {missing}. Response: {data}")

        coin_df = pd.DataFrame(list(prices.items()), columns=["currency", "price"])
        # Reorder the rows
        coin_df = coin_df.set_index("currency").reindex(url_order).reset_index()
        results[coin] = coin_df

    # Save all DataFrames to CSV files
    for coin, coin_df in results.items():
        coin_df.to_csv(f"output/{coin}.csv", index=False)


