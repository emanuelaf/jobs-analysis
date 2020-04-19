import pandas as pd
netflix = pd.read_csv('netflix_titles.csv')
netflix.head()
netflix.info()

netflix['type'].value_counts()
netflix['date_added'].nunique()

netflix[netflix['type'] == 'Movie']['date_added'].value_counts().head()
netflix[netflix['type'] == 'TV Show']['date_added'].value_counts().head()

netflix['country'].value_counts().head()
netflix[netflix['country'] == 'United States']['listed_in'].value_counts().head()
netflix[netflix['country'] == 'India']['listed_in'].value_counts().head()
netflix[netflix['country'] == 'United Kingdom']['listed_in'].value_counts().head()

# cluster analysis on countries similarities based on movies
# reccommendations based on listed in, actors and directors