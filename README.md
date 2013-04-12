textminr -- my text classification playground
=====================================

**Blog - Mood classification**
Every document in raw.txt is a blog entry extracted from social media (livejournal). The goal is to classify the mood/sentiment of each sentence into "positive" (happy or excited) or "negative" (depressed, sad, or disappointed). The raw.txt file contains 12747 blog posts, already labeled with 1 (positive) or 0 (negative). 75% of raw data is extracted as training data, the rest 25% is for validation.

	$ python NaiveBayes.py -t ./data/train.txt -v ./data/validate.txt

	Precision=0.74607658506

	$ python SVM.py -k linear -t ./data/train.txt -v ./data/validate.txt

	Precision=0.831136220967

	$ python SVM.py -k rbf -t ./data/train.txt -v ./data/validate.txt

	Precision=0.634337727558

	$ python LogReg.py -t ./data/train.txt -v ./data/validate.txt

	Precision=0.829880728186

**Tweet - Political Tweet Classification**
Every document in raw.txt is a microblog extracted from a leading microblogging site. The goal is to classify whether the short document contains political content or not. The raw.txt file contains 200570 tweets, already labeled with 1 (political) or 0 (non-political). 75% of raw data is extracted as training data, the rest 25% is for validation.

	$ python NaiveBayes.py -t ./data/train.txt -v ./data/validate.txt

	Precision=0.918970906468

	$ python SVM.py -k linear -t ./data/train.txt -v ./data/validate.txt

	Precision=0.989420533782

	$ python SVM.py -k rbf -t ./data/train.txt -v ./data/validate.txt

	Precision=0.937100613958

	$ python LogReg.py -t ./data/train.txt -v ./data/validate.txt

	Precision=0.988739280276

