#Importo PyAutogui la libreria para automatizar y la llamo auto 
import pyautogui as auto

#Con el metodo locateCenterOnScreen nos permite que encuentre las coordenadas donde se encuentra la foto que le pasemos como argumento 
x,y = auto.locateCenterOnScreen('mas.png')
#Con la funcion moveTo le pasamos como argumentos donde se va a mover y el tiempo en que va a mover el cursor
auto.moveTo(x,y,1)
#Con la funcion click hacemos que el curso de click 
auto.click(x, y)
#Con la funcion sleep hacemos que pare la ejecución por 1 segundo
auto.sleep(1)
#Con la funcion write hacemos que escriba lo que le pasamos como argumento y con el interval haemos que se escriba en esa cantidad de segundos
auto.write('cd',interval=0.05)
auto.sleep(1)
#Con la función press hacemos que presione la tecla que le pasamos como argumento
auto.press('enter')
auto.sleep(1)
auto.write('cd Desktop',interval=0.05)
auto.press('enter')
auto.sleep(1)
auto.write('mkdir helloWorld',interval=0.05)
auto.press('enter')
auto.sleep(1)
auto.write('cd helloWorld',interval=0.05)
auto.press('enter')
auto.sleep(1)
auto.write('cat > info.txt',interval=0.05)
auto.press('enter')
auto.sleep(1)
auto.write('Nombre -- Cristian',interval=0.05)
auto.sleep(1)
auto.press('enter')
auto.write('Edad -- 20',interval=0.05)
auto.sleep(1)
auto.press('enter')
auto.write('Skills -- Programming in general',interval=0.05)
auto.sleep(1)
auto.press('enter')
auto.write('Exp -- U',interval=0.05)
auto.sleep(1)
auto.press('enter')
auto.sleep(1)
#Con la funcion hotkey presione las teclas que le pasamos como argumento
auto.hotkey('ctrl','d')