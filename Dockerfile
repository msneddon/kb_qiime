FROM kbase/kbase:sdkbase.latest
MAINTAINER Michael Sneddon (mwsneddon@lbl.gov)


# set the working directory to the KB area
WORKDIR /kb/module

# install system library dependencies
RUN apt-get update

RUN apt-get -y install pkg-config libpng-dev libfreetype6-dev
RUN apt-get -y install libopenblas-base libopenblas-dev libatlas-base-dev gfortran libblas-dev liblapack-dev mklibs
RUN apt-get -y install libhdf5-dev

RUN pip install numpy
RUN pip install h5py

# install QIIME
RUN pip install -U qiime

# setup the QIIME config file specifying the temporary directory
RUN echo "temp_dir /kb/module/work/tmp/qiime_scratch/" > /kb/module/qiime_config
RUN mkdir -p /kb/module/work/tmp/qiime_scratch
ENV QIIME_CONFIG_FP /kb/module/qiime_config

# check installation
RUN print_qiime_config.py -t

# copy module files
COPY ./ /kb/module
RUN mkdir -p /kb/module/work

# build the KBase SDK module
RUN make

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
