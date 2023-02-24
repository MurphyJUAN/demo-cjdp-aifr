# dockerfile template
#
# VERSION               0.0.1

FROM      ubuntu:16.04
LABEL     maintainer="allen7575@gmail.com"

##
## Ubuntu - Packages - Search
## https://packages.ubuntu.com/search?suite=xenial&section=all&arch=amd64&searchon=contents&keywords=Search
##

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

############
# update package list
############
#RUN apt update

##############################
#########################
## install packages
#########################
##############################

############
# put something here...
############

# RUN apt update && \
#     apt install -y python3 python3-pip && \
#     apt-get autoremove -y && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# COPY ./requirements.txt /backend/

# RUN cd /backend && \
#     pip3 install -r requirements.txt



RUN apt update && \
    apt install -y curl && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt update && \
    apt install -y nodejs && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*



##########
# install vim
##########
# RUN apt install -y vim

##############################
#########################
## modify configuration
#########################
##############################

############
# put something here...
############

############
# add, change username,password,group here
############
# change root password
# RUN echo root:root | chpasswd

# add guest user
# useradd - Ubuntu 14.04: New user created from command line has missing features - Ask Ubuntu
# https://askubuntu.com/questions/643411/ubuntu-14-04-new-user-created-from-command-line-has-missing-features
# RUN useradd -m guest -s /bin/bash && \
#     echo guest:guest | chpasswd

# grant access for guest to video device
# RUN usermod -a -G video guest `# grant access to video device`

##############################
#########################
## cleanup image
#########################
##############################

##############
# upgrade
##############
# RUN apt upgrade -y

##############
# cleanup
##############
# debian - clear apt-get list - Unix & Linux Stack Exchange
# https://unix.stackexchange.com/questions/217369/clear-apt-get-list
#
# bash - autoremove option doesn't work with apt alias - Ask Ubuntu
# https://askubuntu.com/questions/573624/autoremove-option-doesnt-work-with-apt-alias
#
# RUN apt-get autoremove && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

##############################
#########################
## run commands when image start
#########################
##############################

#################
# initial script
#################

# ADD ./scripts/* /scripts/

# starting container process caused "exec: \"./extra/service_startup.sh\": permission denied" · Issue #431 · facebook/fbctf
# https://github.com/facebook/fbctf/issues/431
#RUN chmod +x /scripts/*



#ENTRYPOINT ["python3", "/backend/api.py"]

COPY . /frontend

# RUN chmod +x -R /frontend

WORKDIR /frontend

RUN npm install


EXPOSE 8080

CMD ["npm", "run", "dev"]
