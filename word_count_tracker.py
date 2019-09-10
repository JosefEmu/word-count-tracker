import docx2txt, subprocess, time


def wordcount():	
	# Getting the docx document
	MY_TEXT = docx2txt.process(input("Enter the full URL to your .docx here: "))

	#copying text from .docx to .txt file 
	with open("output_file.txt", "w") as f:
	    print(MY_TEXT, file=f)

	#getting the word count (less characters in MS word)
	with open("output_file.txt") as text_file:
		words = [word for line in text_file for word in line.strip().split()]
		current_word_count = (len(words))

	if current_word_count>3000:
		print("Done!")
		quit()
	else:
		print(f"\nCurrent word count is: {current_word_count} words.\nOnly {3000-current_word_count} words left to go...\n")

def run_it():
	while True:
		wordcount()
		time.sleep(300)
		subprocess.call("cls", shell=True)
		subprocess.call("exit", shell=True)
