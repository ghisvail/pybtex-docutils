# -*- coding: utf-8 -*-

import nose.tools

expected_result = (
    u'<document source="example.rst">'
    u'<paragraph>D.\xa0Lindley. <emphasis>Making Decisions</emphasis>. '
    u'Wiley, 2nd edition, 1985.</paragraph></document>'
    )

def test_install_example():

    import docutils.utils
    import StringIO
    import pybtex.database.input.bibtex
    import pybtex.plugin

    style = pybtex.plugin.find_plugin('pybtex.style.formatting', 'plain')()
    backend = pybtex.plugin.find_plugin('pybtex.backends', 'docutils')()
    parser = pybtex.database.input.bibtex.Parser()
    data = parser.parse_stream(StringIO.StringIO(u"""
    @Book{1985:lindley,
      author =    {D. Lindley},
      title =     {Making Decisions},
      publisher = {Wiley},
      year =      {1985},
      edition =   {2nd},
    }
    """))
    document = docutils.utils.new_document('example.rst')
    for entry in style.format_entries(data.entries.itervalues()):
        document += backend.paragraph(entry)

    print(document)


    nose.tools.assert_equal(unicode(document), expected_result)
