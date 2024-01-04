<img src="./logo.png" width="90" align="right" />

# SMSSpamDetector
SMS spam detection is a crucial task for filtering out unwanted and potentially harmful messages. The Naive Bayes algorithm is a widely used machine learning algorithm that effectively classifies text data, making it a suitable choice for SMS spam detection.

The Naive Bayes algorithm relies on Bayes' theorem, which relates the probability of a hypothesis to the probability of the evidence. In spam detection, the hypothesis is whether a message is spam or not, and the evidence is the words contained in the message.

The algorithm assigns probabilities to spam and ham messages (non-spam) based on the frequency of words in their respective classes. For a new message, the algorithm calculates the probabilities of it being spam and ham, considering the word frequencies. The message is classified as spam if the spam probability is higher.

## Install Dependencies
Install the required dependencies:
```sh
pip install -r requirements.txt
```
or 
```sh
pip3 install -r requirements.txt
```

# Hints

- Modify namenode volumes config in docker-compose.yml according to your need
- Remember to install  dependencies from requirements.txt in all of the (namenode, datanode, nodemanager) nodes
