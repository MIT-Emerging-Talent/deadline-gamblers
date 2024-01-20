# Broswer History  
This modue contains the BrowserHistory class that provides a simple way to simulate a browser's history functionality. It allows you to visit new URLs, navigate backward and navigate forward through the history.



## Examples
Here are some examples of how to use each method in the BrowserHistory class:






```python
# Initialize a new BrowserHistory object with 'http://google.com' as the start_url
browser = BrowserHistory('http://google.com')

# Visit a new URL
browser.visit('http://stackoverflow.com')

# Go back one step in the history
print(browser.back(1)) # Outputs: 'http://google.com'

# Go forward one step in the history
print(browser.forward(1)) # Outputs: 'http://stackoverflow.com'

# Visit another new URL
browser.visit('http://github.com')

# Go back two steps in the history
print(browser.back(2)) # Outputs: 'http://google.com'

# Go forward two steps in the history
print(browser.forward(2)) # Outputs: 'http://github.com'

```
In these examples, we first create a BrowserHistory object with 'http://google.com' as the start_url. We then visit 'http://stackoverflow.com', go back one step to 'http://google.com', and go forward one step to 'http://stackoverflow.com'. We then visit 'http://github.com', go back two steps to 'http://google.com', and go forward two steps to 'http://github.com'.


## Approach

The BrowserHistory class simulates a browser's history functionality. Here's an explanation of each method:

- `__init__(self, start_url)`: Initializes a new instance of the class, setting the starting URL and creating an empty history list.
- `visit(self, url)`: Updates the browser history with a new URL by appending it to the history list and incrementing the current position.
- `back(self, steps)`: Decreases the current position in the history list by the specified number of steps and returns the item at the updated position.
- `forward(self, steps)`: Moves the current position forward by the specified number of steps and returns the item at the updated position.


## Unittest results
test command:
```
design_browser_history % python3 -m unittest discover -v
```

results:

```
test_1 (tests.test_design_browser_history.TestDesignBrowserHistory.test_1) ... ok
test_2 (tests.test_design_browser_history.TestDesignBrowserHistory.test_2) ... ok
test_3 (tests.test_design_browser_history.TestDesignBrowserHistory.test_3) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```


## Author

Abed Hamami