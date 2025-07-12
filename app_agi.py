from asterisk.ami import AMIClient, SimpleAction

def lancer_appel(depuis, vers):
    client = AMIClient(address='127.0.0.1', port=5038)
    client.login(username='webuser', secret='webpassword')

    action = SimpleAction(
        'Originate',
        Channel=f'PJSIP/{depuis}',
        Context='from-internal',
        Exten=vers,
        Priority=1,
        CallerID='WebCall',
    )

    response = client.send_action(action)
    print(response.response)
    client.logoff()
