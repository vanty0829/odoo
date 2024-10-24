https://www.surekhatech.com/blog/how-to-install-odoo-in-windows

https://github.com/Mountant2021/odoo-basic

https://gist.github.com/Guidoom/d5db0a76ce669b139271a528a8a2a27f

gen ssh-key
ssh-keygen -t ed25519 -C "vanty0829@gmail.com" 


Get-Service ssh-agent

ssh-agent

ssh-add
ssh-add ~/.ssh/id_rsa

Fix Error unable to start ssh-agent service, error: 1058(xxxx)
win + R, Go To services.msc
Find And Check Is OpenSSH Authentication Agent Service Running -> change to manual

start-ssh-agent

conda remove --name ENV_NAME --all

conda create -n py38 python=3.8

git clone --branch 17.0 git@github.com:odoo/odoo.git

python -m venv .venv

https://visualstudio.microsoft.com/visual-cpp-build-tools/

pip install setuptools wheel
pip install -r requirements.txt


python odoo-bin -r odoo -w odoo --addons-path=addons,C:\Users\vanty\Downloads\Odoo\odoo-basic -d odoo -i base # -i base to init database

python odoo-bin -r odoo -w odoo --addons-path=addons,C:\Users\vanty\Downloads\Odoo\odoo-basic -d odoo
python odoo-bin scaffold module-2 C:\Users\vanty\Downloads\Odoo\odoo-basic


https://www.odoo.com/documentation/13.0/developer/howtos/web.html
https://minhng.info/odoo/tao-widget-odoo.html
https://www.cybrosys.com/blog/how-to-effectively-create-a-field-widget-in-odoo-15
https://www.odoo.com/documentation/18.0/developer/howtos/javascript_field.html
https://minhng.info/odoo/them-button-list-view-odoo.html


fabric permission
https://www.mssqltips.com/sqlservertip/8024/microsoft-fabric-warehouse-configure-access-and-permissions/
https://www.data-traveling.com/articles/microsoft-fabric-admin-how-to-create-multiple-workspaces-using-python
https://github.com/gjoaquim/GuilhermeJoaquim/blob/main/Fabric%20Admin/CreateFabricWorkspace.py
https://learn.microsoft.com/en-us/fabric/data-engineering/notebook-public-api
https://learn.microsoft.com/en-us/rest/api/fabric/articles/
https://gist.github.com/murggu/09d7befcb157011c340c51cb5d4af42f

https://learn.microsoft.com/en-us/graph/auth-v2-user?tabs=http


https://learn.microsoft.com/en-us/fabric/onelake/security/data-access-control-model
https://learn.microsoft.com/en-us/fabric/data-warehouse/security