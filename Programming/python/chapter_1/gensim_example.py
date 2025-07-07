from gensim.models import Word2Vec

sentences = [["επεξεργασία", "φυσικής", "γλώσσας"], ["τεχνητή", "νοημοσύνη"]]
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=2)
vector = model.wv['γλώσσας']
print(vector)