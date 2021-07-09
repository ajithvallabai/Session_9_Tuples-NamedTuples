import decimal
from faker import Faker
from collections import namedtuple,Counter
from datetime import datetime
import time 
import random
from decimal import Decimal

# Task 1 : Generate fake data with tuple
def genrate_with_faker_tuple(seed_no: int, n: int) -> 'tuple':
    """
    Generate n number of fake profiles and find largest blood group,
    average age, oldest age, mean geo location with tuples
	:param seed_no: Seed no of faker data
	:type seed_no: int
    :param n: Number of datas to be generated
	:type n: int
	:return tuple: result, profile list , time
    """    
    if (not isinstance(n,int)):
        raise TypeError("Input should be a positive integer")
    Faker.seed(seed_no)
    fake = Faker()
    Person = namedtuple("Person",fake.profile().keys())
    Calculate = namedtuple("Calc",("largest_blood_group","mean_current_location", "oldest_person_age", \
        "averageage"))        
    blood_group = {}
    oldest_person_age = 0
    averageage = 0
    mean_current_location = 0
    list_Person = []    
    for iter in range(n):
        PersonN = Person(**fake.profile())
        list_Person.append(PersonN)
    start_time = time.perf_counter()
    for person in list_Person:
        # oldest age 
        Age = datetime.now().year - person.birthdate.year        
        if oldest_person_age <  Age:                     
            oldest_person_age = Age
        # average age
        averageage +=  Age
        #mean current location
        mean_current_location +=  sum(person.current_location)/2
        #largest blood group
        if person.blood_group in blood_group:
            blood_group[person.blood_group] += 1
        else:
            blood_group[person.blood_group] = 0
    largest_blood_group = max(blood_group , key = blood_group.get)    
    averageage = (averageage/n)
    mean_current_location = mean_current_location/n 
    Calc = Calculate(largest_blood_group, mean_current_location, oldest_person_age, averageage)
    stop_time = time.perf_counter()   
    return Calc, list_Person, (stop_time -start_time)
    
# Task 2 : Generate fake data with dictionary
def genrate_with_faker_dict(seed_no: int, n: int) -> 'tuple':
    """
    Generate n number of fake profiles and find largest blood group,
    average age, oldest age, mean geo location with dictionary
	:param seed_no: Seed no of faker data
	:type seed_no: int
    :param n: Number of datas to be generated
	:type n: int
	:return tuple: result, profile list , time
    """        
    if (not isinstance(n,int)):
        raise TypeError("Input should be a positive integer")
    Faker.seed(seed_no)
    fake = Faker()
    Person = dict.fromkeys(fake.profile().keys(),"null")
    Calculate = {"largest_blood_group" : "","mean_current_location":"", "oldest_person_age":"", \
        "averageage":""}     
    blood_group = {}
    oldest_person_age = 0
    averageage = 0
    mean_current_location = 0
    list_Person = []    
    person_keys = fake.profile().keys()    
    for iter in range(n):
        PersonN = dict(zip(person_keys,fake.profile().values()))        
        list_Person.append(PersonN)
    start_time = time.perf_counter()
    for person in list_Person:
        # oldest age 
        Age = datetime.now().year - person["birthdate"].year        
        if oldest_person_age <  Age:                     
            oldest_person_age = Age

        # average age
        averageage +=  Age

        #mean current location
        mean_current_location +=  sum(person["current_location"])/2

        #largest blood group
        if person["blood_group"] in blood_group:
            blood_group[person["blood_group"]] += 1
        else:
            blood_group[person["blood_group"]] = 0
         
    largest_blood_group = max(blood_group , key = blood_group.get)    
    averageage = (averageage/n)
    mean_current_location = mean_current_location/n    
    values = [largest_blood_group, mean_current_location, oldest_person_age, averageage]
    Calculate.update(dict(zip(Calculate,values)))   
    stop_time = time.perf_counter()
    return Calculate, list_Person, (stop_time -start_time)
    
# Task 3 : Stock exchange 
def faker_stock_exchange(seed_num : int, n :int) -> 'tuple':
    """
    Generate n number of stock data and find open, high, close of stock exchange
	:param seed_no: Seed no of faker data and randomness
	:type seed_no: int
    :param n: Number of datas to be generated
	:type n: int
	:return tuple: result, company profile list , time
    """       
    if (not isinstance(seed_num,int)) or (not isinstance(n,int)):
        raise TypeError("Input should be a positive integer")

    Faker.seed(seed_num)
    fake = Faker()
    Stock = namedtuple("Stock",("Company","Symbol","Price","Open","High", "Close"))    
    Stock.__doc__ = "Contains company details and their stock details"
    stock_list = []
    random.seed(seed_num)
    def getData():
        name = fake.company()
        symbol = list(name)
        symbol = symbol[0],symbol[len(symbol)//3],symbol[len(symbol)//2],symbol[-1]
        symbol = "".join(symbol).upper()
        price = float(Decimal(random.randrange(1000, 6000))/100)
        base = float(Decimal(random.randrange(10000, 38900))/100)
        high = float(Decimal(random.randrange(100, 300))/10)
        close = float(Decimal(random.randrange(-200, 300))/10)
        return name,symbol, price, base , base + high , base + close 
    
    for iter in range(n):
        Stock1 = Stock(*getData())
        stock_list.append(Stock1)

    start_time = time.perf_counter()
    stock_exchange = namedtuple("StockExchange",("Open","High", "Close", ))
    stock_exchange.__doc__ = "Contains total Open, high, close stock exchange details "    
    stock_open = 0
    stock_high = 0
    stock_close = 0
    for company in stock_list:
        stock_open += (company.Open * company.Price)
        stock_high += (company.High * company.Price)
        stock_close += (company.Close * company.Price)
    display_Stock = stock_exchange(stock_open, stock_high, stock_close)
    stop_time = time.perf_counter()
    return display_Stock, stock_list, (stop_time -start_time)

