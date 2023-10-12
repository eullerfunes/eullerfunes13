#RPA -robotic process automation

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
import pyautogui
import time
import pandas as pd

#Abrir chrome
time.sleep(3)
pyautogui.press("win")
time.sleep(2)
pyautogui.write("chrome")
time.sleep(2)
pyautogui.press("enter")
time.sleep(5)
pyautogui.hotkey("win", "up")

#Abrir Link
pyautogui.write (link)
pyautogui.press("enter")
time.sleep(10)
# Login
pyautogui.click(x=702, y=365)
time.sleep(1)
pyautogui.write("euller_funes@hotmail.com")
time.sleep(1)
pyautogui.click(x=398, y=461)
time.sleep(1)
pyautogui.write("aquidauana13")
time.sleep(1)
pyautogui.click(x=667, y=524)
time.sleep(1)
tabela = pd.read_csv("C:/Users/NOTE/Desktop/automacao/produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=406, y=247)
    
    pyautogui.write(str(tabela.loc[linha,"codigo"]))
    pyautogui.press("tab")
   
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")
   

    obs = tabela.loc[linha,"obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))

   
    pyautogui.press("tab")
  
    pyautogui.press("enter")
   
    pyautogui.scroll(5000)