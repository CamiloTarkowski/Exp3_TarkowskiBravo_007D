function valiRegistro()
            {
                nom= document.getElementById('nombre').value;
                apellidop= document.getElementById('apellidop').value;
                apellidom= document.getElementById('apellidom').value;
                rut= document.getElementById('rut').value;
                fono= document.getElementById('fono').value;
                email= document.getElementById('email').value;
                confemail= document.getElementById('confemail').value;
                pass = document.getElementById('pass').value;
                confpass = document.getElementById('confpass').value; 
                genero = document.getElementById('genero').value;
                re=/^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/;
                terminos=document.getElementById('terminos').value; 

                if(nom == null || nom.length==0 || /^\s+$/.test(nom))
                {
                    alert('Debe escribir su(s) nombre(s)');
                    document.getElementById('nombre').value="";
                    document.datos.nom.focus();
                    return false;
                }
                if(apellidop == null || apellidop.length==0 || /^\s+$/.test(apellidop))
                {
                    alert('Debe escribir su apellido paterno');
                    document.getElementById('apellidop').value="";
                    document.datos.apellidop.focus();
                    return false;
                }
                if(apellidom == null || apellidom.length==0 || /^\s+$/.test(apellidom))
                {
                    alert('Debe escribir su apellido materno');
                    document.getElementById('apellidom').value="";
                    document.datos.apellidom.focus();
                    return false;
                }
                if(rut == null || rut.length==0 || /^\s+$/.test(rut))
                {
                    alert('Debe escribir su RUT');
                    document.getElementById('rut').value="";
                    document.datos.rut.focus();
                    return false;
                }
                if(!(/^\d{9}$/.test(fono)) )
                 {
                    alert('Debe ingresar un teléfono válido');
                    document.getElementById('fono').value="";
                    document.datos.fono.focus();
                    return false;
                }
                if(!re.exec(email)){
                    alert('El email ingresado no es válido');
                    document.datos.email.focus();
                    return false;
                }
                if(!re.exec(confemail)){
                    alert('Confirmación de email no válida');
                    document.datos.confemail.focus();
                    return false;
                }
                if(pass == null || pass.length==0 || /^\s+$/.test(pass))
                {
                    alert('Debe escribir su contraseña');
                    document.getElementById('pass').value="";
                    document.datos.pass.focus();
                    return false;
                }
                if(confpass == null || confpass.length==0 || /^\s+$/.test(confpass))
                {
                    alert('Debe confirmar su contraseña');
                    document.getElementById('confpass').value="";
                    document.datos.confpass.focus();
                    return false;
                }
               
                if (genero == null || genero == 0)
                {
                    alert('Seleccione género');
                    document.datos.genero.focus();
                    return false;
                }

                if (document.datos.terms.checked == false)
                {
                alert('Debe aceptar los términos y condiciones para continuar');
                return false;
                }

                if (confemail != email)
                {
                    alert('Error. Confirmación de email incorrecta');
                    document.datos.confemail.focus();
                    return false;

                }
                if (pass != confpass)
                {
                    alert('Error. Las contraseñas deben ser las mismas');
                    document.datos.confpass.focus();
                    return false;

                }
                alert('¡BIENVENIDO(A), '+nom+'! SU REGISTRO FUE EXITOSO.')
                return true;      

                
            }
function valiComentario(){
          nombre= document.getElementById('nombre').value;
          rut= document.getElementById('rut').value;
          fono= document.getElementById('fono').value;
          email= document.getElementById('email').value;
          tipocoment = document.getElementById('tipocomentario').value;
          comentario=document.getElementById('comentario').value;
          re=/^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/;

                if(nombre == null || nombre.length==0 || /^\s+$/.test(nombre))
                {
                alert('Debe escribir su nombre completo');
                    document.getElementById('nombre').value="";
                    document.datos.nombre.focus();
                    return false;
                }
                if(rut == null || rut.length==0 || /^\s+$/.test(rut))
                {
                    alert('Debe escribir su RUT');
                    document.getElementById('rut').value="";
                    document.datos.rut.focus();
                    return false;
                }
                if(!(/^\d{9}$/.test(fono)) )
                 {
                    alert('Debe ingresar un teléfono válido');
                    document.getElementById('fono').value="";
                    document.datos.fono.focus();
                    return false;
                }
                if(!re.exec(email)){
                    alert('El email ingresado no es válido');
                    document.datos.email.focus();
                    return false;
                }
                
                
                if (tipocoment == null || tipocoment == 0)
                {
                    alert('Seleccione tipo de comentario');
                    document.datos.genero.focus();
                    return false;
                }
                if(comentario == null || comentario.length==0 || /^\s+$/.test(comentario))
                {
                alert('Debe escribir su comentario');
                    document.getElementById('nombre').value="";
                    document.datos.nom.focus();
                    return false;
                }

                alert('Gracias por tu comentario. Tu opinión nos ayuda a mejorar')
                return true;

}