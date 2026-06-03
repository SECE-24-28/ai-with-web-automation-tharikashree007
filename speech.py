# ==========================================
# SPEECH SENTIMENT ANALYSIS SYSTEM
# Google Colab Version
# ==========================================

# Install Required Libraries
!apt-get -qq install ffmpeg -y
!pip -q install openai-whisper textblob gtts

from google.colab import output
from base64 import b64decode
from textblob import TextBlob
from gtts import gTTS
from IPython.display import Audio, display
import whisper
import time

# ==========================================
# PROJECT HEADER
# ==========================================

print("=" * 60)
print("      SPEECH SENTIMENT ANALYSIS SYSTEM")
print("=" * 60)

# ==========================================
# START RECORDING MESSAGE
# ==========================================

start_message = "Started recording. Please speak clearly for five seconds."

print("\n🎤 Started Recording...")
print("🗣️ Please speak clearly for 5 seconds...\n")

tts_start = gTTS(start_message)
tts_start.save("start_message.mp3")

display(Audio("start_message.mp3", autoplay=True))

# Wait for announcement to finish
time.sleep(4)

# ==========================================
# RECORD AUDIO FROM BROWSER
# ==========================================

RECORD = """
const sleep = time => new Promise(resolve => setTimeout(resolve, time))
const b2text = blob => new Promise(resolve => {
 const reader = new FileReader()
 reader.onloadend = e => resolve(e.srcElement.result)
 reader.readAsDataURL(blob)
})

var record = async () => {
 const stream = await navigator.mediaDevices.getUserMedia({audio:true})
 const recorder = new MediaRecorder(stream)
 let chunks = []

 recorder.ondataavailable = e => chunks.push(e.data)

 recorder.start()

 await sleep(5000)

 recorder.stop()

 await new Promise(resolve => recorder.onstop = resolve)

 const blob = new Blob(chunks)

 return await b2text(blob)
}

record()
"""

audio_data = output.eval_js(RECORD)

audio_bytes = b64decode(audio_data.split(',')[1])

with open("speech.webm", "wb") as f:
    f.write(audio_bytes)

print("✅ Recording Completed")

# ==========================================
# SPEECH TO TEXT
# ==========================================

print("\n⏳ Converting Speech To Text...")

model = whisper.load_model("base")

result = model.transcribe("speech.webm")

text = result["text"].strip()

# ==========================================
# DISPLAY RECOGNIZED TEXT
# ==========================================

print("\n" + "=" * 60)
print("RECOGNIZED TEXT")
print("=" * 60)
print(text)
print("=" * 60)

# ==========================================
# SENTIMENT ANALYSIS
# ==========================================

blob = TextBlob(text)

polarity = blob.sentiment.polarity

if polarity > 0:
    sentiment = "Positive 😊"
elif polarity < 0:
    sentiment = "Negative 😔"
else:
    sentiment = "Neutral 😐"

# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n" + "=" * 60)
print("SENTIMENT ANALYSIS RESULT")
print("=" * 60)
print("Recognized Text :", text)
print("Sentiment       :", sentiment)
print("Polarity Score  :", round(polarity, 2))
print("=" * 60)

# ==========================================
# TEXT TO SPEECH OUTPUT
# ==========================================

speech_output = f"""
The recognized text is:
{text}

The sentiment is {sentiment}

The polarity score is {round(polarity,2)}
"""

tts_result = gTTS(text=speech_output, lang='en')
tts_result.save("sentiment_result.mp3")

print("\n🔊 Playing Voice Output...\n")

display(Audio("sentiment_result.mp3", autoplay=True))

# ==========================================
# END OF PROJECT
# ==========================================
