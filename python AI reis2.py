import pyodbc

# Verbinding met de Access database
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\niekw\OneDrive\Reisbureau\AI reizen.accdb;'
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Gebruik de exacte kolomnamen zoals in je database
cursor.execute('SELECT september, bestemming, stadnatuur, uitgaan, toeristisch, openbaarvervoer, strandzee FROM AI1')

# Vraag input van de gebruiker
print("AIstudenttrip.com")
print("Vind jullie beste/goedkope September reis")
temperatuur = int(input("Gemiddelde dagtemperatuur 0°-6°C (0), 6°-12°C (1), 12°C-18°C (2), 18°-24°C(3); 24°C+ (4): "))
print("geef scores van 0 tot 4")
stad = int(input("stad(0) - natuur(4): "))
uitgaan = int(input("uitgaan weinig (0) - veel (4): "))
toeristich = int(input("toeristisch(0) - authentiek/origineel(4): "))
openbaarvervoer = int(input("openbaar vervoer: niet belangrijk(0) - belangrijk(4): "))
strandzee = input("strand/zee een must? ja of nee: ")
if strandzee == 'ja':
    strandzee = True
else:
    strandzee = False

# Variabelen om de top 3 locaties en scores bij te houden
plaats = 'tba'
plaats2 = 'tba'
plaats3 = 'tba'
score = 16
scoreA = 16
scoreB = 16

# Haal alle rijen op uit de query
rows = cursor.fetchall()

# Verwerk elke rij
for row in rows:
    print(row)  # Print de rijen om te zien of de query nu werkt
