# database.py

import sqlite3
import os
from pathlib import Path
import logging

PROJECT_ROOT = Path(__file__).parent.parent.parent
DB_PATH = os.path.join(PROJECT_ROOT, "data", "diseases.db")
print("DB PATH:", DB_PATH)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Main disease table
    c.execute('''CREATE TABLE IF NOT EXISTS diseases (
        id INTEGER PRIMARY KEY,
        disease_name TEXT UNIQUE
    )''')

    # Related tables
    c.execute('''CREATE TABLE IF NOT EXISTS symptoms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        disease_id INTEGER,
        symptom TEXT,
        UNIQUE(disease_id, symptom),
        FOREIGN KEY(disease_id) REFERENCES diseases(id)
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS treatments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        disease_id INTEGER,
        treatment TEXT,
        UNIQUE(disease_id, treatment),
        FOREIGN KEY(disease_id) REFERENCES diseases(id)
    )''')

    c.execute('''CREATE TABLE IF NOT EXISTS preventions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        disease_id INTEGER,
        prevention TEXT,
        UNIQUE(disease_id, prevention),
        FOREIGN KEY(disease_id) REFERENCES diseases(id)
    )''')

    # Insert data for Canine Distemper as an example
    diseases_data = [
        (1, 'Canine Distemper', [
            'Fever', 'Nasal & eye discharge', 'Coughing', 'Pneumonia',
            'Diarrhea', 'Vomiting', 'Hardened footpads', 'Neurological signs (seizures, paralysis, tremors)'
        ], [
            'No cure (supportive care only)', 'IV fluids', 'Antibiotics for secondary infections',
            'Anticonvulsants (for seizures)'
        ], [
            'Vaccination (DHPP vaccine)'
        ]),
        (2, 'Parvovirus (Parvo)', [
            'Severe bloody diarrhea', 'Vomiting', 'Lethargy', 'Dehydration',
            'High fever or hypothermia'
        ], [
            'Hospitalization (IV fluids, antiemetics)', 'Antibiotics (for secondary infections)'
        ], [
            'Vaccination (DHPP vaccine)'
        ]),
        (3, 'Rabies', [
            'Behavioral changes (aggression or lethargy)', 'Excessive drooling (foaming mouth)',
            'Paralysis', 'Seizures', 'Death within 10 days'
        ], [
            'No cure once symptoms appear', 'Immediate post-exposure vaccination (if bitten)'
        ], [
            'Annual rabies vaccination (legally required in Sri Lanka)'
        ]),
        (4, 'Leptospirosis', [
            'Fever', 'Muscle pain', 'Jaundice (yellow gums/eyes)', 'Blood in urine', 'Kidney & liver failure'
        ], [
            'Antibiotics (Doxycycline, Penicillin)', 'IV fluids', 'Liver support'
        ], [
            'Vaccination (Lepto vaccine)'
        ]),
        (5, 'Tick Fever (Ehrlichiosis & Babesiosis)', [
            'Fever', 'Lethargy', 'Pale gums (anemia)', 'Swollen lymph nodes',
            'Nosebleeds (Ehrlichiosis)', 'Dark urine (Babesiosis)'
        ], [
            'Ehrlichiosis: Doxycycline', 'Babesiosis: Imidocarb dipropionate'
        ], [
            'Tick control (collars, spot-ons)'
        ]),
        (6, 'Intestinal Worms', [
            'Diarrhea (sometimes bloody)', 'Pot-bellied appearance (puppies)', 'Weight loss',
            'Visible worms in stool'
        ], [
            'Deworming medication (Pyrantel, Fenbendazole, Praziquantel)'
        ], [
            'Monthly deworming'
        ]),
        (7, 'Skin Mange', [
            'Intense itching', 'Hair loss', 'Crusty skin', 'Sores', 'Bacterial infections'
        ], [
            'Medicated dips (Amitraz)', 'Oral medications (Ivermectin, Milbemycin)',
            'Antibiotics (for secondary infections)'
        ], [
            'Regular grooming', 'Anti-mite treatments'
        ]),
    ]

    for disease_id, name, symptoms, treatments, preventions in diseases_data:
        c.execute("INSERT OR IGNORE INTO diseases (id, disease_name) VALUES (?, ?)", (disease_id, name))
        for s in symptoms:
            c.execute("INSERT OR IGNORE INTO symptoms (disease_id, symptom) VALUES (?, ?)", (disease_id, s))
        for t in treatments:
            c.execute("INSERT OR IGNORE INTO treatments (disease_id, treatment) VALUES (?, ?)", (disease_id, t))
        for p in preventions:
            c.execute("INSERT OR IGNORE INTO preventions (disease_id, prevention) VALUES (?, ?)", (disease_id, p))

    conn.commit()
    conn.close()

def query_disease(disease_name):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT id, disease_name FROM diseases WHERE disease_name LIKE ?", (f"%{disease_name}%",))
    disease = c.fetchone()

    if not disease:
        conn.close()
        return None

    disease_id, disease_name = disease

    c.execute("SELECT symptom FROM symptoms WHERE disease_id = ?", (disease_id,))
    symptoms = [row[0] for row in c.fetchall()]

    c.execute("SELECT treatment FROM treatments WHERE disease_id = ?", (disease_id,))
    treatments = [row[0] for row in c.fetchall()]

    c.execute("SELECT prevention FROM preventions WHERE disease_id = ?", (disease_id,))
    preventions = [row[0] for row in c.fetchall()]

    conn.close()

    return {
        "disease": disease_name,
        "symptoms": symptoms,
        "treatments": treatments,
        "preventions": preventions
    }

init_db()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info("Database initialized")