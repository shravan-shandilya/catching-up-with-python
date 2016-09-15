from Crypto.PublicKey import RSA
from Crypto import Random
import os

def gen_key_pair(the_guy):
		rand = Random.new().read
		private_key = RSA.generate(1024,rand)
		private_key_file = open(the_guy+"_private","w+")
		public_key_file = open(the_guy+"_public","w+")
		private_key_file.write(private_key.exportKey("PEM"))
		public_key_file.write(private_key.publickey().exportKey("PEM"))
		
		
def publish_public_key(the_guy):
		cmd="copy "+the_guy+"_public ..\\"+the_guy+"_public"
		os.system(cmd)		