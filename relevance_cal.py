from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.metrics import jaccard_distance
import numpy as np

import relevance_data

questions_map = relevance_data.rel_questions_map
rel_questions_relevance = relevance_data.rel_questions_relevance

enhanced_questions_map = relevance_data.rel_enhanced_questions_map
rel_enhanced_relevance = relevance_data.rel_enhanced_questions_relevance
def cal_jaccard_similarity(orig_question, followup_question):
    orig_question = set(orig_question.split())
    followup_question = set(followup_question.split())
    jaccard_sim = 1 - jaccard_distance(orig_question, followup_question)
    return jaccard_sim

def cal_cosine_similarity(orig_question, followup_question):
    corpus = [orig_question, followup_question]
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(corpus)
    return cosine_similarity(matrix[0:1], matrix[1:])[0][0]


relevance_map = {}
def rank_related_questions(questions_map):


    for qid in questions_map:

        main_question = list(questions_map[qid].keys())[0]
        related_questions = list(questions_map[qid].values())[0]

        # Calculate similarity scores
        question_scores = {}
        for rel_ques in related_questions:
            js = cal_jaccard_similarity(main_question, rel_ques)
            cs = cal_cosine_similarity(main_question, rel_ques)
            score = js + cs

            if score > 0.4:
                question_scores[rel_ques] = 1
            else:
                question_scores[rel_ques] = 0

        # Rank related questions by score
        # ranked_related_questions = sorted(question_scores.items(), key=lambda x: x[1], reverse=True)

        # Map main question to ranked related questions
        relevance_map[main_question] = question_scores


def calc_avg_precision(main_q, rel_questions):
    sorted_rel_q = sorted(rel_questions.items(),
                          key=lambda x: x[1],
                          reverse=True)

    precision_values = []

    num_relevant = sum(rel_questions.values())

    relevant_so_far = 0
    for idx, (rel_q, rel_label) in enumerate(sorted_rel_q):

        if rel_label == 1:
            relevant_so_far += 1
            precision = relevant_so_far / (idx + 1)
            precision_values.append(precision)

    ap = sum(precision_values) / num_relevant
    return ap


def avg_precision(rel_scores):
    # Sort by predicted relevance
    ranked = [(i, s) for i, s in enumerate(rel_scores)]

    precision_values = []

    num_relevant = sum(rel_scores)

    relevant_so_far = 0
    for rank, (i, actual) in enumerate(ranked):
        if actual == 1:
            relevant_so_far += 1
            precision_values.append(relevant_so_far / (rank + 1))

    return sum(precision_values) / num_relevant


def calc_f1(rel_scores):
    true_pos = sum(rel_scores)
    false_pos = len(rel_scores) - true_pos

    precision = true_pos / len(rel_scores)
    recall = true_pos / true_pos

    f1 = 2 * precision * recall / (precision + recall)

    return f1








def main():
    # Your main code goes here
    map_scores = []
    for qid, rel_scores in rel_questions_relevance.items():
        ap = avg_precision(rel_scores)
        map_scores.append(ap)

    mean_ap = np.mean(map_scores)
    print("Simple Mean Average Precision:", mean_ap)

    f1_scores = []
    for qid, rel_scores in rel_questions_relevance.items():
        f1 = calc_f1(rel_scores)
        f1_scores.append(f1)

    mean_f1 = np.mean(f1_scores)
    print("Simple Mean F1 Score:", mean_f1)

    map_scores = []
    for qid, rel_scores in rel_enhanced_relevance.items():
        ap = avg_precision(rel_scores)
        map_scores.append(ap)

    mean_ap = np.mean(map_scores)
    print("Complex Mean Average Precision:", mean_ap)

    f1_scores = []
    for qid, rel_scores in rel_enhanced_relevance.items():
        f1 = calc_f1(rel_scores)
        f1_scores.append(f1)

    mean_f1 = np.mean(f1_scores)
    print("Complex Simple Mean F1 Score:", mean_f1)


# Check if this script is the main program entry point
if __name__ == "__main__":
    main()
