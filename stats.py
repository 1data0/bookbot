from typing import Dict, List, Any


def get_num_words(text: str) -> int:
    return len(text.split())

def get_num_chars(text: str) -> Dict[str, int]:
    chars = {}

    for c in text:
        key = c.lower()
        if key not in chars.keys():
            chars[key] = 0

        chars[key] += 1

    return chars

def sort_num_chars(num_chars: Dict[str, int]) -> List[Dict[str, Any]]:
    sorted = []

    for k, v in num_chars.items():
        sorted.append({"name": k, "value": v})

    sorted.sort(reverse=True, key=lambda x: x["value"])

    return sorted
