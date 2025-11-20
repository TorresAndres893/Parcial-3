grammar DotProduct;

prog
    : expr EOF
    ;

expr
    : expr '.' expr          
    | expr '+' expr         
    | expr '-' expr          
    | ID                     
    | '(' expr ')'           
    ;

ID  : [a-zA-Z_][a-zA-Z0-9_]* ;
WS  : [ \t\r\n]+ -> skip ;
