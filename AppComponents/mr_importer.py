from AppComponents.mr_logger import logger

# list to import
importerlist=[
    "webview",
    "time","sys"
    
]

# Import From list importerlist  auto fail safe with logs for unsupported imports
for myimport in importerlist:
    try:
        #add imports from list and Error out to log if fail
        globals()[myimport] = __import__(myimport)
    except Exception as e:
        logger.error(e)
        


