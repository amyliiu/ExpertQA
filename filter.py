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



def find_lengths(input_file):
    total_length = 0
    count = 0
    with open(input_file, 'r') as f:
        data = json.load(f)
        for entry in data:
            if(len(entry['answer']) > 500):
                total_length += len(entry['answer'])
                count += 1
                if(count <= 3):
                    print(entry['answer'])
    print(count)
    print(total_length/count)


def calculate_average_tokens(input_file):
    total_tokens = 0
    count = 0
    with open("filtered_protein_description_generation.jsonl", 'w') as outfile:
        with open(input_file, 'r') as f:
            for line in f:
                entry = json.loads(line)  # Load each JSON object
                if(len(entry['answer']) > 500):
                    total_tokens += len(entry['answer'])
                    count += 1  # Increment the count of entries
                    outfile.write(line)

    if count == 0:
        return 0  # Avoid division by zero

    print(count)
    average_tokens = total_tokens / count  # Calculate the average
    return average_tokens

def find_percentages(input_file):
    total_tokens = 0
    count = 0

    with open(input_file, 'r') as f:
        counts = [0,0,0,0,0,0,0, 0  ]
        length = 0
        for line in f:
            count = 0
            length += 1
            entry = json.loads(line)  # Load each JSON object
            if( "(1)" in entry['answer']):
                count += 1
            if( "(2)" in entry['answer']):
                count += 1
            if( "(3)" in entry['answer']):
                count += 1
            if( "(4)" in entry['answer']):
                count += 1
            if( "(5)" in entry['answer']):
                count += 1
            if( "(6)" in entry['answer']):
                count += 1
            if( "(7)" in entry['answer']):
                count += 1
                
            counts[count] += 1
    counts[0] = counts[0] / length
    counts[1] = counts[1] / length
    counts[2] = counts[2] / length
    counts[3] = counts[3] / length
    counts[4] = counts[4] / length
    counts[5] = counts[5] / length
    counts[6] = counts[6] / length

    print(length)
    print(counts)



# Example usage
# input_file = "data/r2_compiled_anon.jsonl"
# output_file = "data/filtered_questions.jsonl"
# question_types_to_filter = ["Summarization of information on a topic",
#                             "Advice or suggestions on how to approach a problem",
#                             "Question that describes a hypothetical scenario and asks a question based on this scenario",
#                             "Request for opinion on a topic"]  # Replace with actual question types to filter
# filter_question_types(input_file, output_file, question_types_to_filter)

input_file = "filtered_protein_description_generation.jsonl"
print(find_percentages(input_file))
