#Prérequis
apt update
apt dist-upgrade
apt -y install gnupg2 apt-transport-https


#installations
echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu bionic main" | tee /etc/apt/sources.list.d/ansible.list
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
apt update
apt install -y ansible
ansible --version

#désactivation ipv6
cat <<EOF > /etc/sysctl.conf
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.all.autoconf = 0
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.default.autoconf = 0
EOF
sysctl -p


#awx
cd ~
git clone --depth 50 https://github.com/ansible/awx.git
cd awx/installer
sed -i "s|docker_compose_dir=.*$|docker_compose_dir=/var/lib/awx|g" inventory
sed -i "s|^#project_data_dir=.*$|project_data_dir=/var/awx_projects|g" inventory
sed -i "s|^postgres_data_dir=.*$|postgres_data_dir=/var/pgdocker|g" inventory
sed -i "s|^secret_key=.*$|secret_key=$(pwgen -N 1 -s 30)|g" inventory
sed -i "s|^pg_admin_password=.*$|pg_admin_password=$(pwgen -N 1 -s 30)|g" inventory
sed -i "s|^pg_password=.*$|pg_password=$(pwgen -N 1 -s 30)|g" inventory
sed -i "s|^rabbitmq_password=.*$|rabbitmq_password=$(pwgen -N 1 -s 30)|g" inventory
ansible-playbook -i inventory install.yml

#source: https://www.qth.fr/477/ansible-avec-awx
