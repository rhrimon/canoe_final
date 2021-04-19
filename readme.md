# Canoe Final Assessment

### INSTRUCTIONS
In the terminal, run the following command in the `final_tests` directory: `docker build -t test .` 
This will build the docker image from the provided dockerfile. I've chosen the name *test* but this can be anything you choose. Once the image has been built, run the following command: `docker run -it test`

## Question 1
### THOUGHTS
For this problem it was mostly a combination of using BeautifulSoup and Selenium, with a little bit of regex. The diacritics and whitespace joiners were an interesting problem to solve, as they either caused some of the matches to be omitted or made parsing through the text more tricky. Making the test check the "Ignore joiners" box ensured that joiners would no longer be an issue, and for the diacritics I opted to use the unidecode module to convert the pulled text to ASCII characters for easier parsing. I then used regex to find all matches for the word `'lorem'` and compared them to the amount of times `.configurator .context :not(p):not(.ignore)` was present, as this is the css selector present in every highlighted match on the page and therefore an accurate representation of the number of matches found. I then had selenium check the "Case Sensitive" box to find all case sensitive matches and asserted the same way, only this time against the number of case sensitive matches found in the example text using regex.

## QUESTION 2
### THOUGHTS
A fairly straightforward example form with the usual text fields, dropdowns and checkboxes. Mostly just Selenium used here, with some extra bits of Python to generate some text strings and emails. For the positive scenario, I filled out all forms with valid data, submitted and asserted that the success message was present. For negative scenarios, I asserted that it was not. In a real world scenario, I might also include specific assertions for error message text that was previously agreed upon as per the requirements, however for the purposes of this problem and example form I felt a success message assertion was enough. Please find the list of negative scenarios tested below: 

1. Completely blank form
2. Blank first name 
3. Blank last name 
4. Invalid email
5. Blank email
6. Subscription type left blank
7. Terms and conditions not accepted
## QUESTION 3
### THOUGHTS
I approached this problem with the assumption that there would be a gif with the #cute hashtag on the first page as the problem did not specifically mention continuing to search until a gif was found, and so no scrolling was implemented and all tests look for the mentioned hashtag in the initial gifs returned by the search. This was certainly the most tricky problem out of the three, mainly due to the question of approach. The tags for each gif were present on the page for that gif itself, so one potential solution was to parse the page for each gif link then use the `requests` module to make a request to that page, that would consequently be parsed through BeautifulSoup to retrieve the tags. However this approach may have some unwanted side effects, as many requests are being made to the page at once. To avoid any potential issues or blacklisting I opted to retrieve the tags by parsing through the script present on the page itself, as I realized all the tags are present there anyway. Once the tags were retrieved it was just a matter of looping through them until a cute one was found.