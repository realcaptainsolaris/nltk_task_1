import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk import pos_tag

# Download necessary NLTK data
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")


# Input text (fun quote)
text = "Why, sometimes I've believed as many as six impossible things before breakfast."

# Tokenization
sentences = sent_tokenize(text)
words = word_tokenize(text)

# Stopword removal
stop_words = set(stopwords.words("english"))
filtered_words = [
    word for word in words if word.lower() not in stop_words and word.isalnum()
]

# Part-of-Speech tagging
pos_tags = pos_tag(filtered_words)

# Frequency analysis
freq_dist = FreqDist(filtered_words)
most_common = freq_dist.most_common(3)

# Results
print("Sentences:", sentences)
print("Words:", words)
print("Filtered Words (without stopwords):", filtered_words)
print("POS Tags:", pos_tags)
print("Most Frequent Words:", most_common)
