import random
import webbrowser
from datetime import datetime
from datetime import timedelta
from datetime import date

service = input("Enter the service you'd like (ex. First-Class Mail, First-Class Package, or USPS Retail Ground): ")
weight = float(input("How much does your package weigh (ex. 4.45)?: "))
if service == "First-Class Mail":
    cost = weight * .55

if service == "First-Class Package":
        cost = weight * 4.00

if service == "USPS Retail Ground":
    cost = weight * 7.70

print("your cost is", format(cost, ".2f"))
name = input("Input your first name (ex. Sam): ")
tracking = input("Input your address so we can give you a tracking number: ")
tracking_num = random.randint(1000000000000000000000, 2000000000000000000000)
print("Here is the tracking number you will use to track your package: ", tracking_num)
webbrowser.open("https://www.usps.com/")
print("USPS website open in new tab for easy access")

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Time order was recieved by USPS (military time): ", current_time)
print("please remember to visit the USPS site for more package information")
queue = ["Billy", "John", "Sean", "Jake", "Ryan"]
print("Order Processing...")
queue.append(name)
print("Virtual queue: ", queue)
queue.pop(0)
print("Virtual queue: ", queue)
queue.pop(0)
print("Virtual queue: ", queue)
queue.pop(0)
print("Virtual queue: ", queue)
queue.pop(0)
print("Virtual queue: ", queue)
queue.pop(0)
print("Virtual queue: ", queue)
queue.pop(0)
print("Virtual queue: ", queue)
print("Order processed!")
start_date = date.today()
dt = datetime.now()
td = timedelta(days=4)
my_date = dt + td
end_date = my_date

print("Expect order from" ,start_date, "on: ", end_date)
print("Thank you for your bussiness! Goodbye!")
