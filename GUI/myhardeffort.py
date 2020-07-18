
a = "0.5+3/3-4*5+5"
d = []


def divmul_calculate(string):
    final = string
    if len(d) == 0:
        item = 0
        while ("*" in final or "/" in final):
            #!By using a while loop, note that that all the numbers checked are the first numbers
            #!But since + and - are also included, we have to check where the multiply is.
            no_bedmas = []
            for checker in range(0, len(final)):
                if final[checker] == "+" or\
                        final[checker] == "-" or\
                    final[checker] == "*" or\
                        final[checker] == "/":
                    no_bedmas.append(checker)

            if final[item] == "*"\
                    or final[item] == "/":
                if final[item] == "*":
                    mul_location = no_bedmas.index(item)
                    if mul_location == 0:
                        first_num = float(final[:no_bedmas[0]])
                        if len(no_bedmas) == 1:
                            second_num = float(final[no_bedmas[0] + 1:])
                            result = first_num * second_num
                            final = result
                            if final % 1 == 0:
                                final = str(int(final))
                            else:
                                final = str(round(final, 14))

                        else:
                            second_num = float(
                                final[no_bedmas[0] + 1: no_bedmas[1]])
                            result = first_num * second_num
                            final = final.replace(
                                final[:no_bedmas[1]], str(result))
                            item = 0

                    elif mul_location == len(no_bedmas) - 1:
                        first_num = float(
                            final[(no_bedmas[mul_location - 1]) + 1:no_bedmas[mul_location]])
                        second_num = float(final[item + 1:])
                        result = first_num * second_num
                        final = final.replace(
                            final[(no_bedmas[mul_location - 1]) + 1:], str(result))
                        item = 0
                    else:
                        first_num = float(
                            final[(no_bedmas[mul_location - 1]) + 1:no_bedmas[mul_location]])
                        second_num = float(
                            final[no_bedmas[mul_location] + 1: no_bedmas[mul_location + 1]])
                        result = first_num * second_num
                        final = final.replace(
                            final[(no_bedmas[mul_location - 1]) + 1: no_bedmas[mul_location + 1]], str(result))
                        item = 0

                elif final[item] == "/":
                    div_location = no_bedmas.index(item)
                    if div_location == 0:
                        first_num = float(final[:no_bedmas[0]])
                        if len(no_bedmas) == 1:
                            second_num = float(final[no_bedmas[0] + 1:])
                            result = first_num / second_num
                            final = result
                            if final % 1 == 0:
                                final = str(int(final))
                            else:
                                final = str(round(final, 14))

                        else:
                            second_num = float(
                                final[no_bedmas[0] + 1: no_bedmas[1]])
                            result = first_num / second_num
                            final = final.replace(
                                final[:no_bedmas[1]], str(result))
                            item = 0

                    elif div_location == len(no_bedmas) - 1:
                        first_num = float(
                            final[(no_bedmas[div_location - 1]) + 1:no_bedmas[div_location]])
                        second_num = float(final[item + 1:])
                        result = first_num / second_num
                        final = final.replace(
                            final[(no_bedmas[div_location - 1]) + 1:], str(result))
                        item = 0
                    else:
                        first_num = float(
                            final[(no_bedmas[div_location - 1]) + 1:no_bedmas[div_location]])
                        second_num = float(
                            final[no_bedmas[div_location] + 1: no_bedmas[div_location + 1]])
                        result = first_num / second_num
                        final = final.replace(
                            final[(no_bedmas[div_location - 1]) + 1: no_bedmas[div_location + 1]], str(result))
                        item = 0

            else:
                item += 1
    return final


b = divmul_calculate(a)


def plusminus_calculate(string):
    final = string
    if len(d) == 0:
        item = 0
        while ("+" in final or "-" in final):
            #!By using a while loop, note that that all the numbers checked are the first numbers
            #!But since + and - are also included, we have to check where the multiply is.
            no_bedmas = []
            for checker in range(0, len(final)):
                if final[checker] == "+" or\
                        final[checker] == "-" or\
                    final[checker] == "*" or\
                        final[checker] == "/":
                    no_bedmas.append(checker)

            if final[item] == "+"\
                    or final[item] == "-":
                if final[item] == "+":
                    plus_location = no_bedmas.index(item)
                    if plus_location == 0:
                        first_num = float(final[:no_bedmas[0]])
                        if len(no_bedmas) == 1:
                            second_num = float(final[no_bedmas[0] + 1:])
                            result = first_num + second_num
                            final = result
                            if final % 1 == 0:
                                final = str(int(final))
                            else:
                                final = str(round(final, 14))

                        else:
                            second_num = float(
                                final[no_bedmas[0] + 1: no_bedmas[1]])
                            result = first_num + second_num
                            final = final.replace(
                                final[:no_bedmas[1]], str(result))
                            item = 0

                    elif plus_location == len(no_bedmas) - 1:
                        first_num = float(
                            final[(no_bedmas[plus_location - 1]) + 1:no_bedmas[plus_location]])
                        second_num = float(final[item + 1:])
                        result = first_num + second_num
                        final = final.replace(
                            final[(no_bedmas[plus_location - 1]) + 1:], str(result))
                        item = 0
                    else:
                        first_num = float(
                            final[(no_bedmas[plus_location - 1]) + 1:no_bedmas[plus_location]])
                        second_num = float(
                            final[no_bedmas[plus_location] + 1: no_bedmas[plus_location + 1]])
                        result = first_num + second_num
                        final = final.replace(
                            final[(no_bedmas[plus_location - 1]) + 1: no_bedmas[plus_location + 1]], str(result))
                        item = 0

                elif final[item] == "-":
                    minus_location = no_bedmas.index(item)
                    if minus_location == 0:
                      #!Gives error for negative values since the computer recognizes the negative sign
                        first_num = float(final[:no_bedmas[0]])
                        if len(no_bedmas) == 1:
                            second_num = float(final[no_bedmas[0] + 1:])
                            result = first_num - second_num
                            final = result
                            if final % 1 == 0:
                                final = str(int(final))
                            else:
                                final = str(round(final, 14))

                        else:
                            second_num = float(
                                final[no_bedmas[0] + 1: no_bedmas[1]])
                            result = first_num - second_num
                            final = final.replace(
                                final[:no_bedmas[1]], str(result))
                            item = 0

                    elif minus_location == len(no_bedmas) - 1:
                        first_num = float(
                            final[(no_bedmas[minus_location - 1]) + 1:no_bedmas[minus_location]])
                        second_num = float(final[item + 1:])
                        result = first_num - second_num
                        final = final.replace(
                            final[(no_bedmas[minus_location - 1]) + 1:], str(result))
                        item = 0
                    else:
                        first_num = float(
                            final[(no_bedmas[minus_location - 1]) + 1:no_bedmas[minus_location]])
                        second_num = float(
                            final[no_bedmas[minus_location] + 1: no_bedmas[minus_location + 1]])
                        result = first_num - second_num
                        final = final.replace(
                            final[(no_bedmas[minus_location - 1]) + 1: no_bedmas[minus_location + 1]], str(result))
                        item = 0

            else:
                item += 1
    return final


print(plusminus_calculate(b))


