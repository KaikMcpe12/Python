from whatssap_message_filter import WhatsAppMessageFilter

messages = WhatsAppMessageFilter()

messages.readText('messages-02.txt')


# messages.save_count_words(limit=100, output_file='words.xlsx')
# messages.save_emoji_usage(output_file='emoji_usage.xlsx')
# messages.save_all_statistics(output_file='stat.xlsx')
# messages.save_day_most_active_senders(output_file='days.xlsx')
# messages.save_most_active_senders(output_file='most_active_senders.xlsx')
# messages.count_specific_word('ENEM', output_file='enem_word.xlsx')
# messages.save_laughs_count(output_file='laught.xlsx')
# messages.save_laughs_by_sender(output_file='laughs_senders.xlsx')