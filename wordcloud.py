from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# lecture du fichier de synthèse qui comprend la transcription des entretiens
file_path = r''
 
with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

# exclure les mots communs de la liste
exclure_mots = ['d', 'ne', 'n', 'pourrait', 'entre', 'avoir','peut', 'cela', 'Lyon', 'être', 'du', 'de', 'la', 'des', 'le', 'et', 'est', 'elle', 'une', 'en', 'que', 'aux', 'qui', 'ces', 'les', 'dans', 'sur', 'l', 'un', 'pour', 'par', 'il', 'ou', 'à', 'ce', 'a', 'sont', 'cas', 'plus', 'leur', 'se', 's', 'vous', 'au', 'c', 'aussi', 'toutes', 'autre', 'comme', 'Francois', 'Gac', 'pas', 'cette', 'là', 'où', 'donc', 'je', 'été', 'va', 'y', 'même', 'cetera', 'avec', 'voilà', 'dis', 'moi', 'qu\'on', 'tout', 'fois', 'comment dire', 'faut', 'fait', 'Alors', 'même', 'c\'est', 'très', 'mais', 'on', 'ça', 'faire', 'si', 'nous', 'beaucoup', 'tant', 'comment dire', 'pouvoir', 'dire', 'parce', 'chose', 'doit', 'type', 'soit', 'trouve', 'd\'un', 'votre', 'ont', 'coup', 'chose']

# parametrage du nuage de mots avec la librairie WordCloud
wordcloud = WordCloud(background_color = 'white', stopwords = exclure_mots, max_words = 35).generate(file_content)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

