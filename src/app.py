import streamlit as st
from basedatos import (
    crear_empleado, listar_empleados,
    crear_departamento, listar_departamentos,
)

st.set_page_config(page_title="EcoTech Solutions", layout="wide")
st.title("EcoTech Solutions - Sistema de Gestión Interna")

# Menú lateral para elegir sección
seccion = st.sidebar.radio("Ir a:", ["Empleados", "Departamentos"])

if seccion == "Empleados":
    st.header("Gestión de Empleados")

    with st.form("form_empleado"):
        nombre = st.text_input("Nombre")
        direccion = st.text_input("Dirección")
        telefono = st.text_input("Teléfono")
        mail = st.text_input("Correo")
        fecha_inicio = st.date_input("Fecha de inicio")
        salario = st.number_input("Salario", min_value=0.0, step=1000.0)

        enviado = st.form_submit_button("Guardar empleado")

        if enviado:
            if nombre and direccion and telefono and mail:
                nuevo_id = crear_empleado(
                    nombre, direccion, telefono, mail, str(fecha_inicio), salario
                )
                if nuevo_id:
                    st.success(f"Empleado creado con ID {nuevo_id}")
                else:
                    st.error("No se pudo crear el empleado. Revisa la terminal para más detalle.")
            else:
                st.warning("Completa todos los campos obligatorios.")

    st.subheader("Empleados registrados")
    empleados = listar_empleados()
    if empleados:
        st.dataframe(empleados)
    else:
        st.info("Aún no hay empleados registrados.")

elif seccion == "Departamentos":
    st.header("Gestión de Departamentos")

    with st.form("form_departamento"):
        nombre = st.text_input("Nombre del departamento")
        descripcion = st.text_area("Descripción")
        gerente = st.text_input("Gerente")

        enviado = st.form_submit_button("Guardar departamento")

        if enviado:
            if nombre and descripcion:
                nuevo_id = crear_departamento(nombre, descripcion, gerente)
                if nuevo_id:
                    st.success(f"Departamento creado con ID {nuevo_id}")
                else:
                    st.error("No se pudo crear el departamento (¿el nombre ya existe?).")
            else:
                st.warning("Completa nombre y descripción.")

    st.subheader("Departamentos registrados")
    departamentos = listar_departamentos()
    if departamentos:
        st.dataframe(departamentos)
    else:
        st.info("Aún no hay departamentos registrados.")