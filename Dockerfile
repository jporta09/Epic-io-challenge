FROM conda/miniconda3

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN conda update -n base -c defaults conda &&\
    conda install numpy &&\
    conda install -c conda-forge opencv

COPY ./service ./service

ENTRYPOINT ["python", "./service/VideoTracker.py"]

