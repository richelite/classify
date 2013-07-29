raw = open('./data/raw.txt','r')
train = open('./data/train.txt','w')
validate = open('./data/validate.txt','w')
lineCount = 0

for line in raw:
	lineCount += 1
	cat, message = line.split('\t')
	if lineCount % 4 == 0:
		validate.write(cat+'\t'+message)
	else:
		train.write(cat+'\t'+message)

raw.close()
train.close()
validate.close()