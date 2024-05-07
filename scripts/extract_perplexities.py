import os
import re


def extract_perplexities(log_file):
    with open(log_file, 'r') as file:
        content = file.read()

    perplexities = re.findall(r'Evaluation result \(greedy\) loss:\s+\d+\.\d+,\s+ppl:\s+(\d+\.\d+),', content)

    return perplexities


def main():
    # Ensure the logs directory exists
    if not os.path.exists('logs'):
        os.makedirs('logs')

    baseline_perplexities = extract_perplexities('logs/baseline.log')
    pre_norm_perplexities = extract_perplexities('models/deen_transformer_prenorm/train.log')
    post_norm_perplexities = extract_perplexities('models/deen_transformer_postnorm/train.log')

    with open('logs/baseline_perplexities.csv', 'w') as file:
        file.write('Validation Perplexity\n')
        file.write('\n'.join(baseline_perplexities))

    with open('logs/prenorm_perplexities.csv', 'w') as file:
        file.write('Validation Perplexity\n')
        file.write('\n'.join(pre_norm_perplexities))

    with open('logs/postnorm_perplexities.csv', 'w') as file:
        file.write('Validation Perplexity\n')
        file.write('\n'.join(post_norm_perplexities))


if __name__ == "__main__":
    main()


