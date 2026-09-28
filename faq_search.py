import re

STOP_WORDS = {
    "a", "an", "the", "is", "are", "was", "were", "am", "be", "do", "does",
    "did", "what", "when", "where", "who", "how", "which", "can", "i", "you",
    "we", "me", "my", "your", "our", "of", "in", "on", "at", "to", "for",
    "and", "or", "please", "tell", "about", "there", "it", "this", "that",
    "with", "from", "has", "have", "will", "would", "should", "could",
}

MIN_MATCH_RATIO = 0.6


def normalize_words(text):
    """Text-a lowercase pannitu, mukkiyamana words-oda set-a return pannum."""
    words = re.findall(r"[a-z0-9]+", text.lower())

    result = set()
    for word in words:
        if word in STOP_WORDS:
            continue
        # Chinna trick: "hours" -> "hour", "fees" -> "fee"
        if len(word) > 3 and word.endswith("s"):
            word = word[:-1]
        result.add(word)
    return result


def find_best_answer(user_question, faqs):
    """Best matching answer-a return pannum. Match illana None return pannum."""
    user_words = normalize_words(user_question)

    if not user_words:
        return None

    best_answer = None
    best_matches = 0

    for faq in faqs:
        faq_words = normalize_words(faq["question"] + " " + faq["keywords"])
        matches = len(user_words & faq_words)

        if matches > best_matches:
            best_matches = matches
            best_answer = faq["answer"]

    if best_matches == 0:
        return None
    if best_matches / len(user_words) < MIN_MATCH_RATIO:
        return None

    return best_answer