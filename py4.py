import random
sentence = "Have you done your project with the *adj *noun today?"
sentence = sentence.split()
adjectives = ["cranky", "pretty", "stupid", "kind", "fantastic"]
nouns = ["student", "co-worker", "professor", "dog", "girl"]

indexCount = 0
for word in sentence:
	if word == "*adj":
		wordChoice = random.choice(adjectives)
		sentence[indexCount] = wordChoice
	indexCount += 1
	if word == "noun":
		wordChoice = random.choice(nouns)
		sentence[indexCount] = wordChoice
	indexCount += 1
st = ""
for word in sentence:
	st += word + " "
print(st)

