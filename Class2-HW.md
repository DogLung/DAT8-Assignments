Douglas Leung

**Class 2: Command Line and Version Control**

1. Look at the head and the tail of chipotle.tsv in the data subdirectory of this repo. Think for a minute about how the data is structured. What do you think each column means? What do you think each row means? Tell me! (If you're unsure, look at more of the file contents.)

```
head ~/Desktop/DAT8/data/chipotle.tsv
tail ~/Desktop/DAT8/data/chipotle.tsv
```

The columns contained in the chipotle.tsv file are the following:

* order_id - The identifier of an order group that may contain one or more individual items within it.
* quantity - The amount of a particular item that is ordered given all else remains constant.
* item_name - The particular main item that is ordered, not including additional ingredients.
* choice_description - A list of all the additional ingredients that are partnered with the item_name field.1
* item_price - The cost of item(s) within the order.  It should equate to quantity(item_name + choice_description).
 
2. How many orders do there appear to be?
Assuming that these order_id's remained in numerical order and started with 1, the number of orders is 1834.

3. How many lines are in this file?

```
wc -l ~/Desktop/DAT8/data/chipotle.tsv
```

There are 4623 lines within the file

4. Which burrito is more popular, steak or chicken?

```
grep "Chicken Burrito" ~/Desktop/DAT8/data/chipotle.tsv | wc -l
grep "Steak Burrito" ~/Desktop/DAT8/data/chipotle.tsv | wc -l
```

Assuming that the measure of popularity is based upon the occurance of the word "Chicken" or "Steak" and ignoring the possibility of high multiples of steak, then chicken is more popular 1 to 706.

5. Do chicken burritos more often have black beans or pinto beans?

```
grep "Chicken Burrito" ~/Desktop/DAT8/data/chipotle.tsv | grep "Black" | wc -l
grep "Chicken Burrito" ~/Desktop/DAT8/data/chipotle.tsv | grep "Pinto" | wc -l
```

Ignoring order count, Chicken Burritos are more often paired with Black beans over Pinto beans.

6. Make a list of all of the CSV or TSV files in the DAT8 repo (using a single command). Think about how wildcard characters can help you with this task.

```
find ~Desktop/DAT8/ -name "*.?sv"
```

There are three files. airlines.csv, chipotle.tsv, and sms.tsv.  All of them are located in the data folder.

7. Count the approximate number of occurrences of the word "dictionary" (regardless of case) across all files in the DAT8 repo.

```
grep -ri dictionary ~Desktop/DAT8/ | wc -l
```

there are apprximately 13 instances of the word "dictionary" in the DAT8 repo.

8. Optional: Use the the command line to discover something "interesting" about the Chipotle data. Try using the commands from the "advanced" section!

```
cut -f3,3 ~/Desktop/DAT8/data/chipotle.tsv |sort | uniq -c	
```

Not very interesting, but Chicken Bowl is obviously the most popular item, but there also seem to be some redundant listings due to dashes instead of spaces.

*Review the code from the beginner and intermediate Python workshops. If you don't feel comfortable with any of the content (excluding the "requests" and "APIs" sections), you should spend some time this weekend practicing Python: ?Introduction to Python does a great job explaining Python essentials and includes tons of example code.
?If you like learning from a book, Python for Informatics has useful chapters on strings, lists, and dictionaries.
?If you prefer interactive exercises, try these lessons from Codecademy: "Python Lists and Dictionaries" and "A Day at the Supermarket".
?If you have more time, try missions 2 and 3 from DataQuest's Learning Python course.
?If you've already mastered these topics and want more of a challenge, try solving Python Challenge number 1 (decoding a message) and send me your code in Slack.

•To give you a framework for thinking about your project, watch What is machine learning, and how does it work? (10 minutes). (This is the IPython notebook shown in the video.) Alternatively, read A Visual Introduction to Machine Learning, which focuses on a specific machine learning model called decision trees.
•Optional: Browse through some more example student projects, which may help to inspire your own project!

