# generic_alphabet.py

# Creation of the proper probability functions required
# (cumul_distr, prob_distr, next_message, get_inverse_cumul_distr_samples)
# to create a MessageSpaceProbabilityFxns object that represents
# the message space of an arbitrary generic alphabet given only a
# alphabet, letter probabilities, message length.

"""
Requires generic alphabet specifications:
alphabet : list of letters in alphabet (determines ordering for cumul)
letter_prob : dict of letter to probability - sum of all letters is 1
msg_len : number of letters per message
"""

from probabilityfunctionAPI import MessageSpaceProbabilityFxns


"""
Creates letter cumulative probability distribution
"""
def create_cumul_fxn(alphabet, letter_prob):
    cumul_prob = 0
    letter_cumul = {}
    for l in alphabet:
        letter_cumul[l] = cumul_prob
        cumul_prob += letter_prob[l]
    return letter_cumul

"""
Creates letter to order dictionaries
"""
def create_letter_order_dict(alphabet):
    letter_to_order = {}
    for i in range(len(alphabet)):
        letter_to_order[alphabet[i]] = i
    return letter_to_order

"""
Create inverse sampling table
"""
def create_inverse_sample_table(alphabet, letter_cumul, msg_len):    
    table = [] #(prob, m)

    if msg_len >= 10:
        pad = alphabet[0] * (msg_len - 10)
        for l1 in alphabet:
            for l2 in alphabet:
                for l3 in alphabet:
                    for l4 in alphabet:
                        for l5 in alphabet:
                            for l6 in alphabet:
                                for l7 in alphabet:
                                    for l8 in alphabet:
                                        for l9 in alphabet:
                                            for l10 in alphabet:
                                                m = l1+l2+l3+l4+l5+l6+l7+l8+l9+l10+pad
                                                table.append((
    
    pad = alphabet[0]*(msg_len - 1)
    for l in alphabet:
        table.append((letter_cumul[l], l + pad))
    return table


class GenericAlphabetProbabilityFxns(MessageSpaceProbabilityFxns):

    def __init__(self, alphabet, letter_prob, msg_len):
        self.alphabet = alphabet
        self.letter_prob = letter_prob
        self.msg_len = msg_len
        self.letter_cumul = create_cumul_fxn(alphabet, letter_prob)
        self.letter_order = create_letter_order_dict(alphabet)
        self.inverse_table = create_inverse_sample_table(alphabet, self.letter_cumul, msg_len)

        # define probability distribution fxn
        def prob(self, m):
            # product of each letter's probability
            product = 1
            for l in m:
                product *= self.letter_prob[l]
            return product

        # define cumul distribution fxn
        def cumul(self, m):
            # special case if msg_len is 1
            if self.msg_len == 1:
                return self.letter_cumul[m[0]]
            # sum of each index cumulative contribution
            value = 0
            for i in range(1, self.msg_len)[::-1]:
                value += self.letter_cumul[m[i]]
                value *= self.letter_prob[m[i-1]]
            return value

        # define next message fxn
        def next_msg(self,m):
            least_sig_index = -1
            # Find index of message to increment letter
            for i in range(msg_len)[::-1]:
                if m[i] != alphabet[-1]:
                    least_sig_index = i
                    break
            if least_sig_index == -1:
                print "no next message - max message"
                return m
            # Increase letter order of index
            new_letter = self.alphabet[self.letter_order[m[least_sig_index]] + 1]
            return m[:least_sig_index] + new_letter + alphabet[0]*(self.msg_len - least_sig_index - 1)

        # create inverse sampling table
        def create_inverse_sample_table(self, alphabet, letter_cumul, msg_len):    
            table = [] #(prob, m)
            alphabet = self.alphabet
            letter_cumul = self.letter_cumul
            
            if msg_len >= 10:
                pad = alphabet[0] * (msg_len - 10)
                for l1 in alphabet:
                    for l2 in alphabet:
                        for l3 in alphabet:
                            for l4 in alphabet:
                                for l5 in alphabet:
                                    for l6 in alphabet:
                                        for l7 in alphabet:
                                            for l8 in alphabet:
                                                for l9 in alphabet:
                                                    for l10 in alphabet:
                                                        m = l1+l2+l3+l4+l5+l6+l7+l8+l9+l10+pad
                                                        table.append((
    
            pad = alphabet[0]*(msg_len - 1)
            for l in alphabet:
                table.append((letter_cumul[l], l + pad))
            return table

        # create get sample table
        def get_inverse_table(self):
            return self.inverse_table

        # Initialize MessageSpaceProbabilityFxns
        MessageSpaceProbabilityFxns.__init__(self, cumul, prob, next_msg, get_inverse_table)

    
