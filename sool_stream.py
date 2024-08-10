#Python program to simulate streaming data.  
# 
# Program sends data to port 44444 on the localhost.  User point to a datafile to stream.
#
# Parameters:
#     files: path to a source data file
#


import sys
import shutil
import time
import socket
import signal

if __name__ == "__main__":
  if len(sys.argv) < 1:
    print >> sys.stderr, "Usage: spool_stream.py <spool_dir> <lines> <files> "
    exit(-1)

  sleeptime = float(5)
  spool_dir = sys.argv[1]
  N = int(sys.argv[2])
  filelist = sys.argv[3:]

  def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    infile.close()
