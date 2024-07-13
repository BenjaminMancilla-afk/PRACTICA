Proceso cachipum
	Definir jugador Como Entero;
	Definir CPU Como Entero;
	
	Definir opcionJugador, opcionCPU Como Caracter;
	
	Repetir
		Escribir "=== Cachipum ===";
		Escribir "1- Piedra";
		Escribir "2- Papel";
		Escribir "3- Tijera";
		Escribir "Ingresar una de las opciones:";
		Leer jugador;
		
		Si jugador <= 0  o jugador >= 4 Entonces
			Escribir "Opción no válida, intente nuevamente";
			Esperar 2 Segundos;
			Limpiar Pantalla;
		FinSi
		
	Hasta Que jugador > 0 y jugador < 4
	
	CPU = azar(3)+1;
	
	Si jugador = CPU Entonces
		Escribir "==== EMPATE ====";
	FinSi
	
	Si (jugador = 1 y CPU = 3) o (jugador=2 y CPU=1) o (jugador=3 y CPU=2) Entonces
		Escribir "==== GANASTE ====";
	FinSi
	
	Si (jugador=3 y CPU=1) o (jugador=1 y CPU=2) o (jugador=2 y CPU=3) Entonces
		Escribir "==== PERDISTE ====";
	FinSi
	
	Si jugador = 1 Entonces
		opcionJugador = "PIEDRA";
	FinSi
	Si jugador = 2 Entonces
		opcionJugador = "PAPEL";
	FinSi
	Si jugador = 3 Entonces
		opcionJugador = "TIJERAS";
	FinSi
	
	si CPU = 1 Entonces
		opcionCPU = "PIEDRA";
	FinSi
	si CPU = 2 Entonces
		opcionCPU = "PAPEL";
	FinSi
	si CPU = 3 Entonces
		opcionCPU = "TIJERAS";
	FinSi
	
	Escribir "Jugador: ", opcionJugador, " VS CPU: ", opcionCPU;
	
	Escribir "=== FIN ===";
	
FinProceso
