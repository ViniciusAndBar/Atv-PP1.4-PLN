import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Carregar o tokenizador e o stemmer Porter
nltk.download('punkt')
nltk.download('wordnet')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Texto de exemplo em inglês


texto = "The cat jump over the fence."
texto2 = "The cats jumped over the fences."

# Tokenização
tokens = word_tokenize(texto)
tokens2 = word_tokenize(texto2)

# Stemming
stems = [stemmer.stem(token) for token in tokens]
stems2 = [stemmer.stem(token) for token in tokens2]

# Lematização
lemmas = [lemmatizer.lemmatize(token) for token in tokens]
lemmas2 = [lemmatizer.lemmatize(token) for token in tokens2]

# Ordenando e removendo duplicatas
stems_sorted = sorted(set(stems))
lemmas_sorted = sorted(set(lemmas))
stems_sorted2 = sorted(set(stems2))
lemmas_sorted2 = sorted(set(lemmas2))

# Resultados
print("Stems ordenados:", stems_sorted)
print("Stems ordenados:", stems_sorted2)

print("Lemas ordenados:", lemmas_sorted)
print("Lemas ordenados:", lemmas_sorted2)
