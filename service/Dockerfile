FROM conda/miniconda3

RUN conda install numpy
RUN conda install -c conda-forge opencv

COPY VideoTracker.py /

ENTRYPOINT ["python", "./VideoTracker.py"]
