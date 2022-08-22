from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\driverChrome\chromedriver.exe")
driver.get("http://localhost:3000/login")
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test.png")


#prueba para ir al area de registar usuario
link_de_registro = driver.find_element("id", "btn_r")
link_de_registro.click()


#prueba de registro de usuario
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test2.png")
registro = driver.find_element("name", "name")
registro.send_keys("usuario_nuevo2")
registro2 = driver.find_element("name", "user")
registro2.send_keys("usuario_nuevo2")
registro3 = driver.find_element("name", "password")
registro3.send_keys("usuario_nuevo2")
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test3.png")
registro.send_keys(Keys.ENTER)
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test4.png")
time.sleep(3)

#prueba de redireccion a login
ir_a_login = driver.find_element("id", "btn_lg")
ir_a_login.click()
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test5.png")
time.sleep(3)

# Prueba de login con datos incorrectos
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test6.png")
usuario = driver.find_element("name", "user")
usuario.send_keys("usuario_inexistente")
password = driver.find_element("name", "password")
password.send_keys("12345")
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test7.png")
usuario.send_keys(Keys.ENTER)
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test8.png")
time.sleep(3)

#brueba de login con campos vacios
usuario = driver.find_element("name", "user")
usuario.send_keys("")
password = driver.find_element("name", "password")
password.send_keys("")
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test9.png")
usuario.send_keys(Keys.ENTER)
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test10.png")
time.sleep(3)

#Prueba de login con datos correctos
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test11.png")
usuario = driver.find_element("name", "user")
usuario.send_keys("admin")
password = driver.find_element("name", "password")
password.send_keys("admin")
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test12.png")
usuario.send_keys(Keys.ENTER)
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test13.png")
time.sleep(3)

#Ver lista de libros
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test14.png")
libros = driver.find_element("id", "biblioteca")
libros.click()
time.sleep(3)

#LLamar formulario de registro de libros
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test15.png")
libros= driver.find_element("id","lib_b")
libros.click()
time.sleep(3)

#Prueba de registro de libros
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test16.png")
libros = driver.find_element("name", "titulo")
libros.send_keys("El quijote")
libros = driver.find_element("name", "autor")
libros.send_keys("Miguel del Cervantes")
libros = driver.find_element("name", "genero")
libros.send_keys("Fantasia")
libros = driver.find_element("name", "paginas")
libros.send_keys(500)
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test17.png")
libros.send_keys(Keys.ENTER)

#prueba de cierre de seccion
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test18.png")
libros= driver.find_element("id","salir")
libros.click()
time.sleep(3)
driver.get_screenshot_as_file("C:\\Users\\brian\\PycharmProjects\\test_p\\imagenes\\test19.png")










