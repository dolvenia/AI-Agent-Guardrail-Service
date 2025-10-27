{
 "cells": [
  {
   "cell_type": "code",
   "execution_count":2,
   "id": "34ff0884-90e3-4faf-abe9-c49ef25e5cd3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# api.py\n",
    "from fastapi import FastAPI, HTTPException\n",
    "from pydantic import BaseModel\n",
    "from db_setup import SessionLocal, Document\n",
    "from redactor import ai_redact_text\n",
    "\n",
    "app = FastAPI()\n",
    "\n",
    "class TextPayload(BaseModel):\n",
    "    text: str\n",
    "\n",
    "@app.post(\"/redact\")\n",
    "def redact_text(payload: TextPayload):\n",
    "    db = SessionLocal()\n",
    "    try:\n",
    "        redacted = ai_redact_text(payload.text)\n",
    "        doc = Document(original_text=payload.text, redacted_text=redacted)\n",
    "        db.add(doc)\n",
    "        db.commit()\n",
    "        db.refresh(doc)\n",
    "        return {\"id\": doc.id, \"redacted_text\": redacted}\n",
    "    finally:\n",
    "        db.close()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
