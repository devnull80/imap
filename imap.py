#!/usr/bin/env python3
# coding: utf-

# yum search python oauth
# yum install python-oauth2
# yum install python3-oauth2
# yum install python-oauth2
# yum search python oauth
# yum install python3-oauthlib.noarch
# yum install python3-requests-oauthlib.noarch python3-sanction.noarch

from exchangelib import DELEGATE, Account, Credentials

credentials = Credentials(
    username='imap_test@outlook.fr',  # Or myusername@example.com for O365
    password='!m@p_t35T'
)

account = Account(
    primary_smtp_address='imap_test@outlook.fr',
    credentials=credentials,
    autodiscover=True,
    access_type=DELEGATE
)
# Print first 100 inbox messages in reverse order
for item in account.inbox.all().order_by('-datetime_received')[:100]:
    print(item.subject, item.body, item.attachments)
