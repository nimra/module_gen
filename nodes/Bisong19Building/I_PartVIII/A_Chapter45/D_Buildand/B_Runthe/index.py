# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
#                                       Chapter 45     Containers and Google Kubernetes Engine
# 
# Important Docker Commands
# In this section, let’s review some important Docker commands.
# 
# Commands for Managing Images
# Table 45-2 contains commands for managing Docker images.
# 
# Table 45-2. Docker Commands for Managing Images
# Command                           Description
# 
# docker images                     List all images on the machine.
# docker rmi [IMAGE_NAME]           Remove the image with name IMAGE_NAME on the machine.
# docker rmi $(docker               Remove all images from the machine.
# images -q)
# 
# 
# 
# Commands for Managing Containers
# Table 45-3 contains commands for managing Docker containers.
# 
# 
# Table 45-3. Docker Commands for Managing Containers
# Command               Description
# 
# docker ps             List all containers. Append –a to also list containers not running.
# docker stop           Gracefully stop the container with [CONTAINER_ID] on the machine.
# [CONTAINER_ID]
# docker kill           Forcefully stop the container with [CONTAINER_ID] on the machine.
# CONTAINER_ID]
# docker rm             Remove the container with [CONTAINER_ID] from the machine.
# [CONTAINER_ID]
# docker rm $           Remove all containers from the machine.
# (docker ps -a -q)
# 
# 
# 
# 
#                                                                                             663
# 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Run the Container",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Run the Container"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Runthe(HierNode):
    def __init__(self):
        super().__init__("Run the Container")
        self.add(Content())

# eof
