{
 "cells": [
  {
   "cell_type": "code",
   "execution_count":2,
   "id": "656444fe-9762-488e-932a-036b3c523aef",
   "metadata": {},
   "outputs": [],
   "source": [
    "# redactor.py\n",
    "import re\n",
    "from openai import OpenAI\n",
    "\n",
    "client = OpenAI(api_key=\"YOUR_OPENAI_API_KEY\")\n",
    "\n",
    "def ai_redact_text(text: str) -> str:\n",
    "    \"\"\"\n",
    "    Uses LLM to detect and redact personal and payment information.\n",
    "    \"\"\"\n",
    "    prompt = f\"\"\"\n",
    "    You are a data privacy compliance assistant.\n",
    "    Identify and redact (replace with [REDACTED]) any of the following:\n",
    "    - Names\n",
    "    - Email addresses\n",
    "    - Phone numbers\n",
    "    - ID numbers\n",
    "    - Bank account or credit card numbers\n",
    "    - Physical addresses\n",
    "    - IP addresses\n",
    "    - Any sensitive personal or financial info.\n",
    "    \n",
    "    Text:\n",
    "    {text}\n",
    "    \"\"\"\n",
    "    response = client.chat.completions.create(\n",
    "        model=\"gpt-4o-mini\",\n",
    "        messages=[{\"role\": \"user\", \"content\": prompt}],\n",
    "        temperature=0\n",
    "    )\n",
    "\n",
    "    return response.choices[0].message.content.strip()\n"
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
