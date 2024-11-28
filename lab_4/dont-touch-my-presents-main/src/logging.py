import logging

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('lab_4\\dont-touch-my-presents-main\\app.log'),
    ]
)


logger = logging.getLogger('base_logger')
score_logger = logging.getLogger('score_logger')
