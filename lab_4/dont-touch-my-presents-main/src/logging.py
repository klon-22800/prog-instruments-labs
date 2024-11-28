import logging

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('lab_4\\dont-touch-my-presents-main\\info.log'),
    ]
)


logger = logging.getLogger('base_logger')
score_logger = logging.getLogger('score_logger')



debug_logger = logging.getLogger('debug_logger')
debug_logger.setLevel(logging.DEBUG) 

debug_handler = logging.FileHandler('lab_4\\dont-touch-my-presents-main\\debug.log')
debug_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
debug_logger.addHandler(debug_handler)
debug_logger.propagate = False