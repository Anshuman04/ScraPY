# Logic practice questions

- You will first print the Main Menu to user like below:
    ```bash
      **** MAIN MENU ****
       1. Playing with lists
       2. Playing with strings
       3. Patterns
       4. Exit
    ```
- Last option of the menu will be `Exit`. You code should not exit until user chooses exit from main menu


## Playing with Lists
- When user selects `Playing with lists` from Main Menu, below menu will get printed:
    ```bash
        #### LISTS - SUB-MENU ####
         1. Enter a new list
         2. Search an element in a list
         3. Count elements in a list
         4. Insert element in a list
         5. Remove element from a list
         6. Reverse a list
         7. Exit
    ```
- NOT ALLOWED IN-BUILT FUNCTIONS: `append`, `clear`, `count`, `extend`, `index`, `insert`, `pop`, `remove`, `reverse`, `sort`
- See below to understand working of each

### Enter a new list:
When this option is selected,
- Ask user, what do they want to name the list
- Remember this name somehow
- Ask user how many elements they want to enter
- Take all the elements from user and store in the list. **Remeber you cannot use append function**

### Search an element in a list
When this option is selected,
- Ask user which list they want to search in
    - `In which list you want to search element?: <Print names of all created lists till now>`
- Ask user what element they want to search
    - `Element to search?: <user_will input element here>`
- Ask user which occurence they want to search
    - `Which occurence of element?: `
- If nth occurence is found print below:
    - `Occurence <nth> of your element <actual_element> exists at location <actual_searched_location>`
- If nth occurence not found print below:
    - `Not Found. Sorry!`
- Print lists sub menu back

### Count elements in a list
When this option is selected,
- Ask user which list they want to count in
    - `In which list you want to count element?: <Print names of all created lists till now>`
- Ask user what element they want to count
    - `Element to count?: <user_will input element here>`
- Print number of selected element in selected list:
    - `There are <n> items with a value <actual_user_element>`

### Insert element in a list
When this option is selected,
- Ask user which list they want to insert in
    - `In which list you want to insert element?: <Print names of all created lists till now>`
- Ask the location where do they want to insert
    - `Where do you want to insert the element?: <user_input_for_location>`
- Insert the element at specified location and print below. **Remember location count starts at 0**
    - `Your element is successfully inserted at right location`

### Remove element from a list
When this option is selected,
- Ask user which list they want to remove from
    - `From which list you want to remove element?: <Print names of all created lists till now>`
- Ask user if they want to remove based on element or location:
    - `Do you want to remove based on location or element`
    - You can select your way to take input here like: 0 is location and 1 is element OR, taking the actual string (`element`, `location`) OR, something else
    - If the location doesn't exist for location based or element doesn't exist in element based. Print below:
        - `Unsuccessful deletion. Sorry!`
    - If location based and valid location, delete the element and print below:
        - `Deletion Successful!`
    - If element based and valid element, first check if there are more occurences and print:
        - `There are multiple such elements at locations <locations>`
        - Ask the user which occurence to delete and then delete that occurence, Then after deletion, print below:
            - `Deletion Successful!`
    - If element based and there is only one occurence, delete that element and print below:
        - `Deletion Successful!`

### Reverse a list
When this option is selected,
- Ask user which list they want to reverse
    - `Which list you want to reverse?: <Print names of all created lists till now>`
- Reverse the list and Print below:
    - `Reverse Successful`

### Print a list
When this option is selected,
- Ask user which list they want to print
    - `Which list you want to print?: <Print names of all created lists till now>`
- Print the contents of the list selected. **Remember the list printed here should be updated with all the user operations done before.**





