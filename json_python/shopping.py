import json
dic={
    "shopping_list":
        { 
            "chaco":"15",
            "biscuits":"50",
            "diary_milk":"30",
            "ice_cream":"20",
        } 
}
user_item=input("which item you wants=")
user_quantity=int(input("enter the user_quantity="))
del dic['shopping_list'][user_item]
print(dic)

my_file=open("shopp.json","w")
my_data=json.dump(dic,my_file,indent=4)
print(my_data)
