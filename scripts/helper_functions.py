import json

def load_workout_data(file_path="data/swim_workout_prompts.json"):
    """Loads workout questions and answers from a JSON file."""
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def find_workout_answer(question, data):
    """Simple function to find an answer based on a direct question match."""
    for item in data:
        if "question" in item and item["question"].lower() == question.lower():
            return item["answer"]
    return None

def check_payment_status(query, data):
    """Checks if the query matches a payment-related question and returns the appropriate answer."""
    for item in data:
        if "payment_query" in item and item["payment_query"].lower() in query.lower():
            if "paid" in query.lower(): # Simple check, might need more sophisticated logic
                return item.get("payment_answer_paid")
            else:
                return item.get("payment_answer_unpaid")
    return None

def format_response(answer):
    """Formats the chatbot's response (optional)."""
    return f"Chatbot: {answer}"

if __name__ == "__main__":
    workout_data = load_workout_data()
    print("Sample workout data:", workout_data[0])

    question = "What's a good endurance workout for a beginner?"
    answer = find_workout_answer(question, workout_data)
    if answer:
        print(f"Q: {question}\nA: {answer}")
    else:
        print(f"No direct answer found for: {question}")

    payment_query = "Has Alice paid for April?"
    payment_status = check_payment_status(payment_query, workout_data)
    if payment_status:
        print(f"Payment check for '{payment_query}': {payment_status}")
    else:
        print(f"Could not determine payment status for: {payment_query}")