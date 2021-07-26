import nltk
import json
import hashlib

class Article:
    """An article to be linguistically analyzed.
    self.title - The title of the article.
    self. text - The body or text of the article.  May include the author and date of publication.
    self.hash - the SHA256 hash of the article's body.
    self.url - The URL the article was retrieved from.
    self.source - The organization responsible for publishing the article.
    self.tagTotals - Tags come from the nltk module.  See nltk.help.upenn_tagset().  Some are reproduced here:

    $, (, ), ., etc - punctuation marks
    CC - Coordinating Conjunction (and, or, but, &, either, neither, nor, yet, and/or
    CD - numeral, cardinal (1, 2, 3, one, two, three, 645, 1,119
    DT - Determiner/pronoun - (this, each, another, that, \'nother)
    EX - existential there (there)
    FW - Foreign Word
    IN - Preposition
    JJ - Adjective
    JJR - Adjective, comparitive (ecent, over-all, possible, hard-fought, favorable, hard, meager, fit)
    JJS - Adjective, gentive (Great's)
    MD - Modal auxillary (should, may, might, will, would, must, can, could, shall, ought, need, wilt)
    NN - Noun, singular, common (failure, burden, court, fire, appointment, awarding, compensation, Mayor)
    NNS - noun, plural, common (irregularities, presentments, thanks, reports, voters, laws, legislators)
    RB - adverb (only, often, generally, also, nevertheless, upon,together, back, newly, no, likely)
    RBR - adverb, comparitive (further, earlier, better, later, higher, tougher, more, harder, longer)
    RP - adverb, particle (up, out, off, down, over, on, in, about, through, across, after)
    TO - infinitival to
    UH - interjection (hurrah, bang, whee, hmpf, ah, goodbye, oops, oh-the-pain-of-it, ha, crunch, say)
    VB - Verb, base: uninflected present, imperative or infinitive (investigate, find, act, follow, inure)
    VBD - verb, past tense (said, produced, took, recommended, commented, urged, found, added)
    VBG - Verb, present participle or gerund (modernizing, improving, purchasing, Purchasing, lacking, enabling)
    VBN - Verb, past participle (conducted, charged, won, recieved, studied, revised, operated)
    VBZ - verb, present tense, 3rd person singular (deserves, believes, receives, takes, goes, expires, says)
    WDT - WH-determiner (which, what, whatever, whichever, whichever-the-hell)
    WPO - WH-pronoun, accusative (whom, that, who)
    WP$ - WH-pronoun, gentive (whose, whosever)
    WRB - WH-adverb (however, when, where, why, whereby, wherever, how, whenever)

    self.tagPercentages - tags/total words in self.text
    """
    def __init__(self, title, publishedat, text, url, source, tokens, tagTotals, tagPercentages):
        self.title = title
        self.publishedat = publishedat
        self.text = text
        self.hash = hashlib.sha256(str(self.text).encode()).hexdigest()
        self.url = url
        self.source = source
        self.tokens = tokens
        self.wordcount = len(self.text.strip().split(" "))
        self.tagTotals = tagTotals  # a dictionary
        self.tagPercentages = tagPercentages  # a dictionary

    def tokenize(self):
        """Inputs an Article.  Returns a unique set of words and all the word tags."""
        lower_case = self.text.lower()
        tokens = nltk.word_tokenize(lower_case) #before we can tag, we need a list of words
        return set(tokens), nltk.pos_tag(tokens)

    def total_tags(self, tags):
        """Inputs a list of tags.  Outputs count for each tag found to self.tagTotals."""
        if len(tags) != 0:
            for i in tags:
                if i[1] in self.tagTotals:
                    self.tagTotals[i[1]] += 1
                else:
                    self.tagTotals[i[1]] = 1
        else:
            print("setting nokey")
            self.tagTotals['nokey'] = 0
        return

    def calculate_tag_percentages(self):
        """Inputs a single article.  Outputs the percentage of total words for each tag in self.text."""
        totalTags = 0.0
        for i in self.tagTotals:
            totalTags += self.tagTotals[i]
        for i in self.tagTotals:
            self.tagPercentages[i] = self.tagTotals[i] / totalTags
        return
