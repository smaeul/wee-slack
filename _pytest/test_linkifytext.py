from wee_slack import linkify_text

#def test_linkifytext():
#    linkify_text('@ryan')

#    assert False


def test_linkifytext_does_partial_html_entity_encoding(realish_eventrouter):
    team = next(iter(realish_eventrouter.teams.values()))
    channel = next(iter(team.channels.values()))

    text = linkify_text('& < > \' "', team, channel)

    assert text == '&amp; &lt; &gt; \' "'
