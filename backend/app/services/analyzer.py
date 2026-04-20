import re
import random
from app.services.semantic_engine import semantic_detect

# --- Keyword Tactical Mapping ---
TACTIC_KEYWORDS = {
    "Execution": ["powershell", "cmd", "script", "bash"],
    "Initial Access": ["phishing", "vpn", "exploit", "credential"],
    "Persistence": ["registry", "autorun", "scheduled"],
    "Lateral Movement": ["smb", "rdp", "psexec"],
    "Defense Evasion": ["disable defender", "obfuscate"],
    "Privilege Escalation": ["admin", "root", "token"]
}

# --- Technique Mapping ---
TECHNIQUES = {
    "powershell": ("T1059.001", "PowerShell Execution"),
    "ransomware": ("T1486", "Data Encrypted for Impact"),
    "credential": ("T1003", "Credential Dumping"),
    "smb": ("T1021", "Remote Services SMB"),
}


# --- Mitigation Library ---
MITIGATIONS = [
    "Apply latest security patches on all exposed systems",
    "Enable multi-factor authentication (MFA)",
    "Monitor abnormal login patterns",
    "Block suspicious outbound C2 connections",
    "Segment internal network zones",
    "Deploy endpoint detection solutions"
]


def normalize(text):
    return re.sub(r"\s+", " ", text.lower())


def detect_tactics(text):
    scores = {}

    for tactic, words in TACTIC_KEYWORDS.items():
        hits = sum(text.count(w) for w in words)
        if hits:
            scores[tactic] = hits

    total = sum(scores.values()) or 1

    # Convert to percentage
    return {
        k: round((v / total) * 100, 1)
        for k, v in scores.items()
    }


def detect_techniques(text):
    found = []

    for kw, (tid, name) in TECHNIQUES.items():
        if kw in text:
            found.append({
                "id": tid,
                "name": name,
                "confidence": random.randint(70, 90),
                "evidence": f"Keyword '{kw}' detected"
            })

    return found


def generate_summary(tactics):
    if "Execution" in tactics:
        return (
            "Indicators suggest malicious execution behavior with "
            "possible script-based intrusion activity. Monitoring "
            "and containment are recommended."
        )
    return "No high-risk behavioral patterns strongly detected."


def generate_trend():
    base = 50
    trend = []
    for year in range(2018, 2026):
        base += random.randint(5, 20)
        trend.append({"year": year, "value": base})
    return trend


# --- MAIN ENTRY ---
def advanced_analyze(text):

    text = normalize(text)

    tactics = detect_tactics(text)
    techniques = detect_techniques(text)
    semantic_scores = semantic_detect(text)

    result = {
        "tactics": tactics,
        "techniques": techniques,
        "semantic_scores": semantic_scores,
        "mitigations": random.sample(MITIGATIONS, 4),
        "summary": generate_summary(tactics),
        "trend": generate_trend()
    }

    return result
