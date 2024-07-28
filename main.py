from functions import getlocation,getipaddress,getweather
import pyttsx3
import speech_recognition as sr
import re
# Initialize text-to-speech engine
engine = pyttsx3.init()


def main():
    while True:
        global start
        
        if start==0:
            ipaddress = getipaddress.get_ip_address()
            location = getlocation.get_location_from_ip(ipaddress)
            weather_info = getweather.get_weather(location["city"])
            greeting = f"Hello! this is Orion. {weather_info} so i am setting your air condition accordingly. you can modify any time."
            greeting = "hello this is orion have a great ride. im exited to assist you during the ride."
            engine.say(greeting)
            engine.runAndWait()
            start=1
            recognizer = sr.Recognizer()
            microphone = sr.Microphone() 
            with microphone as source:
                # print("Adjusting for ambient noise...")
                recognizer.adjust_for_ambient_noise(source)
                
                while True:
                    try:
                        print("Listening...")
                        audio = recognizer.listen(source)
                        # print("Recognizing...")
                        text = recognizer.recognize_google(audio)
                        print(text)
                        if "hey orion" in text.lower() or "hey aryan" in text.lower():
                            if "set the temperature" in text.lower():
                                numbers = re.findall(r'\d+', text)
                                engine.say(f"ok setting the temperature to {numbers[0]} degrees")
                                engine.runAndWait()
                    except sr.UnknownValueError:
                        pass
                        # print("Google Speech Recognition could not understand the audio")
                    except sr.RequestError as e:
                        pass
                        # print(f"Could not request results from Google Speech Recognition service; {e}")
                    except Exception as e:
                        pass
                        # print(f"An unexpected error occurred: {e}")
                
            
        
        
        
if __name__ == "__main__":
    start = 0
    main()