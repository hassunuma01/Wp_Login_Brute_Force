# Wp_Login_Brute_Force
Make a PitchFork attack.

This Python script is used to perform a brute force attack on the login credentials of a WordPress website. 
The script uses the requests library to perform HTTP requests and manage sessions.

USAGE

To use the script, create two text files named user.txt and pass.txt, containing a list of usernames and 
passwords to be tested. Make sure that each username and password is on a separate line.

The script first reads the contents of these files into two lists using the open function and the with statement. 
It then uses the zip function to iterate over the two lists simultaneously.

For each pair of username and password, the script creates a new session using the requests.Session() method. 
It sets the headers and data for the HTTP request, and sends a POST request to the login page of the WordPress website.

If the response status code is 302 (indicating a successful login attempt), and the username is "admin", the script
prints the username and password that were successful and terminates.

DEPENDENCIES

This script requires the requests library, which can be installed using pip:

pip install requests

Usage Example

python wp-bruteforce.py

DISCLAIMER

This script is for educational purposes only. The author does not condone or endorse any illegal activity. 
The user is solely responsible for any actions taken using this script.
