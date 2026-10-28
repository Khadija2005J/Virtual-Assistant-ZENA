# ZENA – Virtual Assistant

**A desktop voice assistant written in Python, with a graphical interface.**

Talk to ZENA or type a command: she answers out loud, tells the time and date, checks the weather, plays music and opens websites. She understands simple commands in English and French.

<p align="center"><img src="image/assitant.png" alt="ZENA" width="180"></p>

## Features

- **Voice input** with Google Speech Recognition, or type in the text box
- **Voice output** with pyttsx3 (works offline)
- Small talk: name, greetings, "how are you", thanks
- Current time and date
- Weather lookup
- Play music
- Open Google, YouTube, Facebook, Instagram and other websites
- Commands in English and French ("quelle heure", "ouvre youtube", "ferme toi"…)

## Tech stack

| Purpose | Tools |
|---------|-------|
| GUI | Tkinter, Pillow |
| Speech to text | SpeechRecognition, PyAudio |
| Text to speech | pyttsx3 |
| Web / weather | requests, BeautifulSoup |

## Project structure

```
├── gui.py               # Tkinter window – start here
├── action.py            # Command handling
├── spech_to_text.py     # Microphone input
├── speak.py             # Text to speech
├── weather.py           # Weather lookup
└── image/               # Assistant avatar
```

## Getting started

**Prerequisites:** Python 3.9+ and a microphone.

```bash
git clone https://github.com/Khadija2005J/Virtual-Assistant-ZENA.git
cd Virtual-Assistant-ZENA
pip install -r requirement.txt
python gui.py
```

> On Windows, if `pyaudio` fails to install, run `pip install pipwin && pipwin install pyaudio`.
> The weather location is currently set in `weather.py`.

## Team

Built by Khadija Alaoui Mrani and [Rim Ben Moussa](https://github.com/RimBenMoussa).
