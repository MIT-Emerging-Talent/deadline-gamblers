
class BrowserHistory:
    def __init__(self, homepage: str):
        """
        Initializes a new BrowserHistory instance with the given homepage.

        Parameters:
        - homepage (str): The URL of the homepage.

        :param homepage: str
        """
        # List to store visited url webpages
        self.urls_history= [homepage]
        # current position index
        self.index= 0

    def visit(self, url: str) -> None:
        """
        :param url: str -  The url of webpage
        :return: None
        I tried another solution but since the test cases are fixed
        , I could not change the function storing way
        """
        self.urls_history = self.urls_history[: self.index + 1]
        # append new webpage
        self.urls_history.append(url)

        # increase webpage index
        self.index = len(self.urls_history) -1

    def back(self, steps: str) -> str:
        """
        :param steps: the backward steps
        :return: string - current url webpage after moving backward
        """
        # go backward # steps, but not  further than 0 (worst case)
        self.index = max(0, self.index - steps)

        # return the new webpage url
        return self.urls_history[self.index]

    def forward(self, step: int) -> str:
        """
        :param step:the forward steps
        :return:string - current url webpage after moving forward
        """
        # move forward # steps, limited by the last index
        self.index = min(len(self.urls_history)-1, self.index + step)

        ## return the new webpage url
        return self.urls_history[self.index]
