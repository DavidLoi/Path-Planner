from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import requests
import itertools
import math
import urllib3

from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

import helpers

# Size of app
Window.size = (300, 500)

# List of locations
locations = []

# API key
api_key = "AIzaSyBPxKHzJxJ64K1p11DyoHHP8EGDZtON4yg"


# Navigation toolbar
class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


# Home screen
class HomeScreen(Screen):
    pass


count = 0


# Plan screen
class PlanScreen(Screen):
    plan = ObjectProperty()

    # Function to add location from plan screen to locations screen
    def add_location(self):
        location = self.ids.address.text
        if location != "":
            global count
            count += 1
            if count == 1:
                self.ids.address.hint_text = "Enter ending location"
            elif count > 1:
                self.ids.address.hint_text = "Enter additional locations"
            MDApp.get_running_app().root.ids.screen_manager.get_screen(
                "location"
            ).ids.locationsList.add_widget(OneLineListItem(text=location))
            locations.append(location)
            self.ids.address.text = ""

    # Function to add location from plan screen to saved screen
    def favourite_location(self):
        location = self.ids.address.text
        MDApp.get_running_app().root.ids.screen_manager.get_screen(
            "saved"
        ).ids.savedList.add_widget(OneLineListItem(text=location))

# Location screen
class LocationScreen(Screen):
    location = ObjectProperty()

    # Function to calculate shortest distance path
    def path(self):
        if len(locations) >= 2:
            start = locations[0]
            end = locations[1]

            if len(locations) > 1:
                # Base url
                url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=" + start

                # Adding additional roots
                for i in range(2, len(locations)):
                    url += "|" + locations[i]

                # Adding destinations
                url += "&destinations=" + end

                # Adding additional destinations
                for i in range(2, len(locations)):
                    url += "|" + locations[i]

                # Avoiding tolls
                url += "&avoid=tolls"

                # Get response
                r = requests.get(url + "&key=" + api_key)

                # Generate sequences for each possible path
                nums = range(len(locations))
                sequences = (list(itertools.permutations(nums[1:-1])))
                best = float('inf')
                route = []
                print(sequences)

                # Determine fastest path amongst sequences
                for i in sequences:
                    time = 0
                    curr = 0
                    for n in i:
                        print(r.json())
                        time += r.json()['rows'][curr]['elements'][n]['duration']['value']
                        curr = n
                    time += r.json()['rows'][curr]['elements'][0]['duration']['value']

                    # Save fastest path
                    if time < best:
                        route = i
                        best = time

                print(best)

                hours = math.floor(best / 3600)
                print(hours)
                best -= hours * 3600
                print(best)

                minutes = math.floor(best / 60)
                best -= minutes * 60
                print(best)

                seconds = best
                print(seconds)

                # Returns ideal route and total travel time
                print(route, best)

                MDApp.get_running_app().root.ids.screen_manager.get_screen(
                    "route"
                ).ids.routeList.add_widget(OneLineListItem(text=locations[0]))

                for i in route:
                    MDApp.get_running_app().root.ids.screen_manager.get_screen(
                        "route"
                    ).ids.routeList.add_widget(OneLineListItem(text=locations[i + 1]))

                MDApp.get_running_app().root.ids.screen_manager.get_screen(
                    "route"
                ).ids.routeList.add_widget(OneLineListItem(text=locations[1]))

                self.manager.get_screen("route").msg = "Estimated travel time is " + str(hours) + " hours, " + str(minutes)\
                                                       + " minutes, and " + str(seconds) + " seconds!"

                self.manager.current = "route"

    def clear(self):
        global locations
        locations = []
        self.ids.locationsList.clear_widgets()
        MDApp.get_running_app().root.ids.screen_manager.get_screen(
            "plan").ids.address.hint_text = "Enter starting location"
        global count
        count = 0

# Saved screen
class SavedScreen(Screen):
    pass

# Route Screen
class RouteScreen(Screen):
    msg = StringProperty()


# Adding screens to screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(PlanScreen(name='plan'))
# sm.add_widget(SavedScreen(name='saved'))
sm.add_widget(RouteScreen(name='root'))


# Main app
class MainApp(MDApp):
    def build(self):
        # Color theme of app
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"

        # Loading kivy file
        return Builder.load_string(helpers.screen_helper)


# Run app
MainApp().run()
