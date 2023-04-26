from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

sentences = ['I love apples', 'I hate oranges', 'Apples are better than oranges']
vectorizer = CountVectorizer().fit_transform(sentences)

cosine_similarities = cosine_similarity(vectorizer)

print(cosine_similarities)
# [[1.         0.         0.31622777] 
#  [0.         1.         0.31622777] 
#  [0.31622777 0.31622777 1.        ]]