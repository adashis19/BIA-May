import json
BASE_DIR = "D:/BIA/BIA-May/"
import uvicorn

def read_alternatives():
    with open(f"{BASE_DIR}data/alternatives.json") as stream:
        return json.load(stream)

def get_alternatives_for_question(question_id: int):
    alternatives = read_alternatives()
    matching = [item["alternative"] for item in alternatives if item["question_id"] == question_id]
    return matching

# Example usage
if __name__ == "__main__":
    qid = 3  # Change to test different questions
    result = get_alternatives_for_question(qid)
    print(f"Alternatives for question {qid}:", result)