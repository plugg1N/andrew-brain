# Andrew's Brain

This is a fun project that will try to imitate a part of my friend's brain that is responsible for making a decision whether a girl appeals to him or not.
We will see if Neural Network (NN) can predict a very subjective choice of a human with high precision.

## Plan

In order to get information about Andrew's choices I've made a **Telegram bot** that will send him a picture of a girl that he has to judge. Send her a `like` or a `dislike`.
Then, after receiving info. about *1200* images, he will send a command that will create a CSV file with all his choices.

After, I will train the best NN model possible for this task and evaluate on 200 pictures given from 1200 *(1000 images will be left for training)*. Finally, we will
create a bot that can **receieve a picture of a girl, analyze it and give an answer that Andrew *could possibly give*.** 
