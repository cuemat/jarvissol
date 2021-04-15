import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init()  # to call the initial function


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishme():
    speak("Hello student, Wellcome back")
    speak("Jarvis at your service, please let me know how can I help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.record(source, duration=8)
        print(source)

    try:
        print("recognizing...")
        query = r.recognize(audio)
        print(f"you said {query}")
    except Exception as e:
        print(e)
        speak("I didn't quite understand, say that again please!")
        return "None"

    return query


def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    print(op1,op2)
    print(oper)
    if oper == "+":
        speak(f"The answer is {op1+op2}")
    elif oper == "-":
        speak(f"The answer is {op1-op2}")
    elif oper =="x" or "X":
        speak(f"The answer is {op1*op2}")
    elif oper == "Divided" or "divided":
        speak(f"The answer is {op1/op2}")



if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
  

        elif "solve" in query:
            speak("Please tell me the math problem you want me to solve, please try saying 3 plus 3")
            prob = takecommand()
            print(f"you said {prob.split()}")
            eval_binary_expr(*(prob.split()))


        elif "offline" in query:
            speak("I am glad to be of your service, take care")
            quit()


