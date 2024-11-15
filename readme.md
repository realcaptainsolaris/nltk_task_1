# NLP with NLTK: Fun Text Processing Example

This project demonstrates basic Natural Language Processing (NLP) techniques using the NLTK library in Python. It processes a whimsical quote from *Alice in Wonderland* and applies several text analysis steps, including tokenization, stopword removal, part-of-speech tagging, and word frequency analysis.

## Quote Used

*"Why, sometimes I've believed as many as six impossible things before breakfast."*  
– *Alice in Wonderland* by Lewis Carroll

## Features

- **Tokenization:** Splits the text into sentences and words.
- **Stopword Removal:** Filters out common words like "as," "the," or "and" that add little meaning.
- **Part-of-Speech (POS) Tagging:** Identifies the grammatical roles of each word (e.g., noun, verb, adjective).
- **Word Frequency Analysis:** Counts the occurrences of words and highlights the most frequent ones.

## Installation

1. Clone this repository or copy the script to your local machine.
2. Ensure Python 3.x is installed.
3. Install the NLTK library:

   ```bash
   pip install nltk
   ```

4. Download required NLTK resources:

   ```python
   import nltk
   nltk.download("punkt")
   nltk.download("stopwords")
   nltk.download("punkt_tab")
   nltk.download("averaged_perceptron_tagger_eng")
   ```

## How to Run

1. Save the script as `nlp_task.py`.
2. Run the script:

   ```bash
   python nlp_task.py
   ```

## Example Output

```plaintext
Sentences: ["Why, sometimes I've believed as many as six impossible things before breakfast."]
Words: ['Why', ',', 'sometimes', 'I', "'ve", 'believed', 'as', 'many', 'as', 'six', 'impossible', 'things', 'before', 'breakfast', '.']
Filtered Words (without stopwords): ['Why', 'sometimes', 'believed', 'six', 'impossible', 'things', 'breakfast']
POS Tags: [('Why', 'WRB'), ('sometimes', 'RB'), ('believed', 'VBD'), ('six', 'CD'), ('impossible', 'JJ'), ('things', 'NNS'), ('breakfast', 'NN')]
Most Frequent Words: [('things', 1), ('breakfast', 1), ('six', 1)]
```

## License

This project is open-source and available under the MIT License. Have fun exploring NLP with NLTK!
