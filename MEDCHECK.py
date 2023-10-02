import csv

# ANSI escape code for lime green color
lime_green = "\033[92m"
reset_color = "\033[0m"

# Define the list of bodily systems and their corresponding symptoms
systems_and_symptoms = {
    "nervous": ["headache", "dizziness", "nausea", "blurred vision", "numbness", "tingling", "memory loss", "seizures", "difficulty coordination", "tremors", "fatigue", "insomnia", "anxiety"],
    "cardiovascular": ["chest pain", "palpitations", "shortness of breath", "rapid heartbeat", "fatigue", "edema", "fainting", "dizziness", "high blood pressure", "cold sweats", "irregular heartbeat", "swelling", "nausea", "leg pain"],
    "respiratory": ["cough", "shortness of breath", "wheezing", "chest pain", "sputum production", "rapid breathing", "fever", "chills", "difficulty breathing", "bluish skin", "fatigue", "loss of appetite", "headache", "sore throat"],
    "musculoskeletal": ["joint pain", "muscle pain", "stiffness", "swelling", "limited range of motion", "weakness", "muscle spasms", "bone pain", "back pain", "fractures", "deformities", "fatigue", "tenderness", "numbness"],
    "digestive": ["abdominal pain", "nausea", "vomiting", "diarrhea", "constipation", "bloating", "heartburn", "loss of appetite", "weight loss", "blood in stool", "jaundice", "difficulty swallowing", "fatigue", "pale stool"],
    "integumentary": ["skin rash", "itching", "dry skin", "acne", "bruising", "lesions", "swelling", "redness", "ulcers", "hair loss", "nail changes", "skin discoloration", "fatigue", "sweating"],
    "endocrine": ["fatigue", "increased thirst", "frequent urination", "weight changes", "hunger changes", "heat intolerance", "cold intolerance", "changes in skin texture", "changes in hair growth", "mood changes", "irregular menstruation", "impotence", "tremors", "weakness"],
    "immune": ["fever", "fatigue", "swollen glands", "sore throat", "cough", "skin rash", "joint pain", "muscle pain", "abdominal pain", "diarrhea", "nausea", "vomiting", "headache", "shortness of breath"],
    "urinary": ["frequent urination", "urgency", "burning sensation", "blood in urine", "dark urine", "cloudy urine", "foamy urine", "lower back pain", "abdominal pain", "pelvic pain", "changes in urine color", "difficulty urinating", "fatigue", "fever"],
}

# Ask the user if they are feeling sick or well
feeling = input(f"{lime_green}Are you feeling sick or well today? {reset_color}")

if feeling == "healthy":
    print(f"{lime_green}Alright. The doctor will be right with you.{reset_color}")
else:
    # Ask the user which systems are of concern
    print("Here is a list of bodily symptoms we cater to at this office:")
    print(", ".join(systems_and_symptoms.keys()))
    
    systems_input = input("Please enter the bodily systems of concern (comma-separated, e.g., 'nervous, cardiovascular'): ").lower().split(", ")
    symptoms_data = {}

    # Iterate through selected systems
    for system in systems_input:
        if system == "list":
            print("Bodily systems of concern:")
            print(", ".join(systems_and_symptoms.keys()))
            continue
        
        if system in systems_and_symptoms:
            print(f"Questions related to the {system} system:")
            symptoms_data[system] = {}

            # Ask yes or no questions for each symptom
            for symptom in systems_and_symptoms[system]:
                answer = input(f"Do you have {symptom}? (yes/no): ").lower()
                symptoms_data[system][symptom] = answer

    # Save the user's responses to a CSV file
    with open("patient_symptoms.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["System", "Symptom", "Response"])
        for system, symptoms in symptoms_data.items():
            for symptom, response in symptoms.items():
                writer.writerow([system, symptom, response])

    # Print the final message in lime green
    print(f"{lime_green}Thank you for providing that information! The doctor will be with you shortly.{reset_color}")
