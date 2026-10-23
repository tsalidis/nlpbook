from __future__ import annotations

import json
import re
from typing import Dict, Any, List
from openai import OpenAI

client = OpenAI()

SYSTEM = """Είσαι σύστημα Υπολογιστικής Γλωσσολογίας.
Σου δίνεται μία ελληνική πρόταση και μία λέξη-στόχος που είναι αμφίσημη.

ΕΠΙΣΤΡΕΨΕ ΜΟΝΟ ένα έγκυρο JSON αντικείμενο με τα πεδία:
- target: η λέξη-στόχος (string)
- chosen_sense: σύντομη περιγραφή της επιλεγμένης σημασίας (string)
- sense_id: ένας σύντομος αναγνωριστικός κωδικός της σημασίας (string, π.χ. S1, S2)
- candidates: λίστα υποψήφιων σημασιών, καθεμία ως αντικείμενο:
    { "sense_id": "...", "gloss": "...", "example": "..." }
- justification: 1–2 προτάσεις που εξηγούν ποια στοιχεία των συμφραζομένων οδήγησαν στην επιλογή

Μην χρησιμοποιήσεις markdown. Μην προσθέσεις κείμενο εκτός JSON.
"""

def extract_json_object(text: str) -> str:
    t = text.strip()
    t = re.sub(r"^\s*```(?:json)?\s*", "", t, flags=re.IGNORECASE)
    t = re.sub(r"\s*```\s*$", "", t)
    m = re.search(r"\{.*\}", t, flags=re.DOTALL)
    return m.group(0).strip() if m else t


def disambiguate_word(sentence: str, target: str) -> Dict[str, Any]:
    prompt = (
        f"Πρόταση: {sentence}\n"
        f"Λέξη-στόχος: {target}\n"
        "Επίλεξε τη σωστή σημασία της λέξης-στόχου με βάση τα συμφραζόμενα."
    )

    resp = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt},
        ],
    )

    raw = resp.output_text.strip()
    json_text = extract_json_object(raw)

    try:
        return json.loads(json_text)
    except json.JSONDecodeError:
        return {
            "target": target,
            "chosen_sense": None,
            "sense_id": None,
            "candidates": [],
            "justification": "Η έξοδος δεν ήταν έγκυρο JSON.",
            "raw_output": raw,
        }


def main() -> None:
    # Παραδείγματα λεξικής αμφισημίας (πολυσημία/ομωνυμία)
    examples: List[Dict[str, str]] = [
        {
            "sentence": "Αγόρασα καινούργια λάμπα φωτισμού για το γραφείο μου.",
            "target": "γραφείο",
        },
        {
            "sentence": "Το γραφείο μου έδωσε συγχαρητήρια.",
            "target": "γραφείο",
        },
        {
            "sentence": "Ο ιός χτύπησε τον υπολογιστή και χάθηκαν τα αρχεία.",
            "target": "ιός",
        },
        {
            "sentence": "Ο γιατρός είπε ότι ο ιός εξαπλώνεται γρήγορα τον χειμώνα.",
            "target": "ιός",
        },
        {
            "sentence": "Η κεφαλή της βίδας έσπασε και δεν ξεβιδώνει.",
            "target": "κεφαλή",
        },
        {
            "sentence": "Η κεφαλή του οργανισμού ανακοίνωσε νέα μέτρα.",
            "target": "κεφαλή",
        },
    ]

    for ex in examples:
        out = disambiguate_word(ex["sentence"], ex["target"])
        print("\nΠρόταση:", ex["sentence"])
        print("Λέξη-στόχος:", ex["target"])
        print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
