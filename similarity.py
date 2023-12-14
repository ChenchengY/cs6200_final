
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.metrics import jaccard_distance
import data
import chat

questions_map = data.questions_map
question_pairs = data.question_pairs
enhanced_questions = data.enhanced_questions
enhanced_questions_map = data.enhanced_questions_map





# count = 1
# for q in previous_question:
#     print(count)
#     count += 1
#     print(f"User: {q}")
#     response = chatbot.ask(q + " " + generate_questions)
#     print(f"Bot: {response}\n\n")

import numpy as np


# def calculate_cosine_similarity(main_question, related_questions):
#     """
#     Calculate the cosine similarity between a main question and a list of related questions.
#     """
#     # Combine the main question with the related questions
#     questions = [main_question] + related_questions
#
#     # Vectorize the questions using TF-IDF
#     vectorizer = TfidfVectorizer()
#     tfidf_matrix = vectorizer.fit_transform(questions)
#
#     # Calculate cosine similarity between the main question and each of the related questions
#     cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
#
#     # Return the cosine similarity scores
#     return cosine_similarities
#
# similarities = calculate_cosine_similarity(list(questions_map[2].keys())[0], list(questions_map[2].values())[0])
# # questions_list = list(questions_map[1].values())[0]
# # print(questions_list)
# print(similarities)
#
# import nltk
# from nltk.tokenize import word_tokenize
#
#
# def calculate_jaccard_similarity(main_question, related_questions):
#     """ Calculate the Jaccard similarity between a main question and a list of related questions. """
#
#     # Tokenize each question into words
#     main_ques_words = set(word_tokenize(main_question))
#     related_ques_words = []
#     for ques in related_questions:
#         related_ques_words.append(set(word_tokenize(ques)))
#
#     # Calculate Jaccard similarity between the main question and each related question
#     jaccard_similarities = []
#     for related_ques_set in related_ques_words:
#         intersection = main_ques_words.intersection(related_ques_set)
#         union = main_ques_words.union(related_ques_set)
#         jaccard_sim = len(intersection) / len(union)
#         jaccard_similarities.append(jaccard_sim)
#
#     return jaccard_similarities

# for i in range(10):
#     print(i)
#     js = calculate_jaccard_similarity(list(questions_map[i+1].keys())[0], list(questions_map[i+1].values())[0])
#     cs = calculate_cosine_similarity(list(questions_map[i+1].keys())[0], list(questions_map[i+1].values())[0])
#     print(similarities)
    # write a function to calculate the sum of js and cs and rank the questions based on the sum

import nltk



def calculate_jaccard_similarity(main_question, related_question):
    main_words = set(word_tokenize(main_question))
    related_words = set(word_tokenize(related_question))

    if len(main_words) == 0 or len(related_words) == 0:
        return 0

    intersection = main_words.intersection(related_words)

    return len(intersection) / len(main_words.union(related_words))


def calculate_cosine_similarity(main_question, related_question):
    corpus = [main_question, related_question]

    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(corpus)

    return cosine_similarity(matrix[0:1], matrix[1:])[0][0]



def print_ranked_questions(ranked_maps):
    for main_ques, ranked_related in ranked_maps.items():
        print(f"\nMain Question: {main_ques}\n")
        print("-" * len(main_ques))

        rank = 1
        for rel_ques, score in ranked_related:
            print(f"{rank}. {rel_ques}")
            print(f"   Score: {score:.4f}")
            rank += 1


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


def compare():
    for qid in questions_map:

        orig_question = list(questions_map[qid].keys())[0]
        orig_followups = questions_map[qid][orig_question]

        enhanced_question = list(enhanced_questions_map[qid].keys())[0]
        enhanced_followups = enhanced_questions_map[qid][enhanced_question]

        # Calculate similarity sums
        orig_sum = 0
        for fq in orig_followups:
            js = cal_jaccard_similarity(orig_question, fq)
            cs = cal_cosine_similarity(orig_question, fq)
            orig_sum += (js + cs)

        enhanced_sum = 0
        for fq in enhanced_followups:
            js = cal_jaccard_similarity(enhanced_question, fq)
            cs = cal_cosine_similarity(enhanced_question, fq)
            enhanced_sum += (js + cs)
        print(f"topic {qid}")
        print(f"Simple Question Avg Similarity: {orig_sum / len(orig_followups)}")
        print(f"Complex Question Avg Similarity: {enhanced_sum / len(enhanced_followups)}")
# ranked_maps = rank_related_questions(questions_map)
# print_ranked_questions(ranked_maps)

def main():
    # Your main code goes here
    compare()


# Check if this script is the main program entry point
if __name__ == "__main__":
    main()

