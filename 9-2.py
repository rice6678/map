import folium
import webbrowser

m=folium.Map([36.509966169639654, 127.2659707123968], zoom_start=15)

folium.Marker([36.50836270150055, 127.26884668756118], popup='학교').add_to(m)
folium.Marker([36.511481685979106, 127.26299314522721], popup='초등학교').add_to(m)
folium.Marker([36.509984857079395, 127.26629368754531], popup='우리집').add_to(m)

m.save('index.html')
webbrowser.open('index.html')
