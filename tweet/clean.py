raw = open('raw.txt','r')
clean = open('clean.txt','w')
train = open('train.txt','w')
validate = open('validate.txt','w')
lineCount = 0

for line in raw:
	lineCount += 1
	if line[:2]!='1\t' and line[:2]!='0\t': 
		continue
	cat, message = line.split('\t')
	clean.write(cat+'\t'+message)
	if lineCount % 4 == 0:
		validate.write(cat+'\t'+message)
	else:
		train.write(cat+'\t'+message)

raw.close()
clean.close()
train.close()
validate.close()