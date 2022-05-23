from datetime import date

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

coin_user = crypto_coin 