import math
import sys

args = sys.argv

tipo = str(args[1]).split("=")

if tipo[1] != "annuity" or tipo[1] != "diff" or len(args) != 5:
    print("Incorrect parameters")

if tipo[1] == "annuity" and len(args) == 5:
    listaArgs1 = (args[2]).split("=")
    listaArgs2 = (args[3]).split("=")
    listaArgs3 = (args[4]).split("=")
    
    if listaArgs1[0] == "--principal" and listaArgs2[0] == "--periods" and listaArgs3[0] == "--interest": 
        P = int(listaArgs1[1])
        n = int(listaArgs2[1])
        i = float(listaArgs3[1]) / (12 * 100)
        if P > 0 and n > 0 and i > 0:
            A = P * ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
            A = math.ceil(A)
            overpayment = (A * n) - P
            print("Your annuity payment = "+str(A)+"!")
            print("Overpayment = "+str(overpayment))
        elif P < 0 or n < 0 or i < 0:
            print("Incorrect parameters")
                
    elif listaArgs1[0] == "--payment" and listaArgs2[0] == "--periods" and listaArgs3[0] == "--interest":
        A = int(listaArgs1[1])
        n = int(listaArgs2[1])
        i = float(listaArgs3[1]) / (12 * 100)
        if A > 0 and n > 0 and i > 0:
            P = A / (((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1)))
            P = math.floor(P)
            overpayment = (A * n) - P
            print("Your credit principal = "+str(P)+"!")
            print("Overpayment = "+str(overpayment))
        elif A < 0 or n < 0 or i < 0:
            print("Incorrect parameters")
    
    elif listaArgs1[0] == "--principal" and listaArgs2[0] == "--payment" and listaArgs3[0] == "--interest":
        P = int(listaArgs1[1])
        A = int(listaArgs2[1])
        i = float(listaArgs3[1]) / (12 * 100)

        if P > 0 and A > 0 and i > 0:
            base = 1 + i
            x = (A / (A - i * P))
            n = math.log(x, base)
            n = math.ceil(n)
            years = math.ceil(n) // 12
            months = math.ceil(n) % 12
            overpayment = A * n - P
            if years == 0:
                print("{} months".format(months))
                print("Overpayment = " + str(overpayment))
            elif months == 0:
                print("{} year".format(years))
                print("Overpayment = " + str(overpayment))
            else:
                print('You need {} years and {} months to repay this credit!'.format(years, months))
                print("Overpayment = " + str(overpayment))
        elif A < 0 or n < 0 or i < 0:
            print("Incorrect parameters")

elif tipo[1] == "diff" and len(args) == 5:
    listaArgs1 = (args[2]).split("=")
    listaArgs2 = (args[3]).split("=")
    listaArgs3 = (args[4]).split("=")
    
    P = int(listaArgs1[1])
    n = int(listaArgs2[1])
    i = float(listaArgs3[1]) / (12 * 100)
    D = [0]

    if listaArgs1[0] == "--principal" and listaArgs2[0] == "--periods" and listaArgs3[0] == "--interest" and P > 0 and n > 0 and i > 0:
        for m in range(1, n+1):
            calculo = math.ceil(P / n + i * (P - (P * (m - 1)) / n))
            D += [calculo]
        total = sum(D)
        overpayment = total - P
        for k in range(1, len(D)):
            print("Month " + str(k) + ": paid out " + str(D[k]))
        print()
        print("Overpayment = " + str(overpayment))
    elif listaArgs1[0] != "--principal" or listaArgs2[0] != "--periods" or listaArgs3[0] != "--interest" or P < 0 or n < 0 or i < 0:
        print("Incorrect parameters")
