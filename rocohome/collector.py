import logging

logger = logging.getLogger(__name__)


class Collector:
    def __init__(self, event_table):
        self.accounts = {}
        self.event_table = event_table

    def record_event(self, event):
        """Insert an event into the database."""

        encoded_event = event.encode()
        logger.info('recording event: %s' % encoded_event)
        self.event_table.put_item(Item=encoded_event)
