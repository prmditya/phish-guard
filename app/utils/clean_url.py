from urllib.parse import urlparse, urljoin

def clean_and_normalize_url(url):
    """
    Cleans and normalizes a URL by adding a scheme if missing and validating the domain.
    """
    if not url:
        return None  # Handle empty or None URLs
    
    # Parse the URL
    parsed = urlparse(url)
    
    # Add scheme if missing
    if not parsed.scheme:
        url = "http://" + url.lstrip("/")  # Add scheme and avoid leading slashes
        parsed = urlparse(url)
    
    # Check if the hostname is valid
    if not parsed.hostname:
        return None  # Invalid URL
    
    return url