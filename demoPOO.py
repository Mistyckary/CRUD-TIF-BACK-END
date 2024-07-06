#clase

class Pelicula():
    def init__(self,n,d,a): #constructor
        self.nombre= n  #atributo
        self.director= d
        self.año= a
        
        def reproducirPelicula (self):#metodo
            return"reproduciendo" + self.nombre
            #def__del__(self):se llama automaticamente al finalizar el programa 
            # print ("Objeto Pelicula destruido")
            # 
            def__repr__(self)
            return f"Pelicula ( nombre= {self.nombre},director={self.director} ,año={self.año})"
            
            #instancia
            
            p=Pelicula("Mario Bros","Roberto Perez",2024) #objeto
            print(p.reproducirPelicula)
                #reproducirPelicula()  #da error
            print(repr(p))
                #del p
            print(p.reproducirPelicula() )
                
                

            #ENCAPSULAMIENTO
class Pelicula():
    def init__(self,nombre,director,año,precio):

        self.nombre="nombre"#atributos privados
        self.director
        self.año
        self.precio
                        
    def reproducirPelicula (self):
                        return"Reproduciendo"+self.__nombre
                            
                            # property y .setter:asociar correctamente los datos getter
                            # y setter con propiedad
@property
def nombre(self):
                                return self.__nombre
                                
                                @nombre.setter
                                def nombre(self, nuevoNombre):
                                    self.__nombre=nuevoNombre
            
@property
def director(self):
                                return self.__director
                                
                                @director.setter
                                def director(self, nuevodirecto):
                                    self.__director=nuevodirector
            
            
p=Pelicula("Mario Bros","Roberto Perez",2024,1000) 
print (p.año) #unico que no es privado
print (p.director) #metodo get
p.director= "Pepe Perez" #metodo set
print (p.director)
                        
                        #print (p.__nombre)  #dara error por estar privado
                        #print(p.__reproducirPelicula()) #da error tambien
                        

                        
                        #HERENCIA Y POLIMORFISMO

class PeliculaGratuita(Pelicula):
    def init__(self,nombre,director,año ):
                        super().__init__ ("nombre,director,año O")
                        
    def reproducirPelicula(self):
                        return"reproduciendo en 720.."
class PeliculaPaga(Pelicula):
    def init__(sel,nombre,director,año,precio):
                        
                        super().__init__(nombre,director,año,precio)
    def reproducirPelicula(self):
                        return "reproduciendo en ULTRA HD.."
                        pg=PeliculaGratuita("Mario" ,"Pepe Perez",2024)
                        print(pg.precio)
                        print(pg.reproducirPelicula())
                        
                        pp=PeliculaPaga("Titanic","Pepe Perez",2024,5000)
                        print(pp.precio)
                        print(pp.reproducirPelicula())
