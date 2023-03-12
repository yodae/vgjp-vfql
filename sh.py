from selenium import webdriver

# especifica la ubicación del controlador de Chrome WebDriver
webdriver_path = "/path/to/chromedriver"

# crea una instancia del controlador de Chrome WebDriver
driver = webdriver.Chrome(webdriver_path)

# abre la página de Google
driver.get("https://yoelmod.blogspot.com/2022/02/hbo-max-premium-mod-apk-para-android.html")

#espera
sleep 10

# cierra el navegador
driver.quit()
