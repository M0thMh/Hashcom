import hashlib
import time

print("\n\n")
print("	██╗░░██╗░█████╗░░██████╗██╗░░██╗░█████╗░░█████╗░███╗░░░███╗")
print("	██║░░██║██╔══██╗██╔════╝██║░░██║██╔══██╗██╔══██╗████╗░████║")
print("	███████║███████║╚█████╗░███████║██║░░╚═╝██║░░██║██╔████╔██║")
print("	██╔══██║██╔══██║░╚═══██╗██╔══██║██║░░██╗██║░░██║██║╚██╔╝██║")
print("	██║░░██║██║░░██║██████╔╝██║░░██║╚█████╔╝╚█████╔╝██║░╚═╝░██║")
print("	╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝")
print("								v0.01")





def choose_method (method):
     match method:
          case 1:
               return hashlib.md5()
          case 2:
               return hashlib.sha1()
          case 3:
               return hashlib.sha224()
          case 4:
               return hashlib.sha256()
          case 5:
               return hashlib.sha384()
          case 6:
               return hashlib.sha512()              
          case default:
              return "ERROR"


def hash_file(filename, crypt):
     h = crypt
     with open(filename,'rb') as file:
          chunk = 0
          while chunk != b'':
               chunk = file.read(1024)
               h.update(chunk)
     return h.hexdigest()




path = input("\n\nEnter The File Path: ")
print("\n")
print("1. MD5       4. SHA256")
print("2. SHA1      5. SHA384")
print("3. SHA224    6. SHA512")

number = int(input("\nChoose The Hash Method By Enter The Number Of The Hash: "))
method = choose_method(number)

file_hash = hash_file(path, method)

correct_hash = input("Enter The Hash To Compare Between Them: ")


print("\n================================================ RESULT ================================================")
print("\n")
print(f"The File Hash Is : {file_hash}")
print(f"The Correct Hash Is : {correct_hash}")


if file_hash == correct_hash:
     print("The File Is Correct !!\n\n")
elif file_hash != correct_hash:
     print("The File Is Hacked !!\n\n")
































