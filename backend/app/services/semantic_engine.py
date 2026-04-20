from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# Load model once (cached in memory)
model = SentenceTransformer("all-MiniLM-L6-v2")


# Reference behavioral patterns
REFERENCE_PATTERNS = {
    "Execution": [
        "attacker executed malicious scripts",
        "powershell command launched",
        "remote code execution occurred"
    ],
    "Lateral Movement": [
        "spread across network using smb",
        "rdp connection to other machines",
        "psexec used for propagation"
    ],
    "Credential Access": [
        "password hashes dumped",
        "credentials stolen",
        "mimikatz activity observed"
    ],
    "Exfiltration": [
        "data transferred externally",
        "sensitive files uploaded",
        "information leak detected"
    ]
}


# Pre-embed reference patterns
reference_embeddings = {
    k: model.encode(v)
    for k, v in REFERENCE_PATTERNS.items()
}


def semantic_detect(text):
    text_embedding = model.encode([text])[0]

    scores = {}

    for category, embeds in reference_embeddings.items():
        sim = cosine_similarity(
            [text_embedding],
            embeds
        ).max()

        scores[category] = float(sim)

    return scores
