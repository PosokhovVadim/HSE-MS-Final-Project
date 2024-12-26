import yaml
import logging


class Config:
    def __init__(self, config_path, log: logging.Logger):
        self.config = self.readConfig(config_path,log)
        self.service_name = self.config["service_name"]
        self.host = self.config["http_server"]["host"]
        self.port = self.config["http_server"]["port"]

    def readConfig(self, config_path, log: logging.Logger):
        try:
            with open(config_path, "r") as config_file:
                log.info("Reading config file successfully")
                return yaml.safe_load(config_file)
        except IOError:
            log.error("Config file not found")
            raise IOError
