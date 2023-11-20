import joblib
import streamlit as st
import pandas as pd

modelo = joblib.load('starpredict.joblib.pkl')

cor_fundo = "#000000"  
cor_texto = "#FFFFFF" 
cor_destaque = "#0073E6" 
cor_sidebar = "#DC2831" 

st.set_page_config(
    page_title="Previsor Estelar",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

image_url = "https://cdn.mos.cms.futurecdn.net/7BHv7n2L3KJNuRgDDbaJVf-970-80.jpg"
st.image(image_url, use_column_width=True)

st.write("""
# Previsor Estelar

Este site consegue prever o tipo da Estrela com base em seus dados

## Propósito:
O objetivo de fazer o conjunto de dados é provar que as estrelas seguem um determinado gráfico no Espaço celeste, para que possamos classificar estrelas traçando suas características com base nos gráficos Hertzsprung-Russell e DiagramHR-Diagram
""")

img1 = "https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3791628%2F14338bbebf77d18e1faef582bccdbdd6%2Fhr.jpg?generation=1597349509841965&alt=media"
img2 = "https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F3791628%2Ffe9436bf4e2d23b5b18fb3db1f1fcbcb%2FHRDiagram.png?generation=1597348809674507&alt=media"
st.image(img1, use_column_width=True)
st.image(img2, use_column_width=True)

st.write("""
### observação:
O conjunto de dados é criado com base em várias equações em astrofísica. Eles são dados abaixo:

- Lei de Stefan-Boltzmann da radiação do corpo negro (Para encontrar a - luminosidade de uma estrela)
- Lei de deslocamento de Wienn (para encontrar a temperatura da superfície de uma estrela usando comprimento de onda)
- Relação de magnitude absoluta
- Raio de uma estrela usando paralaxe
""")

st.sidebar.title('Filtros')
st.sidebar.header('Características da Estrela 🌟')

Temperature = st.sidebar.slider('Temperatura (K)', 1939, 40000, 23546)
Luminosity = st.sidebar.slider('Luminosidade (L/Lo)', 0.0024, 849420.0, 30000.0)
Radius = st.sidebar.slider('Raio (R/Ro)', 0.1, 1948.5, 1000.0)
Absolute_magnitude = st.sidebar.slider('Magnitude Absoluta(Mv)', -11.92, 20.06, -2.3)
Star_color = st.sidebar.selectbox('Cor da Estrela', ["Vermelha", "Azul", "Ciano", "outra"])
Spectral_Class = st.sidebar.selectbox('Classe Espectral', ["M", "B", "O", "A", "F", "K", "G"])

user_data = pd.DataFrame({
    'Temperature (K)': [Temperature],
    'Luminosity(L/Lo)': [Luminosity],
    'Radius(R/Ro)': [Radius],
    'Absolute magnitude(Mv)': [Absolute_magnitude],
    'Star color': [0 if Star_color == 'Vermelha' else 1 if Star_color == 'Azul' else 2 if Star_color == 'Ciano' else 3],
    'Spectral Class': [0 if Spectral_Class == 'M' else 1 if Spectral_Class == 'B' else 2 if Spectral_Class == 'O' else 3 if Spectral_Class == 'A' else 4 if Spectral_Class == 'F' else 5 if Spectral_Class == 'K' else 6 if Spectral_Class == 'G' else -1]
})

    
prediction = modelo.predict(user_data)[0]

if st.button("Prever"):
    st.subheader("Resultado da Previsão:")
    if prediction == 0:
        st.write("⭐ A Estrela é uma Anã Marrom!")
        image_url = "https://i0.wp.com/www.ovnihoje.com/wp-content/uploads/2017/07/an%C3%A3-marrom.jpg?fit=702%2C459&ssl=1"
        st.image(image_url, use_column_width=True)
        st.write("## Anãs Marrons")
        st.write("Anãs marrons não são tecnicamente estrelas. Eles são mais massivos do que os planetas, mas não tão massivos quanto as estrelas. Geralmente, eles têm entre 13 e 80 vezes a massa de Júpiter. Eles não emitem quase nenhuma luz visível, mas os cientistas viram alguns na luz infravermelha. Algumas anãs marrons se formam da mesma forma que as estrelas da sequência principal, a partir de aglomerados de gás e poeira em nebulosas, mas nunca ganham massa suficiente para fazer fusão na escala de uma estrela da sequência principal. Outros podem se formar como planetas, a partir de discos de gás e poeira ao redor de estrelas.")
    elif prediction ==1:
        st.write("⭐ A Estrela é uma Anã Vermelha!")
        image_url = "https://1.bp.blogspot.com/-MlZ6MCXAqJ0/WcZ9-8xxcwI/AAAAAAAADnk/XDlU5d3wm_85IFAiVgRV3ifN-oG3VblXgCLcBGAs/s2560/red_dwarf_star_4k-2560x1600.jpg"
        st.image(image_url, use_column_width=True)
        st.write("## Anãs Vermelhas")
        st.write("Anãs vermelhas são as menores estrelas da sequência principal – apenas uma fração do tamanho e massa do Sol. Eles também são os mais legais e aparecem mais alaranjados do que vermelhos. Quando uma anã vermelha produz hélio via fusão em seu núcleo, a energia liberada traz material para a superfície da estrela, onde esfria e afunda de volta, levando consigo um novo suprimento de hidrogênio para o núcleo. Por causa dessa agitação constante, as anãs vermelhas podem queimar constantemente todo o seu suprimento de hidrogênio ao longo de trilhões de anos sem alterar suas estruturas internas, ao contrário de outras estrelas. Os cientistas acreditam que algumas anãs vermelhas de baixa massa, aquelas com apenas um terço da massa do Sol, têm vida útil maior do que a idade atual do universo, até cerca de 14 trilhões de anos. Anãs vermelhas também nascem em número muito maior do que estrelas mais massivas. Por causa disso, e por viverem muito tempo, as anãs vermelhas representam cerca de 75% da população estelar da Via Láctea.")
    elif prediction ==2:
        st.write("⭐ A Estrela é uma Anã Branca!")
        image_url = "https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/cf219951aa6d3560d191992b82eff7db.jpg"
        st.image(image_url, use_column_width=True)
        st.write("## Anãs Brancas")
        st.write("Depois que uma gigante vermelha perdeu toda a sua atmosfera, apenas o núcleo permanece. Os cientistas chamam esse tipo de remanescente estelar de anã branca. Uma anã branca é geralmente do tamanho da Terra, mas centenas de milhares de vezes mais massiva. Uma colher de chá de seu material pesaria mais do que uma caminhonete. Uma anã branca não produz calor novo próprio, por isso esfria gradualmente ao longo de bilhões de anos. Apesar do nome, as anãs brancas podem emitir luz visível que varia de azul branco a vermelho. Os cientistas às vezes descobrem que as anãs brancas são cercadas por discos empoeirados de material, detritos e até planetas – restos da fase de gigante vermelha da estrela original. Em cerca de 10 bilhões de anos, após seu tempo como uma gigante vermelha, o Sol se tornará uma anã branca.")
    elif prediction ==3:
        st.write("⭐ A Estrela é uma estrela da sequência principal!")
        image_url = "https://th.bing.com/th/id/OIP.duFdz5ydW0X50QMKPk6ynQHaE8?rs=1&pid=ImgDetMain"
        st.image(image_url, use_column_width=True)
        st.write("## Estrela de sequência principal")
        st.write("Uma estrela normal se forma a partir de um aglomerado de poeira e gás em um berçário estelar. Ao longo de centenas de milhares de anos, o aglomerado ganha massa, começa a girar e esquenta. Quando o núcleo do aglomerado aquece a milhões de graus, a fusão nuclear começa. Esse processo ocorre quando dois prótons, os núcleos dos átomos de hidrogênio, se fundem para formar um núcleo de hélio. A fusão libera energia que aquece a estrela, criando pressão que empurra contra a força de sua gravidade. Nasce uma estrela. Os cientistas chamam uma estrela que está fundindo hidrogênio ao hélio em seu núcleo de estrela da sequência principal. As estrelas da sequência principal representam cerca de 90% da população estelar do universo. Eles variam em luminosidade, cor e tamanho – de um décimo a 200 vezes a massa do Sol – e vivem por milhões a bilhões de anos.")
    elif prediction ==4:
        st.write("⭐ A Estrela é uma Super Gigante!")
        image_url = "https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/rockcms/2022-01/220111-supernova-mn-1525-30fb35.jpg"
        st.image(image_url, use_column_width=True)
        st.write("## Supergigantes")
        st.write("Estrelas supergigantes estão entre as estrelas mais maciças. No diagrama de Hertzsprung-Russell elas ocupam a parte superior do diagrama. Na classificação espectral de Yerkes, as supergigantes estão na classe Ia (supergigantes mais luminosas) ou Ib (supergigantes menos luminosas). Tipicamente, possuem magnitudes bolométricas (absolutas) entre -5 e -12. As mais luminosas das supergigantes são freqüentemente classificadas como hipergigantes de classe 0. Supergigantes podem ter massas de 8 a 70 massas solares e brilho de 30.000 a centenas de milhares de vezes a luminosidade do Sol. Variam grandemente em raio, geralmente entre 30 e 500, ou mesmo em mais de 1000 raios solares. A lei de Stefan-Boltzmann estabelece que as superfícies relativamente frias das supergigantes vermelhas irradiam muito menos energia por unidade de área do que aquelas das supergigantes azuis; assim, para uma dada luminosidade, supergigantes vermelhas são maiores do que suas contrapartidas azuis. Por causa de suas massas excessivas, elas têm um curto (em termos estelares) ciclo de vida, de somente 10 a 50 milhões de anos, e são observadas principalmente em estruturas cósmicas jovens tais como aglomerados abertos, os braços de galáxias espirais e em galáxias irregulares. Elas são menos abundantes no núcleo de galáxias espirais, e raramente são observadas em galáxias elípticas ou aglomerados globulares, a maioria dos quais supõe-se ser constituídos de estrelas velhas. Supergigantes ocorrem em todas as classes espectrais, de jovens supergigantes azuis classe O até velhas supergigantes vermelhas classe M. Rigel, a estrela mais brilhante da constelação de Órion é uma típica supergigante branco-azulada; por outro lado, Betelgeuse e Antares são supergigantes vermelhas.")
    else:
        st.write("⭐ A Estrela é uma Hiper Gigante!")
        image_url = "https://kipmu.ru/wp-content/uploads/zvezda.jpg"
        st.image(image_url, use_column_width=True)
        st.write("## Hipergigantes")
        st.write("Uma hipergigante (classe de luminosidade 0,IX2 ou Ia+) é um tipo muito raro de estrela que tem uma luminosidade extremamente alta, massa, tamanho, juventude e perda de massa por causa de seus ventos estelares extremos. O termo hipergigante é definido como classe de luminosidade 0 (zero) no sistema MKK. No entanto, isso é raramente visto na literatura ou em classificações espectrais publicadas, exceto para grupos específicos bem definidos, como as hipergigantes amarelas, RSG, DRSG (supergigantes vermelhas) ou supergigantes azuis B(e) com espectros de emissão. Mais comumente, as hipergigantes são classificadas como Ia-0,Ia(0)+1,Ia(-1) ou Ia+, mas as supergigantes vermelhas raramente recebem essas classificações espectrais. Os astrônomos estão interessados nessas estrelas porque elas se relacionam com a compreensão da evolução estelar, especialmente a formação estelar, a estabilidade e sua esperada morte como supernovas.")
        
st.markdown("---")
st.markdown("Criado por Miguel Julio 🚀")