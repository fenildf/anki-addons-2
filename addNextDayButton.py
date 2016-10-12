# import the main window object from aqt
from aqt.reviewer import Reviewer
from aqt.utils import showInfo
from anki.hooks import wrap

def buttonPressed(self):
  showInfo("pressed" + `self`)

def mySetupButtons(self):
  self._addButton("myButton", lambda s=self buttonPressed(self), text="pressMe", size=False)

Reviewer.setupButtons = wrap(Reviewer.setupButtons, mySetupButtons)
