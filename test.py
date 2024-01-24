# %%
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from collections import Counter
import matplotlib.pyplot as plt

# Ensure the necessary NLTK models are downloaded (do this in your local environment)
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

# Sentences from each dataset
sentences = {
    'SquAD': "What is in front of the Notre Dame Main Building?",
    'NQ': "when is the last episode of season 8 of the walking dead?",
    'Ours': "And my last one is just on the 9% CAGR. I'm just kind of curious how you're thinking about the 9% as a CAGR for the next 5 years. Is that what you think you can get on an EPS basis? Or is that what you think you can get on an AFFO basis?"
}

# POS tags that we are interested in
# POS tags that we are interested in
pos_tags_of_interest = {
    'Proper Noun': ['NNP', 'NNPS'],  # Adjusted to focus on proper nouns
    'Verb': ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'],
    'Adj': ['JJ', 'JJR', 'JJS'],
    'Others': ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'LS', 'MD', 'PDT', 'POS', 'PRP', 
               'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'WDT', 'WP', 
               'WP$', 'WRB', 'NN', 'NNS',  # Include common nouns here
               '.', ',', ':', '(', ')', '"', "'"]
}


# Function to get the POS tag counts
def get_pos_tag_counts(sentence):
    # Tokenize and tag the sentence
    tokens = word_tokenize(sentence)
    tagged_tokens = pos_tag(tokens)
    
    # Count the tags
    tag_counts = Counter(tag for word, tag in tagged_tokens)
    return tag_counts

# Get POS tag counts for each dataset
pos_counts = {dataset: get_pos_tag_counts(sentence) for dataset, sentence in sentences.items()}

# Calculate the POS percentages for each dataset
pos_percentages = {}

for dataset, counts in pos_counts.items():
    total_count = sum(counts.values())
    pos_percentages[dataset] = {tag: sum(counts[pos] for pos in tags) 
                                for tag, tags in pos_tags_of_interest.items()}

# Now we plot the results in a bar chart
fig, ax = plt.subplots()

# Defining the position of the bars
bar_width = 0.25
positions = list(range(len(pos_tags_of_interest)))

# Plotting each dataset
for i, (dataset, percentages) in enumerate(pos_percentages.items()):
    pos_values = [percentages[tag] for tag in pos_tags_of_interest]
    ax.bar([p + i * bar_width for p in positions], pos_values, width=bar_width, label=dataset)

# Adding labels and titles
ax.set_xlabel('Part of Speech')
ax.set_ylabel('Percentage (%)')
ax.set_title('POS Distribution in Different Datasets')
ax.set_xticks([p + bar_width for p in positions])
ax.set_xticklabels(list(pos_tags_of_interest.keys()))
ax.legend()

# Show the plot
plt.tight_layout()
plt.show()

# %%
