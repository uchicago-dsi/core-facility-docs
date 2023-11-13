import requests
import os

# from dotenv import load_dotenv  # don't do this in Docker

BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places/"


def geocode_address(
    street: str = None, city: str = None, state: str = None, zip: str = None
) -> tuple[float, float]:
    """Geocodes an address using the Mapbox API

    A variety of formats for addresses work here since the Mapbox API is pretty
    smart with how it parses stuff. You can, for example, give a specific
    address or you can give only a city like "Chicago"

    Args:
        street: Street address (ie 123 Fake Street)
        city: City name
        state: State name. This can be the full state name or the abbreviation
        zip: Zip code. This must be a string!

    Returns:
        A tuple of latitude and longitude. These are returned as floats. For
        example:
        (-41.8781, 87.6298)."""
    # load_dotenv()  # don't do this in a Docker container
    url = (
        BASE_URL
        + street
        + " "
        + city
        + " "
        + state
        + " "
        + zip
        + ".json?access_token="
        + os.getenv("MAPBOX_ACCESS_TOKEN")
    )
    try:
        r = requests.get(url)
        lng, lat = r.json()["features"][0]["center"]
    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"API request status code: {r.status_code}")
    return lat, lng
