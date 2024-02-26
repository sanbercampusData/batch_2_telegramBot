from nltk import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



class SearchDocument:
    def __init__(self, tp, config):
        self.dataset_path = config.get('PATH_DATASET')
        self.tp = tp
        self.raw_file = open(f'{self.dataset_path}/bpjs.txt', 'r', errors='ignore', encoding='utf-8')
        paragraph = self.raw_file.read()
        self.sent_tokens = sent_tokenize(paragraph)
        self.word_tokens = word_tokenize(paragraph)

    def cosine_similarity(self, data:str):
        print("mulai cosine similarity services")
        sentences = [self.clean_text(item) for item in self.sent_tokens]
        sentences.append(data)

        tfidf = TfidfVectorizer()
        model = tfidf.fit_transform(sentences)
        cosine_similarities = cosine_similarity(model[-1], model)
        
        similarity_result = cosine_similarities.flatten()
        similarity_result.sort()
        print('nilai maks:',similarity_result[-2])
        print('nilai maks:',similarity_result[-3])

        idx = cosine_similarities.argsort()[0][-2]
        idx_2 = cosine_similarities.argsort()[0][-3]

        print('teks:',self.sent_tokens[idx])
        print('teks_2:',self.sent_tokens[idx_2])

        return f"{self.sent_tokens[idx]}. {self.sent_tokens[idx_2]}"



    def clean_text(self, data:str):
        result = self.tp.case_folding(data)
        result = self.tp.hapus_stopword(result)
        # result = self.tp.lemmatisasi(result)

        return result
