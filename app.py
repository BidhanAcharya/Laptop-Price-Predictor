import streamlit as st
import pickle
import numpy as np

##pickle file is already created so import it
pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))


##select the title of the web app
st.title("Predict the price of a Laptop")

##select the brand
Company =st.selectbox('Brand',df['Company'].unique())

##select the type of laptop
TypeName =st.selectbox('TypeName',df['TypeName'].unique())

##select the RAM 
# Ram =st.selectbox('RAM',df['Ram'].unique())
RAM =st.selectbox('RAM in GB',[2,4,6,8,16,24,32,64])

##Weight of the laptop
weight =st.number_input('Weight of the laptop') 

##Touchscreen or not
touchscreen =st.selectbox('Touchscreen',['No','Yes'])

##select the type of display
ips =st.selectbox('IPS',['No','Yes'])

##select the screen size
screen_size =st.selectbox('Screen Size',['13.3','15.6','15.4','14.0','12.0','17.3'])  

##select the resolution
resolution =st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','2560x1440','3840x2160','3200x1800','2880x1800','2304x1440'])

##select the type of CPU
cpu =st.selectbox('CPU',df['CPU_Brand'].unique())

## Select the size of the hard disk
HDD =st.selectbox('HDD in GB',[0,128,256,512,1024,2048])

## Select the size of the SSD
SSD =st.selectbox('SSD in GB',[0,8,128,256,512,1024])

## Select the brand  of the GPU
GPU =st.selectbox('GPU',df['Gpu_Brand'].unique())

## Select the type of operating system
os =st.selectbox('OS',df['OS'].unique())

# os='Mac'
# if Company!='Apple': 
#     os =st.selectbox('OS',['Others/No OS/Linux','Windows'])
    

if st.button('Predict Price'):
    ppi=None
    if touchscreen=='Yes':
        touchscreen=1
    else:
        touchscreen=0
    if ips=='Yes':
        ips=1
    else:
        ips=0
        
    X_resolutionoflaptop=int(resolution.split('x')[0])
    Y_resolutionoflaptop=int(resolution.split('x')[1])
    ppi=int((((X_resolutionoflaptop**2)+(Y_resolutionoflaptop**2))**0.5)/float(screen_size))
    query=np.array([Company,TypeName,RAM,weight,touchscreen,ips,ppi,cpu,HDD,SSD,GPU,os])
    query=query.reshape(1,12)
    predicted_price = np.exp(pipe.predict(query))[0]
    ##since we have converted int log so we have to convert it back to original form using exponential
    st.write('The Price of the Laptop would be')
    st.title(predicted_price)



