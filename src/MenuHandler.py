import os

class MenuHandler:
    """Handle Menu related tasks"""
    menu = list()

    def clear_menu_options(self):
        """
        Description:
        ------------
        This will clear out the whole menu
        """
        self.menu.clear()

    def add_option(self, option: str):
        """
        Description:
        ------------
        This method add an option into the menu if it is not already exist

        Param:
        ------
        option - A string option that you want to add in the menu
        """
        if option not in self.menu:
            self.menu.append(option)

    def show_menu(self):
        os.system("cls")
        """
        Description:
        ------------
        This method use to show the menu in order that was added
        """
        print("Welcome to our Music Project")
        counter = 1
        for i in self.menu:
            print(f"{counter} {i}")
            counter += 1

    def remove_option(self, option: int):
        """
        Description:
        ------------
        This method will remove an option if it exist.
        
        Param:
        ------
        option - an option number to be remove
        """
        if len(self.menu) >= option and len(self.menu) != 0 and option >= 1:
            self.menu.remove(self.menu[option-1])

    def valid_user_input(self, user: str) -> str:
        """
        Description:
        ------------
        This method will validate user input into cmd for selecting a menu's option.
        Then ask user to type again until correct

        Param:
        ------
        user - user's input string from cmd

        Return:
        -------
        Return the correct user option
        """
        while not user.isdigit():
            user = input("Please enter only integer number: ")
        while int(user) > len(self.menu) or int(user) < 1:
            user = input(f"Please type only integer from 1 to {len(self.menu)}: ")
            
        return user

    def print_help(self):
        os.system("cls")
        print("Type only integer number to select your option. We will display the answer according to the option you entered")
        os.system("pause")
        os.system("cls")
        self.show_menu()

    def default_menu(self):
        """
        Description:
        ------------
        This will create a default menu object

        Return:
        -------
        The default menu
        """
        self.clear_menu_options()
        new_menu = MenuHandler()
        new_menu.add_option(
            "What is the most popular genre global (Spotify)?")
        new_menu.add_option("What is the top song in the US (spotify)?")
        new_menu.add_option("Who is the most listened artist on Spotify?")
        new_menu.add_option("Who are the top artists on Billboard?")
        new_menu.add_option("How many songs does each top artist have on the Billboard top 200 chart?")
        new_menu.add_option("Is the top streamed song the same as the most played song on the radio, according to billboard?")
        #TODO Add more option as you need above!!
        new_menu.add_option("Help")
        new_menu.add_option("Quit")
        return new_menu
