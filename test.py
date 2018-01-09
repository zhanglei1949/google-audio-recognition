import speech_recognition as sr
import wave
import argparse
r = sr.Recognizer()

parser = argparse.ArgumentParser(description=None)
parser.add_argument('--in', type=str,dest="input",required=True, help="the file you want to be recognized.")
#audio = wave.open(wave_file, 'r')
args = parser.parse_args()
with sr.AudioFile(args.input) as source:
	audio = r.record(source)

try:
	print("Predicted: "+ r.recognize_google(audio))
except sr.UnknownValueError:
	print("Could not understand")
except sr.RequestError as e:
	print("Reuqest error {0}".format(e))
