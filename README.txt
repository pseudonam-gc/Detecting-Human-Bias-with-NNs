Make sure to install everything on requirements.txt.
Run the code with 'flask run', then open the given webpage.
(For me, this is http://127.0.0.1:5000)

Inspiration
The Fake Randomness Project showed that humans could not replicate a truly random series of coin flips. We were largely inspired by the Fake Randomness Project, and wanted to extend the concept to see if neural networks could catch the same human biases as the project.

How We Built It
Collect Data: We got a ton of data by simply mashing 1 and 2 in an attempt to be random, and doubled our dataset by reversing 1's and 2's to speed things up. We also used the random.randint() function to generate 'true' random numbers.
Preprocess Data: We added various features that made the program more useful.
Train Neural Network: We trained a neural network on the preprocessed data. The neural network would be designed to detect whether a series of coin flip were actually random. We mostly used dense and dropout layers as well as the ReLU activation function.
Test and Release: Finally, we tested and made a quick frontend to display the project cleanly.

What's Next for Our App
Educational tool: The model could be used as an educational tool to teach people about probability when trying to be random. It could be used in classrooms, workshops, or online courses. 
Gaming industry: The model could be integrated into games with elements of luck, such as betting games, board games, or casino games, to confirm the validity of randomness. 
Psychology: The model demonstrates flaws in human randomness and paves the way for human prediction models in the future. 
Game theory: Many games generally assume a perfect opponent, but do not account for human biases. As a result, this could help ensure better decisions or at least identify when human bias is at play.

The project identifies whether a sequence is human-generated or not with 98% accuracy.
