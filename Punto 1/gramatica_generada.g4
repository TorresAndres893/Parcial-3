grammar Grama2;

CREATE : 'CREATE' ;
TABLE : 'TABLE' ;
INSERT : 'INSERT' ;
INTO : 'INTO' ;
VALUES : 'VALUES' ;
SELECT : 'SELECT' ;
FROM : 'FROM' ;
WHERE : 'WHERE' ;
UPDATE : 'UPDATE' ;
SET : 'SET' ;
DELETE : 'DELETE' ;
DROP : 'DROP' ;
AND : 'AND' ;
OR : 'OR' ;
TRUE : 'TRUE' ;
FALSE : 'FALSE' ;
ID : [a-zA-Z][a-zA-Z0-9_]* ;
NUMBER : [0-9]+ ('.' [0-9]+)? ;
STRING : '\'' ~[']* '\'' ;
EQ : '=' ;
NE : '!=' ;
GT : '>' ;
LT : '<' ;
GE : '>=' ;
LE : '<=' ;
SEMICOLON : ';' ;
COMMA : ',' ;
LPAREN : '(' ;
RPAREN : ')' ;
WS : [ \t\n\r]+ -> skip ;

programa
    : sentencia SEMICOLON programa
    | sentencia SEMICOLON
    ;

sentencia
    : create returns [String code, boolean valid]
    | read returns [String code, boolean valid]
    | update returns [String code, boolean valid]
    | delete returns [String code, boolean valid]
    ;

create returns [String code, boolean valid]
    : CREATE TABLE ID LPAREN listaCampos RPAREN { $code = $text; $valid = true; }
    | INSERT INTO ID LPAREN listaCampos RPAREN VALUES LPAREN listaValores RPAREN { $code = $text; $valid = true; }
    ;

read returns [String code, boolean valid]
    : SELECT listaCampos FROM ID { $code = $text; $valid = true; } (WHERE condicion)?
    ;

update returns [String code, boolean valid]
    : UPDATE ID SET listaAsignaciones { $code = $text; $valid = true; } (WHERE condicion)?
    ;

delete returns [String code, boolean valid]
    : DELETE FROM ID { $code = $text; $valid = true; } (WHERE condicion)?
    | DROP TABLE ID { $code = $text; $valid = true; }
    ;

listaCampos
    : ID (COMMA ID)*
    ;

listaValores
    : valor (COMMA valor)*
    ;

listaAsignaciones
    : asignacion (COMMA asignacion)*
    ;

asignacion
    : ID EQ valor
    ;

condicion
    : condicionSimple
    | condicion AND condicion
    | condicion OR condicion
    | LPAREN condicion RPAREN
    ;

condicionSimple
    : ID operador valor
    ;

operador
    : EQ
    | NE
    | GT
    | LT
    | GE
    | LE
    ;

valor
    : NUMBER
    | STRING
    | TRUE
    | FALSE
    ;