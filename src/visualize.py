import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

def plot_similarity_distribution(matches):
    """
    matches: list of dicts from similarity.match_records
    """
    df = pd.DataFrame(matches)
    plt.figure(figsize=(10, 5))
    sns.histplot(df['similarity'], bins=10, kde=True, color='skyblue')
    plt.title('Similarity Score Distribution')
    plt.xlabel('Similarity Score')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def plot_match_results(matches, threshold=85):
    df = pd.DataFrame(matches)
    df['status'] = df['similarity'].apply(lambda x: 'Match' if x >= threshold else 'No Match')
    count_data = df['status'].value_counts()
    plt.figure(figsize=(6, 4))
    count_data.plot(kind='bar', color=['green', 'red'])
    plt.title('Matched vs Unmatched Records')
    plt.ylabel('Count')
    plt.xticks(rotation=0)
    plt.grid(True)
    plt.show()

def interactive_match_table(matches):
    df = pd.DataFrame(matches)
    fig = px.bar(df, x='source1_id', y='similarity', color='name2',
                 title='Interactive Match Scores',
                 labels={'source1_id': 'Source 1 ID', 'similarity': 'Similarity Score'})
    fig.show()
