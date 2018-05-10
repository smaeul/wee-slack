from __future__ import print_function

import glob
import json

from wee_slack import ProcessNotImplemented

def test_process_team_join(mock_websocket, realish_eventrouter):

    e = realish_eventrouter

    t = next(iter(e.teams.keys()))
    #u = next(iter(e.teams[t].users.keys()))

    #user = e.teams[t].users[u]
    #print(user)

    #delete charles so we can add him
    del e.teams[t].users['U4096CBHC']

    assert len(e.teams[t].users) == 3

    socket = mock_websocket
    e.teams[t].ws = socket

    datafiles = glob.glob("_pytest/data/websocket/1485975606.59-team_join.json")

    print(datafiles)
    #assert False

    notimplemented = set()

    for fname in datafiles:
        try:
            print("####################")
            data = json.loads(open(fname, 'r').read())
            socket.add(data)
            print(data)
            e.receive_ws_callback(t)
            e.handle_next()
        except ProcessNotImplemented as e:
            notimplemented.add(str(e))
        #this handles some message data not existing - need to fix
        except KeyError:
            pass

    if len(notimplemented) > 0:
        print("####################")
        print(sorted(notimplemented))
        print("####################")

    #print(len(e.queue))
    assert len(e.teams[t].users) == 4



