#lst=[1,2,3]
#my_str="mlops playlist"
#my_int= 155

#print(type(my_str))
#lst.clear()
#my_str=my_str.capitalize()
#print(my_str)

from oops_proj import chatbook
user1=chatbook()
print(user1.id)


# using static method directly from class rather than obj
chatbook.set_id(10)
user2=chatbook()
print(user2.id)
#print(user1.get_name()) 
#user1.set_name("Agent X")
#print(user1.get_name())
#print(user1._chatbook__name)
# func vs meth below
#lst = [1,2,3]
# function
#a1=len(lst)
#print(a1)

# method
#user1=chatbook()
#user1.sendmsg()