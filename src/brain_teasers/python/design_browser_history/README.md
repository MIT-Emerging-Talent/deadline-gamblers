
---
##BrowserHistory Class

The `BrowserHistory` class is a Python implementation of a basic browser history tracking system. It enables navigation between webpages, keeping track of visited URLs, and supports backward and forward movements within the history.

### Class Initialization

#### Constructor:

```python
def __init__(self, homepage: str):
    """
    Initializes a new BrowserHistory instance with the given homepage.

    Parameters:
    - homepage (str): The URL of the homepage.

    :param homepage: str
    """
```

- **`homepage` (str):** The URL of the homepage to initialize the browser history.

- **`urls_history` (List[str]):** A list to store visited URL webpages.

- **`index` (int):** The current position index in the history.

### Methods

#### `visit(url: str) -> None`

```python
def visit(self, url: str) -> None:
    """
    :param url: str - The URL of the webpage
    :return: None
    I tried another solution but since the test cases are fixed,
    I could not change the function storing way
    """
```

- **`url` (str):** The URL of the webpage to be visited.

- **Return:** None

- **Description:** Adds a new webpage to the history. It truncates the history after the current index and appends the new URL. The index is then updated to the last position in the history.

#### `back(steps: int) -> str`

```python
def back(self, steps: int) -> str:
    """
    :param steps: int - The backward steps
    :return: str - Current URL webpage after moving backward
    """
```

- **`steps` (int):** The number of steps to move backward.

- **Return:** str - The URL of the current webpage after moving backward.

- **Description:** Moves backward in the history by the specified number of steps, but not beyond the first webpage. Returns the URL of the current webpage after moving backward.

#### `forward(steps: int) -> str`

```python
def forward(self, steps: int) -> str:
    """
    :param steps: int - The forward steps
    :return: str - Current URL webpage after moving forward
    """
```

- **`steps` (int):** The number of steps to move forward.

- **Return:** str - The URL of the current webpage after moving forward.

- **Description:** Moves forward in the history by the specified number of steps, limited by the last index in the history. Returns the URL of the current webpage after moving forward.

---