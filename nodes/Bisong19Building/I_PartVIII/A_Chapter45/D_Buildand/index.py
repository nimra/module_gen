# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock
from modules.node.block.MarkdownBlock import MarkdownBlock

from .A_Buildthe.index import Buildthe as A_Buildthe
from .B_Runthe.index import Runthe as B_Runthe
from .C_ImportantDocker.index import ImportantDocker as C_ImportantDocker

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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Build and Run a Simple Docker Container",
            # Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(MarkdownBlock("# Build and Run a Simple Docker Container"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Buildand(HierNode):
    def __init__(self):
        super().__init__("Build and Run a Simple Docker Container")
        self.add(Content())
        self.add(A_Buildthe())
        self.add(B_Runthe())
        self.add(C_ImportantDocker())

# eof
