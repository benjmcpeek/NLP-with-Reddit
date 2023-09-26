# Problem Statement 


A children's book company has a new series of funny ghost stories for the upcoming Halloween season. Before they advertise these books they wanted to find a way to get public insight on which genre sticks out the most for each story. Using the subreddits, r/Ghostories and r/funnystories, we will create a model that can interpret a post to which subreddit it belongs to. These subreddits will be a great way to determine a sample of public opinion on what constitutes a funny and ghost story without the costs of generating our own samples. We will refine our model by iterating our posts to only include the most impactful words and test multiple models to find the best performance. Because the data we extracted is fairly balanced we will determine our success based on the accuracy of our model compared to our baseline. We will also create a test model to determine which form of iteration performs best. Our test model's accuracy will then be our baseline for future models. After creating a reliable model we will run the new series of funny ghost stories to determine how to market the story. If our model interprets a story as part of the r/funnystories subreddit we will market the book as a comedy with a hint of scary. 



# Data Description

Because of Reddit's recent API update we were limited in the amount of posts we could pull from each subreddit. Filtering through the newest and most popular posts for each subreddit I was able to pull on average 5 posts per day. In future adaptations of this project I will aim to pull more data for these models. 


Subreddits = r/Ghoststories, r/funnystories 
Total Unique Posts = 1,977




# Analysis 


### Cleaning and EDA


- After loading in all the posts I could scrape I removed all duplicates and was left with 1,977 unique data points. 
- We discovered two missing posts from our data. We will fill these in with an empty string because later we will combine our title column with our text column.
- Created a column with the amount of words per post and another with the character length of each post. 
- We can see the Ghoststories subreddit has a higher proportion of longer stories (on average have roughly 130 more words). Considering I have a slightly higher amount of Ghoststories in my data, knowing that this subreddit also contains higher word counts tells me I will want to filter out a larger amount of common words between the two. 
- After combining our two subreddit datasets we see that we have two missing subreddits because everytime we pull new data, a single row is generated with the title column names as it's values. These rows have no information on them leaving it easy to remove from our dataset. 
- Lastly we observed the most common words of both subreddits with no stop word filter. This revealed the most common words being noise words that have no indication or characteristic of either subreddit. 


### Preprocessing 


- After loading in the cleaned and combined data I checked to make sure all values were present. It seems that the null values that I replaced with empty strings got recognized as null values when loading in the data. This fillna process will have to be implemented at the start of each notebook. 
- For my initial iteration I only filtered out any links and non alpha-numeric characters. Links are unique and uninformative for our problem because they offer no characteristics of the subreddit and are none identifiable as words. 
- For my first matrix I used the established stop words with no added customization. When looking at the top most frequent individual words we can see that the RegexpTokenizer has split words based on apostrophes. This will give us half words such as 'don', 've', and 'didn' that make it difficult to interpret. 
- Before adding custom stop words, the most frequent bi and trigrams had 'amp' or 'x200b' within it. After looking through some individual posts it was clear this was a coded filler text. I also decided to add 'just', 'house', 'time', and 'said' to my custom stop words because it was the most frequent individual word yet did not show up nearly as much in the bi and trigrams. This tells me this is just a common overlap word with no important context before or after. 
- From our first iteration we can see unique phrases in our trigrams. I am happy with these results because some of these frequent phrases already have distinct characteristics that can hint to which subreddit it's from. Phrases such as 'knock knock knock' or 'woke middle night' I can infer are from the Ghoststories subreddit while others such as 'long story short' aren't as clear. 
- By looking at the most frequent words per subreddit, we can see a lot of overlap. Words such as 'just', 'like', 'time', 'said', 'room', and 'got' are the most frequent for both subreddits. These words are not distinct and tell us very little about either topic. In our second iteration we will additionally remove these words along with other tokenizing. 
- With Spacy we will filter our features by lemmatizing our posts and only extracting proper_nouns, verbs, adjectives, and nouns. This will be our harshest iterations with the least features. By comparing three different strengths of iteration we will be able to see which one performs the best. 
- After filtering the most words with Spacy we will want to look at the amount of overlap that we are getting from the subreddits. 
- We can still see a fair amount of overlap however the overlapped words differ in frequency. We can also find unique words that seem to resemble the characteristics of their subreddits. 


**Unique Words**
- Ghoststories: 'room', 'house', 'hear', 'door', and 'night'
- funnystories: 'friend', 'day', 'story'


### Models


**Logistic Regression**
- We will use a Logistic Regression model to determine our best features. We set up two different iterations of our features that progressively filter more. We will run two different Logistic Reg models and see which performs the best under which iteration. Based on which model performs best will determine which iteration we will use for further complex models. 
- Our first Log Reg model will be using features from our RegExp iteration.
- Our second Log Reg model will be using features from our Spacy iteration. 
- Because our baseline accuracy is a low 52.6% we want to see our Logistic Reg models score as well or better than our baseline. 
- I will use the performance of my best Logistic Regression model to determine how successful my other models will perform. 
- We can see that our Spacy model is performing slightly better than our RegExp model. Checking our cross-val-score, we can see that the Spacy and RegExp models performed fairly similarly. However looking at our Train and Test scores we can see that our Spacy model is less overfit than our RegExp model. 
- We will use our Spacy Iterations to run two other models to find our best accuracy. 


**Random Forest**
- I am using a Random Forest model because I want to reduce correlation in my decision trees. 
- Our Null baseline accuracy is 52.1%. 
- Our baseline model accuracy is (Train: 0.969, Test: 0.925)
- Our Random Forest model will be successful if it surpasses our null baseline and baseline model
- We can see our cross-val-score for our Random Forest model is underperforming compared to our baseline model of 0.922
- Similarly our accuracy scores for the Random Forest are under performing from our baseline model. We will proceed with other models to potentially increase our accuracy. 


**Naive Bayes**
- I choose this model because it is fast and quick at generating predictions. The downside to this model will be that the probabilities of predictions will be difficult to interpret.  
- Our baseline model accuracy is (Train: 0.969, Test: 0.925)
- Our Random Forest model will be successful if it surpasses our null baseline and baseline model
- We can see our cross-val-score for our Naive Bayes model is performing better than our baseline model by 1%
- Similarly our Naive Bayes model is performing better than our baseline model with an increase in accuracy of our Train set of 0.7% and our Test set of 1.2%


# Conclusion 


We were successful in creating a model that out performed our null and model baseline. There are two ways to generate insightful predictions to best market Children's Book Company's new Halloween series. We can use our Naive Bayes model to best accurately predict the genre of each story and market them solely based on the predicted genre. This form of marketing neglects the amount of presence of the lesser prominent genre and will put all of its marketing effort to the predicted genre. Although Naive Bayes is the most accurate model, interpreting the probability of its predictions are difficult. We can use our second best performing model, Random Forest, to find the presence of the genres to each story. This will allow the marketing of each story to be more nuanced and specific. 




**Accuracy Scores for each Model**
Logistic Regression: {Train: 0.969, Test: 0.925}
Random Forest: {Train: 0.901, Test: 0.875}
Naive Bayes: {Train: 0.976, Test: 0.937, Cross_Val_Score: 0.934}

