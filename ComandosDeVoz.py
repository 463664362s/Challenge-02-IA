import speech_recognition as sr
import pyttsx3, speech_recognition as sr
import pyttsx3

en = pyttsx3.init()

en.setProperty('rate', 150)
en.setProperty('volume', 2)
en.setProperty('voice', voices[0].id)

msg = "Seja Bem vindo ao nosso programa de acessibilidade!" 

en.say(msg)
en.runAndWait()

engine = pyttsx3.init()

voices = engine.getProperty("voices") 
engine.setProperty('voice', voices[0].id)
engine.setProperty('volume', 1)
engine.setProperty("rate", 155)

engine.runAndWait() 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n  Listening...\n")
        speak('ouvindo.')
        r.adjust_for_ambient_noise = 1.25
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("  Recognizing...\n")
        speak('Reconhecendo.')
        query = r.recognize_google(audio, language='pt')
    except:
        return "©empty_^_^_queryª"
    return query



speak("Como posso ajudar hoje?")
if __name__ == "__main__":
    while True:

        query = command().lower()
        if '1' in query or 'configuração' in query:
            print("opção: 1, Configuração")
            speak("você escolheu a opção numero 1")
            
        elif '2' in query or 'menu' in query:
            print("opção: 2, Menu Principal")
            speak('você escolheu a opção numero 2')
            
        elif '3' in query  or 'link' in query:
            print("opção: 3, Link")
            speak("você escolheu a opção numero 3")
            
        elif '4'in query  or 'departamento' in query:
            print("opção: 4, Departamento")
            speak("você escolheu a opção numero 4") 
            
        elif 'fim' in query or 'sair' in query : 
            print("Saindo...")
            speak("Obrigado, até a próxima")
            break
  

        else:

            print("opção invalida")
            speak('não entendi o que você disse.')
            speak("Por favor, vamos tentar novamente. escolha uma opção válida.")