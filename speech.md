# Speech-Based Sentiment Analysis with Voice Output

## Project Title

Speech-Based Sentiment Analysis and Voice Response Generation using Whisper, TextBlob, and gTTS

## Introduction

This project is developed to build an intelligent speech processing system that records a user's voice, converts the spoken content into text, analyzes the sentiment of the recognized text, and generates a spoken response. The project combines Speech Recognition, Natural Language Processing (NLP), Sentiment Analysis, and Text-to-Speech technologies into a single workflow. The system accepts speech through a microphone and produces both textual and audio-based sentiment results.

## Objective

The objective of this project is to:

* Record speech from the user
* Convert speech into readable text
* Analyze sentiment from the recognized text
* Identify whether the sentiment is Positive, Negative, or Neutral
* Calculate the polarity score
* Generate a spoken response based on the sentiment
* Display recognized text and sentiment results

## Workflow

Speech Input → Audio Recording → Speech Recognition → Text Generation → Sentiment Analysis → Sentiment Prediction → Text-to-Speech Conversion → Voice Output

## Features

* Record audio using microphone
* Convert speech into text
* Display recognized text
* Perform sentiment analysis
* Classify sentiment as Positive, Negative, or Neutral
* Calculate polarity score
* Generate voice response
* Display final sentiment result
* User-friendly implementation in Google Colab

## Technologies Used

**Programming Language:** Python

**Libraries:**

* OpenAI Whisper
* TextBlob
* gTTS
* FFmpeg

**Models:**

* Whisper Speech Recognition Model
* TextBlob Sentiment Analysis Engine

**Platform:**

* Google Colab

## System Architecture

Microphone Input → Audio Recording → Whisper Model → Text Output → TextBlob Sentiment Analysis → Sentiment Result → gTTS → Voice Output

## Module Description

### Audio Recording Module

Records user speech through the browser microphone.

### Speech Recognition Module

Uses Whisper to convert recorded speech into text.

### Sentiment Analysis Module

Analyzes the recognized text and determines sentiment polarity.

### Result Processing Module

Classifies sentiment as Positive, Negative, or Neutral and calculates polarity score.

### Voice Output Module

Uses gTTS to convert the sentiment result into speech.

## Installation

Install dependencies:

```bash
!apt-get install ffmpeg -y
!pip install openai-whisper
!pip install textblob
!pip install gtts
```

## Execution Procedure

1. Open Google Colab.
2. Install required libraries.
3. Run the notebook.
4. Allow microphone access.
5. Speak clearly when recording starts.
6. Audio is recorded for five seconds.
7. Whisper converts speech into text.
8. TextBlob performs sentiment analysis.
9. Sentiment result is displayed.
10. Voice output is generated automatically.

## Input

### Input Type

Microphone Speech Input

### Example

```text
I am very happy today because I got good marks.
```

## Output

### Generated Outputs

* Recognized Text
* Sentiment Result
* Polarity Score
* Voice Output

### Example

```text
Speech:
I am very happy today because I got good marks.

↓

Recognized Text:
I am very happy today because I got good marks.

↓

Sentiment:
Positive

↓

Polarity Score:
0.85

↓

Voice Output:
The recognized text is I am very happy today because I got good marks.
The sentiment is Positive.
The polarity score is 0.85.
```

## Advantages

* Fully automated workflow
* Supports speech input
* Generates speech output
* Easy to implement
* Accurate speech recognition using Whisper
* Simple sentiment analysis
* Suitable for educational projects

## Limitations

* Requires internet connection
* Recording quality affects accuracy
* Whisper model may take time to load initially
* TextBlob may not understand complex emotions

## Future Enhancements

* Real-time sentiment analysis
* Multilingual speech support
* Emotion detection (Happy, Sad, Angry, Fear)
* Web application deployment
* Mobile application integration
* Deep learning-based sentiment prediction
* Dashboard visualization

## Applications

* Voice Assistants
* Customer Feedback Analysis
* Call Center Monitoring
* Educational Systems
* Accessibility Applications
* Human-Computer Interaction
* Social Media Sentiment Analysis

## Conclusion

This project demonstrates a complete Speech-to-Text Sentiment Analysis pipeline. The system successfully records speech, converts it into text, analyzes sentiment, calculates polarity scores, and generates spoken responses. By integrating Speech Recognition, Natural Language Processing, and Text-to-Speech technologies, the project provides an end-to-end intelligent voice-based sentiment analysis solution.

## References

1. OpenAI Whisper Documentation
2. TextBlob Documentation
3. Google Text-to-Speech (gTTS) Documentation
4. Google Colab Documentation
5. Python Documentation
6. FFmpeg Documentation
