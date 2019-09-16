inputfile = open("inputfile.txt")
outputfile = open("DAT1.TXT", "w+")

#code to put 80 characters at the top
for x in range(8):
  for y in range(10):
    outputfile.write(str(y))
outputfile.write("\n")

#function to edit file with margins included
def edit_file(input_file, leftMargin, rightMargin):
  input_words = input_file.read().split();
  
  lmargin = "" #left margin shape
  fullline = "" #maximum 80 character line
  wordline = "" #line of words


  for m in range(leftMargin):
    for n in range(12):
      lmargin += " "
  lmargin = lmargin[:-1] #slices


  for rem_words in range(len(input_words)):
    if rem_words == 0:
      outputfile.write(lmargin)
    if (len(lmargin) + len(fullline) + 1 + len(input_words[rem_words])) > (80 - (12 * rightMargin)):
      outputfile.write('\n')
      outputfile.write(lmargin)
      fullline = ''
    if rem_words != 0:
      if input_words[rem_words - 1].find('.')!= -1 or input_words[rem_words-1].find('?')!= -1 or input_words[rem_words - 1].find('!')!= -1:
        wordline = " " + " " + input_words[rem_words]
      else:
        wordline = " " + input_words[rem_words]
    fullline += wordline
    outputfile.write(wordline)
  outputfile.close()

edit_file(inputfile, 2, 2);

print(open('DAT1.TXT').read())
