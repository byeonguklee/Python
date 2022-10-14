from currency_converter import CurrencyConverter

cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')

print(cc.currencies) #가져올 수 있는 환율의 단위

print(cc.convert(1,'USD','KRW'))

