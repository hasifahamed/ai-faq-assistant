import os
import sqlite3

# faq.db file-oda full path. Project folder kulla dhaan create aagum.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "faq.db")

# Sample FAQ data: (question, answer, keywords)
# Unga real college details ku maathikonga.
SAMPLE_FAQS = [
    (
        "What are the college working hours?",
        "The college is open from 9:00 AM to 4:30 PM, Monday to Friday.",
        "timing time open hours schedule working",
    ),
    (
        "How can I apply for admission?",
        "You can apply for admission by filling the application form at the "
        "college office or on the college website before the last date.",
        "apply admission join enroll application register",
    ),
    (
        "What is the fee structure?",
        "The fee depends on the course you choose. Please contact the "
        "accounts office for the detailed fee structure.",
        "fees fee payment tuition cost price pay",
    ),
    (
        "Is hostel facility available?",
        "Yes, separate hostel facilities are available for boys and girls.",
        "hostel accommodation stay room residence",
    ),
    (
        "What are the library timings?",
        "The library is open from 9:00 AM to 5:00 PM on working days.",
        "library books reading location located hours open timing",
    ),
    (
        "How can I contact the college office?",
        "You can call the college office at 044-12345678 or email "
        "office@examplecollege.edu.",
        "contact phone email call office reach number",
    ),
    (
        "Does the college provide placement support?",
        "Yes, the placement cell conducts training and campus recruitment "
        "drives every year.",
        "placement job jobs campus recruitment career company",
    ),
]


def get_connection():
    """Database oda connection open pannum."""
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    """Table illana create pannum. Table empty-a irundha sample data insert pannum."""
    connection = get_connection()
    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS faqs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                keywords TEXT NOT NULL DEFAULT ''
            )
            """
        )

      
        count = connection.execute("SELECT COUNT(*) FROM faqs").fetchone()[0]
        if count == 0:
            connection.executemany(
                "INSERT INTO faqs (question, answer, keywords) VALUES (?, ?, ?)",
                SAMPLE_FAQS,
            )
        connection.commit()
    finally:
    
        connection.close()


def get_all_faqs():
    """Ella FAQ rows-um return pannum."""
    connection = get_connection()
    try:
        return connection.execute(
            "SELECT id, question, answer, keywords FROM faqs"
        ).fetchall()
    finally:
        connection.close()


if __name__ == "__main__":
    init_db()
    print("Database ready:", DB_PATH)