# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

required_plugins = %w( vagrant-vbguest )
required_plugins.each do |plugin|
  system "vagrant plugin install #{plugin}" unless Vagrant.has_plugin? plugin
end

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/utopic/current/utopic-server-cloudimg-amd64-vagrant-disk1.box"
  config.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"

  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 2

    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end

  config.vm.define "spv2" do |spv2|
    spv2.vm.network :forwarded_port, guest:8000, host:8000, auto_correct: true
    spv2.vm.network :forwarded_port, guest:9080, host:9080, auto_correct: true
    spv2.vm.network :forwarded_port, guest:5432, host:15432, auto_correct: true
    spv2.vm.network :forwarded_port, guest:15672, host:45672, auto_correct: true

    spv2.vm.synced_folder ".", "/home/vagrant/django_adt"
    spv2.vm.network "private_network", ip: "10.10.10.50"

    spv2.vm.provision :shell, :path => "Vagrant-setup/install.sh", :args => "django_adt"
  end
end
