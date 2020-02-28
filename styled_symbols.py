import click
from collections import namedtuple

ColoredSymbol = namedtuple("ColoredSymbol", "color symbol")

symbol_color_dict = {
    "INFO": ColoredSymbol("cyan", "*"),
    "ERR": ColoredSymbol("bright_red", "!"),
    "WRN": ColoredSymbol("bright_yellow", "?"),
    "OK": ColoredSymbol("bright_green", "~"),
    "FALLBACK": ColoredSymbol("yellow", "-")
}


def print_prefixed_factory(stylestring):
    def print_prefixed(func):
        def wrapper(*args, **kwargs):
            style = symbol_color_dict[stylestring.upper() if stylestring is not None and stylestring.upper() in
                                                             symbol_color_dict.keys() else "FALLBACK"]
            click.secho('[', nl=False)
            click.secho(style.symbol, fg=style.color, nl=False)
            click.secho('] ', nl=False)
            result = func(*args, **kwargs)
            return result

        return wrapper

    return print_prefixed


@print_prefixed_factory("INFO")
def print_info(message):
    click.secho(message)


@print_prefixed_factory("ERR")
def print_error(message):
    click.secho(message)


@print_prefixed_factory("WRN")
def print_warning(message):
    click.secho(message)


@print_prefixed_factory("OK")
def print_good(message):
    click.secho(message)


@print_prefixed_factory("FALLBACK")
def print_fallback(message):
    click.secho(message)
