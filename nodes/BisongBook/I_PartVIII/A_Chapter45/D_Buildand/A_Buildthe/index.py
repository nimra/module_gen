# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
# Chapter 45    Containers and Google Kubernetes Engine
# 
#       Build output
# 
# Sending build context to Docker daemon  2.048kB
# Step 1/4 : FROM docker.io/alpine
# latest: Pulling from library/alpine
# 6c40cc604d8e: Pull complete
# Digest: sha256:b3dbf31b77fd99d9c08f780ce6f5282aba076d70a513a8be859d8d3a4d0c92b8
# Status: Downloaded newer image for alpine:latest
#  ---> caf27325b298
# Step 2/4 : LABEL maintainer="dvdbisong@gmail.com"
#  ---> Running in 306600656ab4
# Removing intermediate container 306600656ab4
#  ---> 33beb1ebcb3c
# Step 3/4 : COPY date-script.sh /date-script.sh
#  ---> Running in 688dc55c502a
# Removing intermediate container 688dc55c502a
#  ---> dfd6517a0635
# Step 4/4 : CMD sh date-script.sh
#  ---> Running in eb80136161fe
# Removing intermediate container eb80136161fe
#  ---> e97c75dcc5ba
# Successfully built e97c75dcc5ba
# Successfully tagged ekababisong.org/first_image:latest
# 
# 
# Run the Container
# Execute the following command to run the Docker container.
# 
# # show the images on the image
# docker images
# 
# # run the docker container from the image
# docker run ekababisong.org/first_image
# 
# Todays date is Sun Feb 24 04:45:08 UTC 2019
# 
# 
# 
# 
# 662
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Build the Image",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Build the Image"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Buildthe(HierNode):
    def __init__(self):
        super().__init__("Build the Image")
        self.add(Content())

# eof
