screen_helper = '''
<ContentNavigationDrawer>:

    ScrollView:
    
        MDList:
        
            OneLineListItem:
                text: "Home"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "home"
                    
            OneLineListItem:
                text: "Plan"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "plan"
                    
            OneLineListItem:
                text: "Locations"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "location"
                                
            OneLineListItem:
                text: "Route"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "route"
                    
            OneLineListItem:
                text: "Saved"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "saved"
                    
          
<HomeScreen>:
    name: "home"
    
    FloatLayout:
        
        MDLabel:
            text: "Welcome to the trip planner!"
            theme_text_color: "Custom"
            text_color: 1, 214/255, 0, 1
            pos_hint: {'center_x': 0.52, 'center_y': 0.95}
            
        MDLabel:
            text: ("This planner can be used when planning out a trip spanning a few days, \
or even when just finding the optimal path to run errands.")
            theme_text_color: "Custom"
            text_color: 1, 214/255, 0, 1
            pos_hint: {'center_x': 0.52, 'center_y': 0.8}
            
        MDLabel:
            text: ("To use the planner, simply input the addresses of the places you wish to visit, \
and the planner will calculate the most efficient path using Google maps.")
            theme_text_color: "Custom"
            text_color: 1, 214/255, 0, 1
            pos_hint: {'center_x': 0.52, 'center_y': 0.58}
            
        MDLabel:
            text: ("If you wish to save a location simply click the star in the planning screen before \
adding it.")
            theme_text_color: "Custom"
            text_color: 1, 214/255, 0, 1
            pos_hint: {'center_x': 0.52, 'center_y': 0.38}
            
        MDRectangleFlatButton:
            text: "Start Planning!"
            on_press: root.manager.current = "plan"
            pos_hint: {'center_x': 0.5, 'center_y': 0.1}
            
<PlanScreen>:
    id: plan
    plan: plan
    address: address
    name: "plan"
    
    FloatLayout:
        padding: '10dp'
        orientation: 'vertical'
        
        MDTextField:
            id: address
            hint_text: 'Enter starting location'
            color_mode: 'primary'
            size_hint: (0.9, None)
            height: 30
            multiline: True
            pos_hint: {'center_x': 0.5, 'center_y': 0.55}
            
        MDFloatingActionButton:
            icon: 'plus'
            pos_hint: {'center_x': 0.35, 'center_y': 0.4}
            on_release: root.add_location()
            
        MDFloatingActionButton:
            icon: 'star'
            pos_hint: {'center_x': 0.65, 'center_y': 0.4}
            on_release: root.favourite_location()
            
        MDRectangleFlatButton:
            text: "View locations"
            pos_hint: {'center_x': 0.75, 'center_y': 0.07}
            on_release: root.manager.current = "location"
            
<LocationScreen>:
    id: location
    location: location
    name: "location"
    
    FloatLayout:
        
        ScrollView:            
            size_hint: (1, 0.7)
            pos_hint: {'y': 0.3}
            
            MDList:
                id: locationsList
                pos_hint: {'top': 1}
                
        MDFillRoundFlatIconButton
            icon: "send"
            text: "Start Planning!"
            pos_hint: {'center_x': 0.5, 'center_y': 0.2}
            on_release: root.path()
        
        MDRectangleFlatButton:
            text: "Return"
            pos_hint: {'center_x': 0.81, 'center_y': 0.07}
            on_release: root.manager.current = "plan"
        
        MDRectangleFlatButton:
            text: "Clear"
            pos_hint: {'center_x': 0.19, 'center_y': 0.07}
            on_release: root.clear()          
                
<RouteScreen>:
    id: route
    name: "route"
         
    FloatLayout:
        MDLabel:
            text: "Proceed in the following order:"
            pos_hint: {'center_x': 0.52, 'center_y': 0.95}
            theme_text_color: "Custom"
            text_color: 1, 214/255, 0, 1
            
        ScrollView:            
            size_hint: (9, 0.7)
            pos_hint: {'y': 0.2}
            
            MDList:
                id: routeList
                pos_hint: {'top': 1}
        
        MDLabel:
            text: root.msg
            pos_hint: {'center_x': 0.55, 'center_y': 0.1} 
            theme_text_color: "Custom"
            text_color: 1, 214/255, 0, 1
            
                    
<SavedScreen>:
    id: saved
    name: "saved"
    
    FloatLayout:
    
        ScrollView:
        
            MDList:
                id: savedList
                pos_hint: {'top': 1}
            
Screen:
    
    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "Trip Planner"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
        
    NavigationLayout:
        x: toolbar.height
        size_hint_y: 1.0 - toolbar.height/root.height
        
        ScreenManager:
            id: screen_manager
            
            HomeScreen:
            
            PlanScreen:
            
            LocationScreen:
            
            RouteScreen:
            
            SavedScreen:
            
            
        MDNavigationDrawer:
            id: nav_drawer
            
            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''
