import unittest
from src.com.jalasoft.search_files.menu.util_disk import UtilDisk

#For run these test is required 2 disk partition for running two test
class UtilDiskTest(unittest.TestCase):


    disk_part = UtilDisk()

    def test_get_disk_partition_with_option_equal_one(self):
        option = 1
        self.assertEqual('C:\\', self.disk_part.get_disk(option))

    def test_get_disk_partition_with_option_equal_two(self):
        option = 2
        self.assertEqual('D:\\',self.disk_part.get_disk(option))

if __name__ == "__main__":
	unittest.main()


import os
import time
def dump(st):
   mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
   print("- size:", size, "bytes")
   print("- owner:", uid, gid)
   print("- created:", time.ctime(ctime))
   print("- last accessed:", time.ctime(atime))
   print("- last modified:", time.ctime(mtime))
   print("- mode:", oct(mode))
   print("- inode/dev:", ino, dev)
(dump(os.stat("D:\\behave\old version serach project\\ui2\\ui2.txt")))