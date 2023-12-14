import numpy as np
from sklearn.metrics import f1_score
import relevance_data

g_questions_map = relevance_data.rel_questions_map
g_questions_relevance = relevance_data.g_questions_relevance


def average_precision(relevances):
    precision_values = []
    relevant_count = 0
    for i, rel in enumerate(relevances):
        if rel == 1:
            relevant_count += 1
            precision_values.append(relevant_count / (i + 1))
    return sum(precision_values) / relevant_count if relevant_count > 0 else 0

# Function to calculate F1 score for a list of binary relevance
def f1_score(relevances):
    true_positives = sum(relevances)
    total_predicted_positives = len(relevances)
    total_actual_positives = relevances.count(1)

    precision = true_positives / total_predicted_positives if total_predicted_positives else 0
    recall = true_positives / total_actual_positives if total_actual_positives else 0

    if precision + recall == 0:
        return 0
    return 2 * (precision * recall) / (precision + recall)






def main():
    results = {}
    for key, relevances_list in g_questions_relevance.items():
        # Flatten the list of lists into a single list
        relevances = [rel for sublist in relevances_list for rel in sublist]
        map_score = average_precision(relevances)
        f1 = f1_score(relevances)
        results[key] = {'MAP': map_score, 'F1': f1}

    print(results)
if __name__ == "__main__":
    main()

