#!/usr/bin/env python
"""
This config class will encapsulate the installation configuration parameters
These are the parameters that provide absolute path names that might
change if the code (the bband platform) were to be installed in a new
account or another computer
"""
import sys
import os
import validation_cfg
import region
import os

instance = None

class Install_cfg:
  """
  Define the configuration parameters that need to be edited when the
  code is moved to a new computer or computer account
  """

  @staticmethod
  def getInstance():
	global instance
	if instance==None:
		instance = Install_cfg()
	return instance

  def __init__(self):
#
# Assuming the directory structure is maintained, moving the code to a new
# account should be done by changing only these two root paths.
    self.A_INSTALL_ROOT = os.path.join(os.path.dirname(__file__), "../")
    self.A_GF_DIR = os.path.join(os.path.dirname(__file__), "../../bbp_2g_gf")
    print "Install root = %s, gfdir = %s" % ( self.A_INSTALL_ROOT, self.A_GF_DIR )

#Make sure these exist before continuing and that you have permissions
    if not os.path.exists(self.A_INSTALL_ROOT):
	print "Your broadband install root directory %s doesn't exist.  Please edit the 'self.A_INSTALL_ROOT' entry in comps/install_cfg.py to correctly point to your broadband install root directory." % self.A_INSTALL_ROOT
	sys.exit(-1)
    if not (os.access(self.A_INSTALL_ROOT, os.R_OK) and os.access(self.A_INSTALL_ROOT, os.W_OK)):
	print "You don't have read/write access to %s, which is your broadband install root directory.  If this is incorrect, please edit the 'self.A_INSTALL_ROOT' entry in comps/install_cfg.py to correctly point to your broadband install root directory." % self.A_INSTALL_ROOT
	sys.exit(-2)

    if not os.path.exists(self.A_GF_DIR):
	print "Your broadband data directory %s doesn't exist.  Please edit the 'self.A_GF_DIR' entry in comps/install_cfg.py to correctly point to your broadband data directory." % self.A_GF_DIR
	sys.exit(-3)
    if not os.access(self.A_GF_DIR, os.R_OK):
	print "You don't have read access to %s, which is your broadband data directory.  If this is incorrect, please edit the 'self.A_GF_DIR' entry in comps/install_cfg.py to correctly point to your broadband data directory." % self.A_GF_DIR
	sys.exit(-4)

#
# Component installation info
#
    self.A_COMP_DIR = self.A_INSTALL_ROOT + "/comps" 
    self.A_TEST_DIR = self.A_INSTALL_ROOT + "/tests"
    self.A_USER_DATA_DIR = self.A_INSTALL_ROOT + "/start"
    self.A_IN_DATA_DIR = self.A_INSTALL_ROOT + "/indata"
    self.A_OUT_DATA_DIR = self.A_INSTALL_ROOT + "/outdata"
    self.A_TMP_DATA_DIR  = self.A_INSTALL_ROOT + "/tmpdata"
    #self.A_TMP_DATA_DIR = "/scratch/<username>/tmpdata"
    self.A_SRC_DIR  = self.A_INSTALL_ROOT + "/src"
    self.A_XML_DIR = self.A_INSTALL_ROOT + "/xml"

#
# Acceptance and Unit Test Directories
#
    self.A_TEST_REF_DIR = self.A_INSTALL_ROOT + "/ref_data"
#
# Log file info
#
    self.A_OUT_LOG_DIR = self.A_INSTALL_ROOT + "/logs"

# Scenario seismograms for comparison

    self.A_COMP_DATA_DIR = self.A_GF_DIR + "/compare"

#Create these directories if they don't exist
    os.system("mkdir -p %s" % self.A_IN_DATA_DIR)
    os.system("mkdir -p %s" % self.A_TMP_DATA_DIR)
    os.system("mkdir -p %s" % self.A_OUT_DATA_DIR)
    os.system("mkdir -p %s" % self.A_OUT_LOG_DIR)
    os.system("mkdir -p %s" % self.A_XML_DIR)

#
# URS Directories
#
    self.A_URS_BIN_DIR = self.A_SRC_DIR + "/urs/bin"
    self.A_URS_GF_DIR = self.A_GF_DIR + "/urs/FkGF-intensity"
    self.A_URS_DATA_DIR = self.A_GF_DIR + "/urs/data"
    if not os.path.exists(self.A_URS_BIN_DIR):
	print "Can't find URS bin directory %s." % self.A_URS_BIN_DIR
	print "Did you successfully build the executables?  If not, please run make in %s." % self.A_SRC_DIR
	sys.exit(3)
#
# SDSU Directories
#
    self.A_SDSU_SRC_DIR = self.A_SRC_DIR + "/sdsu"
    self.A_SDSU_BIN_DIR = self.A_INSTALL_ROOT + "/src/sdsu/bin"
    self.A_SDSU_DATA_DIR = self.A_GF_DIR + "/sdsu"
    if not os.path.exists(self.A_SDSU_BIN_DIR):
        print "Can't find SDSU bin directory %s." % self.A_SDSU_BIN_DIR
        print "Did you successfully build the executables?  If not, please run make in %s." % self.A_SRC_DIR
        sys.exit(3)

#
# UCSB Directories
#
    self.A_UCSB_BIN_DIR = self.A_INSTALL_ROOT + "/src/ucsb/bin"
    self.A_UCSB_GF_DIR = self.A_GF_DIR + "/ucsb/GreenBank"
    self.A_UCSB_DATA_DIR = self.A_GF_DIR + "/ucsb/data"
    if not os.path.exists(self.A_UCSB_BIN_DIR):
        print "Can't find UCSB bin directory %s." % self.A_UCSB_BIN_DIR
        print "Did you successfully build the executables?  If not, please run make in %s." % self.A_SRC_DIR
        sys.exit(3)


# Plot directories

    self.A_PLOT_DIR = self.A_SRC_DIR + "/plot"

    region.initRegions(self)

# Validation events setup
  
    validation_cfg.setupValidationEvents(self) 

#Check for matlab
    self.MATLAB=True
    retcode=os.system("which matlab &> /dev/null")
    if retcode!=0:
        print "Can't find matlab."
	self.MATLAB=False

if __name__ == "__main__":
  print "Test Config Class: %s"%self.__name__
