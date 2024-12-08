
import json
from datasets import load_dataset
from typing import List, Dict, Any

def prepare_manim_dataset(test_split_ratio: float = 0.1) -> tuple[str, str]:
    """
    Prepares the manim-codegen dataset for OpenAI fine-tuning.

    Args:
        test_split_ratio: Ratio of data to use for testing (0.1 = 10%)

    Returns:
        Tuple of (training_file_path, validation_file_path)
    """
    # Load the dataset
    dataset = load_dataset("generaleoley/manim-codegen")

    def create_chat_example(example: Dict[str, Any]) -> Dict[str, Any]:
        """Convert a single example to the OpenAI chat format"""
        return {
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant that converts natural language descriptions into Manim animation code."
                },
                {
                    "role": "user",
                    "content": example['query'].strip()
                },
                {
                    "role": "assistant",
                    "content": example['answer'].strip()
                }
            ]
        }

    # Process all examples
    all_examples = [create_chat_example(ex) for ex in dataset['train']]

    # Split into train and validation sets
    split_index = int(len(all_examples) * (1 - test_split_ratio))
    train_examples = all_examples[:split_index]
    valid_examples = all_examples[split_index:]

    # Save the files
    train_path = "manim_train.jsonl"
    valid_path = "manim_valid.jsonl"

    with open(train_path, 'w') as f:
        for example in train_examples:
            f.write(json.dumps(example) + '\n')

    with open(valid_path, 'w') as f:
        for example in valid_examples:
            f.write(json.dumps(example) + '\n')

    return train_path, valid_path

def validate_files(train_path: str, valid_path: str) -> Dict[str, Any]:
    """
    Validates the prepared files and returns statistics
    """
    def count_tokens(text: str) -> int:
        # This is a very rough approximation
        return len(text.split())

    stats = {
        'train_examples': 0,
        'valid_examples': 0,
        'avg_prompt_tokens': 0,
        'avg_completion_tokens': 0,
        'max_tokens': 0
    }

    total_prompt_tokens = 0
    total_completion_tokens = 0

    for file_path in [train_path, valid_path]:
        with open(file_path, 'r') as f:
            for line in f:
                example = json.loads(line)
                messages = example['messages']

                # Count tokens
                prompt_tokens = count_tokens(messages[1]['content'])  # user message
                completion_tokens = count_tokens(messages[2]['content'])  # assistant message

                total_prompt_tokens += prompt_tokens
                total_completion_tokens += completion_tokens
                stats['max_tokens'] = max(stats['max_tokens'], prompt_tokens + completion_tokens)

                if file_path == train_path:
                    stats['train_examples'] += 1
                else:
                    stats['valid_examples'] += 1

    total_examples = stats['train_examples'] + stats['valid_examples']
    stats['avg_prompt_tokens'] = total_prompt_tokens / total_examples
    stats['avg_completion_tokens'] = total_completion_tokens / total_examples

    return stats


dataset = load_dataset("generaleoley/manim-codegen")

# Look at a few examples
for i, example in enumerate(dataset['train']):
    if i < 3:  # Show first 3 examples
        print(f"\nExample {i+1}:")
        print("Query:", example['query'])
        print("Answer:", example['answer'])
        print("-" * 50)

# To create and view the processed files:
train_path, valid_path = prepare_manim_dataset()

# Read and print a few examples from the processed files
print("\nProcessed examples from training file:")
with open(train_path, 'r') as f:
    for i, line in enumerate(f):
        if i < 3:  # Show first 3 examples
            print(f"\nProcessed Example {i+1}:")
            print(json.loads(line))
            print("-" * 50)

def analyze_jsonl(file_path):
    total_examples = 0
    total_tokens_estimate = 0
    instruction_lengths = []
    response_lengths = []

    with open(file_path, 'r') as f:
        for line in f:
            total_examples += 1
            data = json.loads(line)

            # Get user message (instruction) and assistant message (response)
            instruction = next(msg['content'] for msg in data['messages'] if msg['role'] == 'user')
            response = next(msg['content'] for msg in data['messages'] if msg['role'] == 'assistant')

            # Rough token estimation (words + punctuation)
            instruction_tokens = len(instruction.split())
            response_tokens = len(response.split())

            instruction_lengths.append(instruction_tokens)
            response_lengths.append(response_tokens)
            total_tokens_estimate += instruction_tokens + response_tokens

    stats = {
        'total_examples': total_examples,
        'avg_instruction_tokens': sum(instruction_lengths) / total_examples,
        'avg_response_tokens': sum(response_lengths) / total_examples,
        'max_instruction_tokens': max(instruction_lengths),
        'max_response_tokens': max(response_lengths),
        'total_tokens_estimate': total_tokens_estimate
    }
    return stats

# Analyze both training and validation files
train_stats = analyze_jsonl('manim_train.jsonl')
valid_stats = analyze_jsonl('manim_valid.jsonl')

print("\nTraining File Statistics:")
for key, value in train_stats.items():
    print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")

print("\nValidation File Statistics:")
for key, value in valid_stats.items():
    print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")

# Estimate training cost (using gpt-3.5-turbo pricing of $0.0080/1K tokens)
estimated_cost = (train_stats['total_tokens_estimate'] / 1000) * 0.0080
print(f"\nEstimated training cost: ${estimated_cost:.2f}")