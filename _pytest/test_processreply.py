from __future__ import print_function

#from wee_slack import process_reply

def test_process_reply(realish_eventrouter, mock_websocket):

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

    socket = mock_websocket
    socket.add({"reply_to": 1, "_team": t, "ts": "12341234.111"})

    print(e.teams[t].ws_replies)

    e.receive_ws_callback(t)
    e.handle_next()

    #reply = {"reply_to": 1, "_team": t, "ts": "12341234.111"}
    #print(reply)
    #process_reply(reply, e)
    #print(e.teams[t].ws_replies)
    #assert False
    pass
