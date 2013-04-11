import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def train(pattern,tfidf,clf):
	# df = pd.read_table("train.txt", sep="\t", names=["cat", "message"])
	df = pd.read_table("clean.txt", sep="\t", names=["cat", "message"])
	X_train = tfidf.fit_transform(df.message)
	Y_train = []
	for item in df.cat:
		Y_train.append(int(item)) 
	clf.fit(X_train, Y_train)
	print "Naive Bayes Classifier Trained"

def classify(pattern,tfidf,clf):
	df = pd.read_table("test.csv", names=["message"])
	X_test = tfidf.transform(df.message)
	print "Classified"
	with open('result.txt','w') as f:
		for item in clf.predict(X_test).astype(str):
			f.write(item+'\n')

def validate(pattern,tfidf,clf):
	df = pd.read_table("validate.txt", sep="\t", names=["cat", "message"])
	X_validate = tfidf.transform(df.message)
	Y_validated = clf.predict(X_validate).astype(str)
	totalNum = len(df.cat)
	errorCount = 0
	for i in range(0,totalNum):
		if int(df.cat[i])!=int(Y_validated[i]):
			errorCount += 1
	print "Validated! Precision={}".format((totalNum-errorCount)/float(totalNum))

def main():
	clf = MultinomialNB()
	pattern ='(?u)\\b[A-Za-z]{3,}'
	tfidf = TfidfVectorizer(sublinear_tf=True, lowercase=True, max_df=0.5, stop_words='english', token_pattern=pattern, ngram_range=(1, 3))
	train(pattern,tfidf,clf)
	# validate(pattern,tfidf,clf)
	classify(pattern,tfidf,clf)

if __name__ == '__main__':
	main()