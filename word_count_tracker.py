import docx2txt, subprocess, time

# Getting the docx document
MY_TEXT = docx2txt.process(input("Enter the full URL to your .docx here: "))
TIMER = 300
TARGET_ = input("What is your target word count?: ")

def wordcount():	
	#copying text from .docx to .txt file 
	with open("output_file.txt", "w") as f:
	    print(MY_TEXT, file=f)

	#getting the word count (less characters in MS word)
	with open("output_file.txt") as text_file:
		words = [word for line in text_file for word in line.strip().split()]
		current_word_count = (len(words))

	if current_word_count>TARGET_:
		print("Done!")
		quit()
	else:
		print(f"\nCurrent word count is: {current_word_count} words.\nOnly {TARGET_-current_word_count} words left to go...\n")

def run_it():
	while True:
		wordcount()
		time.sleep(TIMER)
		subprocess.call("cls", shell=True)
		subprocess.call("exit", shell=True)
