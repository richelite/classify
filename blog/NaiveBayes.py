import sys
import numpy
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

class NaiveBayes:
	def __init__(self):
		self.clf = MultinomialNB()
		self.pattern ='(?u)\\b[A-Za-z]{3,}'
		self.tfidf = TfidfVectorizer(sublinear_tf=True, lowercase=True, max_df=0.5, stop_words='english', token_pattern=self.pattern, ngram_range=(1, 3))

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

if __name__ == '__main__':
	if len(sys.argv) not in [5, 6]:
		sys.exit('\nUsage:\n    Validate:\n\tpython NaiveBayes.py -t ./data/train.txt -v ./data/validate.txt\n    Classify:\n\tpython NaiveBayes.py -t ./data/raw.txt -c ./data/test.txt ./data/result.txt')
	classifier = NaiveBayes()
	classifier.train(sys.argv[2])
	if sys.argv[3] == "-v": 
		classifier.validate(sys.argv[4])
	if sys.argv[3] == "-c": 
		classifier.classify(sys.argv[4],sys.argv[5])