from Core.Journal import Journal
import sys
import os

sys.path.append(f"{os.path.dirname(os.path.abspath(__file__))}\\Commands")
sys.path.append(f"{os.path.dirname(os.path.abspath(__file__))}\\Core")
sys.path.append(f"{os.path.dirname(os.path.abspath(__file__))}\\Transfer")

from Core.Presenter import Presenter
from Core.ViewConsole import ViewConsole

if __name__ == "__main__":
    app = Presenter(Journal(), ViewConsole())
    app .run()
