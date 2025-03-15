from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES



def aes_decrypt(input_file, output_file, key):
   
    key = key.encode('utf-8')
    
    with open(input_file, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read() 
    
    
    cipher = AES.new(key[:16], AES.MODE_CBC, iv)  

   
    padded_plaintext = cipher.decrypt(ciphertext)

   
    plaintext = unpad(padded_plaintext, AES.block_size)

   
    with open(output_file, 'wb') as f:
        f.write(plaintext)


input_path = r""  # 암호화된 파일 경로
output_path = r""  # 복호화된 파일 저장 경로

aes_decrypt(input_path, output_path, "s3cR3t_k3y!s_AES")

print(f"파일이 복호화되어 {output_path}에 저장되었습니다.")
