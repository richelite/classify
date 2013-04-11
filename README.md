textminr
========

BLOG:
	$ python NaiveBayes.py -t ./data/train.txt -v ./data/validate.txt

	Precision=0.735091023227

	$ python SVM.py -k linear -t ./data/train.txt -v ./data/validate.txt

	Precision=0.830822347772

	$ python SVM.py -k rbf -t ./data/train.txt -v ./data/validate.txt

	Precision=0.632140615191

TWEET:
	$ python NaiveBayes.py -t ./data/train.txt -v ./data/validate.txt

	Precision=0.915724933878

	$ python SVM.py -k linear -t ./data/train.txt -v ./data/validate.txt

	Precision=0.989280275707

	$ python SVM.py -k rbf -t ./data/train_sample.txt -v ./data/validate_sample.txt

	Precision=0.937100613958

