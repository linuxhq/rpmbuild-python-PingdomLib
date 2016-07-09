# rpmbuild-python-PingdomLib

Create a python-PingdomLib RPM for RHEL/CentOS.

## Requirements

To download package sources and install build dependencies

    yum -y install rpmdevtools yum-utils

## Build process

To build the package follow the steps outlined below

    git clone https://github.com/linuxhq/rpmbuild-python-PingdomLib.git rpmbuild
    mkdir rpmbuild/SOURCES
    spectool -g -R rpmbuild/SPECS/python-PingdomLib.spec
    yum-builddep rpmbuild/SPECS/python-PingdomLib.spec
    rpmbuild -ba rpmbuild/SPECS/python-PingdomLib.spec

## License

BSD

## Author Information

This package was created by [Taylor Kimball](http://www.linuxhq.org).
