from collections import namedtuple

# From click/colors.py
"""
all_colors = 'black', 'red', 'green', 'yellow', 'blue', 'magenta', \
             'cyan', 'white', 'bright_black', 'bright_red', \
             'bright_green', 'bright_yellow', 'bright_blue', \
             'bright_magenta', 'bright_cyan', 'bright_white'
"""

ColorLabel = namedtuple("ColorLabel", "color_name label message")

# Half of these should never occur for Lix, but hey, we got a dict of Http Response codes!
response_code_dict = {
    # Green is good.
    200: ColorLabel('bright_green', 'OK', "Seems good!"),
    201: ColorLabel('green', 'OK(API)', "Created. Usually API Response?"),
    202: ColorLabel('green', 'OK(Proc)', "Accepted. Processing request."),
    204: ColorLabel('green', 'OK(NoRepr)', "No state representation, but up."),

    # We don't know if redirects are good. Original link may or may not be dead.
    301: ColorLabel('bright_yellow', 'REDIR(Moved)', "Moved Permanently."),
    302: ColorLabel('yellow', 'REDIR(URL)', "Found, Getting Redirected."),
    303: ColorLabel('yellow', 'REDIR(API)', "Reference to API Resource"),
    304: ColorLabel('bright_magenta', 'CACHE', "Not modified received, are you caching?"),
    307: ColorLabel('yellow', 'REDIR(APIShift)', "Temporary redirect."),

    # Red = Bad
    400: ColorLabel('bright_red', 'BADREQ', "Bad Request"),
    401: ColorLabel('bright_red', 'UNAUTH', "Unauthorized"),
    403: ColorLabel('bright_red', 'FORBID', "Forbidden!"),
    404: ColorLabel('bright_red', 'NOTFOU', "Not found :("),
    405: ColorLabel('bright_red', 'NOGET!', "Method not Allowed"),
    406: ColorLabel('bright_red', 'UNACC(API)', "Not acceptable"),
    412: ColorLabel('bright_red', 'PRECON', "Link Bad :("),

    500: ColorLabel('bright_magenta', 'UPBUTDEAD', "Internal server error.")
}
