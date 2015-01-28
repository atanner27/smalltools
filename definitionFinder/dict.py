print "testing 1,2"
termfile = file('terms.txt')
glossary = file('gloss.txt')
glossString = open('gloss.txt').read()
text_file = open("answers.txt", "w")
found = False

for line in termfile:
	if line.lower().strip() in glossString.lower():
		index = glossString.lower().find(line.lower().strip())
		nextPeriod = glossString.lower().find(".", index, len(glossString))
		text = glossString[index:nextPeriod]
		text_file.write("Word: " + line.strip() + " \n")
		text_file.write("Definition: " + text.strip() + " \n" + " \n")
		print "Word: " + line.strip()
		print "Definition: " + text.strip()
		print " "

text_file.close()

