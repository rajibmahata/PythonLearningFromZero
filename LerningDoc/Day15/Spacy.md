# **Detailed Guide on spaCy for NLP**
---

## **What is spaCy?**
spaCy is an **open-source NLP (Natural Language Processing) library** designed for **efficiency and scalability**. It is widely used for **text processing**, **named entity recognition (NER)**, **part-of-speech tagging (POS)**, **dependency parsing**, and **word vector similarity**.

---

## **1. Installing spaCy**
```sh
pip install spacy
```
Download the English language model:
```sh
python -m spacy download en_core_web_sm
```
For larger models with better accuracy:
```sh
python -m spacy download en_core_web_md  # Medium model
python -m spacy download en_core_web_lg  # Large model
```
---

## **2. Loading spaCy Models**
```python
import spacy

nlp = spacy.load("en_core_web_sm")  # Load small English model
doc = nlp("Apple is looking at buying a U.K. startup for $1 billion.")
```
---

## **3. Text Processing in spaCy**
### **Tokenization**
Splitting text into individual words, punctuation, or numbers (called **tokens**).
```python
for token in doc:
    print(token.text)
```
**Output:**
```
Apple
is
looking
at
buying
a
U.K.
startup
for
$1
billion
.
```
---

## **4. Named Entity Recognition (NER)**
Identifying entities like **names, places, organizations, dates, and amounts**.
```python
for ent in doc.ents:
    print(ent.text, "-", ent.label_)
```
**Output:**
```
Apple - ORG
U.K. - GPE
$1 billion - MONEY
```
- **ORG** → Organization  
- **GPE** → Geopolitical Entity (Country, City, etc.)  
- **MONEY** → Monetary values  

To get the description of entity labels:
```python
spacy.explain("GPE")
```
**Output:** `"Countries, cities, states"`

---

## **5. Part of Speech (POS) Tagging**
Assigning grammatical categories to words.
```python
for token in doc:
    print(token.text, "-", token.pos_, "-", token.dep_)
```
**Output:**
```
Apple - PROPN - nsubj
is - AUX - aux
looking - VERB - ROOT
at - ADP - prep
buying - VERB - pcomp
a - DET - det
U.K. - PROPN - compound
startup - NOUN - pobj
for - ADP - prep
$1 - NUM - quantmod
billion - NUM - compound
. - PUNCT - punct
```
- **PROPN** → Proper noun  
- **AUX** → Auxiliary verb  
- **VERB** → Verb  
- **DET** → Determiner  

To get explanations:
```python
spacy.explain("PROPN")
```
**Output:** `"Proper noun"`

---

## **6. Lemmatization**
Converting words into their base form.
```python
for token in doc:
    print(token.text, "→", token.lemma_)
```
**Output:**
```
Apple → Apple
is → be
looking → look
buying → buy
```

---

## **7. Dependency Parsing**
Shows how words are grammatically connected.
```python
from spacy import displacy
displacy.render(doc, style="dep")
```
This generates a **syntax tree** visualization in Jupyter Notebook.

---

## **8. Stopword Removal**
Stopwords are common words like "is", "and", "the" that don’t add much meaning.
```python
from spacy.lang.en.stop_words import STOP_WORDS

for token in doc:
    if not token.is_stop:
        print(token.text)
```

---

## **9. Word Similarity**
Checking similarity between words or phrases using word vectors.
```python
word1 = nlp("king")
word2 = nlp("queen")
print(word1.similarity(word2))
```
**Output:** `0.85` (High similarity)

⚠️ **Note:** Works best with **en_core_web_md** or **en_core_web_lg**, not the small model.

---

## **10. Custom NLP Pipeline**
spaCy allows customizing the NLP pipeline by adding or removing components.

#### **Default Pipeline Components**
```python
print(nlp.pipe_names)
```
**Output:**  
```python
['tok2vec', 'tagger', 'parser', 'ner', 'attribute_ruler', 'lemmatizer']
```

#### **Adding a Custom Component**
```python
@nlp.add_pipe("custom_component", last=True)
def custom_component(doc):
    print("Custom component activated!")
    return doc

doc = nlp("Hello World!")
```

---

## **11. Named Entity Customization**
You can train spaCy to recognize **custom entities** like product names, brands, or technical terms.

```python
from spacy.tokens import Span

doc = nlp("Google Cloud offers AI services.")
new_ent = Span(doc, 0, 2, label="SERVICE")
doc.ents = list(doc.ents) + [new_ent]

for ent in doc.ents:
    print(ent.text, "-", ent.label_)
```
**Output:**
```
Google Cloud - SERVICE
```

---

## **12. Saving and Loading Models**
### **Saving a Trained Model**
```python
nlp.to_disk("my_model")
```
### **Loading a Saved Model**
```python
nlp = spacy.load("my_model")
```

---

# **Final Thoughts**
### ✅ **Why Use spaCy?**
- **Fast and Efficient**: Designed for **production use**  
- **Pretrained Models**: Handles **NER, POS, and Parsing**  
- **Custom Training**: Adapt models to **new domains**  

