import os
from dotenv import load_dotenv

load_dotenv()
DAVINCI_TOKEN = os.getenv('DAVINCI_TOKEN')
SALAI_TOKEN = os.getenv('SALAI_TOKEN')
SERVER_ID = os.getenv('SERVER_ID')
CHANNEL_ID = os.getenv('CHANNEL_ID')

#boolean
USE_MESSAGED_CHANNEL = False

#don't edit the following variable
MID_JOURNEY_ID = "936929561302675456"  #midjourney bot id
targetID       = ""
targetHash     = ""
