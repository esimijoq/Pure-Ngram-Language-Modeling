# Pure-Ngram-Language-Modeling
It builds bigram and trigram frequency dictionaries, and uses trigram-based language modeling to predict the next word and generate sentences.

## Key Features:

### 1. Text Reading & Cleaning:

- Reads text from predefined lists and external files (texts.txt, the_stories_eng.txt).

- Removes punctuation and extra newlines.

- Splits text into words.

### 2. Bigram & Trigram Frequency Analysis:

- Generates bigram and trigram dictionaries counting the frequency of consecutive word pairs.

### 3. Trigram-based Next Word Prediction:

- Predicts the most probable next word given a pair of words using the trigram dictionary.

### 4. Sentence Generation:

- Generates new sentences by repeatedly predicting the next word based on the previous two words.
