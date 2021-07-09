### Tuples and NamedTuples

**Faker profile with tuple**

Generate n number of fake profiles and find largest blood group,
    average age, oldest age, mean geo location with tuples


    def genrate_with_faker_tuple(seed_no: int, n: int) -> 'tuple':
        ...
        for iter in range(n):
            PersonN = Person(**fake.profile())
            list_Person.append(PersonN)
        ...
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
        ...

We are using a specific seed so that we can double check our results when generating fake data. We are using two namedtuples'Person' and 'Calculate'. 'Person' is used as a template to store all the profiles of person. largest_blood_group is calculated using counter , age , average age and mean geo location is calculated in a single iteration. Processing time is calculated


**Faker profile with Dictionary**

Generate n number of fake profiles and find largest blood group,
    average age, oldest age, mean geo location with dictionary
	

    def genrate_with_faker_dict(seed_no: int, n: int) -> 'tuple':
        ...
        for iter in range(n):
            PersonN = dict(zip(person_keys,fake.profile().values()))        
            list_Person.append(PersonN)
        ...
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
        ...

We are using a specific seed so that we can double check our results when generating fake data. We are using two dictionaries 'Person' and 'Calculate'. 'Person' is used as a template to store all the profiles of person. largest_blood_group is calculated using counter , age , average age and mean geo location is calculated in a single iteration. Processing time is calculated

For 5 iterations Average Processing time of namedtuples  is less than Average processing time of dictionary 

- Avg namedtuple 0.026053428649902344
- Avg dictionary 0.03391456604003906

**Faker Stock exchange**

Generate n number of stock data and find open, high, close of stock exchange
	

    def faker_stock_exchange(seed_num : int, n :int) -> 'tuple':
        ...
        for iter in range(n):
            Stock1 = Stock(*getData())
            stock_list.append(Stock1)
        ...
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
        ...

We are getting random datas for companyname, symbold, price, open, high and close. we are using the price and the stock and calculating the market value of total stock exchage. With that value we are calculatin overall capital when opening, and when its high and at close time.