# ---------- app.py ----------
from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI(title="Team 9 AI Data Redactor API")

class TextInput(BaseModel):
    text: str

@app.post("/redact")
def redact_text(data: TextInput):
    text = data.text

    # --- Redaction patterns ---
    patterns = {
        # Email addresses
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b": "[EMAIL]",
        # Credit card numbers (Visa, MasterCard, etc.)
        r"\b(?:\d[ -]*?){13,16}\b": "[CREDIT CARD]",
        # South African ID numbers (13 digits, often start with YYMMDD)
        r"\b\d{2}(0[1-9]|1[0-2])(0[1-9]|[13]\d|3[01])\d{7}\b": "[ID NUMBER]",
        # Phone numbers (+27, 0xx, etc.)
        r"(\+?\d{1,3}[-.\s]?)?(\(?\d{2,3}\)?[-.\s]?)?\d{3,4}[-.\s]?\d{4}": "[PHONE]",
        # Names (very simple heuristic: "Firstname Lastname")
        r"\b[A-Z][a-z]+ [A-Z][a-z]+\b": "[NAME]",
        # Street addresses (simple heuristic)
        r"\d{1,5} [A-Za-z ]+(Street|St|Avenue|Ave|Road|Rd|Lane|Ln|Drive|Dr)\b": "[ADDRESS]",
    }

    # --- Apply all redactions ---
    redacted_text = text
    for pattern, replacement in patterns.items():
        redacted_text = re.sub(pattern, replacement, redacted_text)

    return {"redacted_text": redacted_text}
