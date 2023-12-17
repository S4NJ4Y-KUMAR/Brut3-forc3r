Brute-Force Tool
This is a simple Python script for brute-forcing usernames and passwords on a target website using a provided wordlist. 
REQUIREMENTS:
python 3.x
pip install requests
pip install argparse
OPTIONS:
-t, --target: Target website URL
-m, --method: HTTP method for login request (default: post, choices: get, post)
-w, --wordlist: Path to the wordlist file for usernames and passwords
EXAMPLE:
python brute.py -t http://target.com -m post -w wordlist.txt
USAGE:
1.Make sure you have Python installed on your system.
2.Install the required libraries which is listed in REQUIREMENTS.
3.Run the script using the following command:
python brute.py -t targetsite -m get/post -w wordlist.txt
Note:
Ensure that you have the required permissions before using this script, and use it responsibly and ethically. Unauthorized access to systems is illegal and unethical.
