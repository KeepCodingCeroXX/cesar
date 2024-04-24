def funcB():
    print("soy una funcion en B")

#Ejecutate solo cuando te llame directamente python, no cuando seas importado
if __name__ == "__main__":
    print("Y yo soy B, pero python me llama", __name__)