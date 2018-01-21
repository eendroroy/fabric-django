# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.box_check_update = true

  config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = 512
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y nginx
    mkdir -p /etc/nginx/sites-enabled/
    mkdir -p /etc/uwsgi/apps-enabled/
    useradd deployer
    mkdir -p /home/deployer/.ssh
    chown deployer:deployer /home/deployer -R
    sudo apt-get install -y libssl-dev libreadline-dev zlib1g-dev git \
         build-essential checkinstall libncursesw5-dev libssl-dev \
         libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev ccache gcc make
    sudo mkdir /usr/local/pyenv/
    git clone https://github.com/pyenv/pyenv.git /usr/local/pyenv
    mkdir -p /usr/local/pyenv/plugins
    git clone https://github.com/pyenv/pyenv-ccache.git /usr/local/pyenv/plugins/pyenv-ccache
    PYENV_ROOT=/usr/local/pyenv /usr/local/pyenv/bin/pyenv install 3.6.0
    PYENV_ROOT=/usr/local/pyenv PYENV_VERSION=3.6.0 /usr/local/pyenv/bin/pyenv exec pip install virtualenv
    apt-get clean
  SHELL
end
