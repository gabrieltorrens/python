bitcoin_on_hand = 1.2
one_bitcoin_to_usd = 25000

def bitcoinToUSD(bitcoin_amount, bitcoin_value_usd):
  usd_value = bitcoin_amount * bitcoin_value_usd
  return usd_value

investment_in_usd = bitcoinToUSD(bitcoin_on_hand, one_bitcoin_to_usd)

if investment_in_usd <= 30000:
  print("Investment below $30,000! SELL!")
else:
  print("Investment above $30,000")