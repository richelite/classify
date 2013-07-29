##Classify  

My text mining playground

## classify your mind
[http://clfmind.meteor.com/](http://clfmind.meteor.com/) can classify your input to political or non-political category.

## classify your tweet
[http://clftweet.meteor.com/](http://clftweet.meteor.com/) can classify your tweets to positive mood or negative mood category.

Warning! It is not working properly because Twitter deprecated its 1.0 API which is used in clftweet. I am working on the new Twitter API 1.1 to make clftweet work.


## classifier/blog - Mood classification
Every document in ./blog/data/raw.txt is a blog entry extracted from social media (livejournal). The goal is to classify the mood/sentiment of each sentence into "positive" (happy or excited) or "negative" (depressed, sad, or disappointed). The raw.txt file contains 12,747 blog posts, already labeled with 1 (positive) or 0 (negative). 75% of raw data are extracted as training data, the rest 25% are for validation.

	$ python main.py -m NaiveBayes -t ./data/train.txt -v ./data/validate.txt

	Precision=0.74607658506

	$ python main.py -m LinearSVM -t ./data/train.txt -v ./data/validate.txt

	Precision=0.831136220967

	$ python main.py -m RbfSVM -t ./data/train.txt -v ./data/validate.txt

	Precision=0.634337727558

	$ python main.py -m LogReg -t ./data/train.txt -v ./data/validate.txt

	Precision=0.829880728186

## classifier/tweet - Political Tweet Classification
Every document in ./tweet/data/raw.txt is a microblog extracted from twitter. The goal is to classify whether the tweet contains political content or not. The raw.txt file contains 200,570 tweets, already labeled with 1 (political) or 0 (non-political). 75% of raw data are extracted as training data, the rest 25% are for validation.

	$ python main.py -m NaiveBayes -t ./data/train.txt -v ./data/validate.txt

	Precision=0.918970906468

	$ python main.py -m LinearSVM -t ./data/train.txt -v ./data/validate.txt

	Precision=0.989420533782

	$ python main.py -m RbfSVM -t ./data/train.txt -v ./data/validate.txt

	Precision=0.937100613958

	$ python main.py -m LogReg -t ./data/train.txt -v ./data/validate.txt

	Precision=0.988739280276
