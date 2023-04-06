from TkWindow import GameWindows,Menu
import os, sys
import cProfile

import pyximport
pyximport.install()

import c_hangman

""" bu program python 3.10.x için uyumludur ve Linux dosya yapısına uygun yazılmıştır"""

assert sys.version_info > (3,10), "python sürümünüzü güncelleyin"

if __name__ == "__main__":
    game = GameWindows()
    Menu(game)
    game.mainloop()
    cProfile.runctx("game.mainloop()", globals(), locals(), "Profile.prof")
    
