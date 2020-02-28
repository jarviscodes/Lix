from collections import namedtuple

# From click/colors.py
"""
all_colors = 'black', 'red', 'green', 'yellow', 'blue', 'magenta', \
             'cyan', 'white', 'bright_black', 'bright_red', \
             'bright_green', 'bright_yellow', 'bright_blue', \
             'bright_magenta', 'bright_cyan', 'bright_white'
"""

ColorLabel = namedtuple("ColorLabel", "color_name label")

# Half of these should never occur for Lix, but hey, we got a dict of Http Response codes!
response_code_dict = {
    # Green is good.
    200: ColorLabel('bright_green', 'OK'),
    201: ColorLabel('green', 'OK(API)'),
    202: ColorLabel('green', 'OK(Processing)'),
    204: ColorLabel('green', 'OK(NoRepresentation)'),

    # We don't know if redirects are good. Original link may or may not be dead.
    301: ColorLabel('bright_yellow', 'REDIR(Moved)'),
    302: ColorLabel('yellow', 'REDIR(URL)'),
    303: ColorLabel('yellow', 'REDIR(API)'),
    304: ColorLabel('bright_magenta', 'CACHED(lol?)'),
    307: ColorLabel('yellow', 'REDIR(APIShift)'),

    # Red = Bad
    400: ColorLabel('bright_red', 'BADREQ'),
    401: ColorLabel('bright_red', 'UNAUTH'),
    403: ColorLabel('bright_red', 'FORBID'),
    404: ColorLabel('bright_red', 'NOTFOU'),
    405: ColorLabel('bright_red', 'NOGET!'),
    406: ColorLabel('bright_red', 'UNACC(API)'),
    412: ColorLabel('bright_red', 'PRECON'),

    500: ColorLabel('bright_magenta', 'UPBUTDEAD')
}