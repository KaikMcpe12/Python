import pandas as pd
import re
from collections import Counter
import emoji

class WhatsAppMessageFilter:
    def __init__(self):
        self.df = None
        self.all_messages = None

    def readText(self, url):
        with open(url, encoding='utf-8') as f:
            raw_chat = f.read()
            
        # regex
        pattern = re.compile(r'(\d{2}/\d{2}/\d{4}) (\d{2}:\d{2}) - (.*?): ')

        # split text
        chunks = pattern.split(raw_chat)[1:]

        # create dataframe
        df = pd.DataFrame({
            'Data': chunks[0::4],
            'Hora': chunks[1::4],
            'Remetente': chunks[2::4],
            'Mensagem': chunks[3::4]
        })

        # join text together
        df['Mensagem'] = df['Mensagem'].replace('\n+', ' ', regex=True)

        self.df = df
        self.all_messages = " ".join(df['Mensagem'])
    
    def num_caracters(self):
        if self.df.empty:
            print("Dataframes is empty")
        
        return self.df['Mensagem'].str.len().sum()
    
    def num_msg(self):
        if self.df.empty:
            print("Dataframes is empty")
        
        return len(self.df)

    def _saveToFile(self, output_file, df):
        if df.empty:
            print("Dataframes is empty")
            return

        with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Mensagens', index=False)

    def save_all_statistics(self, output_file):
        self._saveToFile(output_file, self.df)

    def save_count_words(self, limit, output_file):
        all_text = " ".join(self.df['Mensagem'])

        # small case
        all_text = re.sub(r'[^\w\s]', '', all_text).lower()

        words = all_text.split()

        # count
        word_counts = Counter(words).most_common(limit)

        word_df = pd.DataFrame(word_counts, columns=['Palavra', 'Frequência'])

        self._saveToFile(output_file, word_df)
    
    def save_most_active_senders(self, output_file):
        sender_counts = self.df['Remetente'].value_counts().reset_index()
        sender_counts.columns = ['Remetente', 'Quantidade de Mensagens']
        self._saveToFile(output_file, sender_counts)

    def save_day_most_active_senders(self, output_file):
        day_counts = self.df['Data'].value_counts().reset_index()
        day_counts.columns = ['Data', 'Mensagens por Dia']

        self._saveToFile(output_file, day_counts)
    
    def save_emoji_usage(self, output_file):
        emojis_used = [char['emoji'] for char in emoji.emoji_list(self.all_messages)]
        
        emoji_counts = Counter(emojis_used).most_common()

        emoji_df = pd.DataFrame(emoji_counts, columns=['Emoji', 'Frequência'])

        self._saveToFile(output_file, emoji_df)
    
    def count_specific_word(self, word, output_file):
        word_lower = word.lower()
        
        all_text = " ".join(self.df['Mensagem']).lower()

        all_text = re.sub(r'[^\w\s]', '', all_text)

        words = all_text.split()
        word_count = words.count(word_lower)

        word_df = pd.DataFrame([(word_lower, word_count)], columns=['Palavra', 'Frequência'])
        self._saveToFile(output_file, word_df)

    def save_laughs_count(self, output_file):
        laugh_patterns = {
            "KKKKKK": r'\b[K]{2,}\b',  # KKKKKK
            "kkkkkk": r'\b[k]{2,}\b',  # kkkkkk
            "KKKkkKKk": r'\b[kK]{2,}\b',  # KKKkkKKkk
            "hahaha": r'\b[hH]+[aeiouAEIOU]+[hH]*[aeiouAEIOU]*\b',  # haha, hEhE, hAhA
            "rsrsrs": r'\b[rR]+[sS]+[rR]*[sS]*\b',  # rsrsrs, RSRSRS, RsRsrS
            "kakakaka": r'\b[kK]+[aA]+[kK]+[aA]+[kK]*[aA]*\b',  # "Kakakaka", "KaKaKa", "kAkAkA"
            "ahhhh": r'\b[aA]+[hH]+[hH]*\b',  # ahhh, AHHHH, AaHHH
            "auhh": r'\b[aA]+[uU]+[hH]+[hH]*\b' # auhh, AUHHH
        }

        laugh_counts = {
            laugh_type: self.df['Mensagem'].str.findall(pattern).explode().count()
            for laugh_type, pattern in laugh_patterns.items()
        }

        # dataframe
        laugh_df = pd.DataFrame(laugh_counts.items(), columns=['Risada', 'Frequência'])
        self._saveToFile(output_file, laugh_df)
    
    def save_laughs_by_sender(self, output_file):
        laugh_patterns = {
            "KKKKKK": r'\b[K]{2,}\b',
            "kkkkkk": r'\b[k]{2,}\b',
            "hahaha": r'\b[hH]+[aeiouAEIOU]+[hH]*[aeiouAEIOU]*\b',
            "rsrsrs": r'\b[rR]+[sS]+[rR]*[sS]*\b',
            "kakakaka": r'\b[kK]+[aA]+[kK]+[aA]+[kK]*[aA]*\b',
            "ahhhh": r'\b[aA]+[hH]+[hH]*\b',
            "auhh": r'\b[aA]+[uU]+[hH]+[hH]*\b'
        }

        # count
        laugh_counts_by_sender = {}
        for _, row in self.df.iterrows():
            sender = row['Remetente']
            message = row['Mensagem']
            
            # laught in message
            laugh_count = sum(len(re.findall(pattern, message)) for pattern in laugh_patterns.values())

            laugh_counts_by_sender[sender] = laugh_counts_by_sender.get(sender, 0) + laugh_count

        laugh_by_sender_df = pd.DataFrame(list(laugh_counts_by_sender.items()), columns=['Remetente', 'Quantidade de Risadas'])
        self._saveToFile(output_file, laugh_by_sender_df)