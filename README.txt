SCEC and OSG integration README
===============================

Mostly following the guide:
http://scec.usc.edu/scecpedia/Broadband_User_Guide_Current


Files
-----
install_cfg.py:
    Customized version of install_cfg.py that is distributed with scec 
    broadband platform.

scec-wrapper.sh:
    Wrapper script called by condor on the remote worker node.

scec.sh:
    File to source that will setup the bin, netcdf, and python paths.

submit.condor:
    Condor submit file for scec.




