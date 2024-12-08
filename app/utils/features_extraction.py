import re
import socket
import time
import requests
import dns.resolver
from urllib.parse import urlparse
from ipwhois import IPWhois
import whois
from datetime import datetime
from app.utils.clean_url import clean_and_normalize_url

def extract_features(url):
    # Validate and normalize the URL
    url = clean_and_normalize_url(url)

    features = {}

    # Parse the URL
    parsed_url = urlparse(url)
    path = parsed_url.path
    domain = parsed_url.hostname

    # Ensure the domain is valid
    if domain is None:
        print(f"Invalid domain for URL: {url}")
        features['time_domain_activation'] = 0  # Set to 0 for invalid domains
        features['ttl_hostname'] = 0
    else:
        # 2. time_domain_activation: Time taken for domain resolution (DNS lookup)
        try:
            start_time = time.time()
            ip_address = socket.gethostbyname(domain)  # Perform DNS lookup
            features['time_domain_activation'] = time.time() - start_time
        except socket.gaierror:
            print(f"Failed to resolve domain: {domain}")
            features['time_domain_activation'] = 0

        # 9. ttl_hostname: Actual TTL value for the domain (DNS query)
        try:
            # Use dnspython to get the TTL value from the DNS record
            resolver = dns.resolver.Resolver()
            answer = resolver.resolve(domain, 'A')  # 'A' for IPv4 address records
            ttl_value = answer.rrset.ttl  # Extract TTL value in seconds
            features['ttl_hostname'] = ttl_value
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            print(f"Failed to fetch TTL for domain: {domain}")
            features['ttl_hostname'] = 0
        except Exception as e:
            print(f"Error fetching TTL for domain: {domain} - {e}")
            features['ttl_hostname'] = 0

        # 11. ASN for IP address (ASN related to the domain's IP address)
        try:
            ip_address = socket.gethostbyname(domain)
            ipwhois = IPWhois(ip_address)
            asn_info = ipwhois.lookup_rdap()
            features['asn_ip'] = asn_info.get('asn', 'N/A')
        except Exception as e:
            print(f"Error fetching ASN for IP: {e}")
            features['asn_ip'] = 'N/A'

    features['asn_ip'] = int(features['asn_ip']) if features['asn_ip'] != 'N/A' else 0

    # Extracting additional features from the URL path
    # 1. directory_length: Length of the directories in the URL path
    directories = path.strip("/").split("/")
    features['directory_length'] = len(directories)

    # 3. qty_questionmark_file: Count the number of '?' in the URL path (query params)
    features['qty_questionmark_file'] = path.count("?")

    # 4. qty_space_directory: Count the number of spaces in directories
    features['qty_space_directory'] = path.count(" ")

    # 5. qty_slash_directory: Count the number of slashes in the directory path
    features['qty_slash_directory'] = path.count("/")

    # 6. file_length: Length of the file name in the URL path
    file_name = path.split("/")[-1]
    features['file_length'] = len(file_name)

    # 7. length_url: Length of the full URL
    features['length_url'] = len(url)

    # 8. ttl_hostname: Already added above for the domain TTL value

    # 10. qty_dot_file: Count the number of dots in the file name (for file extension)
    features['qty_dot_file'] = file_name.count(".")

    # 11. time_response: Time taken to get a response from the URL (HTTP request)
    try:
        start_time = time.time()
        response = requests.get(url, timeout=5)  # Add a timeout to avoid blocking
        features['time_response'] = time.time() - start_time
    except requests.RequestException:
        print(f"Failed to get response from URL: {url}")
        features['time_response'] = 0

    # 12. qty_hyphen_file: Count the number of hyphens '-' in the file name
    features['qty_hyphen_file'] = file_name.count("-")

    # 13. time_domain_expiration: Time until the domain expires
    if domain:
        try:
            domain_info = whois.whois(domain)
            expiration_date = domain_info.expiration_date

            # If `expiration_date` is a list (can occur for some domains), take the first value
            if isinstance(expiration_date, list):
                expiration_date = expiration_date[0]

            if expiration_date and isinstance(expiration_date, datetime):
                current_time = datetime.now()
                time_remaining = (expiration_date - current_time).total_seconds()
                features['time_domain_expiration'] = time_remaining  # Time remaining in seconds
            else:
                features['time_domain_expiration'] = 0  # Set to 0 if expiration date is unavailable
        except Exception as e:
            print(f"Failed to fetch domain expiration for {domain}: {e}")
            features['time_domain_expiration'] = 0
    else:
        features['time_domain_expiration'] = 0

    # 14. qty_space_file: Count spaces in the file name (URL encoding)
    features['qty_space_file'] = file_name.count(" ")

    # 15. qty_exclamation_directory: Count the number of '!' in the directory path
    features['qty_exclamation_directory'] = path.count("!")

    # 16. qty_hashtag_directory: Count the number of '#' in the directory path
    features['qty_hashtag_directory'] = path.count("#")

    # 17. qty_slash_url: Count the number of slashes in the URL
    features['qty_slash_url'] = url.count("/")

    # 18. qty_hyphen_directory: Count the number of hyphens '-' in the directory path
    features['qty_hyphen_directory'] = path.count("-")

    # 19. domain_length: Length of the domain name
    features['domain_length'] = len(domain) if domain else 0

    # 20. qty_underline_file: Count the number of underscores '_' in the file name
    features['qty_underline_file'] = file_name.count("_")

    return features
