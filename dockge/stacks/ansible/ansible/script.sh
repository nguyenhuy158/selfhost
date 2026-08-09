HOST=clouddigital

ansible-playbook -vv -l $HOST fulfillment.playbook.yml 
ansible-playbook -vv -l $HOST fulfillment.playbook.yml -t reset



ansible-playbook -vv -l $HOST n8n.playbook.yml -t restore

ansible-playbook -vv -l $HOST cloudflare.playbook.yml 

ansible-playbook -vv -l $HOST docker.playbook.yml

ansible-playbook -vv -l $HOST glances.playbook.yml

ansible-playbook -vv -l $HOST dozzle.playbook.yml