from Crypto.PublicKey import RSA

private_key_file = open("bheemappa_private","r")
private_key = RSA.importKey(private_key_file.read())

encrypted_msg = open("msg","r")
print private_key.decrypt(encrypted_msg.read())