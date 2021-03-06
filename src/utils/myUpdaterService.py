import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
def formatMessage(text, argsList=[]):
    if isinstance(argsList, list):
        return text.format(*argsList)
    else:
        return text.format(argsList)
class myUpdaterService:
    logger = logging.getLogger(__name__)

    def sendMessage(self,update, msg, args=[], options={}):
        formattedMsg=formatMessage(msg, args)
        if options.get('quote', False):
            update.message.reply_text(formattedMsg,quote=True)
        elif options.get('parse_mode', '')=='HTML':
            update.message.reply_text(formattedMsg, parse_mode='HTML')
        else:
            update.message.reply_text(formattedMsg)
        self.logger.info(formattedMsg)

    def log(self, msg, args=[]):
        formattedMsg=formatMessage(msg, args)
        self.logger.info(formattedMsg)
