# Resumen del proceso

1. Se crea app para el modelo coffee_model.pkl usando Flask y un formulario básico.

2. El modelo toma valores de las siguientes variables:

* country, una de las siguientes opciones: Brazil, Colombia, Guatemala, Mexico, Taiwan, Other
* variety, una de las siguientes opciones: Bourbon, Catuai, Caturra, Typica, Other
* aroma, permite seleccionar un valor flotante entre 0 y 10
* aftertaste, idem aroma
* acidity, idem aroma
* body, idem aroma
* balance, idem aroma
* moisture, permite seleccionar un valor flotante entre 0 y 1

3. Por defecto country=Brazil, variety=Bourbon y los demás campos están vacíos. Se controla antes de realizar la predicción que se hayan completado todos los campos.

4. Para que se imprima el resultado se debe pulsar el botón PREDICT, siendo las opciones de respuesta dos (en función del resultado de la predicción):

* Es un café de especialidad.
* No es un café de especialidad.


Link de la app: https://coffee-model-flask.herokuapp.com/
