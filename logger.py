import logging

## logging config parameters
LOG_FILE:str = "./logs/app.log"
LOG_FORMAT:str = '%(name)s - %(levelname)s - %(message)s'

## configure logging
logging.basicConfig(
        filename = LOG_FILE, 
        filemode = 'w', 
        level=logging.DEBUG
        )
