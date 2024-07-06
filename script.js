document.addEventListener("DOMContentLoaded",()=>{
    const form=document.getElementById("productoForm");
    const tableBody=document.getElementById("productosTable").querySelector("tbody");
    let isUpdating= false;

    //async permite que la funcion se comporte de manera asincrona,
    //puede ejecutar operaciones sin bloquear el hilo principal de ejecución
    const fetchProductos= async () => {
        //luego cambiaremos la url por https://<hostdepanywhere>/productos
        const response=await fetch("https://karyaguilar.pythonanywhere.com/productos");
        const productos= await response.json();
        tableBody.innerHTML=
        productos.forEach(producto=> {
            const row =document.createElement("tr");
            row.innerHTML=
                <><td>${producto.id}
                </td><td>${producto.nombre} 
                    </td><td>${producto.cantidad}
                        </td><td>${producto.precio}
                            </td><td>
    <button onclick="editProducto" />(${producto.id},"${producto.nombre},${producto.cantidad},${producto.precio})" Editar</td>
                        
                        <button onclick="deleteProducto(${producto.id}" >Eliminar</button></>
                    
    
                    tableBody.appendChild(row);
        });
    };

    const addproducto = async (producto)=>{
        await fetch( "https://karyaguilar.pythonanywhere.com/nuevo_productos",{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body: JSON.stringify(producto)
        });
        fetchProductos();
    };
    
    const updateProducto=async(id,producto)=> {
        await fetch( "https://karyaguilar.pythonanywhere.com/eliminar_productos/${id}",{
            method:"PUT",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify(producto)
        });
        fetchProductos();
    };
    const deleteProducto=async(id)=> {
        await fetch( "https://karyaguilar.pythonanywhere.com/actualizar_productos/${id}",{
            method:"DELETE" 
        });
        fetchProductos();
    };
    form.addEventListener("submit", (e)=>{
        e.preventDefault();
        const id=document.getElementById("productoId").value;
        const nombre=document.getElementById("nombre").value;
        const cantidad=document.getElementById("cantidad").value;
        const precio=document.getElementById("precio").value;
        const producto=document.getElementById("nombre, cantidad,precio");
        if (isUpdating) {
            updateProducto(id,producto)
            isUpdating=false;
                }else{
        addproducto(producto);
                }
            
                form.reset();
                document.getElementById("producto").value="";
    });

    window.editProducto=(id,nombre,cantidad,precio)=> {
        document.getElementById("productoId").value=id;
        document.getElementById("nombre").value=nombre;
        document.getElementById("cantida").value=cantidad;
        document.getElementById("precio").value=precio;
        isUpdating=true;
    };
    window.deleteProducto=(id)=>{
        if(confirm("estas seguro de eliminar este producto?")){
            deleteProducto(id);
        }
    };
        fetchProductos(); 
});
