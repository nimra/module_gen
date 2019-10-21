# Lawrence McAfee

# ~~~~~~~~ import ~~~~~~~~
from modules.node.HierNode import HierNode
from modules.node.LeafNode import LeafNode
from modules.node.Stage import Stage
from modules.node.block.CodeBlock import CodeBlock as cbk
from modules.node.block.ImageBlock import ImageBlock as ibk
from modules.node.block.MarkdownBlock import MarkdownBlock as mbk


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Working with GCE from the Command Line
# In this section, we’ll sample the commands for creating and deleting a compute instance
# on GCP using the command-line interface. To create a compute instance using ‘gcloud’
# from the command-line interface, there are a variety of options that can be added to the
# commands for different specifications of the machine. To learn more about a command,
# attach ‘help’ after the command:
# 
#       •   Provisioning a VM instance: To create a VM instance, use the code
#           syntax
# 
#           gcloud compute instances create [INSTANCE_NAME]
# 
#           For example, let’s create an instance named ‘ebisong-howad-instance’
# 
#           gcloud compute instances create ebisong-howad-instance
# 
#             Created [https://www.googleapis.com/compute/v1/projects/secret-­
#             country-­192905/zones/us-east1-b/instances/ebisong-howad-instance].
#             NAME                       ZONE        MACHINE_TYPE   PREEMPTIBLE  
#             INTERNAL_IP  EXTERNAL_IP   STATUS
#             ebisong-howad-instance  us-east1-b  n1-standard-1              
#             10.142.0.2   35.196.17.39  RUNNING
# 
#             To learn more of the options that can be included with the ‘gcloud instance
#             create’ command, run
# 
#             gcloud compute instances create –help
# 
#             NAME
#                 gcloud compute instances create - create Google Compute Engine
#                  virtual
#                     machine instances
# 
#             SYNOPSIS
#                 gcloud compute instances create INSTANCE_NAMES [INSTANCE_
#                  NAMES ...]
#                     [--accelerator=[count=COUNT],[type=TYPE]] [--async]
#                     [--no-boot-disk-auto-delete]
#                     [--boot-disk-device-name=BOOT_DISK_DEVICE_NAME]
#                     [--boot-disk-size=BOOT_DISK_SIZE] [--boot-disk-type=BOOT_
#                         DISK_TYPE]
#                     [--can-ip-forward] [--create-disk=[PROPERTY=VALUE,...]]
#                     [--csek-key-file=FILE] [--deletion-protection]
#                     [--description=DESCRIPTION]
#                     [--disk=[auto-delete=AUTO-DELETE],
#                       [boot=BOOT],[device-name=DEVICE-NAME],[mode=MODE],
#                        [name=NAME]]
#                     [--labels=[KEY=VALUE,...]]
#                     [--local-ssd=[device-name=DEVICE-NAME],[interface=INTERFACE]]
#                     [--machine-type=MACHINE_TYPE] [--maintenance-
#                         policy=MAINTENANCE_POLICY]
#                     [--metadata=KEY=VALUE,[KEY=VALUE,...]]
#                     [--metadata-from-file=KEY=LOCAL_FILE_PATH,[...]]
#             [--min-cpu-platform=PLATFORM] [--network=NETWORK]
#             [--network-interface=[PROPERTY=VALUE,...]]
#             [--network-tier=NETWORK_TIER] [--preemptible]
#             [--private-network-ip=PRIVATE_NETWORK_IP]
#     :
# 
#     To exit from the help page, type ‘q’ and then press the ‘Enter’ key on the
#     keyboard.
#     To list the created instances, run
# 
#     gcloud compute instances list
# 
#     NAME                       ZONE        MACHINE_TYPE   PREEMPTIBLE  
#     INTERNAL_IP  EXTERNAL_IP   STATUS
#     ebisong-howad-instance  us-east1-b  n1-standard-1              
#     10.142.0.2   35.196.17.39  RUNNING
# 
# •   Connecting to the instance: To connect to a created VM instance
#     using SSH, run the command
# 
#     gcloud compute ssh [INSTANCE_NAME]
# 
#     For example, to connect to the ‘ebisong-howad-instance’ VM, run the
#     command
# 
#     gcloud compute ssh ebisong-howad-instance
# 
#     Warning: Permanently added 'compute.8493256679990250176' (ECDSA)
#     to the list of known hosts.
#     Linux ebisong-howad-instance 4.9.0-8-amd64 #1 SMP Debian
#     4.9.110-3+deb9u4 (2018-08-21) x86_64
# 
#     The programs included with the Debian GNU/Linux system are free
#     software;
#     the exact distribution terms for each program are described in the
#     individual files in /usr/share/doc/*/copyright.
# 
#     Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
#     permitted by applicable law.
#     ekababisong@ebisong-howad-instance:~$
# 
#       •     To leave the instance on the terminal, type ‘exit’ and then press the
#             ‘Enter’ key on the keyboard.
# 
#             Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
#             permitted by applicable law.
#             ekababisong@ebisong-howad-instance:~$ exit
#             logout
#             Connection to 35.196.17.39 closed.
# 
#       •     Tearing down the instance: To delete an instance, run the command
# 
#             gcloud compute instances delete [INSTANCE_NAME]
# 
#             Using our example, to delete the ‘ebisong-howad-instance’ VM, run the
#             command
# 
#             gcloud compute instances delete ebisong-howad-instance
# 
#             The following instances will be deleted. Any attached disks
#             configured to be auto-deleted will be deleted unless they are
#             attached to any other instances or the `--keep-disks` flag
#             is given and specifies them for keeping. Deleting a disk is
#             irreversible and any data on the disk will be lost.
#              - [ebisong-howad-instance] in [us-east1-b]
# 
#             Do you want to continue (Y/n)?  Y
# 
#             Deleted ­[https://www.googleapis.com/compute/v1/projects/secret-­
#             country-­192905/zones/us-east1-b/instances/ebisong-howad-instance].
# 
#     This chapter went through the step for launching a compute machine instance on
# GCP. It covered working with the web-based cloud console and using commands via the
# shell terminal.
#     In the next chapter, we’ll discuss how to launch a Jupyter notebook instance on GCP
# called JupyterLab. A notebook provides an interactive environment for analytics, data
# science, and prototyping machine learning models.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Content(LeafNode):
    def __init__(self):
        super().__init__(
            "Working with GCE from the Command Line",
            Stage.REMOVE_EXTRANEOUS,
            # Stage.ORIG_BLOCKS,
            # Stage.CUSTOM_BLOCKS,
            # Stage.ORIG_FIGURES,
            # Stage.CUSTOM_FIGURES,
            # Stage.CUSTOM_EXERCISES,
        )
        self.add(mbk("# Working with GCE from the Command Line"))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Workingwith(HierNode):
    def __init__(self):
        super().__init__("Working with GCE from the Command Line")
        self.add(Content())

# eof
