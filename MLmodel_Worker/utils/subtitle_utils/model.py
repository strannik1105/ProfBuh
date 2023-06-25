# First let import the most necessary libs

import numpy as np
# Library to import pre-trained model for sentence embeddings
from sentence_transformers import SentenceTransformer
# Calculate similarities between sentences
from sklearn.metrics.pairwise import cosine_similarity
# Visualization library
import seaborn as sns
import matplotlib.pyplot as plt
# package for finding local minimas
from scipy.signal import argrelextrema
import math


# First lets load the transcript

def arcticle_model(filename):
    with open(f'{filename}.txt') as f:
        doc = f.readlines()
        f.close()
    # Transcript is one line, so we select it and change question mark for dots so that we split it correctly.
    doc = doc[0].replace("?", ".")
    sentences = doc.split('.')
    # print(sentences)


    # Loading a model - don't try it at home, it might take some time - it is 420 mb
    model = SentenceTransformer('all-mpnet-base-v2')

    # Get the length of each sentence
    sentece_length = [len(each) for each in sentences]
    # Determine longest outlier
    long = np.mean(sentece_length) + np.std(sentece_length) * 2
    # Determine shortest outlier
    short = np.mean(sentece_length) - np.std(sentece_length) * 2
    # Shorten long sentences
    text = ''
    for each in sentences:
        if len(each) > long:
            # let's replace all the commas with dots
            comma_splitted = each.replace(',', '.')
        else:
            text += f'{each}. '
    sentences = text.split('. ')
    # Now let's concatenate short ones
    text = ''
    for each in sentences:
        if len(each) < short:
            text += f'{each} '
        else:
            text += f'{each}. '

    # Split text into sentences
    sentences = text.split('. ')
    # Embed sentences
    embeddings = model.encode(sentences)
    # print(embeddings.shape)

    # Create similarities matrix
    similarities = cosine_similarity(embeddings)
    # Lets plot the result we got
    sns.heatmap(similarities).set_title('Cosine similarities matrix')

    def rev_sigmoid(x: float) -> float:
        return (1 / (1 + math.exp(0.5 * x)))

    def activate_similarities(similarities: np.array, p_size=30) -> np.array:
        """ Function returns list of weighted sums of activated sentence similarities
        Args:
            similarities (numpy array): it should square matrix where each sentence corresponds to another with cosine similarity
            p_size (int): number of sentences are used to calculate weighted sum
        Returns:
            list: list of weighted sums
        """
        # To create weights for sigmoid function we first have to create space. P_size will determine number of sentences used and the size of weights vector.
        x = np.linspace(-10, 10, p_size)
        # Then we need to apply activation function to the created space
        y = np.vectorize(rev_sigmoid)
        # Because we only apply activation to p_size number of sentences we have to add zeros to neglect the effect of every additional sentence and to match the length ofvector we will multiply
        activation_weights = np.pad(y(x), (0, similarities.shape[0] - p_size))
        ### 1. Take each diagonal to the right of the main diagonal
        diagonals = [similarities.diagonal(each) for each in range(0, similarities.shape[0])]
        ### 2. Pad each diagonal by zeros at the end. Because each diagonal is different length we should pad it with zeros at the end
        diagonals = [np.pad(each, (0, similarities.shape[0] - len(each))) for each in diagonals]
        ### 3. Stack those diagonals into new matrix
        diagonals = np.stack(diagonals)
        ### 4. Apply activation weights to each row. Multiply similarities with our activation.
        diagonals = diagonals * activation_weights.reshape(-1, 1)
        ### 5. Calculate the weighted sum of activated similarities
        activated_similarities = np.sum(diagonals, axis=0)
        return activated_similarities

    # Let's apply our function. For long sentences i reccomend to use 10 or more sentences
    activated_similarities = activate_similarities(similarities, p_size=30)

    # Let's create empty fig for our plor
    fig, ax = plt.subplots()
    ### 6. Find relative minima of our vector. For all local minimas and save them to variable with argrelextrema function
    minmimas = argrelextrema(activated_similarities, np.less,
                             order=2)  # order parameter controls how frequent should be splits. I would not reccomend changing this parameter.
    # plot the flow of our text with activated similarities
    sns.lineplot(y=activated_similarities, x=range(len(activated_similarities)), ax=ax).set_title('Relative minimas')
    # Now lets plot vertical lines in order to see where we created the split
    plt.vlines(x=minmimas, ymin=min(activated_similarities), ymax=max(activated_similarities), colors='purple', ls='--',
               lw=1, label='vline_multiple - full height')

    # Create empty string
    split_points = [each for each in minmimas[0]]
    text = ''
    for num, each in enumerate(sentences):
        if num in split_points:
            text += f'\n{each}. '
        else:
            text += f'{each}. '

    fin_text = text.split('\n')

    # with open('rez.txt', 'w') as f:
    #     f.write(text)
    return enumerater(fin_text)


def enumerater(text, start: int = 0) -> dict[int:[list, int]]:
    sequence = text
    dict_abzaz = {}
    n = start
    for elem in sequence:
        dict_abzaz[n] = [elem]
        n += 1
    return dict_abzaz


