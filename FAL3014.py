#FAL3014 CIPHER BY SK

import math 
key = "HACK" # key for transposition


def generateKey(string, key): #generate key with length same as input
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - 
                       len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 
      

def cipherText(string, key): #ecrypting using FAL3014 CIPHER
    cipher_text = [] 
    for i in range(len(string)): 
        x = (ord(string[i]) + 
             ord(key[i])) % 51
        x += ord('A') 
        cipher_text.append(chr(x)) 
    return("" . join(cipher_text)) 












def encryptMessage(msg): #DOING COLUMNAR transformation
    cipher = "" 
  
    # track key indices 
    k_indx = 0
  
    msg_len = float(len(msg)) 
    msg_lst = list(msg) 
    key_lst = sorted(list(key)) 
  
    # calculate column of the matrix 
    col = len(key) 
      
    # calculate maximum row of the matrix 
    row = int(math.ceil(msg_len / col)) 
   
    fill_null = int((row * col) - msg_len) 
    msg_lst.extend('_' * fill_null) 
    
    matrix = [msg_lst[i: i + col]  
              for i in range(0, len(msg_lst), col)] 

    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 
        cipher += ''.join([row[curr_idx]  
                          for row in matrix]) 
        k_indx += 1
  
    return cipher 
      

    
    
    
    
    
def decryptMessage(cipher): #reverse of columnar transformation
    msg = "" 

    k_indx = 0
    msg_indx = 0
    msg_len = float(len(cipher)) 
    msg_lst = list(cipher) 
  

    col = len(key) 
    row = int(math.ceil(msg_len / col)) 

    key_lst = sorted(list(key)) 
    dec_cipher = [] 
    for _ in range(row): 
        dec_cipher += [[None] * col] 

    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 
  
        for j in range(row): 
            dec_cipher[j][curr_idx] = msg_lst[msg_indx] 
            msg_indx += 1
        k_indx += 1

    try: 
        msg = ''.join(sum(dec_cipher, [])) 
    except TypeError: 
        raise TypeError("This program cannot", 
                        "handle repeating words.") 
    null_count = msg.count('_') 
    if null_count > 0: 
        return msg[: -null_count] 
  
    return msg 
    
    
    
    
def originalText(cipher_text, key):  #reverse of FAL3014 CIPHER
    orig_text = [] 
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - 
             ord(key[i]) + 23) % 51
        x += ord('A') 
        orig_text.append(chr(x)) 
    return("" . join(orig_text)) 




if __name__ == "__main__":   #program RUNNER
    string = input(" ENTER IN UPPERCASE,FOR SPACE ADD LETTER 'S' (or) REMOVE EXTRA 'S' FROM THE FINAL OUTPUT \n")
    
    keyword = "FALCON"
    k = generateKey(string, keyword)
    
    
    cipher_text = cipherText(string,k)
    print("ciphertext :",format(cipher_text))
    
    cipher_text1= encryptMessage(cipher_text)
    print("Ciphertext1 :", format(cipher_text1) )
    
    decrypt1=decryptMessage(cipher_text1)
    print("decrypt1 :",decrypt1)
    
    print("Original/Decrypted Text :",  
           originalText(decrypt1, k)) 
  
