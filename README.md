https://www.surekhatech.com/blog/how-to-install-odoo-in-windows

https://github.com/Mountant2021/odoo-basic

gen ssh-key
ssh-keygen -t ed25519 -C "vanty0829@gmail.com" 


Get-Service ssh-agent

ssh-agent

ssh-add

Fix Error unable to start ssh-agent service, error: 1058(xxxx)
win + R, Go To services.msc
Find And Check Is OpenSSH Authentication Agent Service Running -> change to manual

start-ssh-agent

conda remove --name ENV_NAME --all

conda create -n py38 python=3.8

git clone --branch 17.0 git@github.com:odoo/odoo.git

python -m venv .venv

pip install setuptools wheel
pip install -r requirements.txt


python odoo-bin -r odoo -w odoo --addons-path=addons,C:\Users\vanty\Downloads\Odoo\odoo-basic -d odoo -i base # -i base to init database

python odoo-bin -r odoo -w odoo --addons-path=addons,C:\Users\vanty\Downloads\Odoo\odoo-basic -d odoo
python odoo-bin scaffold module-2 C:\Users\vanty\Downloads\Odoo\odoo-basic