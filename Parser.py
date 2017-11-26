def pars(str, sub=" "):
    result = []
    buf=""
    for i in range(0, len(str)):
        if str[i] != sub:
            buf = buf+str[i]

        if str[i] == sub:
            if buf != "":
               result.append(buf)
               buf = ""

    if buf != "":
        result.append(buf)
    return result

def parstxt(file, sub = " "):
    str = file.read()
    result = []
    buf = ""
    for i in range(0, len(str)):
        if str[i] != sub:
            buf = buf + str[i]

        if str[i] == sub:
            if buf != "":
                result.append(buf)
                buf = ""

    if buf != "":
        result.append(buf)
    return result