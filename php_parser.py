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
    '''declaration : var_declaration
                    | print_declaration
                    | while_declaration'''

def p_var_declaration_1(p):
    'var_declaration : variable SEMICOLON'
    pass

def p_var_declaration_2(p):
    'var_declaration : variable LCORCHETE NUMERO RCORCHETE SEMICOLON'
    pass

def p_var_declaration_3(p):
    'var_declaration : variable IGUAL strnum SEMICOLON'
    pass

def p_var_declaration_4(p):
    '''var_declaration : variable MAS variable SEMICOLON
                        | variable MENOS variable SEMICOLON
                        | variable MULTI variable SEMICOLON
                        | variable DIVI variable SEMICOLON
                        | variable MASMAS SEMICOLON
                        | variable MENOSMENOS SEMICOLON'''
    pass

def p_while_declaration(p):
    'while_declaration : WHILE LPAREN variable cond strnum RPAREN LLLAVE  expresion RLLAVE'
    pass

def p_print_declaration(p):
    '''print_declaration : ECHO var_declaration
                                | ECHO strnum SEMICOLON'''

def p_cond(p):
    '''cond : MENOR
                    | MENORIGUAL
                    | MAYOR
                    | MAYORIGUAL
                    | IGUAL
                    | DISTINTO'''
    pass


def p_expresion(p):
    '''expresion : var_declaration
                    | print_declaration'''
    pass

def p_strnum(p):
    '''strnum : STRING
                    | NUMERO'''
    pass

def p_variable(p):
    'variable : DOLAR ID'
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
