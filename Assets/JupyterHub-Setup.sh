# JupyterHub users configuration

echo Adding group...
groupadd -g 9000 jupyterhubusers

echo Adding user 00...
useradd -m -g 9000 user00
echo 'user00:user00' | chpasswd
cp /Notebooks/* /home/user00
chown -R user00:jupyterhubusers /home/user00

echo Adding user 01...
useradd -m -g 9000 user01
echo 'user01:user01' | chpasswd
cp /Notebooks/* /home/user01
chown -R user01:jupyterhubusers /home/user01
