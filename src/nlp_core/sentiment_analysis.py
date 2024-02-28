import pandas as pd
from src.nlp_core.text_preprocessing import TextProcessing
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

import pickle

tqdm.pandas()

class SentimentAnalysis:
    def __init__(self,config):
        self.config = config
        self.dataset_path = config.get('PATH_DATASET')
        self.model_path = config.get('PATH_ML_MODEL')
        self.dataset_name = config.get('TRAIN_DATASET')
        self.vectorizer_data = config.get('VECTORIZER_DATA')
        self.model_data = config.get('MODEL_DATA')

    def train_model(self):
        try:
            print("mengawal proses pelatihan")
            # raw_data = pd.read_csv(f"{self.dataset_path}{self.dataset_name}", sep='\t')
            # raw_data.rename({"Tweet":"tweet"}, axis=1 ,inplace=True)

            # df = raw_data.iloc[:1000,:].copy()

            # print("menjalankan proses pembersihan")

            # df['clean_tweet'] = df["tweet"].progress_apply(self.clean_text)
            # df.to_csv(f"{self.dataset_path}clean_dataset.csv")

            df = pd.read_csv(f"{self.dataset_path}clean_dataset.csv")
            df.dropna(inplace=True)

            print("jalankan proses tfidf")
            vectorizer = TfidfVectorizer()
            vectorizer.fit_transform(df['clean_tweet'])
            v_data = vectorizer.fit_transform(df['clean_tweet']).toarray()

            print("pembuatan model")
            X_train, X_test, y_train, y_test = train_test_split(v_data, df['sentimen'], test_size=0.2, random_state=42)
            model_rf = RandomForestClassifier(max_depth=5, random_state=42, n_estimators=10)
            model_rf.fit(X_train, y_train)

            print("jalankan proses menyimpan")
            pickle.dump(vectorizer, open(f"{self.model_path}{self.vectorizer_data}", "wb"))
            pickle.dump(model_rf, open(f"{self.model_path}{self.model_data}", "wb"))

            return "pelatihan model sukses"

        except Exception as e:
            print(e)
            return "pelatihan model gagal"
        

    def prediksi(self, data):
        try:
            print("proses prediksi")
            vector = pickle.load(open(f"{self.model_path}{self.vectorizer_data}", "rb"))
            model = pickle.load(open(f"{self.model_path}{self.model_data}", "rb"))

            print("selesai memuat model")
            data_in = [self.clean_text(data)]

            print(data_in)

            vector_data = vector.transform(data_in).toarray()
            hasil = model.predict(vector_data)

            print(f"hasilnya adalah {hasil}")

            if hasil[0] == 0:
                sentiment = "netral"
            elif hasil [0] == 1:
                sentiment = "positif"
            else:
                sentiment = "negatif"

            return sentiment

        except Exception as e:
            print(e)
            return "prediksi gagal"

    

    

    def clean_text(self, data:str):
        tp = TextProcessing(self.config)

        result = tp.case_folding(data)
        print(result)
        result = tp.hapus_stopword(result)
        result = tp.lemmatisasi(result)

        return result
