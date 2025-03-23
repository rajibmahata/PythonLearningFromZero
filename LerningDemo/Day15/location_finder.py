import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def find_locations(text):
    
    doc = nlp(text)
    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    return locations

# Example usage
text = "I traveled from New York to London and then visited Paris."
#print(find_locations(text))


def find_all_locations(text):
    doc = nlp(text)
    locations = [ent.text for ent in doc.ents if ent.label_ in ["GPE", "LOC", "FAC"]]
    return locations

text = "Mount Everest is in Nepal, and the Eiffel Tower is in Paris."
print(find_all_locations(text))