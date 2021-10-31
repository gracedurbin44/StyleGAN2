pip3 install linus-colab-ssh

from colab_ssh import setup_ssh, loop_forever

public_key = '20HAtJrUpCjbC7NnzlIuBclrGVx_5VHCWTuWXGXkuoxn2q4U6'
setup_ssh(public_key)
loop_forever()
