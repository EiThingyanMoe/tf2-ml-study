from flask import Flask

from common.config import load_config, Config, load_log_conf
from controller import manage
from service.image.flower_classifier import FlowerClassifier

app = Flask(__name__)
app.register_blueprint(manage.manage)

app.config.from_object(Config)
# upload limit of 10 megabytes
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

conf = load_config()
load_log_conf(conf)

flower_classifier: FlowerClassifier = FlowerClassifier(conf, app.logger)

manage.flower_classifier = flower_classifier

if __name__ == "__main__":
    try:
        app.run(host=conf["common"]["server"]["host"], port=conf["common"]["server"]["port"], threaded=True)
    finally:
        pass
