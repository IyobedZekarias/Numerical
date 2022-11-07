import string
from Library.Rational import Rational
from Library.lunum import ln, e, cos, sin, tan, sqrt, NaiveGauss, Gauss, bisection, secant, NewtonInterp, RichExtrap, Trapezoidal, Romberg, Simpson, Spline, Rand, MonteCarlo
import numpy as np

def parseform(f: string, vars: list): 
    f = f.replace(" ", "")
    f = f.replace("^", "**")
    i = 0
    while(i < len(f)):
        c = f[i]
        if(c.isnumeric()):
            if(i > 0): 
               l = f[i-1]
               if(l == ')'): 
                    f = f[:i] + '*' + f[i:]
                    i+=1
            if(i < len(f) - 1): 
                counter = ''
                while((i + 1) < len(f) and f[i + 1].isnumeric()):
                    counter += f[i + 1]
                    f = f[:i+1] + f[i+2:]
                if(i + 1 >= len(f)):
                    f += counter
                    break;
                r = f[i + 1]
                if(r == '(' or r.isalpha()):
                    if(r in vars): 
                        vcounter = ''
                        while((i + 2) < len(f) and f[i + 2] in vars and not (r == '(')): 
                            vcounter += f[i+2] + '*'
                            f = f[:i+2] + f[i+3:]
                        vcounter = vcounter[:len(vcounter) - 1]
                        if(i + 2 < len(f) - 1 and (f[i+2].isalpha() or f[i+2] == '(')):
                            if(len(vcounter)):
                                f = f[:i] + '(' + c + counter + '*'+r+'*'+vcounter +')*' + f[i+2:] 
                                i += len(counter) + 6 + (len(vcounter))
                            else:
                                f = f[:i] + '(' + c + counter + '*'+r+')*' + f[i+2:] 
                                i += len(counter) + 5
                        else: 
                            if(len(vcounter)):
                                f = f[:i] + '(' + c + counter + '*'+r+'*'+vcounter+')' + f[i+2:]
                                i += len(counter) + 5 + (len(vcounter))
                            else:
                                f = f[:i] + '(' + c + counter + '*'+r+')' + f[i+2:]
                                i += len(counter) + 4 + (len(vcounter))
                    else: 
                        f = f[:i+1] + counter + "*" + f[i+1:]
                        i += len(counter) + 1
        if(c.isalpha()):
            if(i > 0): 
               l = f[i-1]
               if(l == ')'): 
                    f = f[:i] + '*' + f[i:]
                    i+=1
            if(i < len(f)-1): 
                if(c in vars):
                    r = f[i + 1]
                    if(r in vars or r.isnumeric()): 
                        f = f[:i+1] + '*' + f[i+1:]
                        i += 1

        if(c == '('):
            if(i > 0): 
               l = f[i-1]
               if(l == ')'): 
                    f = f[:i] + '*' + f[i:]
                    i+=1
        i += 1

    print(f)
    return f

reservedVars = ['l','n','e','c','o','s','i','t','a','q','r','t'];


from flask import Flask, request
app = Flask(__name__)
#Make an app.route() decorator here

@app.route('/')
def hello_world():
    return 'i love you Alexye 💛'

@app.route("/rational", methods = ['GET', 'POST'])
def RationalFunction():
    if request.method == 'GET':
        data = {'example': 'working'}
        print('working')
        return {'data': data}, 200

    elif request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if(content_type != 'application/json'):
            num = request.args.get('num')
            den = request.args.get('den')
            data = {
                'num': num,
                'den': den,
                'Rational': Rational(int(num), int(den)).__str__() 
            }
            return {'data': data}, 200
        else: 
            json = request.json
            print(json)
            print(type(json))
            destination : string = json['function']
            del json['function']
            
            
            #gaussian
            if destination.startswith('g') or destination.startswith('G'):
                keys = list(json.keys())
                matrix = np.array([[Rational(json[i][0][j], json[i][1][j]) for j in range(len(json[i][0]))] for i in keys])
                if(len(keys) != len(matrix[0]) - 1): 
                    return {'Message' : 'matrix size incorrect, matrix needs to be size rows = rows, cols = rows + 1'}, 405
                try:
                    Naive = NaiveGauss(matrix)
                    iGauss = Gauss(matrix)
                except: 
                    print('there was an error')
                    return {'Message': 'python precision surpassed, use smaller matrix size'}, 405
                nstr = [i.__str__() for i in Naive]
                gstr = [i.__str__() for i in iGauss]
                return {'Naive': nstr, 'Gaussian': gstr}, 200
           
            #interpolation
            elif((destination.startswith('i') or destination.startswith('I')) and (destination.lower()[4] == 'r')): 
                xvals = [Rational(json['points']['x'][0][i], json['points']['x'][1][i]) for i in range(len(json['points']['x'][0]))]
                yvals = [Rational(json['points']['y'][0][i], json['points']['y'][1][i]) for i in range(len(json['points']['y'][0]))]
                x = Rational(json['x']['num'], json['x']['den'])
                return {'Newton': NewtonInterp(x, xvals, yvals).__str__()}, 200
            
            
            #Extrapolation
            elif(destination.startswith('E') or destination.startswith('e')):
                x = Rational(json['x']['num'], json['x']['den'])
                formula = json['f(x)']
                if('x' not in formula):
                    return {'Message': 'Formula mal-formed, f(x) must contain x'}, 405 
                formula = parseform(formula, ['x'])
                try:
                    f = lambda x : eval(formula)
                    return {'Richardson': RichExtrap(f, x, l=0, u=10)[9][9].__str__()}, 200
                except Exception as e:
                    if('floor' in str(e)): 
                        return {'Message': 'Extrapolation contains complex number, beyond scope of this project'}, 405
                    return{'Message': str(e)}, 405
                
            #Monte Carlo
            elif(destination.startswith('M') or destination.startswith('m')):
                formula = json['f(x)']
                vars = json['vars']
                for i in vars: 
                    if (i not in formula): 
                        return {'Message': 'Formula mal-formed, must contain ' + i}, 405
                    if (i in reservedVars):
                        return {'Message': i + ' not allowed as a variable'}, 405
                bounds = [tuple(i) for i in json['bounds']]
                formula = parseform(formula, vars)
                for i in range(len(vars)): 
                    formula = formula.replace(vars[i], 'args[' + i.__str__() + ']')
                try: 
                    f = lambda args : eval(formula)
                    D = MonteCarlo(f, bounds, size=9000, rep=5000)
                    print(D)
                    return {'Monte': D}, 200
                except Exception as e: 
                    return{'Message': str(e)}, 405
                
            
            elif((destination.startswith('i') or destination.startswith('I')) and (destination.lower()[4] == 'g')): 
                formula = json['f(x)']
                ubound = Rational(float(json['bounds']['upper']), 1)
                lbound = Rational(float(json['bounds']['lower']), 1)
                if('x' not in formula):
                    return {'Message': 'Formula mal-formed, f(x) must contain x'}, 405 
                formula = parseform(formula, ['x'])
                try:
                    f = lambda x : eval(formula)
                    return {'Trapezoidal': Trapezoidal(f, lbound, ubound).__str__(), 
                            'Romberg': Romberg(f, lbound, ubound).__str__(), 
                            'Simpson': Simpson(f, lbound, ubound).__str__()}, 200
                except Exception as e:
                    return{'Message': str(e)}, 405


            
            elif(destination.startswith('i') or destination.startswith('I')):
                return {'Message': 'Unclear function: function value must equal integrate or interpolate'}, 405


            else : 
                return {'Message': 'You didn\'t get a function'}, 405

    
if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)