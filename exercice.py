import math

def get_num_letters(text):
	return len([None for i in text if i.isalnum()])

def get_word_length_histogram(text):
	output, lengths = [], []
	for i in text.split():
		lengths.append((get_num_letters(i)))

	for j in range(max(lengths)+1):
		output.append(lengths.count(j)) if j in lengths else output.append(0)

	return output


def format_histogram(histogram):
	ROW_CHAR = "*"
	aligment = len(str(len(histogram)-1))

	return "\n".join([f"{i : >{aligment}} {ROW_CHAR*elem}" for i,elem in enumerate(histogram) if i !=0])

def format_horizontal_histogram(histogram):
	BLOCK_CHAR = "|"
	LINE_CHAR = "¯"
	height = max(histogram)
	result = ""
	for i in range(height-1,-1,-1):
		for j, elem in enumerate(histogram):
			if j ==0:
				continue
			if elem >= i + 1:
				result += BLOCK_CHAR
			else:
				result+= " "
		result += "\n"
	result += LINE_CHAR*len(histogram)
	return result



	return ""


if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	#print(get_num_letters('alpha'))
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
