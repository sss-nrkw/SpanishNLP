import spacy

# spaCyモデルの読み込み
nlp = spacy.load("es_core_news_sm")

# テキストを処理
text = "La educación también ha sido transformada por la tecnología, con plataformas de aprendizaje en línea que ofrecen una amplia variedad de cursos accesibles para personas de todas las edades y antecedentes. La disponibilidad de información al alcance de nuestras manos ha empoderado a las personas para buscar un aprendizaje continuo y adquirir nuevas habilidades."
doc = nlp(text)

# 品詞分解の結果を表示
for token in doc:
    print(token.text.encode("utf-8").decode("cp932", "ignore"), token.pos_.encode("utf-8").decode("cp932", "ignore"))

# 品詞分解の結果を辞書形式で取得
pos_tags = {token.text.encode("utf-8").decode("cp932", "ignore"): token.pos_.encode("utf-8").decode("cp932", "ignore") for token in doc}
print(pos_tags)