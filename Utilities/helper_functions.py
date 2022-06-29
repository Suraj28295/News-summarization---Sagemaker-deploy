
#Extract the data
import re
def extract(filepath):
    pattern = r'(\w+)/(\d+)\.txt$'
    category, file_id = re.search(pattern, str(filepath)).groups()
    with open(filepath, 'r', encoding='unicode_escape') as f:
        text = f.read()
        return category, file_id, text

# Initial cleaning the Raw text
def data_clean(news_articles):
#     from nltk.stem.porter import PorterStemmer
    from tqdm import tqdm
#     ps = PorterStemmer()
    clean_articles = []
    for article in tqdm(news_articles, colour='yellow'):
        # Replace the end lines <\n>
        article = article.replace("\\n",'')

        # Remove all excepth the alphabets
        article = re.sub("[^a-zA-Z'0-9]",' ', article)

        # Lower all the aplhabets
        article = article.lower()

        # Split the article on spaces, returning a list of words
        words = article.split()

       # Remove stopwords
#         clean_article = [ps.stem(word) for word in words]

        # Join clean words
        clean_article = " ".join(words)

        # Append the tweet
        clean_articles.append(clean_article)
    return(clean_articles)

#Convert Pandas Raw df to train,test,val split
def data_for_model_from_pandas(df,test_size,val_from_test_size):
    from datasets import Dataset
    data_for_model=Dataset.from_pandas(df).train_test_split(test_size=test_size )
    test=data_for_model['test'].train_test_split(test_size=test_size)
    data_for_model['test']=test['train']
    data_for_model['val']=test['test']
    return data_for_model