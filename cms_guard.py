import argparse
import requests

def check_wordpress(url):
    print(f"Scanning {url} for WordPress vulnerabilities...")
    # Example check for a common vulnerability
    response = requests.get(url + '/wp-login.php')
    if response.status_code == 200:
        print("WordPress detected. Check for vulnerabilities.")
    else:
        print("WordPress not found.")

def check_joomla(url):
    print(f"Scanning {url} for Joomla vulnerabilities...")
    # Example check for a common vulnerability
    response = requests.get(url + '/administrator/')
    if response.status_code == 200:
        print("Joomla detected. Check for vulnerabilities.")
    else:
        print("Joomla not found.")

def main():
    parser = argparse.ArgumentParser(description='CMSGuard: A simple CMS vulnerability scanner.')
    parser.add_argument('--url', required=True, help='The URL of the CMS to scan.')
    parser.add_argument('--cms', required=True, choices=['wordpress', 'joomla'], help='The type of CMS to scan.')

    args = parser.parse_args()

    if args.cms == 'wordpress':
        check_wordpress(args.url)
    elif args.cms == 'joomla':
        check_joomla(args.url)

if __name__ == '__main__':
    main()
