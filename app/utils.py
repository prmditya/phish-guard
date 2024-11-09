import re
from urllib.parse import urlparse

def extract_features(url):
    features = {}
    
    # 1. Panjang URL
    features['url_length'] = len(url)
    
    # 2. Jumlah Tanda Hubung (-) dan Underscore (_)
    features['num_hyphens'] = url.count('-')
    features['num_underscores'] = url.count('_')
    
    # 3. Jumlah Subdomain
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname if parsed_url.hostname else ''
    subdomains = hostname.split('.')[:-2] if hostname else []
    features['num_subdomains'] = len(subdomains)
    
    # 4. HTTPS
    features['has_https'] = 1 if parsed_url.scheme == 'https' else 0
    
    # 5. Penggunaan IP Address
    ip_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    features['has_ip'] = 1 if ip_pattern.match(hostname) else 0
    
    # 6. Banyaknya Tanda Tanya (?) atau Ampersand (&)
    features['num_question_marks'] = url.count('?')
    features['num_amps'] = url.count('&')
    
    # 7. Apakah Menggunakan Suspicious TLDs
    suspicious_tlds = ['.xyz', '.top', '.win', '.club', '.online']
    features['suspicious_tld'] = 1 if any(hostname.endswith(tld) for tld in suspicious_tlds) else 0
    
    # 8. Banyaknya Tautan Redirect
    redirect_keywords = ['redirect', 'track', 'loading']
    features['has_redirect'] = 1 if any(keyword in url.lower() for keyword in redirect_keywords) else 0
    
    return features