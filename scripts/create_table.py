import csv
import pandas as pd


def main():
    # Read the CSV files
    baseline_df = pd.read_csv('logs/baseline_perplexities.csv')
    pre_norm_df = pd.read_csv('logs/prenorm_perplexities.csv')
    post_norm_df = pd.read_csv('logs/postnorm_perplexities.csv')

    # Create a dictionary to store the perplexities
    perplexities = {
        'Baseline': baseline_df['Validation Perplexity'].tolist(),
        'Prenorm': pre_norm_df['Validation Perplexity'].tolist(),
        'Postnorm': post_norm_df['Validation Perplexity'].tolist()
    }

    # Create a DataFrame
    df = pd.DataFrame(perplexities)

    # Convert the list of integers to a pandas Series
    validation_ppl = pd.Series([500 * i for i in range(1, len(baseline_df) + 1)])
    df.insert(0, 'Validation ppl', validation_ppl)

    # Save the DataFrame to CSV
    df.to_csv('logs/perplexity_table.csv', index=False)


if __name__ == "__main__":
    main()
