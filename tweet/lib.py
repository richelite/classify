import numpy
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.svm import NuSVC

class LogReg:
	def __init__(self):
		self.clf = LogisticRegression(penalty='l1', dual=False, tol=0.0001, C=16, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None)
		self.pattern ='(?u)\\b[A-Za-z]{3,}'
		self.tfidf = TfidfVectorizer(sublinear_tf=True, use_idf=True, smooth_idf=True, stop_words='english', token_pattern=self.pattern, ngram_range=(1, 3))
	
	def train(self,fileName):
		print "Logistic Regression Classifier is being trained"
		table = pandas.read_table(fileName, sep="\t", names=["cat", "message"])
		X_train = self.tfidf.fit_transform(table.message)
		Y_train = []
		for item in table.cat:
			Y_train.append(int(item)) 
		self.clf.fit(X_train, Y_train)
		print "Logistic Regression Classifier has been trained"

	def classify(self,cFileName, rFileName):
		table = pandas.read_table(cFileName, names=["message"])
		X_test = self.tfidf.transform(table.message)
		print "Data have been classified"
		with open(rFileName,'w') as f:
			for item in self.clf.predict(X_test).astype(str):
				f.write(item+'\n')

	def validate(self,fileName):
		table = pandas.read_table(fileName, sep="\t", names=["cat", "message"])
		X_validate = self.tfidf.transform(table.message)
		Y_validated = self.clf.predict(X_validate).astype(str)
		totalNum = len(table.cat)
		errorCount = 0
		for i in range(0,totalNum):
			if int(table.cat[i])!=int(Y_validated[i]):
				errorCount += 1
		print "Data have been validated! Precision={}".format((totalNum-errorCount)/float(totalNum))

class NaiveBayes:
	def __init__(self):
		self.clf = MultinomialNB()
		self.pattern ='(?u)\\b[A-Za-z]{3,}'
		self.tfidf = TfidfVectorizer(norm='l1', sublinear_tf=False, use_idf=True, smooth_idf=True, stop_words='english', token_pattern=self.pattern, ngram_range=(1,3))

	def train(self,fileName):
		print "Naive Bayes classifier is being trained"
		table = pandas.read_table(fileName, sep="\t", names=["cat", "message"])
		X_train = self.tfidf.fit_transform(table.message)
		Y_train = []
		for item in table.cat:
			Y_train.append(int(item)) 
		self.clf.fit(X_train, Y_train)
		self.clf.fit(X_train, Y_train)
		print "Naive Bayes classifier has been trained"

	def classify(self,cFileName, rFileName):
		table = pandas.read_table(cFileName, names=["message"])
		X_test = self.tfidf.transform(table.message)
		print "Data have been classified"
		with open(rFileName,'w') as f:
			for item in self.clf.predict(X_test).astype(str):
				f.write(item+'\n')

	def validate(self,fileName):
		table = pandas.read_table(fileName, sep="\t", names=["cat", "message"])
		X_validate = self.tfidf.transform(table.message)
		Y_validated = self.clf.predict(X_validate).astype(str)
		totalNum = len(table.cat)
		errorCount = 0
		for i in range(0,totalNum):
			if int(table.cat[i])!=int(Y_validated[i]):
				errorCount += 1
		print "Data have been validated! Precision={}".format((totalNum-errorCount)/float(totalNum))

class LinearSVM:
	def __init__(self):
		self.clf = LinearSVC(penalty='l2', loss='l1', dual=True, tol=0.0001, C=2.0, multi_class='ovr', fit_intercept=True, intercept_scaling=1, class_weight=None, verbose=0, random_state=None)
		self.pattern ='(?u)\\b[A-Za-z]{3,}'
		self.tfidf = TfidfVectorizer(norm='l1', sublinear_tf=False, use_idf=True, smooth_idf=True, stop_words='english', token_pattern=self.pattern, ngram_range=(1, 3))
	def train(self,fileName):
		print "LinearSVM Classifier is being trained"
		table = pandas.read_table(fileName, sep="\t", names=["cat", "message"])
		X_train = self.tfidf.fit_transform(table.message)
		Y_train = []
		for item in table.cat:
			Y_train.append(int(item)) 
		self.clf.fit(X_train, Y_train)
		print "LinearSVM Classifier has been trained"

	def classify(self,cFileName, rFileName):
		table = pandas.read_table(cFileName, names=["message"])
		X_test = self.tfidf.transform(table.message)
		print "Data have been classified"
		with open(rFileName,'w') as f:
			for item in self.clf.predict(X_test).astype(str):
				f.write(item+'\n')

	def validate(self,fileName):
		table = pandas.read_table(fileName, sep="\t", names=["cat", "message"])
		X_validate = self.tfidf.transform(table.message)
		Y_validated = self.clf.predict(X_validate).astype(str)
		totalNum = len(table.cat)
		errorCount = 0
		for i in range(0,totalNum):
			if int(table.cat[i])!=int(Y_validated[i]):
				errorCount += 1
		print "Data have been validated! Precision={}".format((totalNum-errorCount)/float(totalNum))

class RbfSVM:
	def __init__(self):
		self.clf = NuSVC(nu=0.7, kernel='rbf', degree=3, gamma=0.0, coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, verbose=False, max_iter=-1)
		self.pattern ='(?u)\\b[A-Za-z]{3,}'
		self.tfidf = TfidfVectorizer(norm='l1', sublinear_tf=False, use_idf=True, smooth_idf=True, stop_words='english', token_pattern=self.pattern, ngram_range=(1, 3))
	def train(self,fileName):
		print "RbfSVM Classifier is being trained"
		table = pandas.read_table(fileName, sep="\t", names=["cat", "message"])
		X_train = self.tfidf.fit_transform(table.message)
		Y_train = []
		for item in table.cat:
			Y_train.append(int(item)) 
		self.clf.fit(X_train, Y_train)
		print "RbfSVM Classifier has been trained"

	def classify(self,cFileName, rFileName):
		table = pandas.read_table(cFileName, names=["message"])
		X_test = self.tfidf.transform(table.message)
		print "Data have been classified"
		with open(rFileName,'w') as f:
			for item in self.clf.predict(X_test).astype(str):
				f.write(item+'\n')

	def validate(self,fileName):
		table = pandas.read_table(fileName, sep="\t", names=["cat", "message"])
		X_validate = self.tfidf.transform(table.message)
		Y_validated = self.clf.predict(X_validate).astype(str)
		totalNum = len(table.cat)
		errorCount = 0
		for i in range(0,totalNum):
			if int(table.cat[i])!=int(Y_validated[i]):
				errorCount += 1
		print "Data have been validated! Precision={}".format((totalNum-errorCount)/float(totalNum))
