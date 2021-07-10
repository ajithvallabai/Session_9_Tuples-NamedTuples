from datetime import datetime
import pytest
from io import StringIO 
import sys
import time
import inspect
import os
import session9
import re 



# Task 1 , 5 test 

# length of returns 10000
def test_tuple_profile_generation_function():
    n = 100
    m = 5000
    result_1, profile_list_1, time_1 = session9.genrate_with_faker_tuple(0, n)
    result_2, profile_list_2, time_2 = session9.genrate_with_faker_tuple(0, m)
    print("For number ",n, "profiles length is ", len(profile_list_1) )
    print("For number ",m, "profiles length is ", len(profile_list_2) )
    if time_1 <= time_2:
        print(n, "is faster in execution")
    else:
        print(m, "is faster in execution")
    assert len(profile_list_1) == 100 , "Generator is not generating specified no of profile , Dont hard code"
    assert len(profile_list_2) == 5000, "Generator is not generating specified no of profile , Dont hard code"
    assert time_1 <= time_2 , "You are doing something fishy"

# oldest person age , blood group
def test_tuple_result():
    # result for seed 0
    
    result_1, profile_list_1, time_1 = session9.genrate_with_faker_tuple(0, 10000)
    print("Largest blood group for seed 0 is ",result_1.largest_blood_group) 
    print("oldes person age for seed 0 is ",result_1.oldest_person_age)   
    assert result_1.largest_blood_group == 'AB+' , "its not correct answer for seed 0"
    assert result_1.oldest_person_age == 116 , "its not correct answer for seed 0"

# check if its a named tuple
def test_namedtuples():
    def isnamedtupleinstance(x):
        t = type(x)
        b = t.__bases__
        if len(b) != 1 or b[0] != tuple: return False
        f = getattr(t, '_fields', None)
        if not isinstance(f, tuple): return False
        return all(type(n)==str for n in f)

    result, profile_list, time = session9.genrate_with_faker_tuple(0, 10)    
    assert isnamedtupleinstance(result) == True , "result is not a instance of named tuple"
    assert isnamedtupleinstance(profile_list[0]) == True , "profile is not a instance of named tuple"
    print("Both result and profile list are instance of named tuples")

# check if output contains all fields
def test_tuple_fields():
    result, profile_list, time = session9.genrate_with_faker_tuple(0, 10)
    assert result._fields == ('largest_blood_group', 'mean_current_location', 'oldest_person_age', 'averageage') , "Please check the field names"
    assert profile_list[0]._fields == ('job', 'company', 'ssn', 'residence', 'current_location', 'blood_group', 'website', 'username', 'name', 'sex', 'address', 'mail', 'birthdate') , "Please check the field names"
    print("Both result and profile list has specified fields as per requirements")

def test_input_argument_tuple():
    with pytest.raises(TypeError):
        session9.genrate_with_faker_tuple(0, 'twenty')
    print("Type error is raised for a string input to number of profiles")

# Task 2 , 6 test 

# length of returns 10000
def test_dict_profile_generation_function():
    n = 100
    m = 5000
    result_1, profile_list_1, time_1 = session9.genrate_with_faker_dict(0, n)
    result_2, profile_list_2, time_2 = session9.genrate_with_faker_dict(0, m)
    print("For number ",n, "profiles length is ", len(profile_list_1) )
    print("For number ",m, "profiles length is ", len(profile_list_2) )
    if time_1 <= time_2:
        print(n, "is faster in execution")
    else:
        print(m, "is faster in execution")
    assert len(profile_list_1) == 100 , "Generator is not generating specified no of profile , Dont hard code"
    assert len(profile_list_2) == 5000, "Generator is not generating specified no of profile , Dont hard code"
    assert time_1 <= time_2 , "You are doing something fishy"

# oldest person age , blood group , average age 
def test_dict_result():
    # result for seed 0
    result_1, profile_list_1, time_1 = session9.genrate_with_faker_dict(0, 10000)    
    assert result_1["largest_blood_group"] == 'AB+' , "its not correct answer for seed 0"
    assert result_1["oldest_person_age"] == 116 , "its not correct answer for seed 0"
    print("largest_blood_group and oldest_person_age is mataching for seed 0 execution")

# check if its a dictionary 
def test_dict():
    result, profile_list, time = session9.genrate_with_faker_dict(0, 10)    
    assert isinstance(result, dict) == True , "result is not a instance of named tuple"
    assert isinstance(profile_list[0], dict) == True , "profile is not a instance of named tuple"   
    print("Both result and profile list are instance of dictionary")


# check if person contains all fields, # check if calc contains all fields
def test_dict_fields():
    result, profile_list, time = session9.genrate_with_faker_dict(0, 10)    
    assert list(result.keys()).sort() == ['largest_blood_group', 'mean_current_location', 'oldest_person_age', 'averageage'].sort() , "Please check the field names"
    assert list(profile_list[0].keys()).sort() == ['job', 'company', 'ssn', 'residence', 'current_location', 
        'blood_group', 'website', 'username', 'name', 'sex', 'address', 'mail', 'birthdate'].sort() , "Please check the field names"
    print("Both result and profile list has specified keys as per requirements")

# combined testing for time taken
def test_input_argument_dict():
    with pytest.raises(TypeError):
        session9.genrate_with_faker_dict(0, 'forty')
    print("Type error is raised for a string input to number of profiles")

# Task 1 and Task 2 , Proving tuples is faster than dict
def test_race_tuples_dict():
    print("This test takes few minitues")
    avg_tuple_time = 0
    avg_dict_time = 0
    n = 5
    for _ in range(n):
        _, _, time_tuple = session9.genrate_with_faker_tuple(0, 10000)
        _, _, time_dict = session9.genrate_with_faker_dict(0, 10000)
        avg_tuple_time += time_tuple
        avg_dict_time += time_dict
    avg_tuple_time /= n
    avg_dict_time /= n     
    assert avg_tuple_time < avg_dict_time , "Dictionary time is greater than Tuple check your program"
    print("Average Time taken by tuples for processing",avg_tuple_time)
    print("Average Time taken by Dictionary for processing", avg_dict_time)
    print("Tuples are faster than dictionary")


# Task 3 - 11 tests

# tuple_result
def test_stock_result():
    # result for seed 0
    result_1, company_stock_list, time_1 = session9.faker_stock_exchange(0, 100)    
    assert result_1.Open == 897359.4830000001 , "its not correct answer for random seed 0"
    assert result_1.High == 966470.362 , "its not correct answer for random seed 0"
    assert result_1.Close == 913638.14 , "its not correct answer for random seed 0"
    print("Open, High, Close results are matching for random seed 0")

# check named_tuple is used
def test_namedtuples_stock():
    def isnamedtupleinstance(x):
        t = type(x)
        b = t.__bases__
        if len(b) != 1 or b[0] != tuple: return False
        f = getattr(t, '_fields', None)
        if not isinstance(f, tuple): return False
        return all(type(n)==str for n in f)

    result, company_stock_list, time = session9.faker_stock_exchange(0, 10)    
    assert isnamedtupleinstance(result) == True , "result is not a instance of named tuple"
    print("Result is a instance of named tuple")

# 10, 100
def test_stock_profile_generation_function():
    result_1, company_stock_list_1, time_1 = session9.faker_stock_exchange(0, 10)
    result_2, company_stock_list_2, time_2 = session9.faker_stock_exchange(0, 100)
    assert len(company_stock_list_1) == 10 , "Generator is not generating specified no of profile , Dont hard code"
    assert len(company_stock_list_2) == 100, "Generator is not generating specified no of profile , Dont hard code"
    print("Function is generating specified number of profiles properly")

# input type, seed
def test_input_argument_stock():
    with pytest.raises(TypeError):
        session9.faker_stock_exchange(0, 'forty')
    with pytest.raises(TypeError):
        session9.faker_stock_exchange('zero', 10)
    print("Type error is raised for a string input to number of profiles and when given to seed value")

# fields
def test_stock_fields_result():
    result, company_stock_list, time = session9.faker_stock_exchange(0, 10)
    assert result._fields == ("Open","High", "Close", ) , "Please check the field names"
    print("Result contains desired number of fields as per requirement")

# fields check
def test_stock_fields_company_stock_list():
    result, company_stock_list, time = session9.faker_stock_exchange(0, 10)    
    assert company_stock_list[0]._fields == ("Company","Symbol","Price","Open","High", "Close") , "Please check the field names"
    print("Company stock contains fields as per requirement")

# named tuple check
def test_namedtuples_company_stock_list():
    def isnamedtupleinstance(x):
        t = type(x)
        b = t.__bases__
        if len(b) != 1 or b[0] != tuple: return False
        f = getattr(t, '_fields', None)
        if not isinstance(f, tuple): return False
        return all(type(n)==str for n in f)

    result, company_stock_list, time = session9.faker_stock_exchange(0, 10)
    assert isnamedtupleinstance(company_stock_list[0]) == True , "profile is not a instance of named tuple"
    print("Company Stocks is a instance of named tuple")

# high is greater than open
def test_stockfieldsresult():
    result, company_stock_list, time = session9.faker_stock_exchange(0, 10)
    assert result.Open < result.High , "Open is higher than High"
    assert company_stock_list[0].Open < company_stock_list[0].High , "Open is higher than High"
    print("High is higher than open for seed 0")

# time 
def test_stock_time():
    result_1, company_stock_list_1, time_1 = session9.faker_stock_exchange(0, 10)
    result_2, company_stock_list_2, time_2 = session9.faker_stock_exchange(0, 5000)    
    assert time_1 < time_2 , "Something is fishy"
    print("Input for n=10 is running in less time than input of 5000")

# open,high, low are different and random
def test_stockfields_result():
    result, company_stock_list, time = session9.faker_stock_exchange(0, 10)
    assert result.Open != result.High  != result.Close , "Your Stock exchange is hard coded"
    assert company_stock_list[0].Open != company_stock_list[0].High != company_stock_list[0].Close , "Your Stock exchange is hard coded"
    print("Open , High, Close values are not same and they are ranodom")

def test_stockdocstring():
    result, company_stock_list, time = session9.faker_stock_exchange(0, 10)
    assert len(result.__doc__) > 3 , "Add doc strings to named tuple"
    assert len(company_stock_list[0].__doc__) > 3 , "Add doc strings to named tuple"
    print("Named tuple contains doc strings")

