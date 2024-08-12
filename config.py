
from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("27098166"))
API_HASH = getenv("962e823666b17f1c4fe94d9b200284a8")

BOT_TOKEN = getenv("6743171827:AAFyMG2xtxhvXYQliq7Yf0EVgigFYSPSyKM")
OWNER_ID = int(getenv("5516578116"))

MONGO_DB_URI = getenv("mongodb+srv://vocon90583:Rishabh1126@cluster0.qyin9uj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/trending_era")
