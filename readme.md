# Canoe Take Home Assessment

## Question 1

### INSTRUCTIONS
*Inside the folder titled `Question 1` you will find two SQL files. The file titled `create_db_and_data` contains the queries for creating the table and adding test data into them. These queries should be ran first. The second file titled `query` contains the actual queries to organize the data. These queries should be ran after the database has been created and populated with test data.*

### THOUGHTS
This was an interesting question, with many different potential approaches to take. I ultimately decided to use SQL, and came to a solution using PostGreSQL and a little bit of Python. After creating the database and tables, the first real challenge was generating enough test data to simulate a real world scenario as outlined in the problem. With every game loser putting in only $10 it would take a little while until the ultimate goal of $800 was reached. 

Pythons random module was a huge help here and with the following code I was able to quickly and easily generate 100 unique employee IDs, then pick from that pool of employee IDs to generate 200 random selections with duplicates to use as potential players in the game nights, and 200 random selections of either `TRUE` or `FALSE` for whether or not they were winners:   

```
def generator(int):
    # generate 100 unique employee IDs
    numlist = random.sample(range(1, 101), 100)
    print("INITIAL LIST OF EMPLOYEES")
    for i in numlist:
        print(f'{i}')
    # pick from pool of employee IDs to generate 200 random selections with duplicates 
    employee_list = random.choices(numlist, k=int)
    print("RANDOM EMPLOYEE IDS WITH DUPLICATES")
    for i in employee_list:
        print(i)
    # generate 200 random selections of either `TRUE` or `FALSE`
    torf = ['true', 'false']
    torf_list = random.choices(torf, k=int)
    print("RANDOM TRUE OR FALSE")
    for i in torf_list:
        print(i)
generator(200)
```

The code above does result in certain employee IDs being potentially repeated multiple times per game. In a real world scenario, this would not happen as no employee would play in the same game twice. For the purposes of generating test data for this problem, I decided that some repetitions would be okay. 

The second challenge was organizing the data in a way that would return the results I needed. 
One key point to track was which employees had lost per game. This would give me the total amount contributed towards the prize pot for that game. Adding these into its own column using an `OVER` clause would give me a running tally of the current prize pot, and a boolean column called `party_next` could keep track of whether or not the pot was greater than or equal to $800. If it was, then it would return `TRUE`, meaning the next event would be a party and not a game. Otherwise it would return `FALSE`. This effectively estimates when the pot will be full. 

Adding $10 for every game loser and removing $800 from the prize pot to reset it are both handled by multiple `CASE` statements. If activity type is game and the boolean column that tracks whether or not an employee is a winner for that game returns `FALSE` then a 1 is returned and counted by a `COUNT` function then multiplied by 10 to stand for the $10 put in by game loser. Otherwise the activity type is party and 800 is subtracted. These are all then organized using a `GROUP BY` statement, giving us everything we need to keep track of game activities, results, players, and pot money. 

## QUESTION 2
### THOUGHTS
This was a fairly straightforward question. I've included everything that I believe should be in a test plan, i.e) a brief introduction, test scope, assumptions/risks, testing approach, testing environments and of course, deliverables. Some of these fields may be blank or include assumptions, as the question only provided the features to be tested and stressed that stability be a focal point of testing, but I've left the fields in to give the most accurate representation of what I believe should be in a test plan. 

## QUESTION 3
### THOUGHTS
These test cases were written with the assumption that all requirements have been agreed on prior to testing, as they would be in a real world test scenario. 

#### EVENT PAGE
1. Verify that items in hamburger menu are displayed as expected
2. Verify that "More Info" button is working as expected
3. Verify that event text is being displayed as expected
4. Verify that "Sign In" button is working as expected
5. Verify that quantity buttons are working as expected
6. Verify that price slider is working as expected
7. Verify that user is able to filter by type
8. Verify that handicap filter is working as expected
9. Verify that reset button is working as expected
10. Verify that layout zoom buttons are working as expected 
11. Verify that layout zoom reset button is working as expected
12. Verify that able to switch between lowest price and best seats 
#### ORDER PAGE
13. Verify that event text is being displayed properly at top of order page
14. Verify that order countdown is working as expected
15. Verify that "Learn More" button is working as expected
16. Verify that parking information is displayed properly, with correct locations
17. Verify that one or multiple parking passes are able to be added as expected
18. Verify that order details dropdown is working as expected
19. Verify that order total is displayed properly
20. Verify that "Next" button is working as expected