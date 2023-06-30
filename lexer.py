from dataclasses import (
    dataclass,
)

import token_types as TokenType

from tokens import (
    FIXED_TOKENS,
    RESERVED_KEYWORDS,
    Token,
)


@dataclass
class Lexer:
    input: str
    position: int = 0
    read_position: int = 0
    ch: str = ""

    def __post_init__(self) -> None:
        self.input_length = len(self.input)
        self.read_char()

    def read_char(self) -> None:
        self.ch = self.peek_char()
        self.position = self.read_position
        self.read_position += 1

    def peek_char(self) -> str:
        if self.read_position >= self.input_length:
            return "\0"
        return self.input[self.read_position]

    def reset(self) -> None:
        self.position = 0
        self.read_position = 0
        self.read_char()

    def skip_until(self, token_name):
        while self.ch != "\x00" and self.get_next_token().type != token_name:
            ...

    def skip_tokens(self, token_names):
        while (
            self.ch != "\x00" and self.get_next_token().type not in token_names
        ):
            ...

    def get_next_token(self) -> Token:
        self.skip_whitespace()

        tok = None
        if self.ch in FIXED_TOKENS:
            tok = FIXED_TOKENS[self.ch]
        match tok:
            case Token(TokenType.ASSING):
                # PEEK
                if self.peek_char() == "=":
                    self.read_char()
                    tok = FIXED_TOKENS["=="]
            case Token(TokenType.BANG):
                # PEEK
                if self.peek_char() == "=":
                    self.read_char()
                    tok = FIXED_TOKENS["!="]
            case None:
                if self.is_letter(self.ch):
                    ident = self.read_ident()
                    if ident in RESERVED_KEYWORDS:
                        return RESERVED_KEYWORDS[ident]
                    return Token(TokenType.IDENT, ident)
                elif self.ch.isdigit():
                    return Token(TokenType.INT, self.read_int())
                tok = Token(TokenType.ILLEGAL, TokenType.ILLEGAL)

        self.read_char()
        return tok

    def read_int(self) -> str:
        pos = self.position

        while self.ch.isdigit():
            self.read_char()

        return self.input[pos: self.position]

    def read_ident(self) -> str:
        pos = self.position

        while self.is_letter(self.ch):
            self.read_char()

        return self.input[pos: self.position]

    def skip_whitespace(self) -> None:
        while self.ch.isspace():
            self.read_char()

    @staticmethod
    def is_letter(ch: str) -> bool:
        return ch.isalpha() or ch == "_"


__all__ = ["Lexer"]
