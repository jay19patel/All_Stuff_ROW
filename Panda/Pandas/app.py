

# Read and DataFrame Using Panda 
import pandas as pd
df = pd.read_csv('data.csv')
print(df)

# Graph 
import matplotlib.pyplot as plt
plt.plot(df.NAME ,df.MATHS,label="Maths")
plt.plot(df.NAME ,df.HINDI,label="Hindi")
plt.plot(df.NAME ,df.GUJRATI,label="Gujratai")
plt.plot(df.NAME ,df.ENGLISH,label="English")
plt.plot(df.NAME ,df.ATTENDANCE,label="attandec")


plt.title("STUDENT DATA")
plt.xlabel("Names")
plt.ylabel("Attandace")
plt.legend()
plt.show()




# col_names = ['name','roll','att','maths','hindi','gujrati','english']
# df = pd.read_csv('Panda/data.csv', name=col_names,skiprows=[0])  #pandas read this csv
# print(df)  # give some first data