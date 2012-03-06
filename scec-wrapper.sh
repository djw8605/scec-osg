#!/bin/bash -x

get_http() {
website=$1
source $OSG_GRID/setup.sh
export OSG_SQUID_LOCATION=${OSG_SQUID_LOCATION:-UNAVAILABLE}
if [ "$OSG_SQUID_LOCATION" != UNAVAILABLE ]; then
  export http_proxy=$OSG_SQUID_LOCATION
fi

wget --retry-connrefused --waitretry=10 $website

# Check if the download worked
if [ $? -ne 0 ]
then
   unset http_proxy
   wget --retry-connrefused --waitretry=10 $website
   if [ $? -ne 0 ]
   then
      exit 1
   fi
fi

}


tar_rm() {
file=$1
tar xzf $1
rm -f $1
}

# First get the necessary files
get_http http://glidein.unl.edu/scec/scec-lib.tar.gz
get_http http://glidein.unl.edu/scec/scec-share.tar.gz
get_http http://glidein.unl.edu/scec/scec-pythonlib.tar.gz
get_http http://glidein.unl.edu/scec/scec-bin.tar.gz
get_http http://glidein.unl.edu/scec/scec-etc.tar.gz
get_http http://glidein.unl.edu/scec/netcdf-3.6.3.tar.gz

globus-url-copy -vb gsiftp://red-gridftp.unl.edu/user/hcc/scec/bbp_data_v11.2.2.tgz file://`pwd`/bbp_data_v11.2.2.tgz
globus-url-copy -vb gsiftp://red-gridftp.unl.edu/user/hcc/scec/bbp_2g.tar.gz file://`pwd`/bbp_2g.tar.gz


tar_rm scec-lib.tar.gz
tar_rm scec-share.tar.gz
tar_rm scec-pythonlib.tar.gz
tar_rm scec-bin.tar.gz
tar_rm scec-etc.tar.gz
tar_rm bbp_2g.tar.gz
tar_rm bbp_data_v11.2.2.tgz
tar_rm netcdf-3.6.3.tar.gz

. scec.sh

ls -lh

cp -f install_cfg.py bbp_2g/comps/
pushd bbp_2g/tests
python AcceptTests.py
popd

rm -rf *.tar.gz lib bin lib64 bbp_2g* netcdf* etc share *.tgz



