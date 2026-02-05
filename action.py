import datetime       # Gestion des dates et heures (date actuelle, formatage, calculs temporels)
import speak          # Module personnalisé : permet de faire parler ton assistant (Text-to-Speech)
import webbrowser     # Ouvre automatiquement des sites web ou des URLs dans le navigateur
import os             # Interactions avec le système d'exploitation (dossiers, fichiers, commandes)
import weather        # Module météo personnalisé : récupérer les informations météo (température, état du ciel)
import urllib.parse   # Encoder ou décoder des URL (utile pour les recherches Google ou les liens dynamiques)
import random         # Générer des nombres, choix aléatoires (utile pour réponses variées)
import re             # Module d'expressions régulières : traiter ou analyser du texte (chercher, valider des mots)
import math           # Fonctions mathématiques avancées (racines, puissance, arrondi, trigonométrie)


# petite liste globale pour les tâches
todo_list = []

# quelques blagues
jokes = [
    "Quelle est la boisson préférée des développeurs ? Le Java."
]

# petites recommandations
films_reco = [
    "Inception",
    "Interstellar",
    "The Pursuit of Happyness",
    "Le Fabuleux Destin d’Amélie Poulain"
]

series_reco = [
    "Breaking Bad",
    "La Casa de Papel",
    "Suits",
    "Dark"
]

livres_reco = [
    "Les Quatre Accords Toltèques",
    "Atomic Habits",
    "L’Alchimiste de Paulo Coelho",
    "Deep Work de Cal Newport"
]

histoires = [
    "Il était une fois une étudiante en génie informatique qui voulait tout abandonner. Elle a décidé de faire une pause, de respirer, puis de recommencer pas à pas. Quelques mois plus tard, c’est elle qui aidait les autres à ne pas abandonner."
]


def Action(send):

    global todo_list

    data_btn = send.lower().strip()

    # --- Présentation / Nom de l'assistant ---
    if "what is your name" in data_btn or "ton nom" in data_btn:
        msg = "Je suis Zéna."
        speak.speak(msg)
        return msg

    # --- Salutations en anglais ET en français ---
    elif ("hello" in data_btn or "hye" in data_btn or "hay" in data_btn or
          "bonjour" in data_btn or "salut" in data_btn):
        msg = "Bonjour, comment puis-je t'aider ?"
        speak.speak(msg)
        return msg

    # --- Comment ça va ? ---
    elif "how are you" in data_btn or "ça va" in data_btn:
        msg = "Je vais très bien, merci de demander ! Et toi ?"
        speak.speak(msg)
        return msg

    # --- Merci ---
    elif "thanku" in data_btn or "thank" in data_btn or "merci" in data_btn:
        msg = "Avec plaisir, je suis là pour t'aider."
        speak.speak(msg)
        return msg

    # --- Good morning ---
    elif "good morning" in data_btn:
        msg = "Bonjour, je pense que tu as besoin d'un coup de main."
        speak.speak(msg)
        return msg

    # --- Heure actuelle ---
    elif "time now" in data_btn or "quelle heure" in data_btn or "heure actuelle" in data_btn:
        now = datetime.datetime.now()
        Time = f"Il est {now.hour:02d} heures {now.minute:02d}."
        speak.speak(Time)
        return Time

    # --- Date du jour ---
    elif "date" in data_btn or "quel jour sommes-nous" in data_btn:
        today = datetime.date.today()
        date_str = today.strftime("Nous sommes le %d/%m/%Y.")
        speak.speak(date_str)
        return date_str

    # --- Shutdown / quitter ---
    elif "shutdown" in data_btn or "quit" in data_btn or "ferme toi" in data_btn:
        speak.speak("D'accord, je me déconnecte.")
        return "ok sir"

    # --- Musique en ligne ---
    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")
        msg = "gaana.com est ouvert, profite de ta musique."
        speak.speak(msg)
        return msg

    # --- Ouvrir Google ---
    elif 'open google' in data_btn or 'google' in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        msg = "Google est ouvert."
        speak.speak(msg)
        return msg

    # --- Ouvrir YouTube ---
    elif ('youtube' in data_btn or "open youtube" in data_btn or
          "ouvre youtube" in data_btn):
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        msg = "YouTube est ouvert."
        speak.speak(msg)
        return msg

    # --- Ouvrir Facebook ---
    elif "facebook" in data_btn or "ouvre facebook" in data_btn:
        url = 'https://facebook.com/'
        webbrowser.get().open(url)
        msg = "Facebook est ouvert."
        speak.speak(msg)
        return msg

    # --- Ouvrir Instagram ---
    elif "instagram" in data_btn or "ouvre instagram" in data_btn:
        url = 'https://instagram.com/'
        webbrowser.get().open(url)
        msg = "Instagram est ouvert."
        speak.speak(msg)
        return msg

    # --- Ouvrir LinkedIn ---
    elif "linkedin" in data_btn or "ouvre linkedin" in data_btn:
        url = 'https://www.linkedin.com/'
        webbrowser.get().open(url)
        msg = "LinkedIn est ouvert."
        speak.speak(msg)
        return msg

    # --- Ouvrir ENSA Fès ---
    elif "ensaf" in data_btn or "ensa fes" in data_btn or "ouvre ensaf" in data_btn:
        url = 'https://ensaf.ac.ma/'
        webbrowser.get().open(url)
        msg = "Le site de l'ENSA Fès est ouvert."
        speak.speak(msg)
        return msg

    # --- Ouvrir l'Espace Étudiant ENSAF ---
    elif ("espace etudiant" in data_btn or "espace étudiant" in data_btn or
          "ensaf etudiant" in data_btn or "ouvre espace etudiant" in data_btn):
        url = 'https://dws.ensaf.ac.ma/'
        webbrowser.get().open(url)
        msg = "L’Espace Étudiant de l’ENSAF est ouvert."
        speak.speak(msg)
        return msg

    # --- Ouvrir l'emploi du temps GI2 ---
    elif "emploi du temps gi2" in data_btn or "edt gi2" in data_btn or "info2" in data_btn:
        url = 'https://docs.ensaf.ac.ma/emplois/info2_05-11-2025.pdf'
        webbrowser.get().open(url)
        msg = "Voici l’emploi du temps de la filière Génie Informatique 2."
        speak.speak(msg)
        return msg

    # --- Météo ---
    elif 'weather' in data_btn or 'météo' in data_btn or 'meteo' in data_btn:
        ans = weather.Weather()
        speak.speak(ans)
        return ans

    
    # Exemple : "recherche recettes healthy"
    elif data_btn.startswith("recherche "):
        query = send[9:].strip()
        if query:
            url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
            webbrowser.open(url)
            msg = f"Je cherche « {query} » sur Google pour toi."
        else:
            msg = "Dis-moi ce que tu veux que je recherche."
        speak.speak(msg)
        return msg

    # --- TODO LIST : ajouter une tâche ---
    # Exemple : "todo: acheter des légumes"
    elif data_btn.startswith("todo:"):
        task = send[5:].strip()
        if task:
            todo_list.append(task)
            msg = f"Tâche ajoutée à ta liste : {task}"
        else:
            msg = "Je n'ai pas compris la tâche à ajouter."
        speak.speak(msg)
        return msg

    # --- TODO LIST : afficher les tâches ---
    elif ("liste des taches" in data_btn or "liste des tâches" in data_btn or
          "affiche mes taches" in data_btn):
        if not todo_list:
            msg = "Ta liste de tâches est vide pour le moment."
        else:
            numbered = [f"{i+1}. {t}" for i, t in enumerate(todo_list)]
            msg = "Voici ta liste de tâches : " + " | ".join(numbered)
        speak.speak(msg)
        return msg

    # --- TODO LIST : effacer toutes les tâches ---
    elif ("efface les taches" in data_btn or "efface les tâches" in data_btn or
          "reset todo" in data_btn):
        todo_list.clear()
        msg = "J'ai effacé toutes les tâches de ta liste."
        speak.speak(msg)
        return msg

    # --- Ouvrir WhatsApp Web ---
    elif "whatsapp" in data_btn or "whatsapp web" in data_btn:
        url = "https://web.whatsapp.com/"
        webbrowser.get().open(url)
        msg = "WhatsApp Web est ouvert."
        speak.speak(msg)
        return msg

    # --- Ouvrir Udemy ---
    elif "udemy" in data_btn:
        url = "https://www.udemy.com/"
        webbrowser.get().open(url)
        msg = "Udemy est ouvert."
        speak.speak(msg)
        return msg

    # --- Ouvrir Oracle ---
    elif "oracle" in data_btn:
        url = "https://www.oracle.com/"
        webbrowser.get().open(url)
        msg = "Le site d'Oracle est ouvert."
        speak.speak(msg)
        return msg

    # --- Ouvrir DataCamp ---
    elif "datacamp" in data_btn or "data camp" in data_btn:
        url = "https://www.datacamp.com/"
        webbrowser.get().open(url)
        msg = "DataCamp est ouvert."
        speak.speak(msg)
        return msg

    # --- Traduire une phrase en temps réel (ouvre Google Traduction) ---
    # Exemple : "traduis Bonjour comment ça va"
    elif data_btn.startswith("traduis "):
        text_to_translate = send.split(" ", 1)[1].strip()
        if text_to_translate:
            base_url = "https://translate.google.com/?sl=fr&tl=en&text="
            url = base_url + urllib.parse.quote(text_to_translate)
            webbrowser.open(url)
            msg = f"J’ouvre Google Traduction pour : {text_to_translate}"
        else:
            msg = "Dis-moi la phrase que tu veux traduire."
        speak.speak(msg)
        return msg

    # --- Calculatrice : effectuer des calculs simples ---
    # Exemple : "calc 2+3*5"
    elif data_btn.startswith("calc ") or data_btn.startswith("calcul "):
        expr = send.split(" ", 1)[1].strip()
        # on autorise seulement chiffres + opérateurs de base
        if not re.match(r"^[0-9\.\+\-\*\/\(\)\s%]+$", expr):
            msg = "Je peux seulement calculer des expressions simples avec des chiffres et + - * / %."
        else:
            try:
                result = eval(expr, {"__builtins__": None}, {"math": math})
                msg = f"Le résultat de ton calcul est : {result}"
            except Exception:
                msg = "Je n'ai pas réussi à calculer cette expression."
        speak.speak(msg)
        return msg

    # --- Conversions simples ---
    # Exemple : "convertis 10 km en miles"
    elif "convertis" in data_btn:
        text = data_btn

        # km -> miles
        m = re.search(r"convertis\s+([\d\.]+)\s*(km|kilometres|kilomètres)\s+en\s+(miles|mile)", text)
        if m:
            val = float(m.group(1))
            miles = val * 0.621371
            msg = f"{val} kilomètres valent environ {miles:.2f} miles."
            speak.speak(msg)
            return msg

        # kg -> livres
        m = re.search(r"convertis\s+([\d\.]+)\s*(kg|kilogrammes?)\s+en\s+(livres|lbs?)", text)
        if m:
            val = float(m.group(1))
            lbs = val * 2.20462
            msg = f"{val} kilogrammes valent environ {lbs:.2f} livres."
            speak.speak(msg)
            return msg

        # euros -> dirhams (taux approximatif)
        m = re.search(r"convertis\s+([\d\.]+)\s*(eur|€|euros?)\s+en\s+(mad|dh|dirhams?)", text)
        if m:
            val = float(m.group(1))
            mad = val * 10.8  # taux approximatif
            msg = f"{val} euros valent environ {mad:.2f} dirhams, taux approximatif."
            speak.speak(msg)
            return msg

        msg = "Je n'ai pas compris la conversion. Essaie par exemple : convertis 10 km en miles."
        speak.speak(msg)
        return msg

    # --- Recommandations films / séries / livres ---
    elif ("recommande" in data_btn and
          ("film" in data_btn or "série" in data_btn or "serie" in data_btn or "livre" in data_btn)):
        if "film" in data_btn or "films" in data_btn:
            reco = random.sample(films_reco, k=min(3, len(films_reco)))
            msg = "Je te recommande ces films : " + ", ".join(reco)
        elif "série" in data_btn or "serie" in data_btn:
            reco = random.sample(series_reco, k=min(3, len(series_reco)))
            msg = "Je te recommande ces séries : " + ", ".join(reco)
        else:
            reco = random.sample(livres_reco, k=min(3, len(livres_reco)))
            msg = "Je te recommande ces livres : " + ", ".join(reco)
        speak.speak(msg)
        return msg

    # --- Blagues ---
    elif "blague" in data_btn:
        joke = random.choice(jokes)
        speak.speak(joke)
        return joke

        # --- Ouvrir Gmail ---
    elif "gmail" in data_btn or "ouvre gmail" in data_btn or "mail google" in data_btn:
        url = "https://mail.google.com/"
        webbrowser.get().open(url)
        msg = "Gmail est ouvert."
        speak.speak(msg)
        return msg
        # --- Ouvrir Google Classroom ---
    elif "classroom" in data_btn or "google classroom" in data_btn or "ouvre classroom" in data_btn:
        url = "https://classroom.google.com/"
        webbrowser.get().open(url)
        msg = "Google Classroom est ouvert."
        speak.speak(msg)
        return msg
        # --- Ouvrir Google Maps ---
    elif "maps" in data_btn or "google maps" in data_btn or "ouvre maps" in data_btn or "carte google" in data_btn:
        url = "https://www.google.com/maps/"
        webbrowser.get().open(url)
        msg = "Google Maps est ouvert."
        speak.speak(msg)
        return msg
        # --- Ouvrir Word ---
    elif "word" in data_btn or "ouvre word" in data_btn:
        try:
            os.startfile("WINWORD.EXE")
            msg = "Microsoft Word est ouvert."
        except:
            msg = "Word n'est pas installé ou introuvable sur ton PC."
        speak.speak(msg)
        return msg
        # --- Ouvrir Excel ---
    elif "excel" in data_btn or "ouvre excel" in data_btn:
        try:
            os.startfile("EXCEL.EXE")
            msg = "Microsoft Excel est ouvert."
        except:
            msg = "Excel n'est pas installé ou introuvable sur ton PC."
        speak.speak(msg)
        return msg
        # --- Ouvrir ChatGPT ---
    elif "chatgpt" in data_btn or "ouvre chatgpt" in data_btn:
        url = "https://chat.openai.com/"
        webbrowser.get().open(url)
        msg = "ChatGPT est ouvert."
        speak.speak(msg)
        return msg
        # --- Ouvrir DeepSeek ---
    elif "deepseek" in data_btn or "ouvre deepseek" in data_btn:
        url = "https://chat.deepseek.com/"
        webbrowser.get().open(url)
        msg = "DeepSeek est ouvert."
        speak.speak(msg)
        return msg
        # --- Ouvrir GitHub ---
    elif "github" in data_btn or "ouvre github" in data_btn:
        url = "https://github.com/"
        webbrowser.get().open(url)
        msg = "GitHub est ouvert."
        speak.speak(msg)
        return msg
        # --- Ouvrir Claude ---
    elif "claude" in data_btn or "ouvre claude" in data_btn:
        url = "https://claude.ai/"
        webbrowser.get().open(url)
        msg = "Claude AI est ouvert."
        speak.speak(msg)
        return msg
        # --- Ouvrir Gemini ---
    elif "gemini" in data_btn or "ouvre gemini" in data_btn:
        url = "https://gemini.google.com/"
        webbrowser.get().open(url)
        msg = "Google Gemini est ouvert."
        speak.speak(msg)
        return msg
        # --- Ouvrir PowerPoint ---
    elif "powerpoint" in data_btn or "ouvre powerpoint" in data_btn or "ppt" in data_btn:
        try:
            os.startfile("POWERPNT.EXE")
            msg = "PowerPoint est ouvert."
        except:
            msg = "PowerPoint n'est pas installé ou introuvable."
        speak.speak(msg)
        return msg
        # --- Ouvrir VS Code ---
    elif "vs code" in data_btn or "vscode" in data_btn or "ouvre vs code" in data_btn:
        try:
            os.startfile(r"C:\Users\pc\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            msg = "VS Code est ouvert."
        except:
            msg = "Impossible d’ouvrir VS Code, vérifie le chemin d’installation."
        speak.speak(msg)
        return msg

        # --- Ouvrir Eclipse ---
    elif "eclipse" in data_btn or "ouvre eclipse" in data_btn:
        try:
            os.startfile(r"C:\eclipse\eclipse.exe")
            msg = "Eclipse est ouvert."
        except:
            msg = "Eclipse n’est pas trouvé. Il faut vérifier son chemin."
        speak.speak(msg)
        return msg  
        # --- Ouvrir Canva ---
    elif "canva" in data_btn or "ouvre canva" in data_btn:
        url = "https://www.canva.com/"
        webbrowser.get().open(url)
        msg = "Canva est ouvert."
        speak.speak(msg)
        return msg
        # --- Ouvrir Netflix ---
    elif "netflix" in data_btn or "ouvre netflix" in data_btn or "lance netflix" in data_btn:
        url = "https://www.netflix.com/"
        webbrowser.get().open(url)
        msg = "Netflix est ouvert."
        speak.speak(msg)
        return msg
        # --- Ouvrir Bloc-notes (Notepad) ---
    elif "bloc note" in data_btn or "bloc-notes" in data_btn or "notepad" in data_btn or "ouvre bloc note" in data_btn:
        try:
            os.startfile("notepad.exe")
            msg = "Bloc-notes est ouvert."
        except:
            msg = "Impossible d’ouvrir le Bloc-notes."
        speak.speak(msg)
        return msg
        # --- Ouvrir l'outil de capture d’écran (Snipping Tool) ---
    elif "capture" in data_btn or "capture d'écran" in data_btn or "snipping tool" in data_btn or "outil capture" in data_btn:
        try:
            os.startfile("SnippingTool.exe")
            msg = "L’outil de capture d’écran est ouvert."
        except:
            msg = "Impossible d’ouvrir l’outil de capture d’écran."
        speak.speak(msg)
        return msg
    # --- Histoires ---
    elif "histoire" or "story" in data_btn:
        story = random.choice(histoires)
        speak.speak(story)
        return story
    
    # --- Réponse par défaut ---
    else:
        msg = "Je n'ai pas compris, peux-tu reformuler ?"
        speak.speak(msg)
        return msg
