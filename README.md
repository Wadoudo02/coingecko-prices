# CoinGecko Prices

Pulls the current Bitcoin, Ethereum and Solana prices in GBP, USD and EUR from the CoinGecko API and saves each coin to its own CSV in `output/`.

## Setup

Needs Python 3.11+.

    python3 -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Run

    python main.py         # fetches prices and writes output/bitcoin.csv, ethereum.csv, solana.csv
    python extension.py    # combines the CSVs and prints the highest, lowest and average GBP price

The CSVs in `output/` are from a sample run so you can check the format straight away. Prices change constantly, so re-run `main.py` to refresh them.

## Extension

`extension.py` reads every CSV in `output/`, tags each row with its coin, combines them into one DataFrame, then finds the highest and lowest priced coin in GBP and the average GBP price.

## Design decisions

- The endpoints live in `Api_URLs.txt` rather than in the code, so adding a coin is just a new line.
- Fetching (`pull.py`) is kept separate from parsing and saving (`main.py`).
- The API doesn't return currencies in a fixed order, so I reorder the rows to match the order in the URL (gbp, usd, eur).
- Every response is checked before anything is saved. If a request fails or a price is missing, the script stops with an error and writes nothing, so you never end up with a mix of new and stale CSVs.
- CoinGecko can return all three coins in one call: `https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=gbp,usd,eur`. I used three calls to match the brief, but in production I'd batch them into one request to go easier on the rate limit.