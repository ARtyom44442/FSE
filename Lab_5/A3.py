text = "Yanka Kupala State University of Grodno"
words = text.split()
abr = ''


for word in words:
    if word[0] == word[0].upper() and len(word) >= 3:
        abr += word[0]
    else :
        abr += ''


print(abr)