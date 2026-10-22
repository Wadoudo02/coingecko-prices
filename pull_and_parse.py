import requests

def get_coingecko_prices(url):
    """
    Fetches cryptocurrency prices from the CoinGecko API.

    Args:
        url (str): The URL of the CoinGecko API endpoint.

    Returns:
        dict: A dictionary containing the cryptocurrency prices.

    Raises:
        requests.exceptions.RequestException: If there is an issue with the HTTP request.
    """
    try:
        response = requests.get(url, timeout=10)  # Set a timeout for the request
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        return response.json()  # Return the JSON response as a dictionary
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data from CoinGecko: {e}")
        return None