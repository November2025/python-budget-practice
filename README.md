# Python Budget Exercise
 
### Scenario
With the upcoming year, your friend has made a resolution to be mindful with the amount of money they spend and stop impulse purchases. Knowing your skills with Python, they have asked you to assist them.

Your friend has given you their regular expenses, income, and wishlist. Using these, they want to know how much they can save over the year. Through that savings, they also want to know how long it will take them to be able to afford their wish list and what order they can purchase their wish items the quickest from their savings.

### Receivables
Your friend is paid every two weeks as indicated in the file "income.csv". You are provided the type of income, the amount, the frequency (how far apart), the time measure (days, weeks, months, years, etc), and what day of the week if applicable. In this case, your friend is paid a salary of $2,167.42 every 2 weeks on Friday.

Their expenses are listed in "bills.csv". You are given the type of expense, the amount, the frequency, the time measure, what month (if applicable in yearly payments), what day of the week (if applicable in weekly payments), and what day (as applicable in monthly payments). Assume in February that any bills typically due on the 29th or later are due on the 28th.

### Budget Strategy
The way your friend wishes to budget their expenses is below. Assume they are starting the year with $3,000 in their checking account, nothing in their savings account, and their first paycheck is on the second Friday of the year.
- Anything on the expenses list is prioritized over anything else.
- After expenses are counted for in each pay, 10% of the remaining amount goes to savings.
- After moving to savings, they wish for the remaining in their checking account to be divided up using the following each pay period:
  - Groceries: $200.00
  - Eating out: 20%
  - Pet supplies: $50.00
  - Gas: $100.00
  - Travel fund: $50.00 (Set aside for future use)
  - Misc: 20%
- At the end of the pay period, if your friend has more than $700 in their checking account after expenses and remaining budget, they will move another $500 to their savings account.
- If for some reason your friend's checking account is overdrafted, then they will immediately transfer the overdraft amount plus $25 into their checking account from their savings account.
  - In the case they do not have any money in savings, your friend can not transfer anything in and must take an additional overdraft fee into their checking account of $30.00.

### Wishlist Purchases
Your friend only desires to purchase something from their wish list if the cost of the item is at most 20% of the amount in their savings account at the beginning of a pay period.

### Methodology
Your code should submitted in a .py file. Be sure to leave comments so the reader knows what you're doing!

I would recommend creating a Jupyter Notebook to document your thought process and breaking down the problem. If you desire, one has been included with some guiding questions.

[Notes on importing and using CSV values in Python](https://python-forum.io/thread-28366.html)