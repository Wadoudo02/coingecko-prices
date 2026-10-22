import pandas as pd
from pull import get_coingecko_prices
from urllib.parse import urlparse, parse_qs

if __name__ == "__main__": 

    df = pd.read_csv("Api_URLs.txt", sep=r"\s+")

    # Pulls the URL for the API from a txt file, so more can be added in the future without changing the code. 

    for url in df["url"]:
        data = get_coingecko_prices(url)
        if data is None:
            continue  # skip this URL if the request failed

        # The API returns currencies in no guaranteed order, so read the order
        # requested in the URL's vs_currencies part (e.g. "gbp,usd,eur") instead
        url_order = parse_qs(urlparse(url).query)["vs_currencies"][0].lower().split(",")

        for coin, prices in data.items():
            coin_df = pd.DataFrame(list(prices.items()), columns=["currency", "price"])
            # Reorder the rows
            coin_df = coin_df.set_index("currency").reindex(url_order).reset_index()
            coin_df.to_csv(f"output/{coin}.csv", index=False)


