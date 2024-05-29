import re

class AmharicDataCleaner:
    def __init__(self, data = None):
        self.data = data

    def normalize_char_level_missmatch(input_token):
        rep1=re.sub('[ሃኅኃሐሓኻ]','ሀ',input_token)
        rep2=re.sub('[ሑኁዅ]','ሁ',rep1)
        rep3=re.sub('[ኂሒኺ]','ሂ',rep2)
        rep4=re.sub('[ኌሔዄ]','ሄ',rep3)
        rep5=re.sub('[ሕኅ]','ህ',rep4)
        rep6=re.sub('[ኆሖኾ]','ሆ',rep5)
        rep7=re.sub('[ሠ]','ሰ',rep6)
        rep8=re.sub('[ሡ]','ሱ',rep7)
        rep9=re.sub('[ሢ]','ሲ',rep8)
        rep10=re.sub('[ሣ]','ሳ',rep9)
        rep11=re.sub('[ሤ]','ሴ',rep10)
        rep12=re.sub('[ሥ]','ስ',rep11)
        rep13=re.sub('[ሦ]','ሶ',rep12)
        rep14=re.sub('[ዓኣዐ]','አ',rep13)
        rep15=re.sub('[ዑ]','ኡ',rep14)
        rep16=re.sub('[ዒ]','ኢ',rep15)
        rep17=re.sub('[ዔ]','ኤ',rep16)
        rep18=re.sub('[ዕ]','እ',rep17)
        rep19=re.sub('[ዖ]','ኦ',rep18)
        rep20=re.sub('[ጸ]','ፀ',rep19)
        rep21=re.sub('[ጹ]','ፁ',rep20)
        rep22=re.sub('[ጺ]','ፂ',rep21)
        rep23=re.sub('[ጻ]','ፃ',rep22)
        rep24=re.sub('[ጼ]','ፄ',rep23)
        rep25=re.sub('[ጽ]','ፅ',rep24)
        rep26=re.sub('[ጾ]','ፆ',rep25)
        #Normalizing words with Labialized Amharic characters such as በልቱዋል or  በልቱአል to  በልቷል  
        rep27=re.sub('(ሉ[ዋአ])','ሏ',rep26)
        rep28=re.sub('(ሙ[ዋአ])','ሟ',rep27)
        rep29=re.sub('(ቱ[ዋአ])','ቷ',rep28)
        rep30=re.sub('(ሩ[ዋአ])','ሯ',rep29)
        rep31=re.sub('(ሱ[ዋአ])','ሷ',rep30)
        rep32=re.sub('(ሹ[ዋአ])','ሿ',rep31)
        rep33=re.sub('(ቁ[ዋአ])','ቋ',rep32)
        rep34=re.sub('(ቡ[ዋአ])','ቧ',rep33)
        rep35=re.sub('(ቹ[ዋአ])','ቿ',rep34)
        rep36=re.sub('(ሁ[ዋአ])','ኋ',rep35)
        rep37=re.sub('(ኑ[ዋአ])','ኗ',rep36)
        rep38=re.sub('(ኙ[ዋአ])','ኟ',rep37)
        rep39=re.sub('(ኩ[ዋአ])','ኳ',rep38)
        rep40=re.sub('(ዙ[ዋአ])','ዟ',rep39)
        rep41=re.sub('(ጉ[ዋአ])','ጓ',rep40)
        rep42=re.sub('(ደ[ዋአ])','ዷ',rep41)
        rep43=re.sub('(ጡ[ዋአ])','ጧ',rep42)
        rep44=re.sub('(ጩ[ዋአ])','ጯ',rep43)
        rep45=re.sub('(ጹ[ዋአ])','ጿ',rep44)
        rep46=re.sub('(ፉ[ዋአ])','ፏ',rep45)
        rep47=re.sub('[ቊ]','ቁ',rep46) #ቁ can be written as ቊ
        rep48=re.sub('[ኵ]','ኩ',rep47) #ኩ can be also written as ኵ  
        
        return rep48

    def normalize_labialized_characters(self, input_token):
        replacements = [
            # labialized characters
            (re.compile(r'(ሉ[ዋአ])'), 'ሏ'),
            (re.compile(r'(ሙ[ዋአ])'), 'ሟ'),
            (re.compile(r'(ቱ[ዋአ])'), 'ቷ'),
            (re.compile(r'(ሩ[ዋአ])'), 'ሯ'),
            (re.compile(r'(ሱ[ዋአ])'), 'ሷ'),
            (re.compile(r'(ሹ[ዋአ])'), 'ሿ'),
            (re.compile(r'(ቁ[ዋአ])'), 'ቋ'),
            (re.compile(r'(ቡ[ዋአ])'), 'ቧ'),
            (re.compile(r'(ቹ[ዋአ])'), 'ቿ'),
            (re.compile(r'(ሁ[ዋአ])'), 'ኋ'),
            (re.compile(r'(ኑ[ዋአ])'), 'ኗ'),
            (re.compile(r'(ኙ[ዋአ])'), 'ኟ'),
            (re.compile(r'(ኩ[ዋአ])'), 'ኳ'),
            (re.compile(r'(ዙ[ዋአ])'), 'ዟ'),
            (re.compile(r'(ጉ[ዋአ])'), 'ጓ'),
            (re.compile(r'(ደ[ዋአ])'), 'ዷ'),
            (re.compile(r'(ጡ[ዋአ])'), 'ጧ'),
            (re.compile(r'(ጩ[ዋአ])'), 'ጯ'),
            (re.compile(r'(ጹ[ዋአ])'), 'ጿ'),
            (re.compile(r'(ፉ[ዋአ])'), 'ፏ'),
            # other characters
            (re.compile(r'[ሃኅኃሐሓኻ]'), 'ሀ'),
            (re.compile(r'[ሑኁዅ]'), 'ሁ'),
            (re.compile(r'[ኂሒኺ]'), 'ሂ'),
            (re.compile(r'[ሔዄ]'), 'ሄ'),
            (re.compile(r'[ሕኅ]'), 'ህ'),
            (re.compile(r'[ኆሖኾ]'), 'ሆ'),
            (re.compile(r'[ሠ]'), 'ሰ'),
            (re.compile(r'[ሡ]'), 'ሱ'),
            (re.compile(r'[ሢ]'), 'ሲ'),
            (re.compile(r'[ሣ]'), 'ሳ'),
            (re.compile(r'[ሤ]'), 'ሴ'),
            (re.compile(r'[ሥ]'), 'ስ'),
            (re.compile(r'[ሦ]'), 'ሶ'),
            (re.compile(r'[ዓኣዐ]'), 'አ'),
            (re.compile(r'[ዑ]'), 'ኡ'),
            (re.compile(r'[ዒ]'), 'ኢ'),
            (re.compile(r'[ዔ]'), 'ኤ'),
            (re.compile(r'[ዕ]'), 'እ'),
            (re.compile(r'[ዖ]'), 'ኦ'),
            (re.compile(r'[ጸ]'), 'ፀ'),
            (re.compile(r'[ጹ]'), 'ፁ'),
            (re.compile(r'[ጺ]'), 'ፂ'),
            (re.compile(r'[ጻ]'), 'ፃ'),
            (re.compile(r'[ጼ]'), 'ፄ'),
            (re.compile(r'[ጽ]'), 'ፅ'),
            (re.compile(r'[ጾ]'), 'ፆ'),
            # standardize ቊ and ኵ
            (re.compile(r'[ቊ]'), 'ቁ'),
            (re.compile(r'[ኵ]'), 'ኩ'),
        ]
        for pattern, replacement in replacements:
            input_token = pattern.sub(replacement, input_token)
        return input_token
    
    def remove_punc_and_special_chars(self, text):
        if text is None:
            raise ValueError("Input text cannot be None")
        try:
            normalized_text = re.sub('[\!\@\#\$\%\^\«\_\°\é\»\&\*\(\)\…\[\]\{\}\;\“\”\›\’\‘\"\'\:\,\.\‹\/\<\>\?\\\\|\`\´\~\-\=\+\፡\።\፤\;\፦\፥\፧\፨\፠\፣]', '',text)
            return normalized_text
        except Exception as e:
            raise ValueError(
                "An error occurred while removing punctuation and special characters from the input text. Exception: {}".format(e)) from e
    
    def remove_ascii_and_numbers(self, text_input):
        if text_input is None:
            raise ValueError("Input text cannot be None")
        try:
            rm_num_and_ascii = re.sub('[A-Za-z0-9]', '', text_input)
            return re.sub('[\'\u1369-\u137C\']+', '', rm_num_and_ascii)
        except Exception as e:
            raise ValueError(
                "An error occurred while removing ASCII characters and numbers from the input text. Exception: {}".format(e)) from e

    def remove_newline_and_extra_space(self, text):
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        return text

    def remove_emojis(self, text):
        # Define a regular expression pattern to match emojis
        emoji_pattern = re.compile("["
                                u"\U0001F600-\U0001F64F"  # Emojis
                                u"\U0001F300-\U0001F5FF"  # Symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # Transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # Flags (iOS)
                                u"\U00002500-\U00002BEF"  # Chinese characters
                                u"\U00002702-\U000027B0"
                                u"\U00002702-\U000027B0"
                                u"\U000024C2-\U0001F251"
                                u"\U0001f926-\U0001f937"
                                u"\U00010000-\U0010ffff"
                                u"\u2640-\u2642"
                                u"\u2600-\u2B55"
                                u"\u200d"
                                u"\u23cf"
                                u"\u23e9"
                                u"\u231a"
                                u"\ufe0f"  # Combining enclosing keycap
                                u"\u3030"
                                "]+", flags=re.UNICODE)
        
        # Remove emojis from the text
        clean_text = emoji_pattern.sub('', text)
        
        return clean_text
