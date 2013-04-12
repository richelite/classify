textminr -- my text classification playground
=====================================
##Classify your thought
[Demo](http://classify.aws.af.cm/)
Simply put SVM classifier online. It could classify your input to good/bad mood and political or not. If your input is neutral, the result will not be accurate enough. Have fun!

If you want to run it on your local, please get your API from [Yhat!](http://yhathq.com/), put your credential to settings-example.js, and change it to setting.js. You have to install node.js to run it. If you are not familiar with it, please see [here](http://nodejs.org/).

##Blog - Mood classification
Every document in /blog/data/raw.txt is a blog entry extracted from social media (livejournal). The goal is to classify the mood/sentiment of each sentence into "positive" (happy or excited) or "negative" (depressed, sad, or disappointed). The raw.txt file contains 12,747 blog posts, already labeled with 1 (positive) or 0 (negative). 75% of raw data are extracted as training data, the rest 25% are for validation.

	$ python NaiveBayes.py -t ./data/train.txt -v ./data/validate.txt

	Precision=0.74607658506

	$ python SVM.py -k linear -t ./data/train.txt -v ./data/validate.txt

	Precision=0.831136220967

	$ python SVM.py -k rbf -t ./data/train.txt -v ./data/validate.txt

	Precision=0.634337727558

	$ python LogReg.py -t ./data/train.txt -v ./data/validate.txt

	Precision=0.829880728186

##Tweet - Political Tweet Classification
Every document in raw.txt is a microblog extracted from twitter. The goal is to classify whether the tweet contains political content or not. The /tweet/data/raw.txt file contains 200,570 tweets, already labeled with 1 (political) or 0 (non-political). 75% of raw data are extracted as training data, the rest 25% are for validation.

	$ python NaiveBayes.py -t ./data/train.txt -v ./data/validate.txt

	Precision=0.918970906468

	$ python SVM.py -k linear -t ./data/train.txt -v ./data/validate.txt

	Precision=0.989420533782

	$ python SVM.py -k rbf -t ./data/train.txt -v ./data/validate.txt

	Precision=0.937100613958

	$ python LogReg.py -t ./data/train.txt -v ./data/validate.txt

	Precision=0.988739280276
