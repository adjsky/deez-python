from dataclasses import (
    dataclass,
)

from token_types import *


@dataclass
class Token:
    type: TokenType
    literal: str

    def __init__(self, token_type: TokenType, literal: str):
        self.type = token_type
        self.literal = literal


RESERVED_KEYWORDS = {
    "let": Token(LET, "let"),
    "loop": Token(LOOP, "loop"),
    "for": Token(FOR, "for"),
    "true": Token(TRUE, "true"),
    "false": Token(FALSE, "false"),
}

FIXED_TOKENS = {
    "=": Token(ASSING, ASSING),
    "+": Token(PLUS, PLUS),
    "-": Token(MINUS, MINUS),
    "/": Token(SLASH, SLASH),
    "*": Token(ASTERISK, ASTERISK),
    "<": Token(LESSTHAN, LESSTHAN),
    ">": Token(GREATERTHAN, GREATERTHAN),
    "!=": Token(NOTEQUAL, NOTEQUAL),
    "==": Token(EQUAL, EQUAL),
    ";": Token(SEMICOLON, SEMICOLON),
    "(": Token(LPAREN, LPAREN),
    ")": Token(RPAREN, RPAREN),
    "{": Token(LSQUIRLY, LSQUIRLY),
    "}": Token(RSQUIRLY, RSQUIRLY),
    "\0": Token(EOF, EOF),
}
