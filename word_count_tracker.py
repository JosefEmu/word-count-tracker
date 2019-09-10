import docx2txt, subprocess, time


MY_DOCX = None
OUTPUT_FILE = None


def wordcount(MY_DOCX, OUTPUT_FILE):	
	# Getting the docx document
	MY_DOCX = docx2txt.process()

	#copying text from .docx to .txt file 
	with open(OUTPUT_FILE, "w") as f:
	    print(OUTPUT_FILE, file=f)

	#getting the word count (less characters in MS word)
	with open("sample.txt") as text_file:
		words = [word for line in text_file for word in line.strip().split()]
		current_word_count = (len(words))

	if current_word_count>3000:
		print("Done!")
		quit()
	else:
		print(f"\nCurrent word count is: {current_word_count} words.\nOnly {3000-current_word_count} words left to go...\n")

while True:
	wordcount()
	time.sleep(300)
	subprocess.call("cls", shell=True)
	subprocess.call("exit", shell=True)
