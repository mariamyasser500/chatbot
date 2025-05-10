import random

# ردود عامة
R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"

def unknown():
    responses = ["Could you please re-phrase that?",
                 "I'm not sure I understand.",
                 "Can you say that again?",
                 "Hmm... I don't know what that means."]
    return random.choice(responses)

# ردود خاصة بـ Deep Learning
R_DEEP_LEARNING = """Deep learning is a type of machine learning that uses neural networks with many layers. 
It is designed to automatically learn features from large amounts of data."""

R_NEURAL_NETWORK = """A neural network is a series of algorithms that mimic the operations of a human brain to recognize relationships in data."""

R_DL_APPLICATIONS = """Deep learning is used in image recognition, speech recognition, language translation, self-driving cars, and many more fields."""

R_DL_VS_ML = """Deep learning is a subset of machine learning. The main difference is that deep learning uses many layers of neural networks to learn from data, while traditional machine learning requires manual feature extraction."""