# List of URLs to analyze
urls = [
    "http://secure-login.xyz",
    "http://google.com",
    "http://verify-account.ru",
    "https://github.com"
]

# Keywords and patterns commonly found in suspicious URLs
suspicious_keywords = ["secure-login", "verify-account", "login", "account", "xyz", "ru"]

# Function to identify suspicious URLs
def identify_suspicious_urls(urls, keywords):
    suspicious_urls = []
    safe_urls = []

    for url in urls:
        if any(keyword in url for keyword in keywords):
            suspicious_urls.append(url)
        else:
            safe_urls.append(url)

    return suspicious_urls, safe_urls

# Identify suspicious and safe URLs
suspicious, safe = identify_suspicious_urls(urls, suspicious_keywords)

# Display results
print("Suspicious URLs:")
for url in suspicious:
    print(f"- {url}")

print("\nSafe URLs:")
for url in safe:
    print(f"- {url}")