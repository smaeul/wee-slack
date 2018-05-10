from __future__ import print_function

def test_send_message(realish_eventrouter, mock_websocket):
    e = realish_eventrouter

    t = next(iter(e.teams.keys()))
    #u = next(iter(e.teams[t].users.keys()))

    #user = e.teams[t].users[u]
    #print(user)

    socket = mock_websocket
    e.teams[t].ws = socket

    c = next(iter(e.teams[t].channels.keys()))

    channel = e.teams[t].channels[c]
    channel.send_message('asdf')

    print(c)

    #assert False
