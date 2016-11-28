# -*- encondig: utf-8 -*-

import ply.lex as lex
import os

# lista de tokens
tokens = (

    # Palabras Reservadas
    'INICIO',
    'FIN',
    'ECHO',
    'ELSE',
    'IF',
    'WHILE',
    'FOR',
    'STRING',

    # Symbolos
    'DOLAR',
    'PUNTO',
    'MAS',
    'MASMAS',
    'MENOS',
    'MENOSMENOS',
    'MULTI',
    'DIVI',
    'MENOR',
    'MENORIGUAL',
    'MAYOR',
    'MAYORIGUAL',
    'IGUAL',
    'IGUALIGUAL',
    'DISTINTO',
    'SEMICOLON',
    'COMMA',
    'MAYORMAYOR',
    'MENORMENOR',
    'LPAREN',
    'RPAREN',
    'LCORCHETE',
    'RCORCHETE',
    'LLLAVE',
    'RLLAVE',
    'COMILLAS',


    #Otros
    'ID',
    'NUMERO',
)


# Reglas de Expresiones Regualres para token de Contexto simple

t_MAS = r'\+'
t_MENOS = r'-'
t_PUNTO = r'\.'
t_MULTI = r'\*'
t_DIVI = r'/'
t_IGUAL = r'='
t_MENOR = r'<'
t_MAYOR = r'>'
t_SEMICOLON = ';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCORCHETE = r'\['
t_RCORCHETE = r'\]'
t_LLLAVE = r'{'
t_RLLAVE = r'}'
t_COMILLAS = r'\"'


def t_DOLAR(t):
    r'\$'
    return t

def t_INICIO(t):
    r'\<\?php'
    return t


def t_FIN(t):
    r'\?>'
    return t


def t_ECHO(t):
    r'echo'
    return t


def t_ELSE(t):
    r'else'
    return t


def t_IF(t):
    r'if'
    return t


def t_RETURN(t):
    r'return'
    return t


def t_WHILE(t):
    r'while'
    return t


def t_FOR(t):
    r'for'
    return t


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

#exprecion regular para reconocer los identificadores


def t_ID(t):
    r'\w+(_\d\w)*'
    return t


def t_STRING(t):
#expresion RE para reconocer los String
    r'\"?(\w+ \ *\w*\d* \ *)\"?'
    return t


def t_MASMAS(t):
    r'\+\+'
    return t

def t_MENOSMENOS(t):
    r'\-\-'
    return t


def t_MENORIGUAL(t):
    r'<='
    return t


def t_MAYORIGUAL(t):
    r'>='
    return t


def t_IGUALIGUAL(t):
    r'=='
    return t


def t_MENORMENOR(t):
    r'<<'
    return t


def t_MAYORMAYOR(t):
    r'>>'
    return t


def t_DISTINTO(t):
    r'!='
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'


def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1


def t_error(t):
    print "Error Lexico: " + str(t.value[0])
    t.lexer.skip(1)

def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print tok

lexer = lex.lex()

# Test
if __name__ == '__main__':

    # Test
    data = '''
            /* comentario
                de varias lineas
            */
            <?php
                $a = 20 ;
                echo "Hola";
                // Esto es otro comentario
                $a * 10;
            ?>
    '''
# Build lexer and try on
    lexer.input(data)
    test(data, lexer)

