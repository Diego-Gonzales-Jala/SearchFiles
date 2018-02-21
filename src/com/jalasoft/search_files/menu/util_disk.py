import psutil
from src.com.jalasoft.search_files.utils.logging_search import logger

# This class check all disk partitions and get one disk in base option
class UtilDisk(object):

    # Get one disk of disk partition
    def get_disk(self, option):
        logger.info("get disk: Enter")
        disk_part = psutil.disk_partitions()
        disk = disk_part[option - 1]
        logger.info("get_disk: Load disk")
        return disk.device

    #Get all disk partition
    def get_disk_partition(self):
        logger.info("get disk partition: Enter")
        disk_partition = psutil.disk_partitions()
        for i in (0, 0):
            partition = disk_partition[i]
            print('{0:2s} {1:3s}'.format(("|"), partition.device))
        logger.info("get_disk: Load disk")
