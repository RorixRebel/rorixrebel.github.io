title: Ansible 101
date: January 18th, 2019
slug: ansible-101
category: devops
summary: Ansible is my favorite configuration management tool, its uses YAML and Python, so you have a winning combo to begin with. One of the main things of why i enjoy using it, is basically that it doesn’t require an installation on the target servers and that is a big factor that in my opinion defeats other management tools like Chef or Puppet.....
image: ansible.png
tags: ansible, devops, automation


Ansible is my favorite configuration management tool, its uses YAML and Python, so you have a winning combo to begin with. One of the main things of why i enjoy using it, is basically that it doesn’t require an installation on the target servers and that is a big factor that in my opinion defeats other management tools like Chef or Puppet.

The fact that you can run and configure servers without anything installed on them besides python (which is almost now standard on every single virtual/physical machine).

**Few things to note:**

1. Requires python on both master and client machine
2. Connects mostly over SSH so credential setup is needed
3. Uses or executes in sequence (top to bottom)

As we talked before, Ansible relies on YAML.
Yaml Aint Markup Language

Meant to be “human readable” Perfect for the simplicity that involves ansible/python YAML uses a dictionary type of input information eg: key:value Name: Mike

YAML Examples (not directly ANSIBLE examples)

    :::yaml
    --- #Pending Items
    - Visa Renewal
    Description: This is needed to renew your visa and this contains all of the information needed
    Type: Important
    Due: Today
    Followups:
    - CAS Appointment
            Date: April 30th
    - Consulate
            Date: April 31st

Same as with Python, indentation is critical for your YAML files.

To use ansible its as simple as: (process may be different based on your distribution)

    :::bash
    sudo apt-get install ansible

Once installed you can start creating what we call “playbooks”, which is basically YAML instructions for Ansible to execute something. We will begin with the classic hello word. Create a file named hello.yml.

    :::yaml
    hello.yml

    --- # Hello World
    - hosts: localhost
    tasks:
        - debug:
            msg: "Hello World"

To run your playbook execute the following command:

    :::yaml
    ansible-playbook hello.yml

    Will produce the following output:

    PLAY [localhost] *****************************************************************

    TASK [Gathering Facts] ***********************************************************
    ok: [localhost]

    TASK [debug] *********************************************************************
    ok: [localhost] => {
        "msg": "Hello World"
    }

    PLAY RECAP ***********************************************************************
    localhost                  : ok=2    changed=0    unreachable=0    failed=0

As you can see, running ansible playbooks is incredibly easy and of course there a lot more topics to cover for Ansible basics. If you want keep learning more, head over to the Ansible Documentation.