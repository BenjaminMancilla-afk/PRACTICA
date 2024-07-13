Algoritmo alexanderMancilla
    Definir nombreJugador, nivel como caracter;
    Definir opc, intentos, numeroAzar, numeroJugador, partida, intentosActuales como entero;
    Definir validacion, inicioPartida como logico;
	
    inicioPartida = verdadero;
	
    Escribir "Ingresa tu nombre: ";
    Leer nombreJugador;
	
    Mientras inicioPartida = Verdadero
        Repetir
            validacion = Falso;
            Imprimir "Menú :";
            Imprimir "1. Start";
            Imprimir "2. Salir";
            Escribir "Seleccione una opcion :";
            Leer opc;
            si opc = 1 o opc = 2
                validacion = Verdadero;
                si opc = 2
                    inicioPartida = falso;
                FinSi
            SiNo
                Limpiar Pantalla
                Imprimir "-Por favor seleccione una opcion valida-";
            FinSi
        Hasta Que validacion = Verdadero
        Si opc = 1
            Repetir
                validacion = Falso;
                Imprimir "Menú Dificultades:";
                Imprimir "1. Facil (12 intentos)";
                Imprimir "2. Medio (8 intentos)";
                Imprimir "3. Dificil (5 intentos)";
                Imprimir "4. Salir";
                Escribir "Seleccione una dificultad :";
                Leer opc;
                si opc = 1 o opc = 2 o opc = 3 o opc = 4
                    validacion = verdadero;
                    si opc = 4
                        inicioPartida = falso;
                    FinSi
                SiNo
                    Limpiar Pantalla
                    Imprimir "-Por favor seleccione una opcion valida-";
                FinSi
            Hasta Que validacion = Verdadero
			
            si opc <> 4
                
                si opc = 1
                    intentos = 12
                    nivel = "Facil"
                Sino
                    si opc = 2
                        intentos = 8
                        nivel = "Medio"
                    Sino
                        si opc = 3 
                            intentos = 5
                            nivel = "Dificil"
                        FinSi
                    FinSi
                FinSi
                
                numeroAzar = Aleatorio(1, 100);
                intentosActuales = 0;
				
                Repetir
                    intentosActuales = intentosActuales + 1;
                    validacion = Falso;
                    Escribir "Ingresa un número entre 1 y 100 :";
                    Leer numeroJugador;
                    si numeroJugador > numeroAzar
                        Imprimir " * El numero que buscas es MENOR";
                        Imprimir "Te quedan : ", intentos - intentosActuales;
                    Sino
                        si numeroJugador < numeroAzar
                            Imprimir " * El numero que buscas es MAYOR";
                            Imprimir "Te quedan : ", intentos - intentosActuales;
                        Sino
                            Limpiar Pantalla
                            Imprimir "Felicidades ", nombreJugador, " haz acertado con : ", intentosActuales, " intentos";
                            Imprimir "Numero secreto : ", numeroAzar;
                            Imprimir "Dificultad : ", nivel;
                            validacion = Verdadero;
                        FinSi
                    FinSi
					
                    Si intentosActuales >= intentos
                        Imprimir "Lo siento ", nombreJugador, " no lograste adivinar el numero en nivel ", nivel ;
                    FinSi
					
                Hasta Que validacion = Verdadero
                
                Repetir
                    Escribir "Desea volver a jugar ?";
                    Imprimir "1. Si";
                    Imprimir "2. No";
                    Leer partida;
                    
                    si partida <> 1 y partida <> 2
                        Limpiar Pantalla
                        Imprimir "-Por favor seleccione una opcion valida-";
                    FinSi
                Hasta Que partida = 1 o partida = 2
                
                Si partida = 2
                    inicioPartida = falso;
                FinSi
                
            FinSi
        FinSi
    FinMientras
	
    Imprimir "* Hasta Pronto ", nombreJugador;
	
FinAlgoritmo
