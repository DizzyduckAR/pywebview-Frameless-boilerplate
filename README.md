# pywebview-Frameless-boilerplate (Updated)

hotfix:
- added html particles
- added window drag to top window div
- HTML parts sit in AppComponents/HtmlParticles/

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



















MIT on each file.
sparkly credits for all the open-source projects are under work :D
