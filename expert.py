import random

knowledge_base = {
    "If the patient has a fever, then they may have a cold.": True,
    "If the patient has a cough, then they may have a cold.": True,
    "If the patient has a runny nose, then they may have a cold.": True,
}

rules = [
    "If the patient has a fever and a cough, then they definitely have a cold.",
    "If the patient has a fever and a runny nose, then they probably have a cold.",
    "If the patient has a cough and a runny nose, then they might have a cold.",
]

def find_diagnosis(symptoms):

    for rule in rules:
        if all(symptom in symptoms for symptom in rule.split(" ")):
            return rule

    return random.choice(list(knowledge_base.keys()))

symptoms = input("What are your symptoms? ").split(" ")

diagnosis = find_diagnosis(symptoms)

print("The diagnosis is:", diagnosis)