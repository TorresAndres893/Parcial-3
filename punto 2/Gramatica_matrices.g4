grammar Gramatica_matrices;

program
    : expr EOF
    ;

expr
    : expr '.' expr      # MulExpr
    | expr '+' expr      # AddExpr
    | expr '-' expr      # SubExpr
    | matrix             # MatrixLiteral
    | ID                 # Var
    | '(' expr ')'       # ParExpr
    ;

matrix
    : '[' row (',' row)* ']'
    ;

row
    : '[' INT (',' INT)* ']'
    ;

ID  : [a-zA-Z_][a-zA-Z0-9_]* ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;
