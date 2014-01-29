import nltk
import os


MY_PATH = "C:/Users/Justin/Desktop"
MY_TEXT_FILE = os.path.join(MY_PATH, "english_sample-utf8.txt")


languages = [['English', 'English-Latin1'], ['French', 'French_Francais-Latin1'],
             ['German', 'German_Deutsch-Latin1'], ['Italian', 'Italian-Latin1'],
             ['Portuguese', 'Portuguese_Portugues-Latin1'],
             ['Spanish', 'Spanish_Espanol-Latin1']]


def get_udhr_freqdist(language_list, language_freq_dict):
    """Add a language name (key) and language frequency distribution (value) 
    to a dictionary."""
    for lang, lang_tag in language_list:
        language_freq_dict[lang] = nltk.FreqDist(nltk.corpus.udhr.words(lang_tag))
    return language_freq_dict

def get_text_freqdist(text_file, text_freq_dict):
    """Return the frequency distribution for a user specified text as a dictionary 
    value."""
    with open(MY_TEXT_FILE, "rb") as my_document:         
        tokenized_text = nltk.word_tokenize(str(my_document.readlines()))
        cleaned_text = [word for word in tokenized_text if word.isalpha()]
        text_freq_dict['text_fd'] = nltk.FreqDist(cleaned_text)    
    return text_freq_dict   

def calculate_similarity(language_freq_dict, text_freq_dict, score_dict):
    """Return the similarity scores for the frequency distribution of the user text 
    compared to the frequency distribution of each specified language in the udhr."""
    for language, lang_freq_dist in language_freq_dict.iteritems():
        score_dict[language] = nltk.spearman_correlation(
            nltk.ranks_from_sequence(text_freq_dict['text_fd']), 
            nltk.ranks_from_sequence(lang_freq_dist))
    return score_dict

def rank_languages(score_dict):
    """Return the most likely language match for the user text."""
    language_ranking = sorted([(value, key) for (key, value) in 
	                            score_dict.items()])[::-1]
    most_likely = language_ranking[0][1]
    return most_likely

def determine_language():
    udhr_freq_words = {}
    text_freq_words = {}
    similarity_scores = {}
    get_text_freqdist(MY_TEXT_FILE, text_freq_words)
    get_udhr_freqdist(languages, udhr_freq_words)
    calculate_similarity(udhr_freq_words, text_freq_words, similarity_scores)
    print "This text is most likely {}.".format(rank_languages(similarity_scores))

determine_language()