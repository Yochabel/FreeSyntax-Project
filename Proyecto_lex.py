# PARTE 1: TOKENIZAR LA ENTRADA USANDO LEX
import json
import ply.lex as lex

# Paso 1: Proporcione una lista de tokens que defina
# PARTE 1: TOKENIZAR LA ENTRADA USANDO LEX


# Paso 1: Proporcione una lista de tokens que defina
# todos los posibles nombres de token que puede producir
# el lexer.
# La lista de tokens también es utilizada YACC
# para identificar terminales.

tokens = (
    "KEY_S",
    "PELICULAS",
    "CORCHETE_I",
    "CORCHETE_F", 
    "KEY_F",
    "DOSPUNTOS",
    "COMA",
    "VALUE",
    "TITULO",
    "ANIO",
    "GENERO",
    "DURACION",
    "DIRECTOR",
    "DIRECTORES",
    "ESTRELLAS",
    "CALIIMB",
    "COMILLAS"
)
   
# 

# Paso 2. Cada token se especifica escribiendo una regla
# de expresión regular, mediante declaraciones que usan
# un prefijo especial *t_* para indicar que define un token.

# Definición de tokens simples:

t_KEY_S = r'\{'
t_PELICULAS=r'\"peliculas\"'
t_CORCHETE_I= r' \['
t_CORCHETE_F=r'\]'
t_KEY_F= r'\}'
t_DOSPUNTOS= r'\:'
t_COMA= r'\,'
t_VALUE=r'[a-zA-Z0-9!¡\-À-ÿ \/ \. \']+'
t_TITULO=r'\"titulo\"'
t_ANIO=r'\"anio\"' 
t_GENERO=r'\"genero\"' 
t_DURACION=r'\"duracion\"' 
t_DIRECTOR=r'\"director\"' 
t_DIRECTORES=r'\"directores\"'
t_ESTRELLAS=r'\"estrellas\"'
t_CALIIMB=r'\"calificacionIMDB\"'
t_COMILLAS=r'\"'

#

# Definición de tokens que incluye código para
# complementar, por ejemplo, para la definición de número,
# se incluye su conversión a entero (para este caso):

##def t_NUMBER(t):
##    r'\d+'
##    t.value = int(t.value)
##    return t


# Para incluir caracteres a ignorar, en este caso,
# tabuladores y espacios.
t_ignore  = " \t\n"


# Para el manejo de errores en las entradas
def t_error(t):
    print('Illegal character', t.value[0])
    t.lexer.skip(1)


# Paso 3. Crear el objeto tipo lex (el tokenizador)
lexer = lex.lex()

with open('archivos.json', 'r',encoding='utf-8') as file:
    data = json.load(file)
    data = json.dumps(data,ensure_ascii=False)
    
    lexer.input(data)
for token in lexer:
   print(token.type ,':',  token.value)