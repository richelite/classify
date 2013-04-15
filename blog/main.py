import sys
from lib import LogReg
from lib import NaiveBayes
from lib import LinearSVM
from lib import RbfSVM

if __name__ == '__main__':
	error = """
Usage: 
	Validate: python main.py -m LinearSVM -t ./data/train.txt -v ./data/validate.txt
	     -m        model: LogReg, NaiveBayes, LinearSVM, RbfSVM
	     -t        training file
	     -v        validate file

	    Classify: python main.py -m LinearSVM -t ./data/clean.txt -c ./data/test.csv -r ./data/result.txt
	    -c         classify file
	    -r         result file
"""
	if len(sys.argv) not in [7,9]:
		sys.exit(error)
	if sys.argv[2]=='LogReg':
		classifier = LogReg()
	if sys.argv[2]=='NaiveBayes':
		classifier = NaiveBayes()
	if sys.argv[2]=='LinearSVM':
		classifier = LinearSVM()
	if sys.argv[2]=='RbfSVM':
		classifier = RbfSVM()
	classifier.train(sys.argv[4])
	if sys.argv[5] == "-v": 
		classifier.validate(sys.argv[6])
	if sys.argv[5] == "-c": 
		classifier.classify(sys.argv[6],sys.argv[8])
