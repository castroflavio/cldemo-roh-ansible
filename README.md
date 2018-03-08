Canarying changes Demo
===========================

This demo is written for the [cldemo-vagrant](https://github.com/cumulusnetworks/cldemo-vagrant) reference topology and applies the reference BGP unnumbered configuration from [cldemo-config-routing](https://github.com/cumulusnetworks/cldemo-config-routing).

Quickstart: Run the demo
------------------------
Before running this demo, install [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds) and [Vagrant](https://releases.hashicorp.com/vagrant/). The currently supported versions of VirtualBox and Vagrant can be found on the [cldemo-vagrant](https://github.com/cumulusnetworks/cldemo-vagrant).

    ### Bring up the vagrant topology
    git clone https://github.com/cumulusnetworks/cldemo-vagrant
    cd cldemo-vagrant
    vagrant up oob-mgmt-server oob-mgmt-switch leaf01
    vagrant up leaf02 leaf03 leaf04 spine01 spine02 

    ### setup oob mgmt server
    vagrant ssh oob-mgmt-server

    ### Run the ROH demo
    git clone https://github.com/castroflavio/cldemo-roh-ansible
    cd cldemo-roh-ansible
    ansible-playbook start.yml

