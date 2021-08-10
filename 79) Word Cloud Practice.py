import matplotlib.pyplot as plt
import wikipedia
from wordcloud import WordCloud, ImageColorGenerator
from nltk.corpus import stopwords
wikipedia.set_lang('pt')

# Defining text
text = wikipedia.page("Brasil").content.lower()

# Creating the object of wordcloud
wordcloud = WordCloud(stopwords = stopwords.words('portuguese'), collocations=True).generate(text)

# Showing Results
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
