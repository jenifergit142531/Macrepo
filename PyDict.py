#Nested Dictionary

product={
    "pen":{
        "brand":"xyz",
        "price":20,
        "quantity":10
    },
    "books":{
        "brand":"classmate",
        "price":40,
        "quantity":20
    },
    "box":{
        "brand":"faber",
        "price":250,
        "quantity":5
    }
}

print(product)

product["pencil"]={"brand:camlin","price:50","color:multicolored"}

print(product)

del product.box["quantity"]

#product.pop("pencil")

print(product)



"""myDict={
    "carName1":"polo",
    "brand1":"volkswagen",
    "year1":2022,
    "carName":"vento",
    "brand":"volkswagenex",
    "year":2024
    
}
myDict["color"]="Silver"
myDict["carName1"]="Jetta"
#myDict["brand3"]="volkswagen"
#myDict["year3"]=2019
#myDict.pop("year")
myDict.clear()


print(myDict)"""