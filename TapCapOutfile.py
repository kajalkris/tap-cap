#Program that randomly picks 5 colors and discards colors that repeat 
#Can work with multiple customers and display names of customers

import random

def main():
    
    again = 'y'
    
    while again == 'y':
        #input customer name
        name=input("Enter name of customer: ")
        print("Customer Name: ", name)
    
        list1=[]
        excluded_list=[]
    
        newList(list1, excluded_list)

        #List of colors to be printed
        print("Colors to be printed:")
        for x in list1:
            print(x,end=' ')
        print()
    
        #List of colors discarded
        print("Repeated Colors(not to be printed):")
        for y in excluded_list:
            print(y,end=' ')
        print()
        
        print("Do you want to add customer?")
        again=input("y=yes, anything else=no: ")
        print()

def newList(list1, excluded_list):
    
    while(len(list1)<5):
        colors=['White', 'Red', 'Orange', 'Blue', 'Green', 'Black', 'Purple', 'Gold']
        list=random.choice(colors)
        if list not in list1:
            list1.append(list)
        else:
            excluded_list.append(list)

main()