import pandas as pd


MIN_VOTOS = 50000

CSV = pd.read_csv('imdb.csv')

top_20 = csv[ csv['vote']> MIN_VOTOS].nlargest(20, 'rating.imdb')[['title', 'rating.imdb', 'vote']]

print(top_20)