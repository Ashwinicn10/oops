class InstagramAccount:
    def __init__(self, account_name, password):
        self.account_name = account_name

        self._private_reels = []

        self.__archived_reels = []
        self.__password = password

    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)

    def display_private_reels(self, is_follower):
        if is_follower:
            print("\nPrivate Reels:")
            for reel in self._private_reels:
                print("-", reel)
        else:
            print("\nAccess Denied! Only followers can view private reels")

    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)

    def display_archived_reels(self, password):
        if password == self.__password:
            print("\nArchived Reels:")
            for reel in self.__archived_reels:
                print("-", reel)
        else:
            print("\nAccess Denied! Only account holder can view archived reels")

    # Getter for archived reels
    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied! Wrong password"

    # Setter to update password
    def set_password(self, new_password):
        self.__password = new_password
        print("\nPassword updated successfully!")

insta = InstagramAccount("ashwini_cn", "insta123")
# Add private reels
insta.add_private_reel("Private Reel 1: Morning Vlog")
insta.add_private_reel("Private Reel 2: Family Time")
# Add archived reels
insta.add_archived_reel("Archived Reel 1: College Days")
insta.add_archived_reel("Archived Reel 2: Old Travel Video")
# Display private reels
insta.display_private_reels(is_follower=True)
insta.display_private_reels(is_follower=False)
# Display archived reels 
insta.display_archived_reels("wrongpass")
insta.display_archived_reels("insta123")
# Update password
insta.set_password("newpass456")
# Check archived reels again
insta.display_archived_reels("insta123")
insta.display_archived_reels("newpass456")