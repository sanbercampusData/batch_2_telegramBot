import re, string

from nlp_id.tokenizer import Tokenizer, PhraseTokenizer
from nlp_id.lemmatizer import Lemmatizer
from nlp_id.stopword import StopWord

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize


class TextProcessing:
    def __init__(self, config) -> None:
        pass
        # self.stopword_en = stopwords.words("english")
        # self.stopword_id = StopWord.get_stopword()
        self.dataset_path = config["PATH_DATASET"]
    
    def case_folding(self, text:str)->str:
        '''fungsi yang digunakan untuk membersihkan teks'''

        result = text.lower()
        result = re.sub(r'\d+', '', result)
        result = re.sub(r'@[A-Za-z0-9]+', '', result)
        result = re.sub(r'https?:\/\/\w+.\w+', '', result)
        result = result.translate(str.maketrans('','',string.punctuation))
        result = result.strip()
        result = re.sub(r'  ',' ',result)

        return result
    
    def tokenisasi(self, text:str,mode:str='word')->list:
        '''fungsi yang digunakan untuk tokenisasi teks
        fungsi ini mempunyai dua mode
        word : melakukan token kata
        sentence : melakukan token kalimat 
        '''

        result = None

        if mode == 'word':
            token_ = PhraseTokenizer()
            result = token_.tokenize(text)
        elif mode == 'sentence':
            result = sent_tokenize(text)

        return result
    
    def lemmatisasi(self, text:str)->str:
        '''fungsi yang digunakan untuk lemmatisasi teks'''

        lemmatizer = Lemmatizer()
        result = lemmatizer.lemmatize(text)
        return result
    
    def hapus_stopword(self, text:str)->str:
        '''fungsi yang digunakan untuk menghapus stopword dari teks'''

        stopword = StopWord()
        result = stopword.remove_stopword(text)

        return result
    
if __name__ == '__main__':
    tp = TextProcessing()
    text = '''
    Indonesia merupakan negara terluas ke-14 sekaligus negara kepulauan terbesar di dunia dengan luas wilayah sebesar 1.904.569 km²,[13] serta negara dengan pulau terbanyak ke-6 di dunia, dengan jumlah 17.504 pulau.[14] Nama alternatif yang dipakai untuk kepulauan Indonesia disebut Nusantara.[15] Selain itu, Indonesia juga menjadi negara berpenduduk terbanyak ke-4 di dunia dengan penduduk mencapai 277.749.853 jiwa pada tahun 2022,[16] serta negara dengan penduduk beragama Islam terbanyak di dunia, dengan penganut lebih dari 238.875.159 jiwa atau sekitar 86,9%.[17][18] Indonesia adalah negara multiras, multietnis, dan multikultural di dunia, seperti halnya Amerika Serikat.[19]
    '''

    list_paragraf = tp.tokenisasi(text,mode='sentence')
    results = []
    for paragraf in list_paragraf:
        result = tp.case_folding(paragraf)
        result = tp.hapus_stopword(result)
        result = tp.lemmatisasi(result)

        results.append(result)
        
    print('.'.join(results))
        
