# immutable and unique
a= {
    "name": "Gaurav",
    32: "thirty_two",
    (1, 2, 3): "tuple_key"
}
print(a["name"])         
# print(a[32])             
# print(a[(1, 2, 3)]) 
# values use garda key rakhena vane error aaucha so u can use get or in le chai existense check garcha.
print(a.get("age", 0))
# print("name" in a)
# print("occupation" in a)