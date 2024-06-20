print ("Questo programmma permette di calcolare il perimetro di una figura scelta \n quadrato: >>1 \n triangolo equilatero: >>2 \n rombo: >>3")
x = int (input ("Scegliere la figura: "))
if x == 1:
	print ("hai selezionato il perimetro del quadrato")
	lato = float (input("inserisce il valore del lato del quadrato: "))
	print ("il perimeto del quadrato, avente lato", lato, "è:", lato*4)
elif x == 2:
	print ("hai selezionato il perimetro del triangolo equilatero")
	lato = float (input("inserisce il valore del lato del triangolo equilatero: "))
	print ("il perimeto del triangolo equilatero, avente lato", lato, "è:", lato*3)
elif x == 3:
	print ("hai selezionato il perimetro del rombo")
	lato = float (input("inserisce il valore del lato del rombo: "))
	print ("il perimeto del rombo, avente lato", lato, "è:", lato*4)
else:
	print ("inserisce una scelta valida")
