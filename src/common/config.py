
import logging.config
import os

import yaml

current_dir = os.path.join(os.path.dirname(__file__), "../../conf/")


class Config(object):
    """
    app setting config
    """
    SECRET_KEY = os.urandom(12).hex()
    JSON_AS_ASCII = False


def merge_dicts(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return dict2
    for data in dict2:
        dict1[data] = merge_dicts(dict1[data], dict2[data]) if data in dict1 else dict2[data]
    return dict1


def load_yaml(file_path: str) -> dict:
    try:
        with open(os.path.join(current_dir, file_path), "r", encoding="utf-8") as conf_f:
            conf = yaml.safe_load(conf_f)
        return conf
    except FileNotFoundError:
        raise Exception("app conf load error")


def load_log_conf(log_conf: dict):
    """
    load logging conf for app
    :param log_conf:
    :return:
    """
    os.makedirs(os.path.dirname(log_conf["common"]["log"]["app"]), exist_ok=True)
    logging.config.dictConfig(load_yaml(log_conf["common"]["log"]["conf"]))


def load_config() -> dict:
    """
    load conf based on environment
    :return:
    """
    env = "dev"
    if os.environ.get("SCRIPT_ENV") == "production":
        env = "prod"
    return merge_dicts(load_yaml("config.yaml"), load_yaml("config_{}.yaml".format(env)))
