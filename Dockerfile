ARG NAME="Au-Zone Technologies"
ARG EMAIL=support@au-zone.com
ARG USER=au-zone
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG BUILD_NUMBER=0

FROM ros:humble AS builder
ARG USER
ARG USER_UID
ARG USER_GID
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y \
    qemu-user-static \
    sudo \
    curl \
    python3-pip \
    python3-bloom \
    python3-rosdep \
    libclang-dev \
    fakeroot \
    debhelper \
    devscripts \
    dh-python

RUN groupadd --gid $USER_GID $USER && \
    useradd --uid $USER_UID --gid $USER_GID -m $USER
RUN echo $USER ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USER && \
    chmod 0440 /etc/sudoers.d/$USER
RUN echo 'source /opt/ros/humble/setup.bash' >> /home/$USER/.bashrc

USER $USER
SHELL ["/bin/bash", "-l", "-c"]

FROM builder AS debian
ARG BUILD_NUMBER
ARG NAME
ARG EMAIL
ARG USER

ENV NAME=$NAME
ENV EMAIL=$EMAIL
ENV BUILD_NUMBER=$BUILD_NUMBER

WORKDIR /home/$USER/schemas
COPY --chown=$USER . .
WORKDIR /home/$USER/schemas/edgefirst_msgs

RUN fakeroot debian/rules version
RUN fakeroot debian/rules binary

WORKDIR /home/$USER/schemas

FROM builder

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y

CMD ["/bin/bash"]