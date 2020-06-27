import numpy as np
import random as rm

# The statespace
states = ["Sunny","Rain","Cloudy"]

# Possible sequences of events
transitionName = [["SS","SR","SC"],["RS","RR","RC"],["CS","CR","CC"]]

# Probabilities matrix (transition matrix)
###missing codes below here
transitionMatrix=[[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]]


if sum(transitionMatrix[0])+sum(transitionMatrix[1])+sum(transitionMatrix[2]) != 3:
    print("Transition matrix went wrong")
else: print("Transition matrix is ok!!")

# A function that implements the Markov model to forecast the state.
def activity_forecast(days):
    # Choose the starting state
    activityToday = "Sunny"
    print("Start state: " + activityToday)
    # Shall store the sequence of states taken. So, this only has the starting state for now.
    activityList = [activityToday]
    i = 0
    # To calculate the probability of the activityList
    prob = 1
    while i != days:
        if activityToday == "Sunny":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            if change == "SS":
                prob = prob * 0.2
                activityList.append("Sunny")
                pass
            elif change == "SR":
                prob = prob * 0.6
                activityToday = "Rain"
                activityList.append("Rain")
            else:
                prob = prob * 0.2
                activityToday = "Cloudy"
                activityList.append("Cloudy")
        elif activityToday == "Rain":
            ###missing codes below here
            if change == "SS":
                prob = prob * 0.1
                activityList.append("Sunny")
                pass
            elif change == "SR":
                prob = prob * 0.6
                activityToday = "Rain"
                activityList.append("Rain")
            else:
                prob = prob * 0.3
                activityToday = "Cloudy"
                activityList.append("Cloudy")



        elif activityToday == "Cloudy":
            ###missing codes below here
            if change == "SS":
                prob = prob * 0.2
                activityList.append("Sunny")
                pass
            elif change == "SR":
                prob = prob * 0.7
                activityToday = "Rain"
                activityList.append("Rain")
            else:
                prob = prob * 0.1
                activityToday = "Cloudy"
                activityList.append("Cloudy")




        i += 1
    print("Possible states: " + str(activityList))
    print("End state after "+ str(days) + " days: " + activityToday)
    print("Probability of the possible sequence of states: " + str(prob))
    return activityList

# Function that forecasts the possible state for the next 2 days
activity_forecast(2)

print("-----end for 2 day forecast----")
'''
def activity_forecast(days):
    # Choose the starting state
    ###missing codes below here


        i += 1
    return activityList
'''

# To save every activityList
list_activity = []
count = 0

# `Range` starts from the first count up until but excluding the last count
for iterations in range(1,10000 ): #10000):
        list_activity.append(activity_forecast(2))

# Check out all the `activityList` we collected
#print(list_activity)

# Iterate through the list to get a count of all activities ending in state:'Rain'
for smaller_list in list_activity:
    if(smaller_list[2] == "Rain"):
        count += 1

# Calculate the probability of starting from state:'Sunny' and ending at state:'Rain'
percentage = count/100

print("The probability of starting at state:'Sunny' and ending at state:'Rain' after 10,000 iterations= " + str(percentage) + "%")
