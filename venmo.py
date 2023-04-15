    from venmo_api import Client
def email():
    email = ""
    amout = 0

    def transactioninfo():
        global email
        global amount
        #access_token = Client.get_access_token(username='rudrappandya@gmail.com', password='SwordsAMillion12')
        access_token = "6acbf7822f859806407f63ae9afb13e2f0d2fc3c068210404cf8722afe545b2c"
        print("Your token (please save):", access_token)

        client = Client(access_token=access_token)

        user1 = client.user.get_my_profile()
        print(user1)

        transactions = client.user.get_user_transactions(user_id='3781626462995850393')
        while transactions:
            for transaction in transactions:
                print(transaction)
                amount = str(transaction).split(",")[6]
                email = str(transaction).split(",")[-18]

            print("\n" + "=" * 15 + "\n\tNEXT PAGE\n" + "=" * 15 + "\n")
            transactions = transactions.get_next_page()

        # client.log_out("Bearer", access_token)
    transactioninfo()

    import smtplib, ssl

    smtp_server = 'smtp.gmail.com' 
    port  =  465

    sender   =  'rkrao1144@gmail.com'
    password = input('enter  your password here')

    receiver = 'rohan.krish.rao@gmail.com'
    message = f"""\
    From: {sender}
    To: {receiver}
    Subject: Project HeadSpace and Timing Donation

    {amount}
    EOI: 83-3998869

    Basic Info About BH&T: PHAT began operating in 2017 and officially began operating as a 501(C)(3) in 2019. The organization was founded by Eric Peterson after a fellow teammate took his own life after multiple tours overseas. As an organization, we believe that we live in a community that supports their veterans but may not know how to show it, and we have veterans that need that support but may not know how to ask. Our three focuses are: Veterans Advocacy, Veterans Outreach and Veterans Village

    Thank you for Donating!

    """


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server,  port, context = context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
    return message
