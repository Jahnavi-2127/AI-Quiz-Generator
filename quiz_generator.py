import nltk
import random

# Download punkt tokenizer (needed by nltk)
nltk.download('punkt')
print("✅ Download complete! Ready to generate quiz 🎉\n")

# Question bank (Education-related)
quiz_questions = [
    {"question": "What does AI stand for?", "answer": "Artificial Intelligence"},
    {"question": "Who is known as the father of modern computer science?", "answer": "Alan Turing"},
    {"question": "Which programming language is most used in AI?", "answer": "Python"},
    {"question": "What is the full form of NLP in AI?", "answer": "Natural Language Processing"},
    {"question": "Which algorithm is used to find the shortest path in graphs?", "answer": "Dijkstra's Algorithm"},
    {"question": "What does HTML stand for?", "answer": "HyperText Markup Language"},
    {"question": "Which layer of the OSI model deals with IP addressing?", "answer": "Network Layer"},
    {"question": "What is the capital of India?", "answer": "New Delhi"},
    {"question": "Who invented the World Wide Web?", "answer": "Tim Berners-Lee"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"}
]

# Pick 5 random questions
selected_questions = random.sample(quiz_questions, 5)

# Quiz Loop
score = 0
print("🎓 Welcome to the Quiz! Answer the following questions:\n")
for i, q in enumerate(selected_questions, 1):
    print(f"Q{i}: {q['question']}")
    user_answer = input("Your Answer: ")
    if user_answer.strip().lower() == q['answer'].lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is: {q['answer']}\n")

print(f"🏆 Your Final Score: {score}/5")
