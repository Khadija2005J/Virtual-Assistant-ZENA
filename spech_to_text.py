import speech_recognition as sr #permet de faire de la reconnaissance vocale.
import speak


def spech_to_text():
  """Try to capture audio and return recognized text.

  If PyAudio / microphone is not available, speak a message and return None.
  """
  r = sr.Recognizer() #convertir l’audio en texte
  try:
    with sr.Microphone() as source:
      # brief ambient adjustment then listen with timeouts to avoid hanging
      r.adjust_for_ambient_noise(source, duration=1)
      try:
        audio = r.listen(source, timeout=5, phrase_time_limit=6) #coupe automatiquement après 6 secondes de parole.
      except sr.WaitTimeoutError:
        speak.speak("Aucun discours détecté. Veuillez réessayer.")
        return None
  except (AttributeError, OSError, Exception) as e:
    # Commonly raises AttributeError if pyaudio is missing, or OSError if no mic
    speak.speak("Microphone indisponible. Veuillez plutôt taper votre question.")
    return None

  voice_data = ''
  try:
    voice_data = r.recognize_google(audio)
    return voice_data

  except sr.UnknownValueError:
    speak.speak("Désolé, je n’ai pas saisi.")
    return None
  except sr.RequestError:
    speak.speak('Pas de connexion internet ; veuillez activer votre connexion.')
    return None



