# run_project.py

from src import preprocess, similarity, entity_resolution, visualize

def main():
    df1 = preprocess.load_data("data/customer_source_1.csv")
    df2 = preprocess.load_data("data/customer_source_2.csv")

    df1 = preprocess.preprocess(df1, 'name', 'email')
    df2 = preprocess.preprocess(df2, 'full_name', 'email_address')

    matches = similarity.match_records(df1, df2, 'name', 'full_name', threshold=80)

    print("\n=== Similarity Matches ===")
    for m in matches:
        print(m)

    visualize.plot_similarity_distribution(matches)
    visualize.plot_match_results(matches)
    visualize.interactive_match_table(matches)

    resolved = entity_resolution.entity_resolution_tfidf(
        df1.rename(columns={'name': 'name'}),
        df2.rename(columns={'full_name': 'name'})
    )

    print("\n=== Entity Resolution Results ===")
    for r in resolved:
        print(r)

if __name__ == "__main__":
    main()
