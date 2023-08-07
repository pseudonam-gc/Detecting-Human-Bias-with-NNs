A brief proof-of-concept thrown together in the last few hours of an AI hackathon.

Can a series of random coinflips be distinguished from human faking attempts? The answer is yes; in fact, this problem has been explored many times in the past. As it turns out, humans have a very skewed perception of randomness. Common "tells" include:

* Humans are much likelier to flip from heads to tails and vice versa, unconsciously correlating change with randomness, when the opposite flip should only occur 50% of the time.
* Humans try to minimize long consecutive streaks, but much more than randomness would. For instance, there is a >50% chance that a 6-length consecutive streak happens in 50 flips, but humans usually do not have streaks this long.
* As an extension of the above two, substrings that occur much more or less than a truly randomly generated sequence. "1010" may be much more represented than "0000", for instance.

The above three tells have been used to differentiate the two by hand with a bit of statistical analysis. Could a neural network do a better job? After all:

* A neural network should be able to simulate each of the above tests, since finding the number of appearances of a substring in a binary string can be done with just binary functions (which can be modeled by a neural network). 
* If any other "tells" existed, the model should be able to pick up on them. 
* Most importantly, it should be able to combine each of the above factors into a total score. A human can only use one individual test at a time, but the neural network should be able to consider everything at once and combine them into a single probability.

We got some very enticing results. Without feeding the model any additional features (just a 50-length set of coinflips), we had a precision of 0.821 and a recall of 0.992. This was not extremely impressive, considering most humans could use the above tells to do better. 

But when we did add additional features (the number of appearances of each 1, 2, 3, 4, and 5-length substring, respectively), we achieved a precision of 0.965 and a recall of 1.000 (which had 600 test cases)! 

Our final accuracy was 98.25%. This exceeds the human standard, and shows that modeling many other possible scenarios with a neural network are also possible. Applications include:

* Normal-form games, such as rock paper scissors, Goofspiel, or other game theory examples. The only thing necessary would be training data, which can be obtained with enough humans.
* Any field that uses game-theoretical models, such as economics, political science, and even the military. Each of them can be largely impacted by human biases, and the optimal decision changes if one knows they are against a human instead of a set of probabilities. 
* Certain multi-agent formulations in machine learning where it is useful to have human-like behavior (for instance, if some of the agents are humans). 

I came up with the hackathon idea, created, trained, and deployed the model with Tensorflow, and wrote the basic functionality for the webpage using Flask. The other team members helped add webpage graphics, assisted with the presentation, and generated input data.

If you want to test out the model on your own, do the following:

Make sure to install everything on requirements.txt, usually with 'pip3 install -r requirements.txt'.
Run the code with 'flask run', then open the given webpage.
(For me, this is http://127.0.0.1:5000)
The site will contain a basic interface. It may take a bit of time to process inputs due to the way the model is set up.