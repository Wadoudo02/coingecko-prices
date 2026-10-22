import glob
import os
import pandas as pd

if __name__ == "__main__":
    # Read every CSV in the output folder and tag each row with its coin name
    frames = []
    for path in glob.glob("output/*.csv"):
        coin_df = pd.read_csv(path)
        coin_df["coin"] = os.path.splitext(os.path.basename(path))[0]
        frames.append(coin_df)

    # Combine all the DataFrames into one
    combined = pd.concat(frames, ignore_index=True)
    print(combined)

    # Keep only the GBP rows
    gbp = combined[combined["currency"] == "gbp"]

    # Highest and lowest priced coin in GBP
    highest = gbp.loc[gbp["price"].idxmax()]
    lowest = gbp.loc[gbp["price"].idxmin()]
    print(f"Highest: {highest['coin']} at £{highest['price']:.2f}")
    print(f"Lowest: {lowest['coin']} at £{lowest['price']:.2f}")

    # Average GBP price across all coins found
    print(f"Average GBP price: £{gbp['price'].mean():.2f}")