
from Liga2 import gestionar_categorias

decision_usuario= str(input("Qué desea hacer:\n1.Gestionar equipos de fútbol\n2.Gestionar jugadores\nEscriba aquí "
"su respuesta\n==>"))
if decision_usuario=="1":
    gestionar_categorias()


