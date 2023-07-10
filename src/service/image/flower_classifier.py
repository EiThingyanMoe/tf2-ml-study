import io
import os
import traceback
from logging import Logger

import numpy as np
import tensorflow as tf
from PIL import Image
from keras.models import load_model
from keras.preprocessing import image
from werkzeug.datastructures import FileStorage

from common.logger import get_common_logger


class FlowerClassifier:
    def __init__(self, conf: dict, logger: Logger=None) -> None:
        if logger is None:
            logger = get_common_logger(__name__)
        self.logger = logger
        self.DIR = os.path.join(os.path.dirname(__file__), "../../../")
        self.IMAGE_SIZE = (224, 224)
        self.FLOWER_MODEL_PATH = os.path.join(self.DIR, conf["common"]["saved_models"]["flower_model"]["model_path"])
        self.FLOWER_TYPES = conf["common"]["saved_models"]["flower_model"]["flower_types"]
        self.saved_model = load_model(self.FLOWER_MODEL_PATH)
        self.ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]

    def is_allowed_file(self, filename: str) -> bool:
        """
        is file is allowed image file
        :param filename:
        :return:
        """
        return '.' in filename and filename.split(".")[-1].lower() in self.ALLOWED_EXTENSIONS

    def predict_flower(self, flower_image: FileStorage) -> str:
        """
        predict flower based on saved model using bilinear (244, 244) images
        :param flower_image:
        :return:
        """
        # convert FileStorage to Image
        flower_image = Image.open(io.BytesIO(flower_image.read()))
        # to synchronize Image mode to 3 channels RGB
        if flower_image.mode != "RGB":
            # to solve tensorflow.python.framework.errors_impl.InvalidArgumentError:
            # input depth must be evenly divisible by filter depth: 2 vs 3
            flower_image.convert("RGB")
        # resize Image to (244, 244) as saved model
        flower_image = flower_image.resize(size=self.IMAGE_SIZE, resample=Image.BILINEAR)
        # convert Image to array and convert to 2D (normalize RGB pixels by /255.0)
        flower_image = image.img_to_array(flower_image)/255.0
        # expand the validation image to (1, 224, 224, 3) before predicting the label
        flower_image = np.expand_dims(flower_image, axis=0)
        try:
            prediction_scores = self.saved_model.predict(flower_image)
            predicted_index = np.argmax(prediction_scores)
            return self.FLOWER_TYPES.get(predicted_index, "Cannot Predict!")
        except (ValueError, tf.errors.InvalidArgumentError):
            self.logger.error("Cannot predict image. error %s", traceback.format_exc())
            return "Cannot Predict!"
