from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from Movie1 import df 
from sklearn.metrics.pairwise import cosine_similarity

# Prepare for modeling:
features=df[['Popularity_score','Normalised__imdb_rating','Genre_Drama', 'Genre_Crime', 'Genre_Action', 'Genre_Adventure',
       'Genre_Biography', 'Genre_History', 'Genre_Sci-Fi', 'Genre_Romance',
       'Genre_Western', 'Genre_Fantasy', 'Genre_Comedy', 'Genre_Thriller',
       'Genre_Animation', 'Genre_Family', 'Genre_War', 'Genre_Mystery',
       'Genre_Music', 'Genre_Horror', 'Genre_Musical', 'Genre_Film-Noir',
       'Genre_Sport']]

X_train,X_test= train_test_split(features, test_size=0.2, random_state=42)

# Split the data into features (X) and target variable (y) if you're going to use supervised learning
scaler= StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

#cosine_similarity to create relationship in the pairs 

matrix_similarity=cosine_similarity(features)
#print(matirx_similarity)

def recomn_fn(m_i):
	similar_movies=matrix_similarity[m_i]
	most_similar=0
	for i in range(len(similar_movies)):
		if (similar_movies[i]>most_similar) and similar_movies[i]!=1:
			most_similar=similar_movies[i]
			index=i
	return index

def index_from_movie(movie):
	l=list(df['Series_Title'])
	movie_index = None
	for i in range(len(list(df['Series_Title']))):

		if l[i]== movie:
			movie_index=i
	return movie_index 

def movie_from_index(i):
	return df.iloc[i]['Series_Title']




# Consider creating a user-item matrix if you're implementing collaborative filtering
