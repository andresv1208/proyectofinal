import streamlit as st
st.markdown("---")
st.title("Cifrado césar")

st.markdown("En el cifrado César a cada letra del abecedario se desplaza x cantidad de puestos quedando $C=(P+K) mod 27$ donde C es la posición de la letra en el texto cifrado, P es la posición de la letra en el texto original, K es el desplazamiento y $mod 27$ es el modulo del alfabeto ya que tiene 27 letras. ")
st.markdown("---")

def cifrado_cesar(texto, desplazamiento):
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    texto_cifrado = ""
    for letra in texto.lower():
        if letra in abecedario:
            posicion = abecedario.find(letra)
            nueva_posicion = (posicion + desplazamiento) % len(abecedario)
            letra_cifrada = abecedario[nueva_posicion]
            texto_cifrado += letra_cifrada
        else:
            texto_cifrado += letra
    return texto_cifrado
st.title("Primer paso del cifrado.")
st.markdown("Anota el texto que deseas cifrar (Recuerda que las tildes no serán afectadas por el cifrado).")
mensaje_original = st.text_area("Ingresa el texto a cifrar:")
st.markdown("En la famosa serie de cómics de Astérix, los galos interceptan mensajes cifrados de César utilizando el código César para frustrar sus planes expansionistas.")

st.markdown("---")
st.title("Segundo paso.")
st.markdown(" Decide cuántas posiciones deseas mover las letras en el alfabeto. Por ejemplo, si seleccionas un desplazamiento de 3, la letra ‘A’ se convertirá en ‘D’, ‘B’ en ‘E’, y así sucesivamente.")
desplazamiento = st.slider("Ingrese el digito de numeros que desea desplazar el texto:", min_value=1, max_value=27, value=3)

st.markdown("Julio César fue un líder político y militar clave durante la transición de la República Romana al Imperio Romano.")

st.markdown("---")

st.title("Tercer paso.")
st.markdown(" Reemplaza cada letra en el mensaje original con la letra desplazada en el alfabeto. Por ejemplo, si tienes la letra ‘H’ y un desplazamiento de 3, se convertirá en ‘K’.")
if st.button("Cifrar"):
    mensaje_cifrado = cifrado_cesar(mensaje_original, desplazamiento)
    st.success(f"Texto cifrado: {mensaje_cifrado}")
st.markdown("Julio César fue un prolífico escritor y orador. Sus obras, como “De Bello Gallico” (sobre las Guerras Galas), influyeron en la evolución del latín clásico.")

st.markdown("---")