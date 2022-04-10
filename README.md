![Script](https://img.shields.io/badge/WaXxX-cryptkit-BF5B16?style=plastic&logo=Ethereum)
![ETH](https://img.shields.io/badge/Ethereum-3C3C3D?style=plastic&logo=Ethereum&logoColor=orange)
![Python](https://img.shields.io/badge/Python-FFD43B?style=plastic&logo=python&logoColor=darkgreen)
![g](https://img.shields.io/badge/GitHub-%2312100E.svg?&style=plastic&logo=Github&logoColor=BF5B16&?labelColor=BF5B16)
![Blah](https://img.shields.io/badge/Python3-RE-7A297B?style=plastic&logo=Python)
![fff](https://img.shields.io/badge/Python3-Requests-7A297B?style=plastic&logo=Python)


<h1 align="center">• <b>CryptKit | Crypto Toolkit</b> •</h1>

<p align="center">
  <!--⁑<img width="300" height="300" src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/python.svg">-->
  <img width="300" height="300" src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/bitcoin.svg">
</p>

<h2 align="center">· A multi-function crypto toolkit written in Python ·</h2>

<hr>

##### · Functions: 
* <b> Has installation script for Linux-based systems [¶](#install)
* <b> Convert crypto [¶](#convert)
  * <b> Convert a crypto currency to your local currency 
  * <b> Convert your local currency to a crypto currency
  * <b> Convert a crypto currency to another crypto currency
    * **Over 150 currencies supported**
* <b> Check crypto prices [¶](#check)</b>
  * Check prices on specified coins 
  * Check prices on 200+ coins all at once
* <b> List decentralized exchanges(DEXes)</b>
  * List ~100 top DEXes


<hr>


<a name="install"></a> 
### • Installation/Usage
#### ° To install:
```python
git clone --depth 1 https://github.com/Waxxx333/cryptkit.git
cd cryptkit
chmod +x install.sh
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<cryptkit>
└─⋗ ./install.sh
```
#### ° Or simply run it:
```python
git clone --depth 1 https://github.com/Waxxx333/cryptkit.git
cd cryptkit
chmod +x cryptkit
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<cryptkit>
└─⋗ python3 cryptkit -h/--help
cryptkit.py crypto toolkit

options:
  -h, --help            Show this help menu
  -t [COIN], --today [COIN] Get today's details on a coin
  -u [KEYWORD], --usage [KEYWORD] Advanced Usage
  -v, --version         cryptkit Version
  -l, --list            List some common crypto currencies
  -e, --exchanges       List ~100 decentralized exchanges
  -c [CURRENCY], --convert [CURRENCY] Currency to convert
  -i INTO, --into INTO  Currency to convert into
  -n [AMOUNT], --amount [AMOUNT] Amount to convert
  -p [PRICE], --price [PRICE] Retrieve crypto prices
```
<!--
<a name="convert"></a>  
## ● Convert crypto currencies 
#### ° ***Some*** of the currencies supported:
* AUR - Auroracoin
* BCC - BitConnect (inactive)
* BCH - Bitcoin Cash
* BTC or XBT - Bitcoin
* DASH - Dash
* DOGE or XDG - Dogecoin
* EOS - EOS.IO
* ETC - Ethereum Classic
* ETH - Ether (also known as Ethereum)
* GRC - Gridcoin
* LTC - Litecoin
* KOI or COYE - Coinye (inactive)
* && many more
 -->
  
  
## • Convert crypto currencies 
  
###### · Use the coin's abreviation for the convert function  
  
```python
# cryptkit --convert/-c [USD/GBP/CAD/EUR/ETH] --into/-i [USD/GBP/CAD/EUR/ETH] --amount/-n [AMOUNT]
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<cryptkit>
└─⋗ cryptkit -c sol -i usd -n 3.9
[■] Conversion is courtesy of: cryps.info
[■] 3.9 SOL to USD (Solana to US Dollar)  [■]
[■] 3.9 SOL = 437.0368 U$D [■]
```
  

<a name="check"></a>
## • Check current crypto prices
#### ° By default it will retrieve just ETH and BTC prices, but you can specify a currency to check the price on by adding it to the <kbd>--price/-p</kbd> flag
###### · Just check Ethereum and Bitcoin
```python
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<cryptkit>
└─⋗ cryptkit -p
[■] ₿TC Price: $37,875.6767
[■] ΞTH Price: $2611 .::. Down: -3.83634%
```
###### · Check the price of another coin
```python
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<cryptkit>
└─⋗ cryptkit -p ravencoin
[■] RVN Price: $0.05963
[■] ₿TC Price: $$42,712.42
[■] ΞTH Price: $3248 .::. Up: +1.17561%
```
###### · Check the price of over 200 coins all at once
```python
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<cryptkit>
└─⋗ cryptkit -p all
[■] Name         Price         Alt                 
[■] Moonriver    $67.57        MOVR                
[■] PancakeSwap  $6.74         CAKE                
[■] Helium       $24.91        HNT                 
[■] Siacoin      $0.009572      SC                  
[■] Polkadot     $18.44        DOT                 
[■] Request      $0.2214       REQ                 
[■] OKB          $17.87        OKB                 
[■] Zilliqa      $0.04461      ZIL                 
[■] Secret       $5.40         SCRT                
[■] GateToken    $6.76         GT 
```  

## • List some common crypto currencies
```python
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<cryptkit>
└─⋗ cryptkit -l
[■] Some common crypto currencies [■]
[■] Name       Abreviation             
[■] Celo       celo                
[■] MXC        mxc                 
[■] Ravencoin  rvn                 
[■] WazirX     wrx                 
[■] NEM        xem                 
[■] Decred     dcr                 
[■] JOE        joe                 
[■] Qtum       qtum                
[■] Dogecoin   doge
```

## • Advanced usage
#### ° More specific help using keywords
###### · Usage: <kbd>--usage/-u price/convert/today/all</kbd>
```python
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<cryptkit>
└─⋗ cryptkit --usage      
# cryptkit optional arguments:
-c, --convert      # Currency to convert [USD, GBP, EUR, BTC, DOGE, etc]
-i, --into         # Currency to convert into [BTC, MATIC, USD, GPB, etc]
-n, --amount       # Amount to convert [0.00000001 - 1000000]
-u, --usage        # Show advanced help: [convert, today, price, all] 
-p, --price        # Get crypto prices [all,{specified coin},blank] 
-l, --list         # List some common crypto currencies
-e, --exchanges    # List exchanges
-t, --today        # Get today's info on a coin
-h, --help         # Show standard help menu 
```
###### · Tips on using price function
```python
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<cryptkit>
└─⋗ cryptkit --usage price
# Price examples:
cryptkit -p litecoin # Get the price of Litecoin
cryptkit -p 'ethereum classic' # Use quotes for two-word cryptos
cryptkit -p [blank] # Leave blank for Ξthereum and ₿itcoin
cryptkit -p all # Retrieve prices on 200+ crypto currencie 
```
###### · Tips on using the convert function
```python
┌──[яoot@ᴡɪɴᴅᴏᴡꜱ95]-<cryptkit>
└─⋗ cryptkit --usage convert
# Conversion examples:
cryptkit -c usd -i btc -n 125 # Convert $125 into ₿itcoin
cryptkit --convert sol --into usd --amount 9.5 # Convert 9.5 Solana into USD.
cryptkit -c matic -i eth -n 2000 # Convert 2000 MATIC into Ξthereu 
```
<hr>

<h1 align="center">· Screenshots ·</h1>
<p align="center">
  <img src="https://i.imgur.com/u1ARbmG.png" width="710" height="500"> <!--Price listing -->
  <img src="https://github.com/Waxxx333/cryptkit/blob/main/assets/conversion.png" width="710" height="500">
  <img src="https://github.com/Waxxx333/cryptkit/blob/main/assets/exchanges.png" width="710" height="500">
  <img src="https://github.com/Waxxx333/cryptkit/blob/main/assets/list_prices.png" width="710" height="500">
  <img src="https://github.com/Waxxx333/cryptkit/blob/main/assets/today.png" width="710" height="500">
  <img src="https://github.com/Waxxx333/cryptkit/blob/main/assets/usage.png" width="710" height="500">
</p>

> <kbd>To Do</kbd>
- [ ] Add more distros' package managers to the installer
- [ ] Make installer work in Winblows
- [ ] Make installer work with Termux
- [ ] Make STDOUT <kbd>prettier</kbd> on Termux
- [ ] A side-by-side comparison function
- [ ] Portfolio

<details>
  <summary><kbd>Changes</kbd></summary>
  <ul>
    <li><b> ·..·</li>
    </ul>
</details>  

###### · Requirements: <kbd>python-requests</kbd> | but the installation script will attempt to install it in Linux based systems. 

###### · For Windows and Termux you will have to manually install python-requests. You will need pip if you're on Windows or Termux to install requests. I will be fixing this at some point. Right now the installer supports: openSUSE, Arch-based distros, Debian-based distros and Fedora
###### · cryptkit now has tab completion if you install it via install.sh. You must be using zsh or bash and you also need to have bash-completion for bash or zsh-completions for zsh. Run the install script, close your shell, reopen a shell and type cryptkit -- (two hyphens) and press tab. Has an advanced usage menu for extra hep with its functions.
  
###### Price conversions are from [cryps.info](https://www.cryps.info/)

###### Price checks are from: [coinmarketcap](https://coinmarketcap.com),  and  [walletinvestor](https://walletinvestor.com)
  
<hr>

<p align="center">
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/dogecoin.svg" width="75" height="75">
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/bitcoin.svg" width="75" height="75">
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/litecoin.svg" width="75" height="75">
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/ethereum.svg" width="75" height="75">
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/python.svg" width="75" height="75">
</p>
<p align="center">
  <a href="https://twitter.com/waxxx333"><img src="https://img.shields.io/badge/-WaXxX-E34F26?style=plastic&logo=Windows%2095&logoColor=white"></a>
</p>

<hr>
