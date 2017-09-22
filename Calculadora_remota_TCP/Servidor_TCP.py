import socket
import struct
import _thread
import math

formato_op = "i"
formato_1 = "f f"
formato_2 = "f"


def servidor_calculadora(socket_conexao, dados_cliente):
    while True:


        arquivo = open("log_servidor.txt", "a")
        arquivo.write("cliente %s conectou." % str(dados_cliente))
        arquivo.write("\n")
        print("cliente %s conectou." % str(dados_cliente))

        while True:
            op_recebido = socket_conexao.recv(struct.calcsize(formato_op))
            op_unpack = struct.unpack(formato_op, op_recebido)

            if op_unpack[0] == 1:
                numeros_recebidos = socket_conexao.recv(struct.calcsize(formato_1))
                numeros_unpack = struct.unpack(formato_1, numeros_recebidos)
                resultado = numeros_unpack[0] + numeros_unpack[1]
                resposta = struct.pack(formato_2, resultado)
                socket_conexao.sendall(resposta)
            elif op_unpack[0] == 2:
                numeros_recebidos = socket_conexao.recv(struct.calcsize(formato_1))
                numeros_unpack = struct.unpack(formato_1, numeros_recebidos)
                resultado = numeros_unpack[0] - numeros_unpack[1]

                resposta = struct.pack(formato_2, resultado)
                socket_conexao.sendall(resposta)
            elif op_unpack[0] == 3:
                numeros_recebidos = socket_conexao.recv(struct.calcsize(formato_1))
                numeros_unpack = struct.unpack(formato_1, numeros_recebidos)
                resultado = numeros_unpack[0] * numeros_unpack[1]

                resposta = struct.pack(formato_2, resultado)
                socket_conexao.sendall(resposta)
            elif op_unpack[0] == 4:
                numeros_recebidos = socket_conexao.recv(struct.calcsize(formato_1))
                numeros_unpack = struct.unpack(formato_1, numeros_recebidos)
                resultado = numeros_unpack[0] / numeros_unpack[1]

                resposta = struct.pack(formato_2, resultado)
                socket_conexao.sendall(resposta)
            elif op_unpack[0] == 5:
                numeros_recebidos = socket_conexao.recv(struct.calcsize(formato_1))
                numeros_unpack = struct.unpack(formato_1, numeros_recebidos)
                resultado = numeros_unpack[0] ** numeros_unpack[1]

                resposta = struct.pack(formato_2, resultado)
                socket_conexao.sendall(resposta)
            elif op_unpack[0] == 6:
                numeros_recebidos = socket_conexao.recv(struct.calcsize(formato_2))
                numeros_unpack = struct.unpack(formato_2, numeros_recebidos)
                resultado = math.sqrt(numeros_unpack[0])

                resposta = struct.pack(formato_2, resultado)
                socket_conexao.sendall(resposta)
            elif op_unpack[0] == 7:
                numeros_recebidos = socket_conexao.recv(struct.calcsize(formato_2))
                numeros_unpack = struct.unpack(formato_2, numeros_recebidos)

                resultado = 1
                for i in range(1, int(numeros_unpack[0] + 1)):
                    resultado = resultado * i
                resposta = struct.pack(formato_2, resultado)
                socket_conexao.sendall(resposta)

            elif op_unpack[0] == 8:
                print("cliente %s desconectou." % str(dados_cliente))
                arquivo.write("Cliente %s desconectou." % str(dados_cliente))
                arquivo.write("\n")
                break


            else:
                print("Cliente escolheu uma opção inválida:", op_unpack[0])

            if op_unpack[0] == 1 or op_unpack[0] == 2 or op_unpack[0] == 3 or op_unpack[0] == 4 or op_unpack[0] == 5:

                arquivo.write("Cliente %s enviou %i %f %f" % (
                str(dados_cliente), op_unpack[0], numeros_unpack[0], numeros_unpack[1]))
                arquivo.write("\n")
            elif op_unpack[0] == 6 or op_unpack[0] == 7:
                arquivo.write("Cliente %s enviou %i %f" % (str(dados_cliente), op_unpack[0], numeros_unpack[0]))
                arquivo.write("\n")
            else:
                arquivo.write("Cliente escolheu uma opção inválida: %i" % op_unpack)
        arquivo.close()
    socket_conexao.close()


socket_servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket_servidor.bind(("0.0.0.0",8080))

print("Aguardando conexão...")
socket_servidor.listen(3)
while True:
    socket_conexao, dados_cliente = socket_servidor.accept()
    _thread.start_new_thread(servidor_calculadora, (socket_conexao,dados_cliente))





