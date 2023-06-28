import logging
import os

# check if logs folder exist else make folder
if not os.path.isdir("logs"):
    os.mkdir("logs")

# write log file to local system + Format options
logging.basicConfig(filename='logs/logfile.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

