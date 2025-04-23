import json

# Load the JSON data from your file
with open('swim_workout_prompts.json', 'r') as file:
    swim_workouts = json.load(file)

# Print the entire loaded data (just to check it's working)
print(swim_workouts)