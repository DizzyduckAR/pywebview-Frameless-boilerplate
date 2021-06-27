# pywebview-Frameless-boilerplate

*added On top auto False after UI show (3 secs timeout). also Demo "onshow" Function and call.
*Bootstrap already hooked.


Based on:
https://github.com/r0x0r/pywebview

Ready To Go Pywebview Frameless Window with all the window handlers.

App Window Default<br>
![blank](https://user-images.githubusercontent.com/52171360/123539355-35511980-d6ee-11eb-97a0-3fb9fbbfec6c.png)


Title<br>
![title](https://user-images.githubusercontent.com/52171360/123539360-3aae6400-d6ee-11eb-9d27-dec7f408e762.png)


Minimize Window<br>
Full Screen<br>
Close window<br>
custom make icons (site href ..)<br>
![handler](https://user-images.githubusercontent.com/52171360/123539365-413cdb80-d6ee-11eb-9f9c-3b3a6fc98d56.png)


Resize Function allow resize of frameless window<br>
![Resize](https://user-images.githubusercontent.com/52171360/123539368-4437cc00-d6ee-11eb-9a66-0f7e0c3a5a41.png)<br>

Minimal imports allow very low size EXE Build<br>
import webview<br>
import webbrowser<br>
import win32api<br>
import pyautogui<br>
import time<br>
import sys<br>


One Click Batch file:<br>
Req- python , python venv

Self deploy and pip all requirements into local venv.<br>

```
python -m venv env
CALL env\Scripts\activate.bat
pip install -r requirements.txt
```

Html Folder Hold:<br>
Blank.html (main html)
CSS files
JS Files
image Files
