# pip install pyttsx3

import pyttsx3 ##Sert a transformer du texte en voix
def speak(text):
    engine = pyttsx3.init() #Cet objet permet de contrôler la voix, le volume, la vitesse
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)
    engine.say(text) #Tu demandes au moteur vocal de prononcer le texte passé dans la fonction.
    engine.runAndWait()

#nous avons créé une petite fonction qui s'appelle speak()
# Elle initialise le moteur vocal, règle la vitesse de la voix, puis lit le texte qu’on lui envoie.
# Donc à chaque fois que l’assistant doit parler, on utilise simplement speak(texte), et il prononce la réponse.
