import os
from openai import OpenAI

def generate_scope(idea: str) -> str:
    """
    Returns a structured scope as plain text (safe to render in <pre>).
    Requires OPENAI_API_KEY in environment.
    """
    api_key = os.getenv("OPENAI_API_KEY", "")
    if not api_key:
        return "OPENAI_API_KEY is not set. Add it as a local .env value or a Heroku config var."

    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    client = OpenAI(api_key=api_key)

    system = (
        "You are a senior AI web consultant. Produce a clear, client-friendly project scope.\n"
        "Output format:\n"
        "1) Clarifying Questions (bullets)\n"
        "2) Proposed Solution (short paragraphs)\n"
        "3) Key Features (bullets)\n"
        "4) Tech Stack (bullets)\n"
        "5) Phases & Timeline (bullets)\n"
        "6) Risks & Assumptions (bullets)\n"
        "Keep it concise but specific."
    )

    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": f"Project idea:\n{idea}"},
        ],
        temperature=0.4,
    )

    return resp.choices[0].message.content.strip()
