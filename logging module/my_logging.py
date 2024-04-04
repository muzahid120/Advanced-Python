import logging
log_formate='%(lineno)d***%(asctime)s *** %(levelname)s *** %(message)s'

logging.basicConfig(filename='app.log', level=logging.DEBUG, format=log_formate,filemode='w')
logger=logging.getLogger('memory')

logger.warning('This most dificult virus on the earth ! Stay Safe !')
logger.debug('debug is done ')
logger.critical('their is no critical')
logger.info('programer skm')
logger.error('there are some error occured ')