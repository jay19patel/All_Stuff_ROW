# import datetime

# mydate1 = datetime.date(2001,11,19) # set datewise 
# print("edit like time formate :",mydate1)

# mydate2= datetime.date.today() # to days date 
# print("To Days Date : ",mydate2)

#  # to days date seprate 
# mydate2= datetime.date.today()
# print("Date: ",mydate2.day)
# print("Month: ",mydate2.month)
# print("Year: ",mydate2.year)


# # simple time to timestanp
# now = datetime.datetime.now() # current time 
# print(now )
# timestamp = datetime.datetime.timestamp(now) # convert simple time to time stamp
# print("current time stamp is :",timestamp)

# time = datetime.datetime.fromtimestamp(timestamp) #convert time stamp to regular time formate 
# print("current time using time stamp is :",time )





# # convert time into string type 
# data = datetime.date.today()
# print(data)
# print("My date type is ",type(data))
# print(datetime.date.isoformat(data))
# print("My date type is ",type(datetime.date.isoformat(data)))



# which day 
# data = datetime.date.today()
# print(" to days day out of 7 is ",datetime.date.isoweekday(data))


# ----------------------------------------------------------------------------------------
# DATE TIME IN TEXT FORMATE :
# import datetime 
# data = datetime.datetime.now()
# print(data.strftime("%A"))

# A,a = day name
# B,b = Month name 
# Y = Year(0000)
# w = weekday(0-6)

# H = Houre (0-23)
# I = Hour (00-12)
# p = AM | PM

# M = minutes
# S = Seconds
# f = microsecond 

# Z = time zone 
# j = day of (365)
# c = Local version of date and time

# x = Local version of date
# X = Local version of time 

# ----------------------------------------------------------------------------------------




# # get unnice id using time :
# def id_genrater():        
#     from datetime import datetime
#     now = datetime.now()
#     stamp = datetime.timestamp(now)
#     my_id = stamp*stamp
#     id = f"jay{int(my_id)}"
#     return id 


# from pymongo import MongoClient

# client = MongoClient('localhost', 27017) 
# db = client['TEST'] 
# myapis = db['mykeys']


# def addata(name):
#     id = id_genrater()
#     findme = myapis.insert_one({"name":name,
#                                 "jays_id": id})
#     return f"successfully created :{id}"

# def create_me():
#     list=["jay","sakman","sarukh","ketrina","babita","jetha","daya","tappu"]
#     for i in list:
#         addata(i)
#         print(addata(i))

# def find_me(id):
#     find_data = myapis.find_one({'jays_id':id})
#     print(find_data)


# find_me("jay2819505685570607616")




