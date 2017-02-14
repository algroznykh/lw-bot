import markovify
import itertools

# Get raw text as string.
with open("corpus.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())


print(list(itertools.islice(text_model.generate_corpus(text), 10)))

