# tf2-ml-study

**tf2-ml-study** is a web application that apply the machine learning study result of [TensorFlow](https://www.tensorflow.org/)

### Prerequisite

1. Flask with python3
2. TensorFlow

### Environment setup

- Install anaconda from [anaconda](https://docs.anaconda.com/anaconda/install/)

- Create conda environment

```shell script
conda create -n <envname>
conda activate <envname>
pip install -r ~/tf-ml-study/requirements.txt
```

- ML Model Preparation
```shell script
for Linux, MAC -> go to directory bin and run ./create_model.sh
for Windows -> go to directory bin and run create_model.bat
```

- Start the Server

```shell script
for Linux, MAC -> go to directory bin and run ./start_app.sh
for Windows -> go to directory bin and run start_app.bat
```

**Flower Classification**
<img width="960" alt="flower_site" src="https://user-images.githubusercontent.com/57161225/110586057-e91cb080-81b4-11eb-8b49-037894e2ba9e.PNG">
