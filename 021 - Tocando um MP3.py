#CRIE UM PROGRAMA Q REPRODUZA UM ARQUIVO AUDIO
from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('Agora você escuta')
