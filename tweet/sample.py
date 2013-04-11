raw = open('./data/raw.txt','r')
clean = open('./data/clean.txt','w')
train = open('./data/train_sample.txt','w')
validate = open('./data/validate_sample.txt','w')
lineCount = 0

for line in raw:
	lineCount += 1
	if line[:2]!='1\t' and line[:2]!='0\t': 
		continue
	cat, message = line.split('\t')
	clean.write(cat+'\t'+message)
	if lineCount % 25 in [5,10,15]:
		train.write(cat+'\t'+message)
	if lineCount % 25 == 20:
		validate.write(cat+'\t'+message)

raw.close()
clean.close()
train.close()
validate.close()