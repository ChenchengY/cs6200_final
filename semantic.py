from nltk.translate.bleu_score import sentence_bleu
import numpy as np
import data
questions_map = data.questions_map
enhanced_questions_map = data.enhanced_questions_map

def semantic_diverse():
    for qid in questions_map:

        orig_question = list(questions_map[qid].keys())[0]
        orig_followups = questions_map[qid][orig_question]

        enhanced_question = list(enhanced_questions_map[qid].keys())[0]
        enhanced_followups = enhanced_questions_map[qid][enhanced_question]

        def bleu_diversity(question_set):
            scores = []
            for q1 in question_set:
                for q2 in question_set:
                    if q1 != q2:
                        bleu = sentence_bleu([q1], q2)
                        scores.append(1 - bleu)

            return np.average(scores)

        orig_div = bleu_diversity(orig_followups)
        enhanced_div = bleu_diversity(enhanced_followups)

        print(f"topic {qid}")
        print(f"Simple Question Diversity: {orig_div:.3f}")
        print(f"Complex Question Diversity: {enhanced_div:.3f}")




def main():
    # Your main code goes here
    semantic_diverse()
# Check if this script is the main program entry point
if __name__ == "__main__":
    main()