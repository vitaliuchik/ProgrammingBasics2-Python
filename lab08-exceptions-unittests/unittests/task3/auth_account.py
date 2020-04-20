import auth

# Set up a test user and permission
auth.authenticator.add_user("admin", "adminpass")
auth.authenticator.add_user("vitaliy", "vitaliypass")
auth.authenticator.add_user("bob", "bobpass")
auth.authenticator.add_user("joe", "joepass")

auth.authorizor.add_permission("rename document")
auth.authorizor.add_permission("write in document")
auth.authorizor.add_permission("read document")


class PermissionCannotExists(Exception):
    pass


class Notebook:
    def __init__(self):
        self.username = None
        self.is_admin = False
        self.menu_map = {
            "login": self.login,
            "make admin": self.make_admin,
            "permit user": self.permit, 
            "rename document": self.rename,
            "write in document": self.write_in,
            "read document": self.read,
            "quit": self.quit,
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = auth.authenticator.login(username, password)
            except auth.InvalidUsername:
                print("Sorry, that username does not exist")
            except auth.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username
                self.is_admin = auth.authenticator.users[username].is_admin
                print(username, "sign in successfully")

    def make_admin(self):
        username = input("Input username: ")
        try:
            user = auth.authenticator.users[username]
        except KeyError:
            raise auth.InvalidUsername(username)
        else:
            if self.is_admin:
                user.is_admin = True
                print(username, "becomes admin")
            else:
                raise auth.NotPermittedError(username)

    def permit(self):
        permission = input("Permission: ")
        username = input("Username: ")
        if permission != 'rename document' and \
        permission != 'write_in document' and permission != 'read document':
            raise PermissionCannotExists
        else:
            if not self.is_admin:
                raise auth.NotPermittedError(username)
            else:
                auth.authorizor.permit_user(permission, username)
                print(username, "can", permission)

    def is_permitted(self, permission):
        try:
            auth.authorizor.check_permission(permission, self.username)
        except auth.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except auth.NotPermittedError as e:
            print("{} cannot {}".format(e.username, permission))
            return False
        else:
            return True

    def rename(self):
        if self.is_permitted("rename document"):
            print("Renaming document now...")

    def write_in(self):
        if self.is_permitted("write in document"):
            print("Writing in document now...")

    def read(self):
        if self.is_permitted("read document"):
            print("Reading document now...")

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ""
            while True:
                print(
                    """
Please enter a command:
\tlogin\tLogin
\tmake admin\tMake the admin
\tpermit user\tGive the permission for user
\trename document
\twrite in document
\tread document
\tquit\tQuit
"""
                )
                answer = input("enter a command: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for testing the notebook's auth")


Notebook().menu()
