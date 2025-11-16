import re
text = "He jests at scars. That never felt a wound! Hello, friend! Are you OK?"
sentences = re.split(r'(?<=[.?!]) ', text)
num = 0

for sentence in sentences:
    num += 1
    print(sentence)


print("Количество предложение равно", num)

