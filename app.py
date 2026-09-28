from flask import Flask, jsonify, render_template, request

from database import get_all_faqs, init_db
from faq_search import find_best_answer

app = Flask(__name__)

init_db()

NOT_FOUND_MESSAGE = "Sorry, I don't know the answer to that question."
MAX_QUESTION_LENGTH = 500


@app.route("/", methods=["GET"])
def home():

    return render_template("index.html")


@app.route("/api/faq", methods=["POST"])
def ask_faq():
    """
    Input  : {"question": "What are the college working hours?"}
    Output : {"answer": "The college is open from ..."}
    """
    # 1) JSON body-a edukkrom. silent=True -> JSON thappa irundha crash aagaama None tharum.
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be valid JSON."}), 400

    # 2) "question" field check
    question = data.get("question")
    if not isinstance(question, str) or not question.strip():
        return jsonify({"error": "'question' is required and must be a non-empty text."}), 400

    if len(question) > MAX_QUESTION_LENGTH:
        return jsonify({"error": f"'question' must be under {MAX_QUESTION_LENGTH} characters."}), 400

    # 3) Database la search pannrom
    try:
        faqs = get_all_faqs()
        answer = find_best_answer(question, faqs)
    except Exception as error:
        app.logger.error("Error while searching FAQ: %s", error)
        return jsonify({"error": "Something went wrong on the server."}), 500

    # 4) Answer kedaikkala na safe-a "theriyaadhu" nu sollrom
    if answer is None:
        return jsonify({"answer": NOT_FOUND_MESSAGE}), 200

    return jsonify({"answer": answer}), 200


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "URL not found."}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method not allowed for this URL."}), 405


if __name__ == "__main__":
    app.run(debug=True)