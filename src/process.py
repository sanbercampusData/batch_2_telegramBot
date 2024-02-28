from src.nlp_core.text_preprocessing import TextProcessing
from src.nlp_core.document_search import SearchDocument
from src.nlp_core.sentiment_analysis import SentimentAnalysis

def search_services(data:str, env)->str:
    '''Digunakan untuk melakukan pencarian pada dataset yang dimiliki'''

    tp = TextProcessing(env)
    text_input = text_preprocessing(data, tp)

    ds = SearchDocument(tp, env)
    result = ds.cosine_similarity(text_input)

    return result

def text_preprocessing(text:str, tp)->str:
    '''Membersihkan text menjadi format yang diinginkan'''
    print(text)
    result = tp.case_folding(text)
    result = tp.hapus_stopword(result)
    result = tp.lemmatisasi(result)

    return result

def train_model(env):
    '''latih model'''
    sa = SentimentAnalysis(env)

    return  sa.train_model()

def prediksi_sentiment(env, data):
    '''latih model'''
    sa = SentimentAnalysis(env)
    
    return  sa.prediksi(data)
