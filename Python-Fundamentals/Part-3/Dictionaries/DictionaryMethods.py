# .keys()  -  returns all key
# .values()  -  retuens all values
# .items()  -  returns (key,val) pairs
# .get(val)  -  returns val acc. to key
# .update(new_item)  -  adds new item to dict

info = {
    "name" : "Prince",
    "cgpa" : "7.5",
    "Subjects" : ["math","Dsa","Devops","DBMS"],
    1:"Student"
}
print(info.keys())

print(info.values())

print(info.items())

print(info.get("name"))

info.update({
    "city":"Aburoad"
})
print(info)