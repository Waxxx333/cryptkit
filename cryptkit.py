#!/bin/python3
import requests, re, argparse, os, sys, random;
from time import sleep;
from decimal import Decimal as D;
DB=("\033[01;38;5;21m")
RD=("\033[01;38;5;9m")
YLW=("\033[01;38;5;220m")
PNK=("\033[01;38;5;135m")
PRP=("\033[01;38;5;55m")
GRN=("\033[01;38;5;10m")
BLUE=("\033[01;38;5;21m")
DRK=("\033[01;38;5;242m")
WHT=("\033[01;38;5;15m")
ORN=("\033[01;38;5;202m")
GRY=("\033[01;38;5;242m")
RESET=("\033[0m")
LOAD=("\033[1;49;32m")
version=(1.0)
if (os.path.isdir('/data/data/com.termux')):
    OS = ('Termux')
elif ('linux') in (sys.platform):
    OS = ('Linux')
elif ('win') in (sys.platform):
    OS = ('Windows')
script = (os.path.basename(sys.argv[0]))
if ('.py') in script:
    script = (script.split('.')[0])
counter = [0]
CHARS = ('/', '-', '\\', '|')
Agent = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36')
def cls():
    os.system('clear')
def loading(duration):	
    for i in range(10):
        counter[0] += 1
        sys.stdout.write('\r')
        sys.stdout.write(f"{LOAD}%s{RESET}" % CHARS[counter[0] % len(CHARS)])
        sys.stdout.flush()
        sleep(duration)
    sys.stdout.write("\b ")
    return()
def echo(data):
    blank = ' '
    s = ''
    for l in blank:
        sys.stdout.write('\r')
        if 'Error' in data:
            sys.stdout.write(f"{DRK}[{RD}■{DRK}] {GRN}{data}")
        else:
            sys.stdout.write(f"{DRK}[{GRN}■{DRK}] {GRN}{data}")
        s += (f"{l}")
        sys.stdout.flush()
        sleep(0.3)
        sys.stdout.write("\n")
        return()
def icon(): #₿Ξ
    if (OS) == ('Termux'):
        icon = (f"""{GRN}┏━┓{DRK}┳┏ 
{GRN}┃{YLW}₿ {DRK}┣┻┓
{GRN}┗━┛{DRK}┇ ┛
{GRN}Crypto Toolkit """)
    else:
        icon = (f"""{GRN}┏━┓{DRK}┳━┓┓ ┳┳━┓┏┓┓┏━┓┳┏ o┏┓┓
{GRN}┃  {DRK}┃┳┛┗┏┛┃━┛ ┃ ┃ {DRK}┃┣┻┓┃ ┃ 
{GRN}┗━┛{DRK}┇┗┛ ┇ ┇ {YLW}₿ {DRK}┇ ┛━┛┇ ┛┇ ┇""")
    sys.stdout.write(f"{icon}\n")
def usage():
    info = (f"""
{PNK}# {DRK}Convert Function {PNK}#
{PNK}# {DRK}Convert {PNK}$1500 {GRN}USD {DRK}into {GRN}Ξthereum
{GRN}{script} {RD}-c {GRN}usd {RD}-i {GRN} eth {RD}-n {GRN}1500
{PNK}# {DRK}Convert {PNK}3 {GRN}Ξthereum {DRK}into {GRN}₿TC
{GRN}{script} {RD}-c {GRN}eth {RD}-i {GRN}btc {RD}-n {GRN}3
{PNK}# {DRK}Convert {PNK}40 {GRN}Ðogecoin {DRK}into {GRN}GBP
{GRN}{script} {RD}-c {GRN}doge {RD}-i {GRN}gbp {RD}-n {GRN}40
{PNK}# {DRK}Convert {PNK}30 {GRN}Polygon{WHT}({PNK}MATIC{WHT}) {DRK}into {GRN}U$D
{GRN}{script} {RD}-c {GRN}matic {RD}-i {GRN}usd {RD}-n {GRN}30
{PNK}# {DRK}Convert {PNK}500 {GRN}Gwei {DRK}into {GRN}U$D
{GRN}{script} {RD}-c {GRN}gwei {RD}-i {GRN}usd {RD}-n {GRN}30
****************************
{PNK}# {DRK}Price Function {PNK}#
{PNK}# {DRK}Check price of just Ξthereum {PNK}& {DRK}₿itcoin
{GRN}{script} {RD}-p {PNK}[{WHT}blank{PNK}]
{PNK}# {DRK}Check price of Solana
{GRN}{script} {RD}-p {GRN}solana
 """)
    info = info.replace('\r','.')
    sys.stdout.write(f"{info}\b")
def msg(name=None) -> None:                                                            
    info = (f"""{PNK}#{DRK} {script} optional arguments{PNK}:{GRN}
{GRN}-c{WHT}, {GRN}--convert      {PNK}# {DRK}Currency to convert {PNK}[{GRN}USD{WHT}, {GRN}GBP{WHT}, {GRN}EUR{WHT}, {GRN}BTC{WHT}, {GRN}DOGE{WHT}, etc{PNK}]
{GRN}-i{WHT}, {GRN}--into         {PNK}# {DRK}Currency to convert into {PNK}[{GRN}BTC{WHT}, {GRN}MATIC{WHT}, {GRN}USD{WHT}, {GRN}GPB{WHT}, {GRN}etc{PNK}]
{GRN}-n{WHT}, {GRN}--amount       {PNK}# {DRK}Amount to convert {PNK}[{RD}0.00000001 {PNK}- {RD}1000000{PNK}]
{GRN}-u{WHT}, {GRN}--usage        {PNK}# {DRK}Show advanced help: {PNK}[{GRN}convert{WHT}, {GRN}today{WHT}, {GRN}price{WHT}, {GRN}all{PNK}] 
{GRN}-p{WHT}, {GRN}--price        {PNK}# {DRK}Get crypto prices {PNK}[{GRN}all{WHT},{PNK}{{{GRN}specified coin{PNK}}}{WHT},{GRN}blank{PNK}] 
{GRN}-l{WHT}, {GRN}--list         {PNK}# {DRK}List some common crypto currencies
{GRN}-e{WHT}, {GRN}--exchanges    {PNK}# {DRK}List exchanges
{GRN}-t{WHT}, {GRN}--today        {PNK}# {DRK}Get today's info on a coin
{GRN}-h{WHT}, {GRN}--help         {PNK}# {DRK}Show standard help menu """)
    info = info.replace('\r','.')
    sys.stdout.write(f"{info}\b")
def specific(query) -> None:
    if (query) == ('convert'):
        info = (f"""{PNK}#{DRK} Conversion examples{PNK}:{WHT}({RD}Use abreviations{WHT})
{GRN}{script} -c usd -i btc -n 125 {PNK}# {DRK}Convert $125 into ₿itcoin
{GRN}{script} --convert sol --into usd --amount 9.5 {PNK}# {DRK}Convert 9.5 Solana into USD.
{GRN}{script} -c matic -i eth -n 2000 {PNK}# {DRK}Convert 2000 MATIC into Ξthereum
{PNK}# {RD}*{DRK}Hint{PNK}: {DRK}run {WHT}({GRN}{script} {RD}--list{WHT}) {DRK}to get abreviations{RD}* """)
        info = info.replace('\r','.')
        sys.stdout.write(f"\n{info}\b")
    elif (query) == ('price'):
        info = (f"""{PNK}# {DRK}Price examples{PNK}:{WHT}({RD}Use full name{WHT}){GRN}
{script} -p litecoin {PNK}# {DRK}Get the price of Litecoin{GRN}
{script} -p 'ethereum classic' {PNK}# {DRK}Use quotes for two-word cryptos{GRN}
{script} -p [blank] {PNK}#{DRK} Leave blank for Ξthereum and ₿itcoin{GRN}
{script} -p all {PNK}#{DRK} Retrieve prices on 200+ crypto currencies""")
        info = info.replace('\r','.')
        sys.stdout.write(f"\n{info}\b")
    elif (query) == ('today'):
        info = (f"""{PNK}#{DRK} Price examples{PNK}:{WHT}({RD}Use full name{WHT}){GRN}
{script} -t litecoin {PNK}# {DRK}Get today's info on Litecoin{GRN}
{script} --today 'ethereum classic' {PNK}# {DRK}Use quotes for two-word cryptos{GRN}
{script} -p [blank] {PNK}#{DRK} Leave blank for ₿itcoin and Ξthereum {GRN}""")
        info = info.replace('\r','.')
        sys.stdout.write(f"\n{info}\b")
    elif (query) == ('help'):
        sys.stdout.write(f"{RD}You need help, we know.\n")
        msg()
    else:
        usage()
class get():
    def __init__(self) -> None:
        self.session = requests.Session()
        self.session.headers.update({'User-Agent':f"{Agent}"})
        parser = argparse.ArgumentParser(description=(f'{GRN}{script} | Crypto Toolkit'),add_help=(False))
        parser.add_argument('-h', '--help',action='help', default=argparse.SUPPRESS,help=(f'Show this help menu'))
        parser.add_argument('-t', '--today' ,nargs='?',const='bitcoin',required=False, action=('store'), help=(f"Get today's details on a coin"))
        parser.add_argument('-u', '--usage' ,nargs='?',const='general',required=False, action=('store'), help=(f"Advanced Usage"))
        parser.add_argument('-v', '--version' ,required=False, action=('store_true'), help=(f"{script} Version"))
        parser.add_argument('-l', '--list' ,required=False, action=('store_true'), help=(f"List some common crypto currencies"))
        parser.add_argument('-e', '--exchanges' ,required=False, action=('store_true'), help=(f"List ~100 decentralized exchanges"))
        parser.add_argument('-c', '--convert' ,required=False, action=('store'),type=(str.lower), help=(f"Currency to convert"))
        parser.add_argument('-i', '--into' ,required=False, action=('store'),type=(str.lower), help=(f"Currency to convert into"))
        parser.add_argument('-n', '--amount' ,required=False, action=('store'),type=(float), help=(f"Amount to convert"))
        parser.add_argument('-p', '--price' ,nargs='?',const='bitcoin' ,required=False, action=('store'), help=(f"Retrieve crypto prices"))
        args = (parser.parse_args())
        if args.today:
            icon()
            loading(0.05)
            coin = (args.today)
            self.today(coin)
            exit(0);
        if args.exchanges:
            loading(0.05)
            self.exchange()
            exit(0);
        else:
            pass
        if args.list:
            icon()
            loading(0.05)
            data = (f"{DRK}Some common crypto currencies {DRK}[{GRN}■{DRK}]")
            echo(data)
            self.list_cryptos()
            exit(0);
        else:
            pass
        if args.price:
            icon()
            loading(0.05)
            currency = (args.price)
            self.get_current_price(currency)
        else:
            pass
        if args.version:
            icon()
            data = (f"{DRK}Version: {GRN}{script} {PNK}{version} {DRK}[{GRN}■{DRK}]")
            echo(data)
            exit(0);
        try:
            if args.convert:
                to_convert = (args.convert)
                if (args.amount) == (0):
                    data = (f"{RD}Error{PNK}: {DRK}Cannot convert {RD}{args.amount} {DRK}[{RD}■{DRK}]")
                    echo(data)
                    exit(0);
                elif (args.amount) > (0):
                    amount = (args.amount)
                else:
                    data = (f"{RD}Error{PNK}: {DRK}You must supply an amount to convert {DRK}[{RD}■{DRK}]")
                    echo(data)
                    exit(0);
                if len(args.convert) < (3):
                    data = (f"{RD}Error {PNK}'{RD}{args.convert}{PNK}' {DRK}is not a currency abbreviation{PNK} {DRK}[{RD}■{DRK}]")
                    echo(data)
                    data = (f"{DRK}Examples{PNK}: {GRN}BTC{PNK}, {GRN}MATIC{PNK}, {GRN}USD{PNK}, {GRN}DOGE{PNK}, {GRN}SHIB {DRK}[{GRN}■{DRK}]")
                    echo(data)
                    data = (f"{PRP}*{GRN}Hint{PRP}*{PNK}::{WHT}({PNK}Doesn't need to be capitalized{WHT}) {DRK}[{GRN}■{DRK}]")
                    echo(data)
                    exit(0);
                if len(args.into) < (3):
                    data = (f"{RD}Error {PNK}'{RD}{args.into}{PNK}' {DRK}is not a currency abbreviation{PNK} {DRK}[{RD}■{DRK}]")
                    echo(data)
                    data = (f"{DRK}Examples{PNK}: {GRN}BTC{PNK}, {GRN}MATIC{PNK}, {GRN}USD{PNK}, {GRN}DOGE{PNK}, {GRN}SHIB {DRK}[{GRN}■{DRK}]")
                    echo(data)
                    data = (f"{PRP}*{GRN}Hint{PRP}*{PNK}::{WHT}({PNK}Doesn't need to be capitalized{WHT}) {DRK}[{GRN}■{DRK}]")
                    echo(data)
                    exit(0);
                else:
                    convert_to = (args.into)
                icon()
                loading(0.05)
                self.convert(to_convert,amount,convert_to)
                exit(0);
        except:
            pass
        if args.usage:
            if (args.usage) != ('general'):
                query = (args.usage)
                icon()
                loading(0.05)
                specific(query)
            else:
                msg()
        else:
            pass
    def list_cryptos(self):
        with open('coins.txt') as coin_list:
            coins = (coin_list.readlines())
            coins = [x.strip() for x in coins]
            title = ["Name", "Abreviation"]
            data = ('{:1s}{:8s} {:14s}{:24s}'.format(DRK,title[0],RD,title[1]))
            echo(data)
            for coin in coins:
                try:
                    data = ("{:10s} {:20s}".format(coin.split()[0],coin.split()[1].lower()))
                    echo(data)
                    sleep(0.01);
                except KeyboardInterrupt:
                    data = (f"{RD}Error{PNK}: {DRK}Keyboard Interruption {DRK}[{RD}■{DRK}]")
                    echo(data)
                    exit(0);
    def today(self,coin):
        if len(coin.split()) > 1:
            coin_raw = (coin.replace(' ','-'))
        else:
            coin_raw = (coin)
        try:
            price_page = (f"https://coinmarketcap.com/currencies/{coin_raw.lower()}/")
            retrieve2 = (self.session.get(price_page).text)
            price_data =  (re.findall('Price Live Data(.*?)</p>',retrieve2)[0])
            try:
                real_name =  (re.findall('<title>(.*?)price',retrieve2)[0])
                title = ["Real Name", "Price"]
            except:
                real_name = (coin.title())
                title = ["Query", "Price"]
            try:
                data2 =  (re.findall('">What Is(.*?)</p>',retrieve2)[0])
                info = (f"What is {data2}")
            except:
                info = (f"")
            try:
                price =  (re.findall('class="priceValue "><span>(.*?)</span>',retrieve2)[0])
            except (IndexError):
                price =  (re.findall('class="priceValue smallerPrice"><span>(.*?)</span>',retrieve2)[0])
            CLEANR = re.compile('<.*?>')
            cleantext = re.sub(CLEANR, '', price_data)
            cleantext2 = re.sub(CLEANR, '', info)
            data = ('{:10s}{:12s} {:17s}{:20s}'.format(DRK,title[0],RD,title[1]))
            echo(data)
            data = ('{:10s}{:12s} {:17s}{:20s}'.format(DRK,real_name,RD,price))
            echo(data)
            sys.stdout.write(f"{GRN}{cleantext}")
            sys.stdout.write(f"\n{GRN}{cleantext2}")
        except (IndexError):
            data = (f"{RD}Error{PNK}: {DRK}Incorrect spelling, wrong name or unsupported coin {DRK}[{RD}■{DRK}]")
            echo(data)
            exit(0);
        except (KeyboardInterrupt):
            data = (f"{RD}Error{PNK}: {DRK}Keyboard Interruption {DRK}[{RD}■{DRK}]")
            echo(data)
            exit(0);
    def exchange(self):
        page = ('https://coinmarketcap.com/rankings/exchanges/dex/')
        retrieve = (self.session.get(page).text)
        exchanges = (list(set(re.findall('href="/exchanges/(.*?)/"',retrieve))))
        count = 0
        title = ["Name", "URL"]
        data = ('{:10s}{:12s} {:17s}{:20s}'.format(DRK,title[0],RD,title[1]))
        echo(data)
        if ('loopring-exchange') in exchanges: exchanges.pop(exchanges.index('loopring-exchange'))
        if ('mento') in exchanges: exchanges.pop(exchanges.index('mento'))
        for exchange in exchanges:
            try:
                page = (f"https://coinmarketcap.com/exchanges/{exchange}")
                get_links = (self.session.get(page).text)
                links = (list(set(re.findall('target="_blank">http(.*?)</',get_links))))
                for link in links:
                    if ('https://medium.com') in link:
                        link = ('Null')
                    data = ('{}{:13s} {}http{:23s}'.format(DRK,exchange,RD,link))
                    echo(data)
            except KeyboardInterrupt:
                data = (f"{RD}Error{PNK}: {DRK}Keyboard Interruption {DRK}[{RD}■{DRK}]")
                echo(data)
                exit(0);
    def all_crypto_prices(self):
        page = ('https://coinmarketcap.com/all/views/all/')
        retrieve = (self.session.get(page).text)
        names = (list(set(re.findall('"name":"(.*?)"',retrieve))))
        count = 0
        title = ["Name", "Price", "Alt"]
        data = ('{:10s}{:12s} {:6s}{:8s} {:17s}{:20s}'.format(DRK,title[0],GRN,title[1],RD,title[2]))
        echo(data)
        try:
            for name in names:
                try:
                    price_page = (f"https://coinmarketcap.com/currencies/{name.lower()}/")
                    retrieve2 = (self.session.get(price_page).text)
                    price =  (re.findall('class="priceValue "><span>(.*?)</span>',retrieve2)[0])
                    alt =  (re.findall('height="32" width="32" alt="(.*?)"',retrieve2)[0])
                    data = ('{:10s}{:12s} {:6s}{:8s} {:17s}{:20s}'.format(DRK,name,GRN,price,RD,alt))
                    echo(data)
                except KeyboardInterrupt:
                    data = (f"{RD}Error{PNK}: {DRK}Keyboard Interruption {DRK}[{RD}■{DRK}]")
                    echo(data)
                    exit(0);
                except:
                    pass
                count += 1
        except KeyboardInterrupt:
            data = (f"{RD}Error{PNK}: {DRK}Keyboard Interruption {DRK}[{RD}■{DRK}]")
            echo(data)
            exit(0);
    def convert(self,to_convert,amount,convert_to):
        data = (f"{DRK}Conversion is courtesy of{PNK}: {PRP}cryps.info")
        echo(data)
        if ('gwei') in to_convert.casefold():
            currency1 = ('Gwei')
        else:
            currency1 = (to_convert.upper())
        if ('gwei') in convert_to.casefold():
            currency2 = ('Gwei')
        else:
            currency2 = (convert_to.upper())
        page = (f"https://www.cryps.info/en/{currency1}_to_{currency2}/{amount}/")
        retrieve = (self.session.get(page).text)
        result = (re.findall('</p><div id="value">(.*?)</div>',retrieve))
        title = (re.findall('<title>(.*?)</title>',retrieve))
        retrieved_amount = (re.split('\s+', result[0])[0])
        retrieved_currency = (re.split('\s+', result[0])[1])
        if retrieved_currency == ('BTC'):
            retrieved_currency = ('₿TC')
        elif retrieved_currency == ('ETH'):
            retrieved_currency = ('ΞTH')
        elif retrieved_currency == ('DOGE'):
            retrieved_currency = ('ÐOGE')
        elif retrieved_currency == ('USD'):
            retrieved_currency = ('U$D')
        
        if currency1 == ('BTC'):
            currency1 = ('₿TC')
        elif currency1 == ('ETH'):
            currency1 = ('ΞTH')
        elif currency1 == ('DOGE'):
            currency1 = ('ÐOGE')
        elif currency1 == ('USD'):
            currency1 = ('U$D')
            
        if currency2 == ('BTC'):
            currency2 = ('₿TC')
        elif currency2 == ('ETH'):
            currency2 = ('ΞTH')
        elif currency2 == ('DOGE'):
            currency2 = ('ÐOGE')
        elif currency2 == ('USD'):
            currency2 = ('U$D')
        csymbol = ('')
        if len(str((amount))) >= 5:
            amount = format(amount, '.{}f'.format(len(str(amount))))
        try:
            title = (title[0])
            new_title = (title.split('|')[0])
            data = (f"{GRN}{new_title} {DRK}[{GRN}■{DRK}]")
            echo(data)
            data = (f"{GRN}{amount} {PNK}{currency1} {WHT}= {GRN}{retrieved_amount} {PNK}{retrieved_currency} {DRK}[{GRN}■{DRK}]")
            echo(data)
        except:
            data = (f"{GRY}Converting{PNK}: {GRN}{currency1} {GRY}into{PNK}: {GRN}{currency2} {PRP}|| {GRN}{amount} {PNK}{currency1} {WHT}= {GRN}{retrieved_amount} {PNK}{retrieved_currency} {DRK}[{GRN}■{DRK}]")
            echo(data)
    def get_current_price(self, currency):
        btc_page = ('https://coinmarketcap.com/currencies/bitcoin/')
        eth_page = ('https://coinmarketcap.com/currencies/ethereum/')
        page2 = ("https://walletinvestor.com/converter/ethereum/usd/1")
        get_btc = (self.session.get(btc_page).text)
        get_eth = (self.session.get(eth_page).text)
        retrieve2 = (self.session.get(page2).text)
        try:
            btc_price = (re.findall('class="priceValue "><span>(.*?)</span>',get_btc)[0])
        except:
            btc_price = (f'N/A')
        try:
            eth_price = (re.findall('class="priceValue "><span>(.*?)</span>',get_eth)[0])
        except (IndexError):
            eth_price = (re.findall('class="priceValue smallerPrice"><span>(.*?)</span>',get_eth)[0])
        except:
            eth_price = ('N/A')
        try:
            down = (re.findall('glyphicon-menu-down"></i> (.*?)</',retrieve2)[0])
            down_clean = (down.replace(" ", ""))
        except:
            down = (re.findall('glyphicon-menu-up"></i> (.*?)</',retrieve2)[0])
            down_clean = (down.replace(" ", ""))
        if currency != 'bitcoin':
            if currency == ('all'):
                data = (f"{DRK}Stats brought to you by{PNK}: {BLUE}https{DRK}://{BLUE}coinmarketcap.com {DRK}[{GRN}■{DRK}]")
                echo(data)
                self.all_crypto_prices()
                exit(0);
            if len(currency.split()) > 1:
               currency = (currency.replace(' ', '-')) 
            try:
                cpage = (f"https://coinmarketcap.com/currencies/{currency.lower()}/")
                retrievec = (self.session.get(cpage).text)
                ccurrency =  (re.findall('class="priceValue "><span>(.*?)</span>',retrievec)[0])
                alt =  (re.findall('height="32" width="32" alt="(.*?)"',retrievec)[0])
                data = (f"{DRK}{alt} Price{PNK}: {GRN}{ccurrency}")
                echo(data)
            except:
                data = (f"{RD}Error{PNK}: {DRK}Check your spelling and try again.{DRK}[{RD}■{DRK}]")
                echo(data)
                data = (f"{PNK}*{GRN}Hint{PNK}*{PNK}::{WHT}({DRK}Complete spelling{PNK}: {GRN}litecoin{PNK}, '{GRN}Ethereum Classic{PNK}'{WHT}) {DRK}[{GRN}■{DRK}]")
                echo(data)
                data = (f"{RD}If the name is two words, use quotes {DRK}[{GRN}■{DRK}]")
                echo(data)
        if ('-') in down:
            data = (f"{DRK}₿TC Price{PNK}: {GRN}${GRN}{btc_price}")
            echo(data)
            loading(0.01)
            data = (f"{DRK}ΞTH Price{PNK}: {GRN}{eth_price} {PNK}.::. {DRK}Down{PNK}: {RD}{down_clean}%\r")
            echo(data)
        else:
            data = (f"{DRK}₿TC Price{PNK}: {GRN}${GRN}{btc_price}")
            echo(data)
            loading(0.01)
            data = (f"{DRK}ΞTH Price{PNK}: {GRN}{eth_price} {PNK}.::. {DRK}Up{PNK}: {GRN}+{down_clean}%\r")
            echo(data)

get()
