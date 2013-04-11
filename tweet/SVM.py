import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.svm import NuSVC

def train(pattern,tfidf,clf):
	df = pd.read_table("train.txt", sep="\t", names=["cat", "message"])
	# df = pd.read_table("clean.txt", sep="\t", names=["cat", "message"])
	X_train = tfidf.fit_transform(df.message)
	Y_train = []
	for item in df.cat:
		Y_train.append(int(item)) 
	clf.fit(X_train, Y_train)
	print "SVM Classifier Trained"

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
	# clf = LinearSVC(penalty='l2', loss='l1', dual=True, tol=0.0001, C=2.0, multi_class='ovr', fit_intercept=True, intercept_scaling=1, class_weight=None, verbose=0, random_state=None)
	clf = NuSVC(nu=0.7, kernel='rbf', degree=3, gamma=0.0, coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, verbose=False, max_iter=-1)
	pattern ='(?u)\\b[A-Za-z]{3,}'
	tfidf = TfidfVectorizer(sublinear_tf=True, lowercase=True, max_df=0.5, stop_words='english', token_pattern=pattern, ngram_range=(1,3))
	train(pattern,tfidf,clf)
	validate(pattern,tfidf,clf)
	# classify(pattern,tfidf,clf)

if __name__ == '__main__':
	main()