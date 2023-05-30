from email_coder import email_masking, email_recovery

email_lst = [
    'abc@def.com',
    'a.b.c.d@e.f.org',
]

default_masked_email_lst = [
    'abc [ at ] def [ dot ] com',
    'a [ dot ] b [ dot ] c [ dot ] d [ at ] e [ dot ] f [ dot ] org',
]

custom_mask_dict = {
    '.': ' ( d o t ) ',
    '@': ' [ a t ] ',
}

custom_masked_email_lst = [
    'abc [ a t ] def ( d o t ) com',
    'a ( d o t ) b ( d o t ) c ( d o t ) d [ a t ] e ( d o t ) f ( d o t ) org',    
]

def testing():
    for email, masked_email in zip(email_lst, default_masked_email_lst):
        assert email_masking(email) == masked_email, f"should be {masked_email}"
    
    for email, custom_masked_email in zip(email_lst, custom_masked_email_lst):
        assert email_masking(email, masking_dict=custom_mask_dict) == custom_masked_email, f"should be {custom_masked_email}"

if __name__ == "__main__":
    testing()
    print('Everything passed')
