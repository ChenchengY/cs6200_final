from revChatGPT.V3 import Chatbot

api_key = "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"


# for i, q in enumerate(enhanced_questions):
#
#     print(f"Original Question: {q}")
#
#     # Generate 10 follow-up questions
#     generate_questions = f"generate 10 possible following up questions for this question: {q}"
#     chatbot = Chatbot(api_key=api_key)
#     followups = chatbot.ask(generate_questions)
#
#     fq_list = []
#     for f in followups:
#         fq_list.append(f)
#
#     # Save to questions map
#     enhanced_questions_map[i + 1] = {
#         q: fq_list
#     }
#
# print(enhanced_questions_map)

def chat():
    generate_questions = "generate 10 possible following up questions for this question and rank them according to their relevance"
    chatbot = Chatbot(api_key=api_key)
    while True:
        user_input = input("You: ")

        # Exit the loop if the user enters an exit command
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye! Chatbot session ended.")
            break

        # Ask the chatbot and print the response

        response = chatbot.ask(user_input)
        fq = chatbot.ask(generate_questions)
        print(f"Bot: {response}\n\n")
        print(f"Bot: {fq}")

def main():
    # Your main code goes here
    chat()
# Check if this script is the main program entry point
if __name__ == "__main__":
    main()
