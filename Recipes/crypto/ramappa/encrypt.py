from Crypto.PublicKey import RSA
import os
def send_message(guy,guys_public_key):
	msg = open("..\\"+guy+"\\msg","w+")
	msg.write(guys_public_key.encrypt(raw_input(":"),"IDK")[0])


bheemappas_public_key_file = open("..\\bheemappa_public","r")
bheemappas_public_key = RSA.importKey(bheemappas_public_key_file.read())
send_message("bheemappa",bheemappas_public_key)