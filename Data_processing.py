import pandas as pd
import numpy as np

df = pd.read_csv("imdb_top_1000.csv")
#print(df.head())
#print(df.columns)

#Check the structure, columns, and data types
#Look for missing values and duplicates

#print(df.dtypes)
#print(df.shape)
#print(df.isna())
df.dropna(subset=['Poster_Link','No_of_Votes'],inplace=True)

# print(df.duplicated("Certificate"))

# Feature extraction:

# Extract relevant features like genre, director, actors, year, etc.
genre=list(df["Genre"])
# print(genre.unique())
# print(df.loc["Star1"])


# Convert the 'genre' column into a list or separate columns using one-hot encoding
def uniquelist(l):

	l2=[]
	for value in l:
		
		v2=value.split(',')
		for i in v2:
			i = i.strip()
			if i not in l2:
				l2.append(i)

	return l2

unique_genre=uniquelist(genre)
# print(unique_genre)
#hot-encoding

for genre in unique_genre:
	df["Genre_"+genre]=0
for index, row in df.iterrows():
	i=row['Genre'].split(',')
	for g in i:
		g=g.strip()
		df.at[index,'Genre_'+g]=1

		   
#print(df.iloc[453])


# Extract the year from the release date if it's not already a separate column
# Clean text fields (title, overview, etc.) by removing special characters, lowercasing


# Consider using natural language processing techniques like tokenization or stemming on text fields


# Create numerical features:

# Convert categorical variables to numerical (e.g., one-hot encoding for genres)
#certificate

# Normalize numerical features if needed (e.g., scale ratings to a 0-1 range)

std=df['IMDB_Rating'].std(axis=0)
# print(std)
mean=df['IMDB_Rating'].mean()
# print(mean)

rating=list(df['IMDB_Rating'])
def normalise(l):
	Z=[]
	for i in l:
		z=(i-mean)/std
		Z.append(round(float(z),3))
	return Z
Zscore=normalise(rating)

df['Zscore']=pd.Series(Zscore)
#print(df['Zscore'])

# Calculate derived features:
# df.at[968,"Released_Year"]="1995"
# df.loc[row_index, 'column_name'] = new_value
df.loc[df['Released_Year'] == "PG", 'Released_Year'] = "1995"
# Create a 'age' feature by subtracting the release year from the current year
def calculate_age(Released_Year):
	
	age=2024-int(Released_Year)
	
	return age
df["Age"] = df["Released_Year"].apply(calculate_age)


# Aggregate ratings or votes if available
#Total number of votes
total_votes=df['No_of_Votes'].sum()

# Normalize votes (e.g., on a scale of 0-1) to compare popularity across movies

#normalized_votes = (votes - min_votes) / (max_votes - min_votes)

Max=df['No_of_Votes'].max()
Min=df['No_of_Votes'].min()
def normalise_max_min(l): 
	normalised_votes=(l-Min)/(Max-Min)
	return  normalised_votes
df['Normalised_votes']=df['No_of_Votes'].apply(normalise_max_min)
#print(df[['Normalised_votes','Zscore']])

# Create a "popularity" score combining rating and number of votes
	#z-scores normalisation
df['Normalised__imdb_rating']=df['Zscore'].apply(lambda x:1/(1+ np.exp(-x)))
#print(df['Normalised__imdb_rating'])

df['Popularity']=0.6*df['Normalised__imdb_rating']+0.4*df['Normalised_votes']

# print(df['Popularity'])

#popularity normalisation

Max=df['Popularity'].max()
Min=df['Popularity'].min()

df['Popularity_score']=df['Popularity'].apply(normalise_max_min)
#print(df['Popularity_score'])






