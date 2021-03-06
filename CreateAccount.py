import Command

class CreateAccount(Command.Command):

    def __init__(self, database):
        self.database = database
    """
        args is a list containing the following:
            ["create_account", username, password, role]
    """
    def action(self, args, user):
        if user is None:
            print("You must be logged in to perform this action.")
            return None

        if user.get_role() is "instructor" or user.get_role() is "TA":
            print("Permission Denied")
            return user

        if len(args) != 4:
            print("Invalid Arguments")
            return user

        if not self.isUnigueUser(args[2]):
            print("Username is already taken.")
            return user

        if not self.isValidRole(args[3]):
            print("Invalid Role")
            return user

        self.database.create_account(args[1], args[2], args[3])

        print("Account Created Successfully")
        return user

    def isUnigueUser(self, name):
        accounts = self.database.get_accounts()
        for account in accounts:
            if account["name"] == name:
                return False
        return True

    def isValidRole(self, role):
        roles = ["supervisor", "administrator", "instructor", "TA"]
        for item in roles:
            if role == item:
                return True
        return False
