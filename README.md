# Brut3-forc3r
**Description:** This is a Python script for performing a simple brute-force attack on a login page. It takes a username and passwords from a wordlist, and then iterates through each password, attempting to log in to the target website until a valid username/password pair is found.

## Requirements :
- Python 3.x
- `requests` library (install with `pip install requests`)
- `argpharse` library (install with `pip install argphrase`)

## Usage:
1. Make sure you have Python installed on your system.
2. Install the required libraries by running the following commands:

  ```python
  pip install requests
  pip install argphrase
  ```
3. Run the script using the following command:

```python
python brute.py -t targetsite -m get/post -w wordlist.txt

```

5. The script will prompt you to provide the necessary information:

- Enter the URL of the login page.
- Enter the mode of the request.
- Enter the path to the wordlist

6. The script will start the brute-force attack and display the attempted username/passwords pairs. If it successfully finds the correct password, it will print the username and password and exit.

## Note :
- This script is intended for educational and ethical purposes only. Only use it on systems that you have explicit permission to test.
- Brute-force attacks are not recommended as they can be illegal and may cause harm to the target system. Use it responsibly and with caution.
