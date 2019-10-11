# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                       Chapter 45    Containers and Google Kubernetes Engine
# 
# 
# 
# 
# Figure 45-4. Containers
# 
# W
#  orking with Docker
# Google Cloud Shell comes pre-configured with Docker.
#    Key concepts to note are
# 
#       •   Dockerfile: A Dockerfile is a text file that specifies how an image will
#           be created.
# 
#       •   Docker images: Images are created by building a Dockerfile.
# 
#       •   Docker containers: Docker containers are the running instance of an
#           image.
#    The diagram in Figure 45-5 highlights the process to build an image and run a
# Docker container.
# 
# 
# 
# 
#                                                                                        659
# 
# Chapter 45    Containers and Google Kubernetes Engine
# 
# 
# 
# 
# Figure 45-5. Steps to deploying a Docker container
# 
#       Table 45-1 shows key commands when creating a Dockerfile.
# 
# 
# Table 45-1. Commands for Creating Dockerfiles
# Command            Description
# 
# FROM               The base Docker image for the Dockerfile.
# LABEL              Key-value pair for specifying image metadata.
# RUN                It executes commands on top of the current image as new layers.
# COPY               Copies files from the local machine to the container file system.
# EXPOSE             Exposes runtime ports for the Docker container.
# CMD                Specifies the command to execute when running the container. This command
#                    is overridden if another command is specified at runtime.
# ENTRYPOINT         Specifies the command to execute when running the container. Entrypoint
#                    commands are not overridden by a command specified at runtime.
# WORKDIR            Set working directory of the container.
# VOLUME             Mount a volume from the local machine file system to the Docker container.
# ARG                Set Environment variable as a key-value pair when building the image.
# ENV                Set Environment variable as a key-value pair that will be available in the
#                    container after building.
# 
# 
# 
# 
# 660
# 
#                                       Chapter 45   Containers and Google Kubernetes Engine
# 
# 
# Build and Run a Simple Docker Container
# Clone the book repository to run this example in Cloud Shell; we have a bash script titled
# date-script.sh in the chapter folder. The script assigns the current date to a variable and
# then prints out the date to the console. The Dockerfile will copy the script from the local
# machine to the docker container file system and execute the shell script when running the
# container. The Dockerfile to build the container is stored in docker-intro/hello-­world.
# 
# # navigate to the folder with images
# cd docker-intro/hello-world
# 
#    Let’s view the bash script.
# 
# cat date-script.sh
# 
# #! /bin/sh
# DATE="$(date)"
# echo "Todays date is $DATE"
# 
#    Let’s view the Dockerfile.
# 
# # view the Dockerfile
# cat Dockerfile
# 
# # base image for building container
# FROM docker.io/alpine
# # add maintainer label
# LABEL maintainer="dvdbisong@gmail.com"
# # copy script from local machine to container file system
# COPY date-script.sh /date-script.sh
# # execute script
# CMD sh date-script.sh
# 
#    The Docker image will be built off the Alpine Linux package. See https://hub.
# docker.com/_/alpine. The CMD routine executes the script when the container runs.
# 
# B
#  uild the Image
# Run the following command to build the Docker image.
# 
# # build the image
# docker build -t ekababisong.org/first_image .
#                                                                                         661
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__("Working with Docker")
        self.add(MarkdownBlock("# Working with Docker"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Workingwith(HierNode):
    def __init__(self):
        super().__init__("Working with Docker")
        self.add(Content())

# eof
