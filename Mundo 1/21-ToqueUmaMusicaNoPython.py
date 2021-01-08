from pygame import mixer
mixer.init()
mixer.music.load('oh-no-no-no-no-laugh.mp3')
mixer.music.play()
while (mixer.music.get_busy()):pass
