### README.md

```markdown
# Python Brute Force Script

Date: August 27, 2024

This repository contains a Python script designed to perform brute force attacks on an online login form. The script attempts to guess the password of a user account by iterating over a wordlist and sending requests to the target URL.

### Features
- Sends HTTP POST requests to the target URL to test each password.
- Handles connection errors and interprets server responses.
- Colored terminal output using the `colorama` library for better readability.
- Simple and easy to customize for different brute force attack scenarios.

### Requirements
- Python 3.x
- Required libraries are listed in the `requirements.txt` file.

You can install all the dependencies with pip:

pip install -r requirements.txt
```

### How to Use

1. **Modify the Script**:  
   Open the script file and update the function `guess_password()` to point to your target URL. Replace the placeholder `'http://example.com/login'` with the actual link you want to target.


   guess_password('http://example.com/login', 'admin', '/path/to/your/wordlist.txt', 'submit')
  

2. **Provide a Wordlist**:  
   Ensure you have a wordlist (a text file containing possible passwords) that the script will iterate over. You can find wordlists online, like the popular `rockyou.txt`, or create your own.

3. **Run the Script**:  
   Execute the script using Python 3:

   python3 script.py


4. **Output**:  
   The script will display each password it tests, and if the correct password is found, it will stop and display a success message in green.

### Example Usage
```
python3 script.py
```

Make sure to replace the path to the wordlist and adjust the target URL and login parameters to fit your specific use case.

### Disclaimer
This script is intended **for educational purposes and authorized security testing only**. Any illegal use of this script is prohibited, and the author assumes no responsibility for any damages or consequences caused by improper use.

```

### Installation Instructions
Once the `requirements.txt` is in your repository, users can install the necessary libraries by running:

```bash
pip install -r requirements.txt
```

This will automatically install `requests` and `colorama` for them to use with the script.
