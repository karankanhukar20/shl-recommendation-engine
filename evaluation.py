from recommend import recommend

# Simple evaluation queries with expected keywords
test_cases = [
    ("data analyst python", ["Python", "SQL"]),
    ("communication manager", ["Verbal"]),
    ("logic developer", ["Logical"])
]

def evaluate():
    correct = 0
    total = len(test_cases)

    for query, expected in test_cases:
        results = recommend(query)["assessment_name"].tolist()
        match = any(any(exp.lower() in r.lower() for r in results) for exp in expected)
        if match:
            correct += 1

    accuracy = correct / total
    print(f"Evaluation Accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    evaluate()