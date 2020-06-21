import re


def get_url(text):
    """Get url from raw text."""
    urls = re.findall(r'http(?:s)?://\S+', text)
    return urls
