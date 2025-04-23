import json

# Function to format data for Alpaca-style tuning
def to_alpaca_format(prompt, response):
    return f"""### Instruction:
{prompt}

### Response:
{response}"""

# Loading the JSON data 
with open('swim_workout_prompts.json', 'r') as file:
    swim_workouts = json.load(file)

# Dictionaries with 'prompt' and 'response' keys
formatted_data = []
for workout in swim_workouts:
    prompt = workout.get('prompt', 'No prompt provided')
    response = workout.get('response', 'No response provided')
    formatted_data.append(to_alpaca_format(prompt, response))

# Print one example to test
print(formatted_data[0])  # Print the first formatted example
