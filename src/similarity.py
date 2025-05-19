from fuzzywuzzy import fuzz, process


def get_similarity_score(str1, str2):
    return fuzz.token_set_ratio(str1, str2)

def match_records(df1, df2, col1, col2, threshold=85):
    matches = []
    for i, row1 in df1.iterrows():
        for j, row2 in df2.iterrows():
            score = get_similarity_score(row1[col1], row2[col2])
            if score >= threshold:
                matches.append({
                    'source1_id': row1['id'],
                    'source2_id': row2['id'],
                    'name1': row1[col1],
                    'name2': row2[col2],
                    'similarity': score
                })
    return matches
