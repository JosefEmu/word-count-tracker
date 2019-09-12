import docx2txt, subprocess, time

# Getting the docx document
print("Welcome\n")
MY_DOCX = docx2txt.process(input("Enter the full URL to your .docx here: "))

change_timer = input("\nWould you like to change the timer from the default 30 seconds interval? Y/N: ")
if change_timer != "Y":
	TIMER = 30

else:
	TIMER= int(input("\nInput new timer in seconds: "))

TARGET_ = int(input("\nWhat is your target word count?: "))

def wordcount():	
	#copying text from .docx to .txt file 
	with open("output_file.txt", "w") as f:
	    print(MY_DOCX, file=f)

	#getting the word count (less characters in MS word)
	with open("output_file.txt") as text_file:
		words = [word for line in text_file for word in line.strip().split()]
		current_word_count = (len(words))
	
	if current_word_count>TARGET_:
		print("Done!")
		quit()
	else:
		print(f"\nCurrent word count is: {current_word_count} words.\nOnly {TARGET_-current_word_count} words left to go...\n\n---\n")

def run_it():
	while True:
		wordcount()
		time.sleep(TIMER)
		subprocess.call("cls", shell=True)
		subprocess.call("exit", shell=True)
run_it()
