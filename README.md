# pywebview-Frameless-boilerplate (Updated)

***  New Update ***

Install:<br>
- req: Python install on the system<br>
- cmd: from Commands.txt cmd the 3 lines to open local python env and pip pywebview into it<br>
- VS code: open the folder on vs code or any other IDE and run main.py<br>

App pipe line:<br>
- main.py will import the files from AppComponents.<br>
- mr_importer will import the list it holds.<br>
- mr_windowinfo is our window object class and we push data into it immediately.<br>
- mr_API holds our API class and handlers. it will also hold the "start window" process.<br>
- the app will start. build window object. call the API to start window and when dom ready function was trigger it will write the window data and handlers<br>

Added:
- Tailwind. use any tailwind syntax.
- Alpine js. call alpine as you wish.
- HTMX. Get/Post/Put into local divs with core header protection
- Lottie Player with some Demos
- All libs are now Python native libs you only need to pip pywebview.
- Renew the Top bar with more space for logo and controls. added light/dark / Mono.
- moved Resize Function to a border on the right bottom and left sides.
- Re-path all pywebview Elements into more modular code (main file import the API and any other part).
- imports from the list. you can now control imports by simply adding them to the mr_importer.py list. (you still need to pip them to the local env).
- window info class added to store app data like name\ver\logo\window handler (allow pass and control all window elements to the API).
- mr_API.py hold the API class and window start commands.
- mr_logger control app bug logs to files.
- Many New Demos and Showcase on how to control HTML with Python. how to hook functions and control UI and DATA.
- Easy Settings. you got Everything waiting for ya on the main.py file. (debug, sizes, logo ..)
- speed improved by around 28-41% for start-up. all memory leaks were removed.
- full Events functions hooked to the base. (on load / on exit / on dom ready ...)
- Added Framework Buy button (optional: allow you to buy the original template and src) 

Image1:

![python_hU91d2Sdd3](https://github.com/DizzyduckAR/pywebview-Frameless-boilerplate/assets/52171360/423dcfa4-3bbd-42a0-be6c-53662d5711bc)

Image2:

![python_gEZJlVbE4W](https://github.com/DizzyduckAR/pywebview-Frameless-boilerplate/assets/52171360/cf3b1218-9d27-429f-a99f-d6f86d6b9502)


Gifs:

*Demo python to HTML

![python_9jMCm9Wy1d](https://github.com/DizzyduckAR/pywebview-Frameless-boilerplate/assets/52171360/1d14a86a-6ff2-4c83-9783-8d7414d0bfeb)

*Demo2

![python_ZpNnjIr39K](https://github.com/DizzyduckAR/pywebview-Frameless-boilerplate/assets/52171360/7da0301f-b8e2-4502-9ac7-ddc4244da6bc)


























*******************************  old ***************************************************************
*Added On top auto False after UI show (3 secs timeout). also Demo "on show" Function and call.<br>
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


Resize Function allows resizing of frameless window<br>
![Resize](https://user-images.githubusercontent.com/52171360/123539368-4437cc00-d6ee-11eb-9a66-0f7e0c3a5a41.png)<br>

Minimal imports allow very low size EXE Build<br>
import webview<br>
import webbrowser<br>
import win32api<br>
import pyautogui<br>
import time<br>
import sys<br>


One Click Batch file:<br>
Req- python, python venv

Self-deploy and pip all requirements into local venv.<br>

```
python -m venv env
CALL env\Scripts\activate.bat
pip install -r requirements.txt
```

Html Folder Hold:<br>
Blank.html (main HTML)
CSS files
JS Files
image Files

MIT on each file.
sparkly credits for all the open-source projects are under work :D
