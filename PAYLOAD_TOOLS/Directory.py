import requests 

target_url = input('[*] Enter Target URL : ' )
file_name = input('[*] Enter Name of The File Containing Directories : ')

def request(url):
    try:
        return request.get("http://"+url)
    except requests.exceptions.ConnectionError :
        pass 


file = open(file_name , 'r')
for line in file :
    directory = line.strip()
    full_url = target_url + '/' + directory
    responce = request(full_url)
    if responce:
        print('[*] ')
        print('[*] Discovered Directory at This Path : ' + full_url)
        