# Path-Planner
This app uses the google distance matrix api to find the most optimal path between a starting location, any additional locations inbetween and an ending location. A feature to save locations will be added in soon to allow users to save locations they frequent often to make the app more convenient as a whole.

# Motivation
I created this app because going on drives around town with my friends made me think about how much time we spent picking up and dropping everyone off. Especially since my friends and I are quite spread out, I always wondered what would be the fastest route for us to take to save on time and gas money.

# Screenshots
The home screen provides a brief description of the app and explains to the user how to use it, as well as basic navigation around the app.

![Home Screen](https://github.com/DavidLoi/Path-Planner/blob/main/Screenshots/HomeScreen.PNG)

This is the navigation drawer which can be accessed by clicking the three horizontal lines in the top left of the window. It allows the user to access the Home, Plan, Locations, Route, and Saved screens.

![Navigation](https://github.com/DavidLoi/Path-Planner/blob/main/Screenshots/Navigation.PNG)

# How to use?
To begin planning your route, click the "Start Planning!" button on the home screen or navigate to the Plan screen through the navigation drawer.

The textfield will then ask the user to input their starting address, which is where the trip begins. After entering a location click the plus button to add the location to the route, this will then clear the textfield.
** Note: If the textfield is empty, the plus button will do nothing.

![Starting Location](https://github.com/DavidLoi/Path-Planner/blob/main/Screenshots/StartingLocation.PNG)

Then the user will be prompted to enter their ending address, which is where the trip ends.

![Ending Location](https://github.com/DavidLoi/Path-Planner/blob/main/Screenshots/EndingLocation.PNG)

Then the user will be prompted to enter the address of any additional locations they need to go to before reaching the ending location.

![Additional Location](https://github.com/DavidLoi/Path-Planner/blob/main/Screenshots/AdditionalLocations.PNG)

At any point while adding locations, the user can check what they've already added by navigating to the locations screen.

![Locations Screen](https://github.com/DavidLoi/Path-Planner/blob/main/Screenshots/LocationsScreen.PNG)

If the user made any mistakes when inputting addresses, clicking the "Clear" button will clear the list of locations and clicking the "Return" button will return the user to the Plan screen.

After adding all locations correctly, simply click the "Start Planning!" button and the user will be taken to the Route screen, which will display the order of locations to visit which results in the fastest travel time and it will also display the total travel timie at the bottom (the travel time assumes the user is travelling by car and avoids tolls).
**Note: If there are less than two locations entered, the "Start Planning!" button will do nothing.

The following example shows the optimal path to visit several tourist attractions in Toronto, starting at the Eaton Centre and ending at the CN Tower. If there are more than 7 locations, the user will need to scroll to see the rest of the route.

![Locations1](https://github.com/DavidLoi/Path-Planner/blob/main/Screenshots/Sample1.PNG)
![Locations2](https://github.com/DavidLoi/Path-Planner/blob/main/Screenshots/Sample2.PNG)
![Route1](https://github.com/DavidLoi/Path-Planner/blob/main/Screenshots/Route1.PNG)
![Route2](https://github.com/DavidLoi/Path-Planner/blob/main/Screenshots/Route2.PNG)
