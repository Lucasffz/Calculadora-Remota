import socket
import struct

formato_op = "i"
formato_1 = "f f"
formato_2 = "f"
socket_cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket_cliente.connect(("127.0.0.1",8080))




while True:
    print("###########################")
    print("Calculadora Remota.")
    print()
    print("Escolha o número de uma opção: ")
    print("1 para somar;")
    print("2 para subtrair;")
    print("3 para multiplicar")
    print("4 para dividir;")
    print("5 potência;")
    print("6 para raiz quadrada;")
    print("7 para fatorial")
    print("8 para sair.")
    op = int(input(">> "))
    op_pack = struct.pack(formato_op,op)
    socket_cliente.sendall(op_pack)
    if op == 1:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        numeros_pack = struct.pack(formato_1,n1,n2)
        socket_cliente.sendall(numeros_pack)

        resposta = socket_cliente.recv(struct.calcsize(formato_2))
        resposta_unpack = struct.unpack(formato_2, resposta)
        print("O resultado da operação foi: %.0f" % resposta_unpack)

    elif op ==2:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        numeros_pack = struct.pack(formato_1, n1, n2)
        socket_cliente.sendall(numeros_pack)

        resposta = socket_cliente.recv(struct.calcsize(formato_2))
        resposta_unpack = struct.unpack(formato_2, resposta)
        print("O resultado da operação foi: %.0f" % resposta_unpack)
    elif op ==3:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        numeros_pack = struct.pack(formato_1, n1, n2)
        socket_cliente.sendall(numeros_pack)

        resposta = socket_cliente.recv(struct.calcsize(formato_2))
        resposta_unpack = struct.unpack(formato_2, resposta)
        print("O resultado da operação foi: %.0f" % resposta_unpack)

    elif op ==4:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        numeros_pack = struct.pack(formato_1, n1, n2)
        socket_cliente.sendall(numeros_pack)

        resposta = socket_cliente.recv(struct.calcsize(formato_2))
        resposta_unpack = struct.unpack(formato_2, resposta)
        print("O resultado da operação foi: %.0f" % resposta_unpack)

    elif op ==5:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        numeros_pack = struct.pack(formato_1, n1, n2)
        socket_cliente.sendall(numeros_pack)

        resposta = socket_cliente.recv(struct.calcsize(formato_2))
        resposta_unpack = struct.unpack(formato_2, resposta)
        print("O resultado da operação foi: %.0f" % resposta_unpack)

    elif op ==6:
        n = float(input("Digite um número: "))
        numero_pack = struct.pack(formato_2,n)
        socket_cliente.sendall(numero_pack)

        resposta = socket_cliente.recv(struct.calcsize(formato_2))
        resposta_unpack = struct.unpack(formato_2, resposta)
        print("O resultado da operação foi: %.0f" % resposta_unpack)

    elif op ==7:
        n = float(input("Digite um número: "))
        numero_pack = struct.pack(formato_2, n)
        socket_cliente.sendall(numero_pack)

        resposta = socket_cliente.recv(struct.calcsize(formato_2))
        resposta_unpack = struct.unpack(formato_2, resposta)
        print("O resultado da operação foi: %.0f" % resposta_unpack)


    elif op ==8:
        print("Cliente encerrando...")
        break
    else:
        print("a opção %i é invalida,tente novamente." % op)



















