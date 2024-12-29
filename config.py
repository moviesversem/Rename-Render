# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "20005485")

API_HASH = os.environ.get("API_HASH", "04318fc5718f88958e10c6eb18c80163")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7615363128:AAGpEyYwOQCr-SGVlfxqmX5pBtUTh-l5d-8") 

FORCE_SUB = os.environ.get("FORCE_SUB", "mvmconvertvideo") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Mvmconvertbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://sayedzainrizvi0:avzh4r5BTS0WMsh2@cluster0.9u6st.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1919829145').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
