import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def entity_resolution_tfidf(df1, df2, field='name'):
    combined = pd.concat([df1[field], df2[field]]).dropna().unique()
    tfidf = TfidfVectorizer().fit_transform(combined)
    sim_matrix = cosine_similarity(tfidf[:len(df1)], tfidf[len(df1):])
    
    resolved_pairs = []
    for i, row in enumerate(sim_matrix):
        max_sim_idx = row.argmax()
        similarity = row[max_sim_idx]
        resolved_pairs.append((df1.iloc[i]['id'], df2.iloc[max_sim_idx]['id'], similarity))
    
    return resolved_pairs
