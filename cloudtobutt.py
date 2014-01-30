"""
Cloud To Butt for XChat/Hexchat

------------------------------------------------------------------------------

Copyright (c) 2013 Shaun Duncan and Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import xchat


__module_name__ = 'cloudtobutt'
__module_author__ = 'Shaun Duncan'
__module_version__ = '0.1'
__module_description__ = 'Replaces "cloud" with "butt"'


def on_unload(data):
    """
    Callback for module unload
    """
    print '%s plugin v%s unloaded' % (__module_name__, __module_version__)


def cloudtobutt(word, word_eol, userdata):
    """
    Callback for message printing events. Scans contents of a message for both
    URLs and nicks and colorizes them. This colorized output is sent along to the
    client
    """
    try:
        message = word_eol[1]
    except IndexError:
        return xchat.EAT_NONE

    # Prevent recursive crap
    if message.count('cloud') == 0:
        return xchat.EAT_NONE

    xchat.emit_print(userdata, word[0], message.replace('cloud', 'butt'))
    return xchat.EAT_ALL


# Hook anything that prints a relevant message
xchat.hook_unload(on_unload)
xchat.hook_print('Channel Message', cloudtobutt, userdata='Channel Message')
xchat.hook_print('Your Message', cloudtobutt, userdata='Your Message')
xchat.hook_print('Private Message', cloudtobutt, userdata='Private Message')
xchat.hook_print('Private Message to Dialog', cloudtobutt, userdata='Private Message to Dialog')


print '%s plugin v%s loaded' % (__module_name__, __module_version__)
