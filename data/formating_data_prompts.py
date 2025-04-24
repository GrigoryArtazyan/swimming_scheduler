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
    # Save the formatted data to a new file
with open('formatted_swim_workouts.txt', 'w') as output_file:
        for item in formatted_data:
            output_file.write(item + "\n\n")  
            # Add double newlines between entries
            