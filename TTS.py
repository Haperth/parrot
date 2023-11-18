import subprocess
import shlex

speakers = {}

speakers['parrot'] = "mimic3 --remote --length-scale 1 --voice en_US/vctk_low#s5 $text"
speakers['britman'] = "mimic3 --remote --length-scale 1.2 $text"
speakers['usaman'] = "mimic3 --remote --length-scale 1.2 --voice en_US/cmu-arctic_low#awb $text"

class TTS():

    #def __init__(self):
    # TODO start server

    def speak(self, speaker, text):
        cmd = speakers[speaker]
        cmd = cmd.replace('$text', shlex.quote(text))
        #print(cmd)
        subprocess.run(cmd, shell=True)

    def quit(self):
        # TODO send msg to server to exit
        print("done")

def main():
    # TODO start server
    tts = TTS()
    tts.speak('parrot', "Hello I am here to annoy you.")
    tts.quit()


if __name__ == "__main__":
    main()

