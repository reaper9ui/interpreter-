from lark import Lark; 

json_parser = Lark(
    """



    """
)

""" 
    <if statement> ::= if <cond> then <expr1> | <if statement> else “ <expr1> | <if statement> 
    <cond> ::= <expr1> = <expr1>
    <expr1> ::= <expr1> + <expr2> | <expr2> 
    <expr2> ::= <expr2> * <factor> | <factor>
    <factor> ::= <INTEGER> | <ID> | ( <expr> )
 """


