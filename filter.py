import json
from data_utils import example_utils
import dataclasses
from collections import defaultdict

def filter_question_types(input_file, output_file, question_types_to_filter):
    # Load the data
    data = example_utils.read_examples(input_file)
    
    # Filter the data
    filtered_data = [
        entry for entry in data
        if not any(q_type in entry.metadata.question_type for q_type in question_types_to_filter)
    ]
    
    # Save the filtered data to a new JSONL file
    with open(output_file, 'w') as f:
        for entry in filtered_data:
            f.write(json.dumps(dataclasses.asdict(entry)) + '\n')  # Convert to dict before serializing

    grouped_entries = defaultdict(list)
    for entry in filtered_data:
        field = entry.metadata.field  # Access the field attribute
        grouped_entries[field].append(entry)

    # Print grouped questions by field and their counts
    for field, entries in grouped_entries.items():
        print(f"Field: {field} (Count: {len(entries)})")  # Print the count of questions
        for entry in entries:
            print(f"  Question: {entry.question}")  # Access the question attribute


# Example usage
input_file = "data/r2_compiled_anon.jsonl"
output_file = "data/filtered_questions.jsonl"
question_types_to_filter = ["Summarization of information on a topic",
                            "Advice or suggestions on how to approach a problem",
                            "Question that describes a hypothetical scenario and asks a question based on this scenario",
                            "Request for opinion on a topic"]  # Replace with actual question types to filter
filter_question_types(input_file, output_file, question_types_to_filter)