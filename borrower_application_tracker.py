import anvil
from kivy import platform
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
import sqlite3

from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget

# anvil.server.connect("server_VRGEXX5AO24374UMBBQ24XN6-ZAWBX57M6ZDN6TBV")


application_tracker = """

<WindowManager>:
    ApplicationTrackerScreen:

<ALLLoansAPT>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Application Tracker "
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
        MDScrollView:

            MDList:
                id: container 

<ApplicationTrackerScreen>
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDTopAppBar:
            title: "Application status"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.borrower_dashboard()]]

        BoxLayout:
            id: box
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(40)

            MDLabel:
                text: 'Application Received'
                font_size: dp(20)
                bold: True
                size_hint_y: None
                height: 50

            MDLabel:
                text: "Congratulations! Your first loan application with P2P has been received. Please wait while we process the loan. You can check the status here"
                size_hint_y: None
                height: 50


            MDGridLayout:
                cols: 2
                spacing: dp(20)  # Adjust spacing between icon and label

                MDIconButton:
                    id: icon1
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 12/255, 105/255, 171/255, 1
                    size_hint_y: None
                    height: 50

                    canvas:
                        Color:
                            rgba: 12/255, 105/255, 171/255, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)


                MDLabel:
                    id: label1
                    text: "Application for #loanamount sent"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon2
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    size_hint_y: None
                    height: 50

                    text_color: 12/255, 105/255, 171/255, 1
                    canvas:
                        Color:
                            rgba: 12/255, 105/255, 171/255, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)


                MDLabel:
                    id: label2
                    text: "Waiting for approval"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon3
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 12/255, 105/255, 171/255, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 12/255, 105/255, 171/255, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)


                MDLabel:
                    id: label3
                    text: "Loan is approved for #loanamount"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon4
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 12/255, 105/255, 171/255, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 12/255, 105/255, 171/255, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)


                MDLabel:
                    id: label4
                    text: "Loan is under disbursal process"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50


                MDIconButton:
                    id: icon5
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 12/255, 105/255, 171/255, 1
                    size_hint_y: None
                    height: 50


                MDLabel:
                    id: label5
                    text: "Loan credited to a/c xxxxxxxxxxx"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height:dp(50)


"""
Builder.load_string(application_tracker)


class ApplicationTrackerScreen(Screen):

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreen'

    def borrower_dashboard(self):
        self.manager.current = 'ALLLoansAPT'


class ALLLoansAPT(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = self.get_table_data()
        email = self.get_table()
        profile = self.profile()
        customer_id = []
        loan_id = []
        email1 = []
        borrower_name = []
        loan_status = []
        product_name = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['loan_updated_status'])
            product_name.append(i['product_name'])
            email1.append(i['borrower_email_id'])

        profile_customer_id = []
        profile_mobile_number = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])

        cos_id = None  # or any appropriate default value
        index = -1

        if email in email1:
            index = email1.index(email)
            cos_id = customer_id[index]

        # Now you can use cos_id safely
        if cos_id is not None:
            print(cos_id,type(cos_id))
            print(customer_id[-1], type(customer_id[-1]))
            c = -1
            index_list = []
            for i in range(s):
                c += 1
                if customer_id[c] == cos_id:
                    index_list.append(c)

            b = 1
            k = -1
            for i in index_list:
                b += 1
                k += 1
                number = profile_customer_id.index(customer_id[i])
                item = ThreeLineAvatarIconListItem(

                    IconLeftWidget(
                        icon="card-account-details-outline"
                    ),
                    text=f"Borrower Name : {borrower_name[i]}",
                    secondary_text=f"Mobile Number : {profile_mobile_number[number]}",
                    tertiary_text=f"Product Name : {product_name[i]}",
                    text_color=(0, 0, 0, 1),  # Black color
                    theme_text_color='Custom',
                    secondary_text_color=(0, 0, 0, 1),
                    secondary_theme_text_color='Custom',
                    tertiary_text_color=(0, 0, 0, 1),
                    tertiary_theme_text_color='Custom'
                )
                item.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
                self.ids.container.add_widget(item)

    def icon_button_clicked(self, instance, loan_id):
        print(loan_id)
        data = self.get_table_data()  # Fetch data here
        loan_status = None
        for loan in data:
            if loan['loan_id'] == loan_id:
                loan_status = loan['loan_updated_status']
                break

        if loan_status == 'approved':
            # Open the screen for approved loans

            sm = self.manager

            # Create a new instance of the LoginScreen
            approved = ApplicationTrackerScreen(name='ApplicationTrackerScreen')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(approved)

            # Switch to the LoginScreen
            sm.current = 'ApplicationTrackerScreen'
            self.manager.get_screen('ApplicationTrackerScreen')

        elif loan_status == 'under process':
            # Open the screen for pending loans
            sm = self.manager

            # Create a new instance of the LoginScreen
            under_process = ApplicationTrackerScreen(name='ApplicationTrackerScreen')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(under_process)

            # Switch to the LoginScreen
            sm.current = 'ApplicationTrackerScreen'
            self.manager.get_screen('ApplicationTrackerScreen')

        elif loan_status == 'rejected':
            # Open the screen for pending loans
            sm = self.manager

            # Create a new instance of the LoginScreen
            rejected = ApplicationTrackerScreen(name='ApplicationTrackerScreen')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(rejected)

            # Switch to the LoginScreen
            sm.current = 'ApplicationTrackerScreen'
            self.manager.get_screen('ApplicationTrackerScreen')

        elif loan_status == 'closed':
            # Open the screen for pending loans
            sm = self.manager

            # Create a new instance of the LoginScreen
            under_process = ApplicationTrackerScreen(name='ApplicationTrackerScreen')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(under_process)

            # Switch to the LoginScreen
            sm.current = 'ApplicationTrackerScreen'
            self.manager.get_screen('ApplicationTrackerScreen')

        elif loan_status == 'disbursed':
            # Open the screen for pending loans
            sm = self.manager

            # Create a new instance of the LoginScreen
            under_process = ApplicationTrackerScreen(name='ApplicationTrackerScreen')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(under_process)

            # Switch to the LoginScreen
            sm.current = 'ApplicationTrackerScreen'
            self.manager.get_screen('ApplicationTrackerScreen')
        else:
            # Handle other loan statuses or show an error message
            pass

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')
    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')
    def profile(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('profile')

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def refresh(self):
        self.ids.container.clear_widgets()
        self.__init__()

    def go_back(self):
        self.manager.current = 'DashboardScreen'


class WindowManager(ScreenManager):
    pass
