import sys
import requests
import datetime
import os

# 1. THE SETUP
# We use standard print statements because GitHub Actions
# captures all "print" output into its execution log.

def check_website(url):
    """Checks if a site is up and prints details."""
    print(f"[{datetime.datetime.now()}] Starting check for: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            print(f"✅ SUCCESS: {url} is ONLINE.")
            print(f"   Latency: {response.elapsed.total_seconds()}s")
        else:
            print(f"⚠️ WARNING: {url} returned status code {response.status_code}")
            # CRITICAL: We must tell GitHub this failed.
            # Exit code 1 turns the status indicator RED.
            sys.exit(1)
            
    except requests.RequestException as e:
        print(f"❌ CRITICAL: Could not reach {url}.")
        print(f"   Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # 2. THE CONFIGURATION
    # We read the target URL from an Environment Variable.
    # This allows us to change the target via GitHub Settings later.
    TARGET_URL = os.getenv("TARGET_URL", "https://www.python.org")
    
    check_website(TARGET_URL)

