"""This is just a sample to check how requests is working."""
import requests

try:
    requests.get("just/to/check", timeout=100)
except requests.exceptions.RequestException:
    print("requests didn\'t work")
