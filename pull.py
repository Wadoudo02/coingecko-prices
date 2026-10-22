import requests

def get_coingecko_prices(url):
    """
    Fetches cryptocurrency prices from the CoinGecko API.

    Args:
        url (str): The URL of the CoinGecko API endpoint.

    Returns:
        dict: A dictionary containing the cryptocurrency prices or None if the request fails.

    """
    try:
        response = requests.get(url, timeout=10) 
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        return response.json()  
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data from CoinGecko: {e}")
        return None