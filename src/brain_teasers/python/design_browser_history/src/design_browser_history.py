class BrowserHistory:
   def __init__(self, start_url):
       """
       Initializes a new instance of the class.

       Args:
           start_url (str): The starting URL of the instance.
       """
       self.history = [start_url]
       self.current_position = 0

   def visit(self, url):
       """
       Updates the browser history with a new URL.

       Args:
           url (str): The URL to be added to the browser history.

       Returns:
           None
       """
       self.history = self.history[:self.current_position + 1]
       self.history.append(url)
       self.current_position += 1

   def back(self, steps):
       """
       Decreases the current position in the history list by the specified number of steps.

       Parameters:
           - steps (int): The number of steps to move backwards in the history list.

       Returns:
           - The item in the history list at the updated current position.
       """
       self.current_position = max(self.current_position - steps, 0)
       return self.history[self.current_position]

   def forward(self, steps):
       """
       Move the current position forward by the specified number of steps.

       Parameters:
           steps (int): The number of steps to move forward.

       Returns:
           The element at the updated current position in the history.
       """
       self.current_position = min(self.current_position + steps, len(self.history) - 1)
       return self.history[self.current_position]
