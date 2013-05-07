boxWidth = 80
sentence = raw_input("Sentence: ")
sentLen = len(sentence)
margin = (boxWidth - sentLen)/2
print " "*margin + "+" + "-"*(sentLen+2) + "+"
print " "*margin + "|" + " "*(sentLen+2) + "|"
print " "*margin + "| " + sentence +" |"
print " "*margin + "|" + " "*(sentLen+2) + "|"
print " "*margin + "+" + "-"*(sentLen+2) + "+"