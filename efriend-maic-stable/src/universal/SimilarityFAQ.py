import numpy as np
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

Y = input("Frase a comparar: ").lower()

o = open("similarityFAQ/Resultado2.txt","a")

f = open("similarityFAQ/Prueba.txt", "r")
for X in f:


	X_list = word_tokenize(X) 
	Y_list = word_tokenize(Y) 

	sw = stopwords.words('spanish') 
	l1 =[];l2 =[] 

	X_set = {w for w in X_list if not w in sw} 
	Y_set = {w for w in Y_list if not w in sw}

	rvector = X_set.union(Y_set) 
	for w in rvector: 
		if w in X_set: l1.append(1) 
		else: l1.append(0) 
		if w in Y_set: l2.append(1) 
		else: l2.append(0) 
	c = 0
  
	for i in range(len(rvector)):
		c+= l1[i]*l2[i]
	cosine = c / float((sum(l1)*sum(l2))**0.5)

	def  jaccard_similarity(x, y):
		"""
		Jaccard Similarity J (A,B) = | Intersection (A,B) | / | Union (A,B) |
		"""
		intersection_cardinality = len(set(x).intersection(set(y)))
		union_cardinality = len(set(x).union(set(y)))
		return intersection_cardinality / float(union_cardinality)

	score = jaccard_similarity (X, Y)

	print(X, file=o)
	print("Similitud Jaccard : %s" %score, file=o)
	print("Similitud Coseno: ", cosine, file=o)
	print("----------------", file=o)

f.close()
o.close()
exit()
