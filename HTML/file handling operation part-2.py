file_read = open('Codingal.txt','r')
print("File id Read Mode-")
print(file_read.read())
file_read.close()

file_write=open('Codingal.txt','w')
file_write.write("File in write mode.....")
file_write.write("HI! I am Penguin I am 1 yr old")
file_write.close()
