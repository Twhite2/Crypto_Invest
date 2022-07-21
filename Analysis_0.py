from datetime import date
from tweet.py import *

"""
Description: Logical evaluation of Algorithm.
Note: Variables are to be attached to values gathered from user input or already existing database.
@crypto_coin: Name of crypto currency inputed by user.
@NFT_mint: Name of NFT brand project input by user.
@EC: Existing Crypto Currency.
@NC: New Crypto currency
@ENFT: Existing NFT
@NNFT: New NFT
@APC: Average Price of Coin
@APNFT: Average Price of NFT
@TVC: Trade Volume of Coin
@TVNFT: Trade Volume of NFT
@coin_cap: Market capacity for crypto currency
@NFT_cap: Market capacity for NFT products
@coin_user: Social Media handle for crypto currency
@NFT_user: Social Media handle for NFT
@followers_count: Number of followers on social media
@coinsellers: Number of users selling coin
@coinbuyers: Number of people buying coin
@NFTsellers: Number of people selling NFT
@NFTbuyers: Number of people buying NFT
@MVP_crypto: Minimum Viable Product of Crypto currency
@MVP_NFT: Minimum Viable Product of NFT
@valsim: validating similarity
"""

crypto_coin = input("Name of coin: \n")
NFT_mint = input("Name of NFT: \n")

# Date Function used to register age of products
def age(birthdate):
	today = date.today()
	age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
	return age
#Crypto and NFT products built over 3 years ago and older are registered as EC, and ENFT respectfully.
if age(crypto_coin) >= 3:
	EC = age(crypto_coin)
else:
	NC = age(crypto_coin)

if age(NFT_mint) >= 3:
	ENFT = age(NFT_mint)
else:
	NNFT = age(NFT_mint)
#Verifying Validity of Crypto currency and NFT

for i in NC:
	if NC == NC.get():
		print("New Coin is valid")
	else:
		print("New Coin is invalid")

for i in NNFT:
	if NNFT == NNFT.get():
		print("New Coin is valid")
	else:
		print("New Coin is invalid")
#Obtaining Current averag price of Crypto currency and NFT input by user.
APC = crypto_coin.get()
APNFT = NFT_mint.get()

#Determining the trade Volume of coins and NFT in the Market
TVC = crypto_coin.get()
TVNFT = NFT_mint.get()

if TVC >= 80:
	print("Trade Volume is High")

elif TVC <= 20:
	print("Trade volume is low")
else:
	print("Trade volume is average")

if TVNFT >= 80:
	print("Trade Volume is High")
elif TVNFT <= 20:
	print("Trade volume is low")
else:
	print("Trade volume is average")

#Coin Market Capacity for crypto currency and NFT
coin_cap = crypto_coin.get()
NFT_cap = NFT_mint.get()

#Social Media Follower Count
if coin_user == crypto_coin:
	coin_user = " "

	user = api.get_user(coin_user)

	followers_count = user.followers_count

	print("The number of followers of the user are : " + str(followers_count))

elif NFT_user == NFT_mint:
	NFT_user = " "

	user = api.get_user(coin_user)

	followers_count = user.followers_count

	print("The number of followers of the user are : " + str(followers_count))
#Getting value of Buyers and Sellers for crypto_coin
coinbuyers = api.get_coinbuyers(crypto_coin)
coinsellers = api.get_coinsellers(crypto_coin)

if coinbuyers > coinsellers:
	print("More Buyers")
elif coinsellers > coinbuyers:
	print("More Sellers")
else:
	print("Equal amount of Buyers and Sellers")

#Getting value of Buyers and Sellers for NFT_mint
NFTbuyers = api.get_NFTbuyers(NFT_mint)
NFTsellers = api.get_NFTsellers(NFT_mint)

if NFTbuyers > NFTsellers:
	print("More Buyers")
elif NFTsellers > NFTbuyers:
	print("More Sellers")
else:
	print("Equal amount of Buyers and Sellers")
#Getting MVP of coins and NFT
MVP_crypto = api.MVP(crypto_coin)
print(MVP_crypto)
MVP_NFT = api.MVP(NFT_mint)
print(MVP_NFT)
#Validating similarity with other products
def valsim(i):
	if i == api.get():
		print("Coins are similar")
	else:
		print("Coins are different")
coinval = valsim(crypto_coin)
NFTval = valsim(NFT_mint)

#determined happenings around coin to be good or bad
pass

#identifyng personalities talking about the coin
if list_user > list_vuser:
	print("Less High ranking personalities")
elif list_vuser > list_user:
	print("More High Ranking personalities")
else:
	print("even number, or none at all.")
#identifying perceptions on product updates
pass

#lines 35 to 57 require API attachments for validation. All will be added as API are acquired.