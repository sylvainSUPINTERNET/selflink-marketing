import logging


LOG = logging.basicConfig(format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s', level=logging.INFO)
LOG = logging.getLogger(__name__)