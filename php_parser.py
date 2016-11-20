# -*- enconding: utf-8 -*-

import ply.yacc as yacc
from php_lex import tokens
import php_lex
import sys

VERBOSE = 1

def p_program(p):
    'program : INICIO declaration_list FIN'
    pass


def p_declaration_list_1(p):
    'declaration_list : declaration_list declaration'
     #p[0] = p[1] + p[2]
    pass

def p_declaration_list_2(p):
    'declaration_list : declaration'
    pass

def p_declaration(p):
    'declaration : var_declaration'

def p_var_declaration_1(p):
    'var_declaration : DOLAR ID SEMICOLON'
    pass

def p_var_declaration_2(p):
    'var_declaration : DOLAR ID LCORCHETE NUMERO RCORCHETE SEMICOLON'
    pass

def p_var_declaration_3(p):
    'var_declaration : DOLAR ID IGUAL NUMERO SEMICOLON'
    pass

def p_var_declaration_4(p):
    'var_declaration : DOLAR ID IGUAL STRING SEMICOLON'
    pass

def p_error(p):
    #print str(dir(p))
    #print str(dir(cminus_lexer))
    if VERBOSE:
        if p is not None:
            print "Syntax error at line " + str(p.lexer.lineno) + " Unexpected token  " + str(p.value)
        else:
            print "Syntax error at line: " + str(php_lex.lexer.lineno)
    else:
        raise Exception('syntax', 'error')

parser = yacc.yacc()

if __name__ == '__main__':

    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin = 'ejemplos/variables.php'

    f = open(fin, 'r')
    data = f.read()
    print data
    parser.parse(data, tracking=True)
